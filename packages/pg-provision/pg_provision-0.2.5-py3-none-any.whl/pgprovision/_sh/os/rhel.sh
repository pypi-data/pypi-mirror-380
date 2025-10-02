#!/usr/bin/env bash
#NOTE: this file is sourced by provision.sh

# Expect these from the caller: run(), err(), and variables PG_VERSION, REPO_KIND
: "${PG_VERSION:=16}"
: "${REPO_KIND:=pgdg}"

_pkgmgr() {
	if command -v dnf >/dev/null 2>&1; then echo dnf; elif command -v yum >/dev/null 2>&1; then echo yum; else return 1; fi
}

_rhel_service_name() {
	# Determine service name after packages are installed
	if systemctl list-unit-files --type=service 2>/dev/null | grep -q "^postgresql-${PG_VERSION}\.service"; then
		echo "postgresql-${PG_VERSION}"
	else
		echo "postgresql"
	fi
}

_rhel_default_pgdata_for_service() {
	local svc
	svc="$(_rhel_service_name)"
	if [[ "$svc" =~ postgresql-[0-9]+ ]]; then
		echo "/var/lib/pgsql/${PG_VERSION}/data"
	else
		echo "/var/lib/pgsql/data"
	fi
}

_rhel_set_pgdata_override() {
	local svc="${1:?svc}" pgdata="${2:?pgdata}"
	local dropin="/etc/systemd/system/${svc}.service.d/override.conf"
	run "${SUDO[@]}" install -d -m 0755 -- "$(dirname "$dropin")"
	# Use tee under sudo to avoid redirection permission issues
	run bash -c "printf '%s\n' '[Unit]' 'RequiresMountsFor=${pgdata}' '' '[Service]' 'Environment=PGDATA=${pgdata}' \
                | ${SUDO[*]} tee '${dropin}' >/dev/null"
	run "${SUDO[@]}" systemctl daemon-reload
}

_rhel_selinux_label_datadir() {
	local dir="${1:?dir}"
	if ! command -v semanage >/dev/null 2>&1; then
		warn "semanage not available; skipping SELinux fcontext for ${dir} (install policycoreutils-python-utils)."
		return 0
	fi
	if ! run "${SUDO[@]}" semanage fcontext -a -t postgresql_db_t "${dir}(/.*)?"; then
		run "${SUDO[@]}" semanage fcontext -m -t postgresql_db_t "${dir}(/.*)?" || {
			warn "Failed to set SELinux context for PGDATA: ${dir}"
			return 0
		}
	fi
	run "${SUDO[@]}" restorecon -Rv "${dir}"
}

_is_valid_pgdata() {
	local d="${1:?}"
	[[ -d "$d" ]] || return 1
	[[ -f "$d/PG_VERSION" ]] || return 1
	[[ -d "$d/global" && -f "$d/global/pg_control" ]] || return 1
	[[ -d "$d/base" ]] || return 1
	# Accept either wal dir (>=10) or xlog (<10); allow symlinked WAL
	[[ -d "$d/pg_wal" || -L "$d/pg_wal" || -d "$d/pg_xlog" || -L "$d/pg_xlog" ]] || return 1
	return 0
}

_rhel_current_pgdata() {
	local svc override pgdata
	svc="$(_rhel_service_name)"
	pgdata="$(_rhel_default_pgdata_for_service)"
	override="/etc/systemd/system/${svc}.service.d/override.conf"
	if [[ -r "$override" ]] && grep -q '^Environment=PGDATA=' "$override"; then
		pgdata=$(sed -n 's/^Environment=PGDATA=\(.*\)$/\1/p' "$override" | tail -n1)
	fi
	printf '%s\n' "$pgdata"
}

_rhel_self_heal_cluster() {
	local svc cur def reason=() broken="false"
	svc="$(_rhel_service_name)"

	# If the service unit isn't present yet, there's nothing to heal—return quietly.
	if ! systemctl cat "$svc" >/dev/null 2>&1; then
		return 0
	fi

	cur="$(_rhel_current_pgdata)"
	def="$(_rhel_default_pgdata_for_service)"

	# Preflight: service + postgres user
	if ! systemctl cat "$svc" >/dev/null 2>&1; then
		broken="true"
		reason+=("service unit missing: $svc")
	fi
	if ! id postgres >/dev/null 2>&1; then
		broken="true"
		reason+=("missing 'postgres' OS user")
	fi

	# PGDATA unset or missing
	if [[ -z "$cur" ]]; then
		broken="true"
		reason+=("PGDATA unset in $svc")
	elif [[ ! -d "$cur" ]]; then
		broken="true"
		reason+=("PGDATA missing: $cur")
	fi

	# If current dir exists, validate + basic perms
	if [[ -d "$cur" ]]; then
		# Try quick perms fix first; then validate layout
		"${SUDO[@]}" chown -R postgres:postgres -- "$cur" >/dev/null 2>&1 || true
		"${SUDO[@]}" chmod 0700 -- "$cur" >/dev/null 2>&1 || true
		_rhel_selinux_label_datadir "$cur" >/dev/null 2>&1 || true

		if ! _is_valid_pgdata "$cur"; then
			broken="true"
			reason+=("invalid PGDATA: $cur")
		else
			# Enforce owner/mode
			local o g m
			o=$(stat -c '%U' -- "$cur" 2>/dev/null || echo "")
			g=$(stat -c '%G' -- "$cur" 2>/dev/null || echo "")
			m=$(stat -c '%a' -- "$cur" 2>/dev/null || echo "")
			[[ "$o:$g" != "postgres:postgres" ]] && {
				broken="true"
				reason+=("PGDATA not owned by postgres ($o:$g)")
			}
			case "$m" in 700 | 750) : ;; *)
				broken="true"
				reason+=("PGDATA mode $m (expect 700/750)")
				;;
			esac

			# On-disk version check when unit is versioned (e.g. postgresql-16)
			if [[ -f "$cur/PG_VERSION" && "$svc" =~ ^postgresql-([0-9]+) ]]; then
				local on_disk_ver
				on_disk_ver=$(tr -d '\n' <"$cur/PG_VERSION" 2>/dev/null)
				local svc_ver="${BASH_REMATCH[1]}"
				[[ -n "$on_disk_ver" && "$on_disk_ver" != "$svc_ver" ]] && {
					broken="true"
					reason+=("PG_VERSION mismatch: $on_disk_ver != $svc_ver")
				}
			fi
		fi
	fi

	# If service expects the default PGDATA but it's absent, that's broken
	if [[ -n "$cur" && "$cur" == "$def" && ! -d "$def" ]]; then
		broken="true"
		reason+=("no default cluster at $def")
	fi

	[[ "$broken" != "true" ]] && return 0
	warn "RHEL self-heal: detected broken cluster (${reason[*]})"

	soft_run "stop $svc" "${SUDO[@]}" systemctl stop "$svc"

	# Try to adopt any valid existing PGDATA (current first, then default)
	local target=""
	if [[ -d "$cur" ]] && _is_valid_pgdata "$cur"; then
		target="$cur"
	elif [[ -d "$def" ]] && _is_valid_pgdata "$def"; then
		target="$def"
	fi

	if [[ -n "$target" ]]; then
		must_run "ownership $target" "${SUDO[@]}" chown -R postgres:postgres -- "$target"
		must_run "chmod 0700 $target" "${SUDO[@]}" chmod 0700 -- "$target"
		_rhel_selinux_label_datadir "$target" || warn "SELinux label failed for $target"
		# Remove stale pid if unit is stopped
		if [[ -f "$target/postmaster.pid" ]]; then
			soft_run "remove stale pid" "${SUDO[@]}" rm -f -- "$target/postmaster.pid"
		fi
		_rhel_set_pgdata_override "$svc" "$target"
		must_run "enable+start $svc" "${SUDO[@]}" systemctl enable --now "$svc"
		log "RHEL self-heal: adopted existing PGDATA at $target"
		return 0
	fi

	# No adoptable PGDATA: initialize
	local pm_init_done="false"

	# Use packaging helpers for default locations only
	if command -v postgresql-setup >/dev/null 2>&1 &&
		[[ "$svc" == "postgresql" ]] &&
		[[ "${DATA_DIR:-auto}" == "auto" ]]; then
		soft_run "postgresql-setup --initdb" "${SUDO[@]}" postgresql-setup --initdb && pm_init_done="true"
	elif [[ -x "/usr/pgsql-${PG_VERSION}/bin/postgresql-${PG_VERSION}-setup" ]] &&
		[[ "$svc" == "postgresql-${PG_VERSION}" ]] &&
		[[ "${DATA_DIR:-auto}" == "auto" ]]; then
		soft_run "pgdg setup initdb" "${SUDO[@]}" "/usr/pgsql-${PG_VERSION}/bin/postgresql-${PG_VERSION}-setup" initdb && pm_init_done="true"
	fi

	local target_new
	if [[ "${DATA_DIR:-auto}" != "auto" && -n "${DATA_DIR}" ]]; then
		target_new="${DATA_DIR}"
	else
		target_new="$def"
	fi

	# If packaging didn't create the cluster or user requested a custom dir, do it ourselves
	if [[ "$pm_init_done" != "true" || "${DATA_DIR:-auto}" != "auto" ]]; then
		must_run "create $target_new" "${SUDO[@]}" install -d -m 0700 -o postgres -g postgres -- "$target_new"
		_rhel_selinux_label_datadir "$target_new" || warn "SELinux label failed for $target_new"
		# pick correct initdb binary
		local initdb_bin="initdb"
		if [[ "$svc" == "postgresql-${PG_VERSION}" && -x "/usr/pgsql-${PG_VERSION}/bin/initdb" ]]; then
			initdb_bin="/usr/pgsql-${PG_VERSION}/bin/initdb"
		fi
		must_run "initdb $target_new" "${SUDO[@]}" -u postgres "$initdb_bin" -D "$target_new"
	fi

	_rhel_set_pgdata_override "$svc" "$target_new"
	must_run "enable+start $svc" "${SUDO[@]}" systemctl enable --now "$svc"
	log "RHEL self-heal: created cluster at $target_new"
}

os_prepare_repos() {
	local repo_kind="${1:-${REPO_KIND}}"
	local pm
	pm="$(_pkgmgr)" || {
		err "No dnf/yum found"
		exit 2
	}
	local PM=("${SUDO[@]}" "$pm")
	if [[ "$repo_kind" == "pgdg" ]]; then
		# Use PGDG and disable AppStream module
		run "${PM[@]}" -y module reset postgresql || true
		run "${PM[@]}" -y module disable postgresql || true
		local rel arch rpm_url
		rel="$(rpm -E %rhel)"
		arch="$(uname -m)"
		case "$arch" in x86_64 | aarch64 | ppc64le | s390x) : ;; *) arch="x86_64" ;; esac
		rpm_url="https://download.postgresql.org/pub/repos/yum/reporpms/EL-${rel}-${arch}/pgdg-redhat-repo-latest.noarch.rpm"
		must_run "install PGDG repo" "${PM[@]}" -y install "$rpm_url"
	else
		# Use OS AppStream module at the requested major version
		run "${PM[@]}" -y module reset postgresql || true
		must_run "enable AppStream module postgresql:${PG_VERSION}" "${PM[@]}" -y module enable "postgresql:${PG_VERSION}"
	fi
}

os_install_packages() {
	local repo_kind="${1:-${REPO_KIND}}"
	local pm
	pm="$(_pkgmgr)" || {
		err "No dnf/yum found"
		exit 2
	}
	local PM=("${SUDO[@]}" "$pm")
	if [[ "$repo_kind" == "pgdg" ]]; then
		must_run "install PGDG packages" "${PM[@]}" -y install \
			"postgresql${PG_VERSION}" "postgresql${PG_VERSION}-server" "postgresql${PG_VERSION}-contrib"
	else
		must_run "install AppStream packages" "${PM[@]}" -y install postgresql postgresql-server postgresql-contrib
	fi
}

os_init_cluster() {
	local data_dir="${1:-auto}"
	local svc
	svc="$(_rhel_service_name)"

	# Self-heal before any init logic
	if [[ "${SELF_HEAL:-true}" == "true" ]]; then
		_rhel_self_heal_cluster || true
	fi

	# If default path is valid and auto mode, ensure service and return
	if [[ "$data_dir" == "auto" ]]; then
		local cur
		cur="$(_rhel_current_pgdata)"
		if [[ -n "$cur" ]] && _is_valid_pgdata "$cur"; then
			must_run "enable+start $svc" "${SUDO[@]}" systemctl enable --now "$svc"
			return 0
		fi
	fi
	# Choose setup command depending on packaging
	local -a setup_cmd=()
	if command -v postgresql-setup >/dev/null 2>&1 && [[ "$svc" == "postgresql" ]]; then
		setup_cmd=("${SUDO[@]}" postgresql-setup --initdb)
	elif [[ -x "/usr/pgsql-${PG_VERSION}/bin/postgresql-${PG_VERSION}-setup" ]]; then
		setup_cmd=("${SUDO[@]}" "/usr/pgsql-${PG_VERSION}/bin/postgresql-${PG_VERSION}-setup" initdb)
	fi

	if [[ "$data_dir" == "auto" ]]; then
		if ((${#setup_cmd[@]})); then
			run "${setup_cmd[@]}"
		else
			# Fallback to initdb if setup helper unavailable
			local pgdata
			pgdata="$(_rhel_default_pgdata_for_service)"
			must_run "create PGDATA" "${SUDO[@]}" install -d -m 0700 -- "$pgdata"
			must_run "chown PGDATA to postgres" "${SUDO[@]}" chown -R postgres:postgres -- "$pgdata"
			must_run "initdb default PGDATA" "${SUDO[@]}" -u postgres initdb -D "$pgdata"
		fi
		must_run "enable+start $svc" "${SUDO[@]}" systemctl enable --now "$svc"
	else
		must_run "create custom PGDATA" "${SUDO[@]}" install -d -m 0700 -- "$data_dir"
		must_run "chown custom PGDATA" "${SUDO[@]}" chown -R postgres:postgres -- "$data_dir"
		must_run "chmod 0700 custom PGDATA" "${SUDO[@]}" chmod 0700 -- "$data_dir"
		_rhel_selinux_label_datadir "$data_dir" || warn "SELinux label for $data_dir did not apply"
		if command -v initdb >/dev/null 2>&1; then
			if [[ ! -d "$data_dir/base" ]]; then
				must_run "initdb custom PGDATA" "${SUDO[@]}" -u postgres initdb -D "$data_dir"
			fi
		else
			err "initdb not found; cannot initialize custom data dir at ${data_dir}"
			exit 2
		fi
		_rhel_set_pgdata_override "$svc" "$data_dir"
		must_run "enable+start $svc" "${SUDO[@]}" systemctl enable --now "$svc"
	fi
}

os_get_paths() {
	local svc
	svc="$(_rhel_service_name)"
	local pgdata
	pgdata="$(_rhel_default_pgdata_for_service)"
	local override="/etc/systemd/system/${svc}.service.d/override.conf"
	if [[ -f "$override" ]] && grep -q '^Environment=PGDATA=' "$override"; then
		pgdata=$(sed -n 's/^Environment=PGDATA=\(.*\)$/\1/p' "$override" | tail -n1)
	fi
	echo "CONF_FILE=${pgdata}/postgresql.conf HBA_FILE=${pgdata}/pg_hba.conf IDENT_FILE=${pgdata}/pg_ident.conf DATA_DIR=${pgdata} SERVICE=${svc}"
}

os_enable_and_start() {
	local svc
	svc="$(_rhel_service_name)"
	run "${SUDO[@]}" systemctl enable --now "$svc"
}
os_restart() {
	local svc
	svc="$(_rhel_service_name)"
	run "${SUDO[@]}" systemctl restart "$svc"
}

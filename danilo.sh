#!/usr/bin/env bash
set -Eeuo pipefail

# -----------------------------------------------------------------------------
# Project DANILO
# Digital Assistant Network for Interactive Learning Offline
# Master deployment script for Ubuntu 24.04
# -----------------------------------------------------------------------------

STACK_NAME="danilo"
export COMPOSE_PROJECT_NAME="${STACK_NAME}"
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="/opt/danilo"
APP_ROOT="${PROJECT_ROOT}/app"
RUNTIME_ROOT="${PROJECT_ROOT}/runtime"
CONTENT_ROOT="${APP_ROOT}/content"
LOCAL_LESSONS_DIR="${SCRIPT_DIR}/lessons"
LOG_FILE="/var/log/danilo-install.log"
BACKUP_ROOT="/var/backups/danilo"

LAN_IP="${DANILO_LAN_IP:-10.10.0.1}"
LAN_PREFIX="${DANILO_LAN_PREFIX:-24}"
PORTAL_DOMAIN="${DANILO_PORTAL_DOMAIN:-danilo.local}"
SSID="${DANILO_SSID:-PROJECT-DANILO}"
WIFI_PASSPHRASE="${DANILO_WIFI_PASSPHRASE:-}"
OLLAMA_MODEL="${DANILO_OLLAMA_MODEL:-llama3.2:3b-instruct-q4_K_M}"
NODE_MAJOR="${DANILO_NODE_MAJOR:-22}"
TEMP_OLLAMA_CONTAINER="danilo-ollama-prepull"
SYNC_ONLY=0
CLEAN_BUILD=0
RESET_DATA="${DANILO_RESET_DATA:-0}"
INSTALL_SUCCEEDED=0
BOLD="$(printf '\033[1m')"
RESET="$(printf '\033[0m')"
DIM="$(printf '\033[2m')"

INSTALL_STARTED_AT="$(date +%s)"
CURRENT_STEP_INDEX=0
CURRENT_STEP_TOTAL=0
CURRENT_STEP_LABEL="Starting"
DANILO_MANAGED_FILES=(
  /etc/apt/sources.list.d/docker.list
  /etc/apt/sources.list.d/nodesource.list
  /etc/default/hostapd
  /etc/dnsmasq.conf
  /etc/dnsmasq.d/danilo.conf
  /etc/hostapd/danilo.conf
  /etc/logrotate.d/danilo-install
  /etc/NetworkManager/conf.d/99-danilo.conf
  /etc/resolv.conf
  /etc/sysctl.d/98-danilo-ipforward.conf
  /etc/systemd/resolved.conf.d/no-stub.conf
  /etc/systemd/system/danilo-ap.service
  /etc/systemd/system/danilo-stack.service
  /usr/local/bin/danilo-network-down.sh
  /usr/local/bin/danilo-network-up.sh
)

if [[ "${EUID:-$(id -u)}" -ne 0 ]]; then
  LOG_FILE="${TMPDIR:-/tmp}/danilo-install.log"
fi
umask 077
exec 3>&1
exec > >(tee -a "${LOG_FILE}") 2>&1

format_duration() {
  local total_seconds="${1:-0}"
  local hours=0
  local minutes=0
  local seconds=0

  if (( total_seconds < 0 )); then
    total_seconds=0
  fi

  hours=$(( total_seconds / 3600 ))
  minutes=$(( (total_seconds % 3600) / 60 ))
  seconds=$(( total_seconds % 60 ))
  printf '%02d:%02d:%02d' "${hours}" "${minutes}" "${seconds}"
}

rule() {
  printf '%s' '------------------------------------------------------------'
}

progress_bar() {
  local current="$1"
  local total="$2"
  local width=28
  local filled=0
  local i=0

  if (( total > 0 )); then
    filled=$(( current * width / total ))
  fi

  if (( filled > width )); then
    filled="${width}"
  fi

  printf '['
  for (( i = 0; i < width; i++ )); do
    if (( i < filled )); then
      printf '='
    else
      printf '.'
    fi
  done
  printf ']'
}

print_install_intro() {
  printf '\n%s\n' "$(rule)"
  printf '%sProject DANILO installer%s\n' "${BOLD}" "${RESET}"
  printf '%slog%s %s\n' "${DIM}" "${RESET}" "${LOG_FILE}"
  printf '%sstarted%s %s\n' "${DIM}" "${RESET}" "$(date '+%Y-%m-%d %H:%M:%S')"
}

step() {
  local current="$1"
  local total="$2"
  local message="$3"
  local now=0
  local elapsed=0
  local completed=0
  local remaining=0
  local eta_text="--:--:--"
  local percent=0

  CURRENT_STEP_INDEX="${current}"
  CURRENT_STEP_TOTAL="${total}"
  CURRENT_STEP_LABEL="${message}"

  now="$(date +%s)"
  elapsed=$(( now - INSTALL_STARTED_AT ))
  completed=$(( current - 1 ))
  remaining=$(( total - completed ))
  percent=$(( current * 100 / total ))

  if (( completed > 0 )); then
    eta_text="$(format_duration $(( (elapsed / completed) * remaining )))"
  fi

  printf '\n%s\n' "$(rule)"
  printf '%s[%02d/%02d]%s %s\n' "${BOLD}" "${current}" "${total}" "${RESET}" "${message}"
  printf '%s %3d%%\n' "$(progress_bar "${current}" "${total}")" "${percent}"
  printf '%selapsed%s %s   %seta%s %s\n' "${DIM}" "${RESET}" "$(format_duration "${elapsed}")" "${DIM}" "${RESET}" "${eta_text}"
}

note() {
  printf '  %s- %s%s\n' "${DIM}" "$1" "${RESET}"
}

print_failure() {
  local exit_code="$1"
  local elapsed=0

  elapsed=$(( $(date +%s) - INSTALL_STARTED_AT ))
  printf '\n%s\n' "$(rule)"
  printf '%s[error]%s Install stopped during step %02d/%02d: %s\n' "${BOLD}" "${RESET}" "${CURRENT_STEP_INDEX}" "${CURRENT_STEP_TOTAL}" "${CURRENT_STEP_LABEL}"
  printf '%selapsed%s %s   %slog%s %s\n' "${DIM}" "${RESET}" "$(format_duration "${elapsed}")" "${DIM}" "${RESET}" "${LOG_FILE}"
  exit "${exit_code}"
}

backup_file() {
  local path="$1"
  local safe_path=""
  safe_path="${path#/}"
  safe_path="${safe_path//\//__}"

  mkdir -p "${BACKUP_ROOT}"
  if [[ -e "${BACKUP_ROOT}/${safe_path}.bak" || -e "${BACKUP_ROOT}/${safe_path}.missing" ]]; then
    return 0
  fi

  if [[ -e "${path}" || -L "${path}" ]]; then
    cp -a --remove-destination "${path}" "${BACKUP_ROOT}/${safe_path}.bak"
  else
    : > "${BACKUP_ROOT}/${safe_path}.missing"
  fi
}

backup_path_for() {
  local path="$1"
  local safe_path=""
  safe_path="${path#/}"
  safe_path="${safe_path//\//__}"
  printf '%s/%s.bak\n' "${BACKUP_ROOT}" "${safe_path}"
}

backup_managed_file() {
  backup_file "$1"
}

backup_managed_files() {
  local path=""
  for path in "${DANILO_MANAGED_FILES[@]}"; do
    backup_file "${path}"
  done
}

restore_file() {
  local path="$1"
  local safe_path=""
  safe_path="${path#/}"
  safe_path="${safe_path//\//__}"

  if [[ -e "${BACKUP_ROOT}/${safe_path}.bak" || -L "${BACKUP_ROOT}/${safe_path}.bak" ]]; then
    cp -a --remove-destination "${BACKUP_ROOT}/${safe_path}.bak" "${path}"
  elif [[ -e "${BACKUP_ROOT}/${safe_path}.missing" ]]; then
    rm -f "${path}"
  fi
}

resolver_file_has_upstream() {
  local path="$1"
  [[ -r "${path}" ]] || return 1
  awk '
    $1 == "nameserver" &&
    $2 != "127.0.0.53" &&
    $2 != "127.0.0.1" &&
    $2 != "::1" {
      found = 1
    }
    END { exit found ? 0 : 1 }
  ' "${path}"
}

rollback_install() {
  local path=""
  [[ "${INSTALL_SUCCEEDED}" -eq 1 ]] && return 0
  note "Attempting rollback of DANILO-owned system changes"
  systemctl stop danilo-stack.service danilo-ap.service >/dev/null 2>&1 || true
  if [[ -x /usr/local/bin/danilo-network-down.sh ]]; then
    /usr/local/bin/danilo-network-down.sh >/dev/null 2>&1 || true
  fi
  for path in "${DANILO_MANAGED_FILES[@]}"; do
    restore_file "${path}"
  done
  systemctl daemon-reload >/dev/null 2>&1 || true
  systemctl restart systemd-resolved >/dev/null 2>&1 || true
  systemctl restart NetworkManager >/dev/null 2>&1 || true
}

on_error() {
  local exit_code="$?"
  rollback_install
  print_failure "${exit_code}"
}

trap 'on_error' ERR

require_root() {
  if [[ "${EUID}" -ne 0 ]]; then
    echo "This installer must be run as root or with sudo."
    exit 1
  fi
}

show_help() {
  cat <<EOF
Usage: $(basename "$0") [--sync]

  --sync    Only mirror the local lessons folder into ${CONTENT_ROOT},
            restart the gateway container, and exit.
  --clean-build
            Force Docker to rebuild local images without using cache.
EOF
}

parse_args() {
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --sync)
        SYNC_ONLY=1
        ;;
      --clean-build)
        CLEAN_BUILD=1
        ;;
      -h|--help)
        show_help
        exit 0
        ;;
      *)
        echo "Unknown argument: $1"
        show_help
        exit 1
        ;;
    esac
    shift
  done
}

list_wifi_interfaces() {
  iw dev 2>/dev/null | awk '$1 == "Interface" { print $2 }'
}

interface_bus_type() {
  local iface="$1"
  local device_path=""
  device_path="$(readlink -f "/sys/class/net/${iface}/device" 2>/dev/null || true)"

  if [[ "${device_path}" == *"/usb"* ]]; then
    printf 'usb\n'
    return 0
  fi

  if [[ "${device_path}" == *"/pci"* ]]; then
    printf 'pci\n'
    return 0
  fi

  printf 'unknown\n'
}

get_interface_mac() {
  local iface="$1"
  cat "/sys/class/net/${iface}/address" 2>/dev/null | tr '[:upper:]' '[:lower:]'
}

detect_internal_wifi_interface() {
  local primary_iface="$1"
  local candidate=""
  local device_path=""

  while read -r candidate; do
    [[ -z "${candidate}" || "${candidate}" == "${primary_iface}" ]] && continue
    device_path="$(readlink -f "/sys/class/net/${candidate}/device" 2>/dev/null || true)"
    if [[ "${candidate}" =~ ^wlp ]] || [[ "${device_path}" == *"/pci"* ]]; then
      printf '%s\n' "${candidate}"
      return 0
    fi
  done < <(iw dev 2>/dev/null | awk '$1 == "Interface" { print $2 }')

  while read -r candidate; do
    [[ -z "${candidate}" || "${candidate}" == "${primary_iface}" ]] && continue
    printf '%s\n' "${candidate}"
    return 0
  done < <(iw dev 2>/dev/null | awk '$1 == "Interface" { print $2 }')

  return 1
}

detect_wifi_roles() {
  local iface=""
  local bus=""
  local first_wifi=""

  AP_WIFI_IFACE="${WIFI_IFACE:-}"
  AP_WIFI_IFACE="${DANILO_WIFI_IFACE:-${AP_WIFI_IFACE}}"
  UPLINK_WIFI_IFACE="${INTERNAL_WIFI_IFACE:-}"
  UPLINK_WIFI_IFACE="${DANILO_INTERNAL_WIFI_IFACE:-${UPLINK_WIFI_IFACE}}"

  while read -r iface; do
    [[ -z "${iface}" ]] && continue
    [[ -z "${first_wifi}" ]] && first_wifi="${iface}"
    bus="$(interface_bus_type "${iface}")"

    if [[ -z "${AP_WIFI_IFACE}" ]]; then
      if [[ "${iface}" =~ ^wlx ]] || [[ "${bus}" == "usb" ]]; then
        AP_WIFI_IFACE="${iface}"
      fi
    fi

    if [[ -z "${UPLINK_WIFI_IFACE}" ]]; then
      if [[ "${iface}" != "${AP_WIFI_IFACE}" ]] && { [[ "${iface}" =~ ^wlp ]] || [[ "${bus}" == "pci" ]]; }; then
        UPLINK_WIFI_IFACE="${iface}"
      fi
    fi
  done < <(list_wifi_interfaces)

  if [[ -z "${AP_WIFI_IFACE}" ]]; then
    AP_WIFI_IFACE="${first_wifi:-}"
  fi

  if [[ -z "${UPLINK_WIFI_IFACE}" ]]; then
    while read -r iface; do
      [[ -z "${iface}" || "${iface}" == "${AP_WIFI_IFACE}" ]] && continue
      UPLINK_WIFI_IFACE="${iface}"
      break
    done < <(list_wifi_interfaces)
  fi

  if [[ -z "${AP_WIFI_IFACE}" ]]; then
    echo "Unable to detect a Wi-Fi interface for the DANILO access point."
    exit 1
  fi
}

command_missing() {
  ! command -v "$1" >/dev/null 2>&1
}

require_command() {
  if command_missing "$1"; then
    echo "Required command is missing: $1"
    echo "Install the base Ubuntu packages or reconnect internet, then re-run this installer."
    exit 1
  fi
}

# -----------------------------------------------------------------------------
# Preflight and dependency installation
# -----------------------------------------------------------------------------

validate_ubuntu_version() {
  if [[ ! -r /etc/os-release ]]; then
    echo "Cannot read /etc/os-release; this installer supports Ubuntu 24.04."
    exit 1
  fi

  . /etc/os-release
  if [[ "${ID:-}" != "ubuntu" || "${VERSION_ID:-}" != "24.04" ]]; then
    echo "Unsupported OS: ${PRETTY_NAME:-unknown}. Project DANILO targets Ubuntu 24.04."
    exit 1
  fi
}

validate_disk_space() {
  local available_kb=0
  local required_kb="${DANILO_MIN_FREE_KB:-31457280}"
  available_kb="$(df -Pk / | awk 'NR == 2 { print $4 }')"
  if (( available_kb < required_kb )); then
    echo "Not enough free disk space under /opt. Need at least $((required_kb / 1024 / 1024)) GB free."
    exit 1
  fi
}

validate_wifi_capability() {
  local iface="$1"
  if [[ -z "${iface}" || ! -d "/sys/class/net/${iface}" ]]; then
    echo "Configured access-point interface is not present: ${iface:-none}"
    exit 1
  fi

  if ! iw list 2>/dev/null | awk '/Supported interface modes:/,/Band [0-9]+:/' | grep -q '\* AP'; then
    echo "No AP-capable Wi-Fi interface was detected. Use DANILO_WIFI_IFACE to select a known AP-capable adapter."
    exit 1
  fi
}

validate_wifi_passphrase() {
  if [[ -z "${WIFI_PASSPHRASE}" ]]; then
    WIFI_PASSPHRASE="$(openssl rand -base64 18 | tr -d '=+/' | cut -c1-16)"
  fi

  if (( ${#WIFI_PASSPHRASE} < 8 || ${#WIFI_PASSPHRASE} > 63 )); then
    echo "Wi-Fi passphrase must be 8-63 characters. Set DANILO_WIFI_PASSPHRASE to override."
    exit 1
  fi
}

check_internet_reachability() {
  if command_missing curl; then
    note "curl is not installed yet; internet reachability will be rechecked after packages are installed"
    return 0
  fi

  if curl -fsS --connect-timeout 5 https://download.docker.com >/dev/null 2>&1; then
    note "Internet is reachable for package and image refresh"
  else
    note "Internet check failed; continuing and relying on cached packages/images where available"
  fi
}

preflight_checks() {
  validate_ubuntu_version
  validate_disk_space
  if [[ ! -d "${LOCAL_LESSONS_DIR}" ]]; then
    echo "Local lessons folder not found: ${LOCAL_LESSONS_DIR}"
    echo "Create it before install so the offline portal has content to serve."
    exit 1
  fi
  require_command awk
  require_command sed
  require_command ip
  require_command systemctl
  check_internet_reachability
}

apt_install() {
  DEBIAN_FRONTEND=noninteractive apt-get install -y -qq "$@"
}

# Base system packages for Docker, Wi-Fi AP control, firewall persistence, and
# resolver management.
prepare_apt() {
  export DEBIAN_FRONTEND=noninteractive
  apt-get update -y -qq || note "apt update failed; attempting install from the local package cache"
  apt_install apt-transport-https ca-certificates curl gnupg software-properties-common \
    lsb-release jq unzip git build-essential rfkill iw net-tools avahi-daemon \
    network-manager hostapd dnsmasq iptables-persistent netfilter-persistent \
    python3.12 python3.12-venv python3-pip openssl e2fsprogs psmisc logrotate rsync
}

install_docker() {
  if command_missing docker || ! docker compose version >/dev/null 2>&1; then
    note "Installing Docker Engine and Docker Compose plugin"
    install -d -m 0755 /etc/apt/keyrings
    if [[ ! -f /etc/apt/keyrings/docker.asc ]]; then
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
      chmod a+r /etc/apt/keyrings/docker.asc
    fi

    backup_managed_file /etc/apt/sources.list.d/docker.list
    cat >/etc/apt/sources.list.d/docker.list <<EOF
deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "${VERSION_CODENAME}") stable
EOF
    apt-get update -y -qq
    apt_install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    systemctl enable --now docker
  else
    note "Docker Engine and Compose plugin already available"
  fi
}

install_node() {
  local current_major="0"
  if command -v node >/dev/null 2>&1; then
    current_major="$(node -p 'process.versions.node.split(".")[0]')"
  fi

  if [[ "${current_major}" -lt 20 ]]; then
    note "Installing Node.js LTS"
    install -d -m 0755 /etc/apt/keyrings
    if [[ ! -f /etc/apt/keyrings/nodesource.gpg ]]; then
      curl -fsSL "https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key" \
        | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
      chmod a+r /etc/apt/keyrings/nodesource.gpg
    fi
    backup_managed_file /etc/apt/sources.list.d/nodesource.list
    cat >/etc/apt/sources.list.d/nodesource.list <<EOF
deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_${NODE_MAJOR}.x nodistro main
EOF
    apt-get update -y -qq
    apt_install nodejs
  else
    note "Node.js LTS already available"
  fi
}

# -----------------------------------------------------------------------------
# Cleanup, rollback, and resolver recovery
# -----------------------------------------------------------------------------

# Remove prior Project DANILO stack remnants so the install always starts clean.
deep_clean() {
  note "Removing previous Project DANILO remnants"

  systemctl stop danilo-stack.service danilo-ap.service >/dev/null 2>&1 || true
  if [[ -f /etc/dnsmasq.d/danilo.conf || -f /etc/hostapd/danilo.conf ]]; then
    systemctl stop hostapd dnsmasq >/dev/null 2>&1 || true
  fi
  if [[ -x /usr/local/bin/danilo-network-down.sh ]]; then
    /usr/local/bin/danilo-network-down.sh >/dev/null 2>&1 || true
  fi

  backup_managed_files

  mkdir -p "${BACKUP_ROOT}"
  if [[ -f "${APP_ROOT}/.env" ]]; then
    install -m 0600 "${APP_ROOT}/.env" "${BACKUP_ROOT}/env.last"
  fi

  if command -v docker >/dev/null 2>&1; then
    docker rm -f "${TEMP_OLLAMA_CONTAINER}" >/dev/null 2>&1 || true
    if [[ -f "${APP_ROOT}/docker-compose.yml" ]]; then
      if [[ "${RESET_DATA}" == "1" ]]; then
        note "DANILO_RESET_DATA=1 set; removing DANILO containers and named volumes"
        docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" down -v --remove-orphans >/dev/null 2>&1 || true
      else
        docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" down --remove-orphans >/dev/null 2>&1 || true
      fi
    fi

    local containers=""
    containers="$(docker ps -aq --filter "label=com.docker.compose.project=${STACK_NAME}" 2>/dev/null || true)"
    if [[ -n "${containers}" ]]; then
      while IFS= read -r container_id; do
        [[ -z "${container_id}" ]] && continue
        docker rm -f "${container_id}" >/dev/null 2>&1 || true
      done <<< "${containers}"
    fi
  fi

  if [[ "${PROJECT_ROOT}" == /opt/danilo ]]; then
    rm -rf "${PROJECT_ROOT}"
  else
    echo "Refusing to remove unexpected PROJECT_ROOT: ${PROJECT_ROOT}"
    exit 1
  fi
  rm -f /etc/dnsmasq.d/danilo.conf
  rm -f /etc/hostapd/danilo.conf
  rm -f /etc/systemd/system/danilo-ap.service
  rm -f /etc/systemd/system/danilo-stack.service
  rm -f /usr/local/bin/danilo-network-up.sh
  rm -f /usr/local/bin/danilo-network-down.sh
  rm -f /etc/sysctl.d/98-danilo-ipforward.conf
  rm -f /etc/systemd/resolved.conf.d/no-stub.conf
  rm -f /etc/NetworkManager/conf.d/99-danilo.conf
  find /etc/NetworkManager/system-connections -maxdepth 1 -type f -name 'danilo-*' -delete 2>/dev/null || true
  systemctl daemon-reload
}

# Force systemd-resolved to release port 53 while keeping resolver behavior as
# close to the school's previous state as possible. Public resolvers are only a
# last resort when neither the prior config nor systemd's upstream file is usable.
clear_port_53_and_restore_upstream_dns() {
  local resolv_backup=""

  note "Disabling the systemd-resolved stub listener on port 53"
  mkdir -p /etc/systemd/resolved.conf.d
  backup_managed_file /etc/systemd/resolved.conf.d/no-stub.conf
  backup_managed_file /etc/resolv.conf
  resolv_backup="$(backup_path_for /etc/resolv.conf)"

  cat >/etc/systemd/resolved.conf.d/no-stub.conf <<'EOF'
[Resolve]
DNSStubListener=no
EOF

  systemctl restart systemd-resolved >/dev/null 2>&1 || true
  chattr -i /etc/resolv.conf >/dev/null 2>&1 || true

  if resolver_file_has_upstream "${resolv_backup}"; then
    note "Restoring previously configured upstream DNS resolver"
    cp -a --remove-destination "${resolv_backup}" /etc/resolv.conf
  elif resolver_file_has_upstream /run/systemd/resolve/resolv.conf; then
    note "Using systemd-resolved upstream resolver file"
    ln -sfn /run/systemd/resolve/resolv.conf /etc/resolv.conf
  elif resolver_file_has_upstream /etc/resolv.conf; then
    note "Keeping existing usable resolver file"
  else
    note "No usable local resolver found; using public DNS as a temporary install fallback"
    printf 'nameserver 1.1.1.1\nnameserver 8.8.8.8\n' > /etc/resolv.conf
  fi
}

# Detect the Beelink dual-radio layout without breaking internet access during
# install. The external USB Archer becomes the AP, while the internal PCI card
# stays online for the pre-pull phase and is only suppressed once the captive
# portal comes up.
prepare_wifi_hardware() {
  note "Releasing wireless hardware for access-point control"
  rfkill unblock wifi || true
  nmcli radio wifi on >/dev/null 2>&1 || true
  systemctl restart NetworkManager
  sleep 4

  detect_wifi_roles

  mkdir -p "${RUNTIME_ROOT}"
  validate_wifi_capability "${AP_WIFI_IFACE}"
  validate_wifi_passphrase
  WIFI_IFACE="${AP_WIFI_IFACE}"
  echo "${AP_WIFI_IFACE}" > "${RUNTIME_ROOT}/wifi_iface"
  printf '%s\n' "${UPLINK_WIFI_IFACE:-}" > "${RUNTIME_ROOT}/internal_wifi_iface"
  WIFI_MAC="$(get_interface_mac "${AP_WIFI_IFACE}")"
  if [[ -z "${WIFI_MAC}" ]]; then
    echo "Unable to determine the MAC address for ${AP_WIFI_IFACE}."
    exit 1
  fi
  echo "${WIFI_MAC}" > "${RUNTIME_ROOT}/wifi_mac"
  note "Using USB Wi-Fi interface for the DANILO hotspot: ${AP_WIFI_IFACE}"
  note "Using Wi-Fi MAC address: ${WIFI_MAC}"
  if [[ -n "${UPLINK_WIFI_IFACE:-}" ]]; then
    note "Keeping internal Wi-Fi active for internet downloads: ${UPLINK_WIFI_IFACE}"
  else
    note "No separate internal Wi-Fi detected; pre-pull will use the current host connectivity."
  fi
}

# -----------------------------------------------------------------------------
# Runtime configuration and generated application files
# -----------------------------------------------------------------------------

generate_secrets() {
  local previous_env="${BACKUP_ROOT}/env.last"

  JWT_SECRET="${DANILO_JWT_SECRET:-}"
  POSTGRES_PASSWORD="${DANILO_POSTGRES_PASSWORD:-}"
  ADMIN_USERNAME="${DANILO_ADMIN_USERNAME:-ADMIN}"
  ADMIN_PASSWORD="${DANILO_ADMIN_PASSWORD:-}"

  if [[ -f "${previous_env}" ]]; then
    [[ -z "${JWT_SECRET}" ]] && JWT_SECRET="$(grep -E '^JWT_SECRET=' "${previous_env}" | tail -n1 | cut -d= -f2- || true)"
    [[ -z "${POSTGRES_PASSWORD}" ]] && POSTGRES_PASSWORD="$(grep -E '^POSTGRES_PASSWORD=' "${previous_env}" | tail -n1 | cut -d= -f2- || true)"
    [[ -z "${ADMIN_PASSWORD}" ]] && ADMIN_PASSWORD="$(grep -E '^ADMIN_PASSWORD=' "${previous_env}" | tail -n1 | cut -d= -f2- || true)"
  fi

  [[ -z "${JWT_SECRET}" ]] && JWT_SECRET="$(openssl rand -hex 32 | tr -d '\r\n')"
  [[ -z "${POSTGRES_PASSWORD}" ]] && POSTGRES_PASSWORD="$(openssl rand -hex 24 | tr -d '\r\n')"
  [[ -z "${ADMIN_PASSWORD}" ]] && ADMIN_PASSWORD="$(openssl rand -base64 24 | tr -d '=+/' | cut -c1-20)"
}

install_logrotate_config() {
  backup_managed_file /etc/logrotate.d/danilo-install
  cat > /etc/logrotate.d/danilo-install <<EOF
${LOG_FILE} {
  weekly
  rotate 8
  compress
  delaycompress
  missingok
  notifempty
  copytruncate
  create 0640 root adm
}
EOF
}

write_env_file() {
  mkdir -p "${BACKUP_ROOT}"
  cat > "${APP_ROOT}/.env" <<EOF
DATABASE_URL=postgresql+psycopg://danilo:${POSTGRES_PASSWORD}@postgres:5432/danilo
POSTGRES_DB=danilo
POSTGRES_USER=danilo
POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
JWT_SECRET=${JWT_SECRET}
JWT_EXPIRE_MINUTES=720
OLLAMA_URL=http://ollama:11434
OLLAMA_MODEL=${OLLAMA_MODEL}
ADMIN_USERNAME=${ADMIN_USERNAME}
ADMIN_PASSWORD=${ADMIN_PASSWORD}
PORTAL_DOMAIN=${PORTAL_DOMAIN}
EOF
  chmod 0600 "${APP_ROOT}/.env"
  install -m 0600 "${APP_ROOT}/.env" "${BACKUP_ROOT}/env.last"
  note "Runtime secrets were written with restricted file permissions"
}

sync_lessons_content() {
  if [[ ! -d "${LOCAL_LESSONS_DIR}" ]]; then
    echo "Local lessons folder not found: ${LOCAL_LESSONS_DIR}"
    exit 1
  fi

  mkdir -p "${CONTENT_ROOT}"
  note "Syncing lesson files into ${CONTENT_ROOT}"

  if command -v rsync >/dev/null 2>&1; then
    rsync -a --delete "${LOCAL_LESSONS_DIR}/" "${CONTENT_ROOT}/"
    return 0
  fi

  note "rsync not available; falling back to a full content refresh"
  find "${CONTENT_ROOT}" -mindepth 1 -maxdepth 1 -exec rm -rf -- {} +
  cp -a "${LOCAL_LESSONS_DIR}/." "${CONTENT_ROOT}/"
}

restart_gateway_container() {
  if [[ ! -f "${APP_ROOT}/docker-compose.yml" ]]; then
    echo "Project DANILO is not installed yet. Expected compose file at ${APP_ROOT}/docker-compose.yml"
    exit 1
  fi

  systemctl enable --now docker >/dev/null 2>&1 || true
  note "Refreshing the gateway container"
  if ! docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" restart gateway; then
    docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" up -d --no-deps gateway
  fi
}

run_sync_mode() {
  printf '\n[SYNC MODE] Updating offline lesson content and refreshing the DANILO gateway\n'
  sync_lessons_content
  restart_gateway_container
  cat <<EOF

${BOLD}Lesson sync complete.${RESET}
${BOLD}Updated source:${RESET} ${LOCAL_LESSONS_DIR}
${BOLD}Deployed to:${RESET} ${CONTENT_ROOT}
${BOLD}Portal URL:${RESET} http://${PORTAL_DOMAIN}
EOF
}

write_backend_files() {
  mkdir -p "${APP_ROOT}/backend/app" "${CONTENT_ROOT}"

  cat > "${APP_ROOT}/backend/requirements.txt" <<'EOF'
fastapi==0.115.12
uvicorn[standard]==0.34.2
sqlalchemy==2.0.40
psycopg[binary]==3.2.6
PyJWT==2.10.1
httpx==0.28.1
pydantic[email]==2.11.3
EOF

  cat > "${APP_ROOT}/backend/Dockerfile" <<'EOF'
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
EOF

  cat > "${APP_ROOT}/backend/app/__init__.py" <<'EOF'
# Project DANILO backend package
EOF

  cat > "${APP_ROOT}/backend/app/database.py" <<'EOF'
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL must be set by the installer-generated environment")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
EOF

  cat > "${APP_ROOT}/backend/app/models.py" <<'EOF'
from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, String, Text, UniqueConstraint, func
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = (
        CheckConstraint("role IN ('admin', 'teacher', 'student')", name="ck_users_role"),
    )

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(20), nullable=False)
    username = Column(String(120), nullable=False, unique=True, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    full_name = Column(String(255), nullable=False)
    grade_level = Column(String(50), nullable=True)
    section_name = Column(String(120), nullable=True)
    password_salt = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    taught_courses = relationship("Course", back_populates="teacher", foreign_keys="Course.teacher_id")
    enrollments = relationship("Enrollment", back_populates="student")


class Course(Base):
    __tablename__ = "courses"
    __table_args__ = (
        CheckConstraint("quarter IN ('Q1', 'Q2', 'Q3', 'Q4')", name="ck_courses_quarter"),
    )

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), nullable=False, unique=True)
    title = Column(String(255), nullable=False)
    subject = Column(String(120), nullable=False)
    grade_level = Column(String(50), nullable=False)
    quarter = Column(String(2), nullable=False)
    school_year = Column(String(20), nullable=False)
    description = Column(Text, nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    teacher = relationship("User", back_populates="taught_courses")
    enrollments = relationship("Enrollment", back_populates="course")
    modules = relationship("Module", back_populates="course")
    posts = relationship("StreamPost", back_populates="course")
    grades = relationship("GradeEntry", back_populates="course")


class Enrollment(Base):
    __tablename__ = "enrollments"
    __table_args__ = (
        UniqueConstraint("course_id", "student_id", name="uq_course_student"),
    )

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String(30), nullable=False, default="active")
    enrolled_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    course = relationship("Course", back_populates="enrollments")
    student = relationship("User", back_populates="enrollments")


class Module(Base):
    __tablename__ = "modules"
    __table_args__ = (
        CheckConstraint("quarter IN ('Q1', 'Q2', 'Q3', 'Q4')", name="ck_modules_quarter"),
    )

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    melc_code = Column(String(120), nullable=False)
    grade_level = Column(String(50), nullable=False)
    subject = Column(String(120), nullable=False)
    quarter = Column(String(2), nullable=False)
    week = Column(Integer, nullable=False)
    sequence_order = Column(Integer, nullable=False, default=1)
    folder_name = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    summary = Column(Text, nullable=False)
    essential_question = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    course = relationship("Course", back_populates="modules")
    conversations = relationship("AIConversation", back_populates="module")


class StreamPost(Base):
    __tablename__ = "stream_posts"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    post_type = Column(String(40), nullable=False, default="announcement")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    course = relationship("Course", back_populates="posts")
    author = relationship("User")


class GradeEntry(Base):
    __tablename__ = "grade_entries"
    __table_args__ = (
        CheckConstraint("quarter IN ('Q1', 'Q2', 'Q3', 'Q4')", name="ck_grade_entries_quarter"),
    )

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    quarter = Column(String(2), nullable=False)
    component = Column(String(80), nullable=False)
    score = Column(Float, nullable=False)
    max_score = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    remarks = Column(Text, nullable=True)
    recorded_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    course = relationship("Course", back_populates="grades")
    student = relationship("User", foreign_keys=[student_id])
    recorder = relationship("User", foreign_keys=[recorded_by])


class AIConversation(Base):
    __tablename__ = "ai_conversations"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=True)
    module_id = Column(Integer, ForeignKey("modules.id"), nullable=True)
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    student = relationship("User")
    course = relationship("Course")
    module = relationship("Module", back_populates="conversations")
EOF

  cat > "${APP_ROOT}/backend/app/security.py" <<'EOF'
import hashlib
import hmac
import os
import secrets
from datetime import datetime, timedelta, timezone

import jwt

PBKDF2_ITERATIONS = 310000
PBKDF2_DIGEST = "sha256"


def hash_password(password: str) -> tuple[str, str]:
    clean_password = str(password).encode("utf-8")
    salt = secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac(PBKDF2_DIGEST, clean_password, bytes.fromhex(salt), PBKDF2_ITERATIONS)
    return salt, digest.hex()


def verify_password(password: str, salt_hex: str, stored_hash_hex: str) -> bool:
    try:
        salt = bytes.fromhex(str(salt_hex).strip())
        stored_hash = str(stored_hash_hex).strip().lower()
    except ValueError:
        return False
    digest = hashlib.pbkdf2_hmac(PBKDF2_DIGEST, str(password).encode("utf-8"), salt, PBKDF2_ITERATIONS)
    return hmac.compare_digest(digest.hex(), stored_hash)


def create_access_token(payload: dict, secret: str, expires_minutes: int) -> str:
    claims = payload.copy()
    claims["exp"] = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    return jwt.encode(claims, secret, algorithm="HS256")


def decode_access_token(token: str, secret: str) -> dict:
    return jwt.decode(token, secret, algorithms=["HS256"])
EOF

  cat > "${APP_ROOT}/backend/app/schemas.py" <<'EOF'
from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str = Field(min_length=1, max_length=255)
    password: str = Field(min_length=1, max_length=255)


class TutorRequest(BaseModel):
    question: str = Field(min_length=4)
    module_id: int | None = None
    course_id: int | None = None
EOF

  cat > "${APP_ROOT}/backend/app/seed.py" <<'EOF'
from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import User
from .security import hash_password


def clean_seed_text(value: str | None) -> str | None:
    if value is None:
        return None
    cleaned = "".join(ch for ch in value.replace("\r", " ").replace("\n", " ") if ord(ch) < 128)
    cleaned = " ".join(cleaned.split())
    return cleaned or None


def get_or_create_user(
    session: Session,
    *,
    role: str,
    username: str,
    email: str,
    full_name: str,
    password: str,
    grade_level: str | None = None,
    section_name: str | None = None,
) -> User:
    user = session.scalar(select(User).where(User.username == username))
    if user:
        return user

    username = clean_seed_text(username) or ""
    email = clean_seed_text(email) or ""
    full_name = clean_seed_text(full_name) or ""
    password = clean_seed_text(password) or ""
    grade_level = clean_seed_text(grade_level)
    section_name = clean_seed_text(section_name)

    salt, digest = hash_password(password)
    user = User(
        role=role,
        username=username,
        email=email,
        full_name=full_name,
        grade_level=grade_level,
        section_name=section_name,
        password_salt=salt,
        password_hash=digest,
        is_active=True,
    )
    session.add(user)
    session.flush()
    return user


def reset_password(user: User, password: str) -> None:
    salt, digest = hash_password(clean_seed_text(password) or "")
    user.password_salt = salt
    user.password_hash = digest


def seed_defaults(
    session: Session,
    *,
    admin_username: str,
    admin_password: str,
) -> None:
    clean_username = clean_seed_text(admin_username) or "ADMIN"
    clean_password = clean_seed_text(admin_password)
    if not clean_password:
        raise RuntimeError("ADMIN_PASSWORD must be set by the installer environment")

    for user in session.scalars(select(User)).all():
        if user.username != clean_username:
            user.is_active = False

    admin = session.scalar(
        select(User).where(User.username == clean_username)
    )
    if admin:
        admin.role = "admin"
        admin.email = "admin@danilo.local"
        admin.full_name = "Danilo Network Administrator"
        admin.grade_level = None
        admin.section_name = None
        admin.is_active = True
        reset_password(admin, clean_password)
    else:
        get_or_create_user(
            session,
            role="admin",
            username=clean_username,
            email="admin@danilo.local",
            full_name="Danilo Network Administrator",
            password=clean_password,
        )

    session.commit()
EOF

  cat > "${APP_ROOT}/backend/app/main.py" <<'EOF'
import os
from contextlib import asynccontextmanager
from datetime import datetime, timezone

import httpx
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from .database import Base, SessionLocal, engine, get_db
from .models import AIConversation, Course, Enrollment, GradeEntry, Module, StreamPost, User
from .schemas import LoginRequest, TutorRequest
from .seed import seed_defaults
from .security import create_access_token, decode_access_token, verify_password

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", "720"))
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b-instruct-q4_K_M")
PORTAL_DOMAIN = os.getenv("PORTAL_DOMAIN", "danilo.local")

if not JWT_SECRET:
    raise RuntimeError("JWT_SECRET must be set by the installer environment")

security = HTTPBearer()
router = APIRouter(prefix="/api")


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_defaults(
            db,
            admin_username=os.getenv("ADMIN_USERNAME", "ADMIN"),
            admin_password=os.getenv("ADMIN_PASSWORD", ""),
        )
    finally:
        db.close()
    yield


app = FastAPI(title="Project DANILO API", version="1.0.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
) -> User:
    try:
        payload = decode_access_token(credentials.credentials, JWT_SECRET)
    except Exception as exc:  # pragma: no cover
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from exc

    user = db.get(User, payload.get("sub"))
    if not user or not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Account is inactive")
    return user


def serialize_user(user: User) -> dict:
    return {
        "id": user.id,
        "role": user.role,
        "username": user.username,
        "email": user.email,
        "fullName": user.full_name,
        "gradeLevel": user.grade_level,
        "sectionName": user.section_name,
    }


def build_grade_summary(db: Session, student_id: int) -> list[dict]:
    rows = (
        db.execute(
            select(GradeEntry, Course)
            .join(Course, GradeEntry.course_id == Course.id)
            .where(GradeEntry.student_id == student_id)
            .order_by(Course.subject.asc(), GradeEntry.quarter.asc(), GradeEntry.created_at.asc())
        )
        .all()
    )

    buckets: dict[tuple[int, str], dict] = {}
    for grade, course in rows:
        key = (course.id, grade.quarter)
        bucket = buckets.setdefault(
            key,
            {
                "courseId": course.id,
                "courseCode": course.code,
                "courseTitle": course.title,
                "subject": course.subject,
                "quarter": grade.quarter,
                "teacher": course.teacher.full_name if course.teacher else "",
                "components": [],
                "weightedScore": 0.0,
                "weightTotal": 0.0,
            },
        )
        normalized = (grade.score / grade.max_score) * 100.0 if grade.max_score else 0.0
        bucket["components"].append(
            {
                "component": grade.component,
                "score": grade.score,
                "maxScore": grade.max_score,
                "weight": grade.weight,
                "remarks": grade.remarks or "",
                "percentage": round(normalized, 2),
            }
        )
        bucket["weightedScore"] += normalized * grade.weight
        bucket["weightTotal"] += grade.weight

    summary = []
    for bucket in buckets.values():
        total = bucket["weightedScore"] / bucket["weightTotal"] if bucket["weightTotal"] else 0.0
        bucket["finalGrade"] = round(total, 2)
        bucket.pop("weightedScore")
        bucket.pop("weightTotal")
        summary.append(bucket)
    return sorted(summary, key=lambda item: (item["subject"], item["quarter"]))


def build_content_tree(db: Session, *, query: str | None = None, quarter: str | None = None, subject: str | None = None) -> list[dict]:
    stmt = (
        select(Module, Course)
        .join(Course, Module.course_id == Course.id)
        .order_by(Module.grade_level.asc(), Module.subject.asc(), Module.quarter.asc(), Module.week.asc(), Module.sequence_order.asc())
    )
    if query:
        like_query = f"%{query.strip()}%"
        stmt = stmt.where(or_(Module.title.ilike(like_query), Module.summary.ilike(like_query), Module.folder_name.ilike(like_query)))
    if quarter:
        stmt = stmt.where(Module.quarter == quarter)
    if subject:
        stmt = stmt.where(Module.subject == subject)

    rows = db.execute(stmt).all()
    items = []
    for module, course in rows:
        items.append(
            {
                "id": module.id,
                "courseId": course.id,
                "courseCode": course.code,
                "courseTitle": course.title,
                "subject": module.subject,
                "gradeLevel": module.grade_level,
                "quarter": module.quarter,
                "week": module.week,
                "folderName": module.folder_name,
                "melcCode": module.melc_code,
                "title": module.title,
                "summary": module.summary,
                "essentialQuestion": module.essential_question,
                "pdfUrl": f"/api/content/{module.id}/pdf",
            }
        )
    return items


def build_stream(db: Session) -> list[dict]:
    rows = (
        db.execute(
            select(StreamPost, Course, User)
            .join(Course, StreamPost.course_id == Course.id)
            .join(User, StreamPost.author_id == User.id)
            .order_by(StreamPost.created_at.desc())
            .limit(12)
        )
        .all()
    )
    return [
        {
            "id": post.id,
            "title": post.title,
            "body": post.body,
            "postType": post.post_type,
            "createdAt": post.created_at.isoformat() if post.created_at else "",
            "courseCode": course.code,
            "courseTitle": course.title,
            "authorName": author.full_name,
        }
        for post, course, author in rows
    ]


def build_teacher_course_cards(db: Session, teacher_id: int) -> list[dict]:
    courses = db.scalars(select(Course).where(Course.teacher_id == teacher_id).order_by(Course.subject.asc())).all()
    cards = []
    for course in courses:
        student_total = db.query(Enrollment).filter(Enrollment.course_id == course.id).count()
        module_total = db.query(Module).filter(Module.course_id == course.id).count()
        cards.append(
            {
                "id": course.id,
                "code": course.code,
                "title": course.title,
                "subject": course.subject,
                "quarter": course.quarter,
                "studentTotal": student_total,
                "moduleTotal": module_total,
                "description": course.description,
            }
        )
    return cards


def build_admin_course_cards(db: Session) -> list[dict]:
    courses = db.scalars(select(Course).order_by(Course.subject.asc(), Course.quarter.asc())).all()
    cards = []
    for course in courses:
        student_total = db.query(Enrollment).filter(Enrollment.course_id == course.id).count()
        module_total = db.query(Module).filter(Module.course_id == course.id).count()
        cards.append(
            {
                "id": course.id,
                "code": course.code,
                "title": course.title,
                "subject": course.subject,
                "quarter": course.quarter,
                "studentTotal": student_total,
                "moduleTotal": module_total,
                "teacherName": course.teacher.full_name if course.teacher else "Unassigned",
                "description": course.description,
            }
        )
    return cards


def build_student_course_cards(db: Session, student_id: int) -> list[dict]:
    rows = (
        db.execute(
            select(Course)
            .join(Enrollment, Enrollment.course_id == Course.id)
            .where(Enrollment.student_id == student_id)
            .order_by(Course.subject.asc())
        )
        .scalars()
        .all()
    )
    return [
        {
            "id": course.id,
            "code": course.code,
            "title": course.title,
            "subject": course.subject,
            "quarter": course.quarter,
            "description": course.description,
        }
        for course in rows
    ]


def escape_pdf_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def build_pdf_document(title: str, lines: list[str]) -> bytes:
    content = ["BT", "/F1 24 Tf", "72 740 Td", f"({escape_pdf_text(title)}) Tj", "/F1 13 Tf"]
    for line in lines:
        content.append("0 -26 Td")
        content.append(f"({escape_pdf_text(line)}) Tj")
    content.append("ET")
    stream = "\n".join(content).encode("latin-1", "replace")

    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Count 1 /Kids [3 0 R] >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        f"<< /Length {len(stream)} >>\nstream\n".encode("latin-1") + stream + b"\nendstream",
    ]

    pdf = b"%PDF-1.4\n"
    offsets = [0]
    for index, obj in enumerate(objects, start=1):
        offsets.append(len(pdf))
        pdf += f"{index} 0 obj\n".encode("latin-1") + obj + b"\nendobj\n"

    xref_offset = len(pdf)
    pdf += f"xref\n0 {len(objects) + 1}\n".encode("latin-1")
    pdf += b"0000000000 65535 f \n"
    for offset in offsets[1:]:
        pdf += f"{offset:010d} 00000 n \n".encode("latin-1")
    pdf += f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode("latin-1")
    return pdf


async def ask_ollama(prompt: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "stream": False,
        "prompt": prompt,
        "options": {
            "temperature": 0.3,
            "num_ctx": 2048,
            "num_predict": 350,
        },
    }
    async with httpx.AsyncClient(timeout=180) as client:
        response = await client.post(f"{OLLAMA_URL}/api/generate", json=payload)
        response.raise_for_status()
        body = response.json()
        return body.get("response", "").strip()


@router.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "service": "project-danilo",
        "model": OLLAMA_MODEL,
        "portalDomain": PORTAL_DOMAIN,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.post("/auth/login")
def login(payload: LoginRequest, db: Session = Depends(get_db)) -> dict:
    lookup = payload.username.strip()
    user = db.scalar(
        select(User).where(
            or_(User.username == lookup, User.email == lookup)
        )
    )
    if not user or not user.is_active or not verify_password(payload.password, user.password_salt, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    token = create_access_token({"sub": user.id, "role": user.role}, JWT_SECRET, JWT_EXPIRE_MINUTES)
    return {
        "accessToken": token,
        "tokenType": "Bearer",
        "user": serialize_user(user),
    }


@router.get("/me")
def me(current_user: User = Depends(get_current_user)) -> dict:
    return serialize_user(current_user)


@router.get("/dashboard")
def dashboard(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> dict:
    grade_summary = build_grade_summary(db, current_user.id) if current_user.role == "student" else []
    if current_user.role == "admin":
        courses = build_admin_course_cards(db)
    elif current_user.role == "teacher":
        courses = build_teacher_course_cards(db, current_user.id)
    else:
        courses = build_student_course_cards(db, current_user.id)

    return {
        "user": serialize_user(current_user),
        "stream": build_stream(db),
        "courses": courses,
        "contentFolders": build_content_tree(db),
        "grades": grade_summary,
        "network": {
            "ssid": "PROJECT-DANILO",
            "portal": f"http://{PORTAL_DOMAIN}",
            "mode": "offline-first captive portal",
        },
        "operationsHighlights": [
            {"label": "Portal", "value": f"http://{PORTAL_DOMAIN}"},
            {"label": "SSID", "value": "PROJECT-DANILO"},
            {"label": "AI Model", "value": OLLAMA_MODEL},
        ],
    }


@router.get("/stream")
def stream(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> list[dict]:
    _ = current_user
    return build_stream(db)


@router.get("/content")
def content(
    query: str | None = None,
    quarter: str | None = None,
    subject: str | None = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[dict]:
    _ = current_user
    return build_content_tree(db, query=query, quarter=quarter, subject=subject)


@router.get("/grades")
def grades(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> list[dict]:
    if current_user.role != "student":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Grades are only available to student accounts")
    return build_grade_summary(db, current_user.id)


@router.get("/content/{module_id}/pdf")
def content_pdf(module_id: int, db: Session = Depends(get_db)) -> Response:
    module = db.get(Module, module_id)
    if not module:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson module not found")

    lines = [
        f"MELC: {module.melc_code}",
        f"Folder: {module.folder_name}",
        f"Week {module.week} | Quarter {module.quarter}",
        f"Summary: {module.summary}",
        f"Guide Question: {module.essential_question}",
        "Prepared for offline classroom delivery through Project DANILO.",
    ]
    pdf_bytes = build_pdf_document(module.title, lines)
    headers = {"Content-Disposition": f'inline; filename="{module.title.lower().replace(" ", "-")}.pdf"'}
    return Response(content=pdf_bytes, media_type="application/pdf", headers=headers)


@router.post("/ai/tutor")
async def tutor(
    payload: TutorRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict:
    module = db.get(Module, payload.module_id) if payload.module_id else None
    course = db.get(Course, payload.course_id) if payload.course_id else (module.course if module else None)

    student_grades = build_grade_summary(db, current_user.id) if current_user.role == "student" else []
    grade_lines = [
        f"{item['courseCode']} {item['quarter']}: final grade {item['finalGrade']}"
        for item in student_grades
    ] or ["No recorded grades yet."]

    lesson_lines = [
        f"Course: {course.title}" if course else "Course: not specified",
        f"Module: {module.title}" if module else "Module: not specified",
        f"MELC: {module.melc_code}" if module else "MELC: not specified",
        f"Folder: {module.folder_name}" if module else "Folder: not specified",
        f"Summary: {module.summary}" if module else "Summary: not specified",
        f"Essential Question: {module.essential_question}" if module else "Essential Question: not specified",
    ]

    prompt = "\n".join(
        [
            "You are DANILO Tutor, an offline academic coach for DepEd last-mile schools in the Philippines.",
            "Teach clearly, use simple language, and adapt explanations to the learner's level.",
            "Offer short examples using school, home, or community situations when helpful.",
            "",
            f"Learner: {current_user.full_name}",
            f"Grade Level: {current_user.grade_level or 'Not specified'}",
            f"Section: {current_user.section_name or 'Not specified'}",
            "Recorded Grades:",
            *[f"- {line}" for line in grade_lines],
            "",
            "Lesson Context:",
            *[f"- {line}" for line in lesson_lines],
            "",
            "Student Question:",
            payload.question.strip(),
            "",
            "Response Format:",
            "1. Answer directly.",
            "2. Explain step by step.",
            "3. Give one short practice task.",
            "4. End with one encouragement line.",
        ]
    )

    try:
        answer = await ask_ollama(prompt)
    except Exception:
        answer = (
            "The local AI model is still warming up. Please try again in a minute. "
            "The lesson and grade context were prepared successfully."
        )

    db.add(
        AIConversation(
            student_id=current_user.id,
            course_id=course.id if course else None,
            module_id=module.id if module else None,
            prompt=payload.question.strip(),
            response=answer,
        )
    )
    db.commit()

    return {
        "answer": answer,
        "context": {
            "moduleTitle": module.title if module else None,
            "courseTitle": course.title if course else None,
            "gradeSignals": grade_lines,
        },
    }


app.include_router(router)
EOF
}

write_frontend_files() {
  mkdir -p "${APP_ROOT}/frontend/src/components" "${APP_ROOT}/frontend/public/icons"

  #  package.json 
  cat > "${APP_ROOT}/frontend/package.json" <<'EOF'
{
  "name": "project-danilo-frontend",
  "version": "2.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite --host 0.0.0.0 --port 5173",
    "build": "vite build",
    "preview": "vite preview --host 0.0.0.0 --port 4173"
  },
  "dependencies": {
    "@fontsource/inter": "^5.0.17",
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.4.1",
    "autoprefixer": "^10.4.21",
    "postcss": "^8.5.3",
    "tailwindcss": "^3.4.17",
    "vite": "^6.3.1"
  }
}
EOF

  #  vite.config.js 
  cat > "${APP_ROOT}/frontend/vite.config.js" <<'EOF'
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    host: "0.0.0.0",
    port: 5173,
  },
});
EOF

  #  postcss.config.js 
  cat > "${APP_ROOT}/frontend/postcss.config.js" <<'EOF'
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
EOF

  #  tailwind.config.js  UPDATED with glass shadows + richer palette 
  cat > "${APP_ROOT}/frontend/tailwind.config.js" <<'EOF'
/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        danilo: {
          blue:       "#1d4ed8",
          "blue-700": "#1e40af",
          gold:       "#d4a017",
          "gold-100": "#fef3c7",
          cloud:      "#f8fafc",
          ink:        "#0f172a",
          emerald:    "#059669",
        }
      },
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"]
      },
      boxShadow: {
        soft:        "0 4px 24px -4px rgba(15,23,42,0.10), 0 1px 4px rgba(15,23,42,0.06)",
        glass:       "0 8px 32px rgba(15,23,42,0.08), 0 2px 8px rgba(15,23,42,0.04), inset 0 1px 0 rgba(255,255,255,0.60)",
        "glass-dark":"0 8px 32px rgba(0,0,0,0.40), inset 0 1px 0 rgba(255,255,255,0.06)",
        "card-hover":"0 16px 48px -8px rgba(29,78,216,0.22)",
        "gold-glow": "0 8px 24px rgba(212,160,23,0.30)",
      },
      borderRadius: {
        "4xl": "2rem",
        "5xl": "2.5rem",
      },
      backdropBlur: {
        xs: "4px",
      }
    }
  },
  plugins: []
};
EOF

  #  index.html  updated theme-color + body background 
  cat > "${APP_ROOT}/frontend/index.html" <<'EOF'
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
    <meta name="theme-color" content="#1d4ed8" />
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-status-bar-style" content="default" />
    <meta name="description" content="Project DANILO - offline LMS and AI Tutor for last-mile schools." />
    <link rel="manifest" href="/manifest.webmanifest" />
    <title>Project DANILO</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
EOF

  #  manifest.webmanifest 
  cat > "${APP_ROOT}/frontend/public/manifest.webmanifest" <<'EOF'
{
  "name": "Project DANILO",
  "short_name": "DANILO",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#eff6ff",
  "theme_color": "#1d4ed8",
  "description": "Digital Assistant Network for Interactive Learning Offline",
  "icons": [
    { "src": "/icons/icon-192.svg", "sizes": "192x192", "type": "image/svg+xml", "purpose": "any" },
    { "src": "/icons/icon-512.svg", "sizes": "512x512", "type": "image/svg+xml", "purpose": "any maskable" }
  ]
}
EOF

  #  sw.js 
  cat > "${APP_ROOT}/frontend/public/sw.js" <<'EOF'
const CACHE_NAME = "danilo-shell-v2";
const SHELL_FILES = ["/", "/index.html", "/manifest.webmanifest", "/icons/icon-192.svg", "/icons/icon-512.svg"];

self.addEventListener("install", (event) => {
  event.waitUntil(caches.open(CACHE_NAME).then((cache) => cache.addAll(SHELL_FILES)));
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key)))
    )
  );
  self.clients.claim();
});

self.addEventListener("fetch", (event) => {
  const { request } = event;
  const url = new URL(request.url);
  if (request.method !== "GET") return;
  if (request.mode === "navigate") {
    event.respondWith(fetch(request).catch(() => caches.match("/index.html")));
    return;
  }
  if (url.origin === self.location.origin && ["/icons/", "/assets/"].some((p) => url.pathname.startsWith(p))) {
    event.respondWith(caches.match(request).then((cached) => cached || fetch(request)));
  }
});
EOF

  #  Icons (unchanged) 
  cat > "${APP_ROOT}/frontend/public/icons/icon-192.svg" <<'EOF'
<svg xmlns="http://www.w3.org/2000/svg" width="192" height="192" viewBox="0 0 192 192">
  <rect width="192" height="192" rx="42" fill="#1d4ed8"/>
  <rect x="18" y="18" width="156" height="156" rx="34" fill="#ffffff" opacity="0.10"/>
  <path d="M52 136V52h44c28 0 44 15 44 40 0 29-20 44-47 44H72v20H52zm20-36h21c16 0 27-7 27-20 0-12-9-19-25-19H72v39z" fill="#ffffff"/>
  <circle cx="142" cy="52" r="18" fill="#d4a017"/>
</svg>
EOF

  cat > "${APP_ROOT}/frontend/public/icons/icon-512.svg" <<'EOF'
<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="104" fill="#1d4ed8"/>
  <rect x="48" y="48" width="416" height="416" rx="80" fill="#ffffff" opacity="0.10"/>
  <path d="M136 366V146h118c75 0 122 40 122 107 0 76-55 113-129 113h-57v57H136zm54-112h52c45 0 78-20 78-58 0-36-27-56-71-56h-59v114z" fill="#ffffff"/>
  <circle cx="378" cy="140" r="42" fill="#d4a017"/>
</svg>
EOF

  #  main.jsx 
  cat > "${APP_ROOT}/frontend/src/main.jsx" <<'EOF'
import "@fontsource/inter/400.css";
import "@fontsource/inter/500.css";
import "@fontsource/inter/600.css";
import "@fontsource/inter/700.css";
import React from "react";
import ReactDOM from "react-dom/client";

import App from "./App";
import "./index.css";

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("/sw.js").catch(() => undefined);
  });
}

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
EOF

  #  index.css  FULL OVERHAUL  OKLCH + Glassmorphism + 2026 animations 
  cat > "${APP_ROOT}/frontend/src/index.css" <<'EOF'
@tailwind base;
@tailwind components;
@tailwind utilities;

/*  OKLCH Design Tokens  */
:root {
  /* Brand palette in OKLCH */
  --c-indigo:        oklch(44.5% 0.22 265);
  --c-indigo-light:  oklch(57% 0.19 265);
  --c-indigo-ghost:  oklch(97% 0.018 265);
  --c-gold:          oklch(71% 0.145 72);
  --c-gold-ghost:    oklch(98% 0.028 72);
  --c-emerald:       oklch(55% 0.19 155);
  --c-emerald-ghost: oklch(97% 0.025 155);
  --c-ink:           oklch(11% 0.025 265);
  --c-muted:         oklch(44% 0.015 265);
  --c-subtle:        oklch(62% 0.012 265);

  /* Glassmorphism surfaces */
  --glass-bg:            oklch(99% 0.004 258 / 0.80);
  --glass-border:        oklch(91% 0.018 258 / 0.65);
  --glass-shadow:        0 8px 32px oklch(11% 0.025 265 / 0.09),
                         0 2px 8px oklch(11% 0.025 265 / 0.05),
                         inset 0 1px 0 oklch(100% 0 0 / 0.65);

  --dark-glass-bg:       oklch(13% 0.035 265 / 0.94);
  --dark-glass-border:   oklch(28% 0.06 265 / 0.55);
  --dark-glass-shadow:   0 8px 32px oklch(0% 0 0 / 0.42),
                         inset 0 1px 0 oklch(100% 0 0 / 0.07);

  /* Typography */
  font-family: "Inter", system-ui, sans-serif;
  font-feature-settings: "cv11" 1, "ss01" 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--c-ink);
}

html { scroll-behavior: smooth; }

body {
  margin: 0;
  min-height: 100dvh;
  background:
    radial-gradient(ellipse 75% 55% at -8% -12%,
      oklch(71% 0.145 72 / 0.20) 0%, transparent 52%),
    radial-gradient(ellipse 65% 50% at 108% 108%,
      oklch(44.5% 0.22 265 / 0.18) 0%, transparent 50%),
    linear-gradient(172deg,
      oklch(97.5% 0.012 258) 0%,
      oklch(99.2% 0.003 240) 55%,
      oklch(97.8% 0.010 230) 100%);
  background-attachment: fixed;
}

#root {
  min-height: 100dvh;
  position: relative;
}

/*  Glassmorphism utilities  */
@layer components {
  .glass {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    box-shadow: var(--glass-shadow);
  }

  @supports (backdrop-filter: blur(1px)) {
    .glass {
      backdrop-filter: blur(20px) saturate(1.8);
      -webkit-backdrop-filter: blur(20px) saturate(1.8);
    }
  }

  .glass-dark {
    background: var(--dark-glass-bg);
    border: 1px solid var(--dark-glass-border);
    box-shadow: var(--dark-glass-shadow);
  }

  @supports (backdrop-filter: blur(1px)) {
    .glass-dark {
      backdrop-filter: blur(20px) saturate(1.5);
      -webkit-backdrop-filter: blur(20px) saturate(1.5);
    }
  }

  /* Subtle grid background decoration */
  .soft-grid {
    background-image:
      linear-gradient(oklch(44.5% 0.22 265 / 0.045) 1px, transparent 1px),
      linear-gradient(90deg, oklch(44.5% 0.22 265 / 0.045) 1px, transparent 1px);
    background-size: 36px 36px;
  }

  /* Network online status indicator */
  .status-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--c-emerald);
    flex-shrink: 0;
  }

  /* Touch-optimized button base */
  .btn-touch {
    min-height: 44px;
    min-width: 44px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
  }
}

/*  Animations  */
.fade-up  { animation: fadeUp 0.52s cubic-bezier(0.23, 1, 0.32, 1) both; }
.fade-in  { animation: fadeIn 0.38s ease both; }
.slide-up { animation: slideUp 0.40s cubic-bezier(0.23, 1, 0.32, 1) both; }

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(18px); }
  to   { opacity: 1; transform: translateY(0);    }
}

@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0);   }
}

@keyframes pulseRing {
  0%   { box-shadow: 0 0 0 0   oklch(55% 0.19 155 / 0.45); }
  70%  { box-shadow: 0 0 0 8px oklch(55% 0.19 155 / 0);    }
  100% { box-shadow: 0 0 0 0   oklch(55% 0.19 155 / 0);    }
}

@keyframes dotBounce {
  0%, 80%, 100% { transform: translateY(0);    opacity: 0.5; }
  40%            { transform: translateY(-6px); opacity: 1;   }
}

@keyframes shimmer {
  0%   { background-position: -200% center; }
  100% { background-position:  200% center; }
}

/* Animated status dot */
.status-dot-pulse {
  animation: pulseRing 2.2s ease-in-out infinite;
}

/* Shimmer text (hero login) */
.shimmer-text {
  background: linear-gradient(
    90deg,
    var(--c-ink) 25%,
    var(--c-indigo) 45%,
    var(--c-gold) 55%,
    var(--c-ink) 75%
  );
  background-size: 300% auto;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: shimmer 5s linear infinite;
}

/* Typing indicator dots */
.typing-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: oklch(57% 0.19 265);
}
.typing-dot:nth-child(1) { animation: dotBounce 1.2s ease-in-out 0.0s infinite; }
.typing-dot:nth-child(2) { animation: dotBounce 1.2s ease-in-out 0.2s infinite; }
.typing-dot:nth-child(3) { animation: dotBounce 1.2s ease-in-out 0.4s infinite; }

/* Reduced motion  respect user preference */
@media (prefers-reduced-motion: reduce) {
  .fade-up, .fade-in, .slide-up { animation: none; opacity: 1; transform: none; }
  .status-dot-pulse              { animation: none; }
  .shimmer-text                  { animation: none; -webkit-text-fill-color: var(--c-indigo); }
  .typing-dot                    { animation: none; opacity: 0.7; }
}

/*  Scrollbar  */
::-webkit-scrollbar        { width: 5px; height: 5px; }
::-webkit-scrollbar-track  { background: transparent; }
::-webkit-scrollbar-thumb  { background: oklch(44.5% 0.22 265 / 0.18); border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: oklch(44.5% 0.22 265 / 0.35); }

/*  Form element resets  */
input, select, textarea { font-family: inherit; }

/*  Safe area helpers (for notched phones)  */
.pb-safe-nav {
  padding-bottom: calc(68px + env(safe-area-inset-bottom, 0px));
}

/*  Stagger helpers  */
.stagger-1 { animation-delay: 60ms; }
.stagger-2 { animation-delay: 120ms; }
.stagger-3 { animation-delay: 180ms; }
.stagger-4 { animation-delay: 240ms; }
EOF

  #  api.js 
  cat > "${APP_ROOT}/frontend/src/api.js" <<'EOF'
const API_BASE = "/api";

function buildHeaders(token, extras = {}) {
  return {
    "Content-Type": "application/json",
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
    ...extras
  };
}

export async function apiRequest(path, { method = "GET", token, body } = {}) {
  const response = await fetch(`${API_BASE}${path}`, {
    method,
    headers: buildHeaders(token),
    body: body ? JSON.stringify(body) : undefined
  });

  const isJson = response.headers.get("content-type")?.includes("application/json");
  const payload = isJson ? await response.json() : await response.text();

  if (!response.ok) {
    const detail = typeof payload === "string" ? payload : payload?.detail || "Request failed";
    throw new Error(detail);
  }

  return payload;
}
EOF

  #  InstallBanner.jsx 
  cat > "${APP_ROOT}/frontend/src/components/InstallBanner.jsx" <<'EOF'
export default function InstallBanner({ promptEvent, onInstall, onDismiss }) {
  if (!promptEvent) return null;

  return (
    <div className="fade-up glass rounded-2xl p-4">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-xl bg-danilo-blue flex items-center justify-center flex-shrink-0">
            <svg className="w-5 h-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
          </div>
          <div>
            <p className="text-sm font-semibold text-slate-900">Install Project DANILO</p>
            <p className="text-xs text-slate-500">Add to home screen for a native app experience</p>
          </div>
        </div>
        <div className="flex items-center gap-2 ml-12 sm:ml-0">
          <button
            type="button"
            onClick={onDismiss}
            className="btn-touch rounded-xl border border-slate-200 bg-white/60 px-4 py-2 text-xs font-semibold text-slate-600 hover:bg-white transition-all"
          >
            Later
          </button>
          <button
            type="button"
            onClick={onInstall}
            className="btn-touch rounded-xl bg-danilo-blue px-4 py-2 text-xs font-bold text-white hover:bg-danilo-blue-700 transition-all"
          >
            Install
          </button>
        </div>
      </div>
    </div>
  );
}
EOF

  #  LoginView.jsx  CINEMATIC GLASSMORPHISM OVERHAUL 
  cat > "${APP_ROOT}/frontend/src/components/LoginView.jsx" <<'EOF'
export default function LoginView({ form, onChange, onSubmit, loading, error }) {
  return (
    <div className="relative min-h-screen overflow-hidden flex items-center justify-center p-4 py-10">

      {/* Atmospheric background orbs */}
      <div className="fixed inset-0 pointer-events-none" aria-hidden="true">
        <div style={{
          position: "absolute", top: "-20%", left: "-18%",
          width: "65vmax", height: "65vmax", borderRadius: "50%",
          background: "radial-gradient(circle, oklch(71% 0.145 72 / 0.32) 0%, transparent 65%)",
          filter: "blur(72px)"
        }} />
        <div style={{
          position: "absolute", bottom: "-25%", right: "-15%",
          width: "72vmax", height: "72vmax", borderRadius: "50%",
          background: "radial-gradient(circle, oklch(44.5% 0.22 265 / 0.28) 0%, transparent 60%)",
          filter: "blur(88px)"
        }} />
        <div className="absolute inset-0 soft-grid opacity-40" />
      </div>

      {/* Two-column layout: hero copy (desktop) + login card */}
      <div className="relative z-10 w-full max-w-5xl mx-auto flex flex-col lg:flex-row items-center gap-10 lg:gap-16">

        {/*  Left: Hero copy (hidden on mobile)  */}
        <section className="hidden lg:flex lg:flex-col lg:flex-1 fade-up">

          {/* Network status badge */}
          <div className="inline-flex items-center gap-2.5 glass rounded-full px-4 py-2 mb-8 self-start">
            <span className="status-dot status-dot-pulse" />
            <span className="text-xs font-bold text-slate-700 tracking-widest uppercase">
              Local School Network Active
            </span>
          </div>

          <h1 className="text-5xl xl:text-6xl font-bold leading-[1.08] text-slate-950 mb-6 tracking-tight">
            Teaching lives on,
            <br />
            <span className="shimmer-text">even offline.</span>
          </h1>

          <p className="text-base xl:text-lg text-slate-600 leading-relaxed mb-10 max-w-md">
            Project DANILO delivers a classroom stream, MELC-aligned lesson folders,
            and a local AI tutor through your school&apos;s own Wi-Fi hotspot.
            No internet required.
          </p>

        </section>

        {/*  Right: Login card  */}
        <section className="w-full max-w-sm mx-auto lg:mx-0 fade-up stagger-2 flex-shrink-0">

          {/* Mobile: logo + status */}
          <div className="lg:hidden flex flex-col items-center mb-8">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-11 h-11 rounded-2xl bg-danilo-blue flex items-center justify-center shadow-soft">
                <svg className="w-6 h-6 text-white" fill="none" viewBox="0 0 24 24">
                  <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"
                    stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
              </div>
              <div>
                <p className="text-xs font-bold text-danilo-blue uppercase tracking-widest">Project</p>
                <p className="text-xl font-bold text-slate-950 leading-none">DANILO</p>
              </div>
            </div>
            <div className="inline-flex items-center gap-2 glass rounded-full px-3 py-1.5">
              <span className="status-dot status-dot-pulse" />
              <span className="text-xs font-semibold text-slate-600">Local School Network</span>
            </div>
          </div>

          {/* Glass card */}
          <div className="glass rounded-[2rem] p-7 shadow-glass">

            {/* Card header */}
            <div className="flex items-start justify-between mb-7">
              <div>
                <p className="text-[10px] font-bold uppercase tracking-[0.18em] text-danilo-blue mb-1">
                  DepEd School Portal
                </p>
                <h2 className="text-2xl font-bold text-slate-950">Sign in</h2>
              </div>
              <div className="rounded-xl border border-amber-200 bg-danilo-gold-100 px-3 py-2 text-center">
                <p className="text-[10px] font-bold text-amber-800 uppercase tracking-wider leading-none">AI Tutor</p>
                <p className="text-[10px] font-semibold text-amber-700 mt-0.5">Offline-Ready</p>
              </div>
            </div>

            <form onSubmit={onSubmit} className="space-y-4">
              <div>
                <label className="block text-[10px] font-bold uppercase tracking-[0.18em] text-slate-500 mb-2">
                  Username
                </label>
                <input
                  name="username"
                  value={form.username}
                  onChange={onChange}
                  className="w-full rounded-xl border border-slate-200/90 bg-white/70 px-4 py-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition-all focus:border-danilo-blue focus:ring-2 focus:ring-blue-500/15 focus:bg-white"
                  placeholder="Enter your username"
                  autoComplete="username"
                  autoCapitalize="none"
                />
              </div>

              <div>
                <label className="block text-[10px] font-bold uppercase tracking-[0.18em] text-slate-500 mb-2">
                  Password
                </label>
                <input
                  type="password"
                  name="password"
                  value={form.password}
                  onChange={onChange}
                  className="w-full rounded-xl border border-slate-200/90 bg-white/70 px-4 py-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition-all focus:border-danilo-blue focus:ring-2 focus:ring-blue-500/15 focus:bg-white"
                  placeholder="Enter your password"
                  autoComplete="current-password"
                />
              </div>

              {error ? (
                <div className="rounded-xl border border-red-100 bg-red-50 px-4 py-3">
                  <p className="text-sm font-medium text-red-700">{error}</p>
                </div>
              ) : null}

              <button
                type="submit"
                disabled={loading}
                className="btn-touch w-full rounded-xl bg-danilo-blue px-4 py-3.5 text-sm font-bold text-white tracking-wide transition-all hover:brightness-110 hover:shadow-card-hover active:scale-[0.98] disabled:opacity-60 disabled:cursor-not-allowed"
              >
                {loading ? (
                  <span className="flex items-center justify-center gap-2">
                    <span className="w-4 h-4 rounded-full border-2 border-white/30 border-t-white animate-spin" />
                    Signing in...
                  </span>
                ) : "Launch Workspace"}
              </button>
            </form>

            <div className="mt-6 pt-5 border-t border-slate-100 flex items-center justify-center gap-2">
              <span className="status-dot" />
              <p className="text-xs text-slate-500">DepEd Last-Mile School Initiative | Offline-First</p>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}
EOF

  #  StreamView.jsx 
  cat > "${APP_ROOT}/frontend/src/components/StreamView.jsx" <<'EOF'
const POST_TYPE_CONFIG = {
  announcement: {
    badge: "bg-blue-50 text-danilo-blue border border-blue-100",
    bar: "bg-danilo-blue",
    label: "Announcement",
  },
  assignment: {
    badge: "bg-amber-50 text-amber-800 border border-amber-100",
    bar: "bg-danilo-gold",
    label: "Assignment",
  },
  reminder: {
    badge: "bg-emerald-50 text-emerald-800 border border-emerald-100",
    bar: "bg-danilo-emerald",
    label: "Reminder",
  },
};

function PostCard({ item, delay }) {
  const cfg = POST_TYPE_CONFIG[item.postType] || {
    badge: "bg-slate-50 text-slate-600 border border-slate-100",
    bar: "bg-slate-400",
    label: item.postType,
  };

  return (
    <article
      className="fade-up glass rounded-[1.75rem] overflow-hidden"
      style={{ animationDelay: `${delay}ms` }}
    >
      {/* Accent bar */}
      <div className={`h-1 w-full ${cfg.bar}`} />

      <div className="p-5 sm:p-6">
        <div className="flex flex-wrap items-center gap-2 mb-4">
          <span className={`rounded-full px-3 py-1 text-[10px] font-bold uppercase tracking-wider ${cfg.badge}`}>
            {cfg.label}
          </span>
          <span className="rounded-full bg-slate-100 px-3 py-1 text-[10px] font-bold uppercase tracking-wider text-slate-600">
            {item.courseCode}
          </span>
        </div>

        <h3 className="text-lg font-semibold text-slate-950 mb-2 leading-snug">{item.title}</h3>
        <p className="text-sm text-slate-600 leading-relaxed">{item.body}</p>

        <div className="mt-5 pt-4 border-t border-slate-100 flex flex-wrap items-center gap-x-3 gap-y-1 text-xs text-slate-400">
          <span className="font-medium text-slate-600">{item.courseTitle}</span>
          <span>|</span>
          <span>{item.authorName}</span>
          <span>|</span>
          <span>{new Date(item.createdAt).toLocaleString()}</span>
        </div>
      </div>
    </article>
  );
}

export default function StreamView({ items }) {
  return (
    <section className="space-y-4">
      <div className="mb-6">
        <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-danilo-blue mb-1">Stream</p>
        <h2 className="text-2xl font-bold text-slate-950">Class Updates</h2>
        <p className="text-sm text-slate-500 mt-1">Announcements, assignments, and reminders from your teachers.</p>
      </div>

      {!items || items.length === 0 ? (
        <div className="glass rounded-[1.75rem] p-10 text-center">
          <p className="text-sm text-slate-500">No posts in the stream yet.</p>
        </div>
      ) : (
        <div className="space-y-4">
          {items.map((item, i) => (
            <PostCard key={item.id} item={item} delay={i * 60} />
          ))}
        </div>
      )}
    </section>
  );
}
EOF

  #  ContentView.jsx 
  cat > "${APP_ROOT}/frontend/src/components/ContentView.jsx" <<'EOF'
const SUBJECT_CONFIG = {
  English:     { accent: "border-l-danilo-blue",    badge: "bg-blue-50 text-danilo-blue",     dot: "bg-danilo-blue" },
  Mathematics: { accent: "border-l-danilo-gold",    badge: "bg-amber-50 text-amber-800",       dot: "bg-danilo-gold" },
  Science:     { accent: "border-l-danilo-emerald", badge: "bg-emerald-50 text-emerald-800",   dot: "bg-danilo-emerald" },
};

function getSubjectConfig(subject) {
  return SUBJECT_CONFIG[subject] || { accent: "border-l-slate-300", badge: "bg-slate-50 text-slate-700", dot: "bg-slate-400" };
}

function ModuleCard({ item, delay }) {
  const cfg = getSubjectConfig(item.subject);

  return (
    <article
      className={`fade-up glass rounded-[1.75rem] overflow-hidden border-l-4 ${cfg.accent}`}
      style={{ animationDelay: `${delay}ms` }}
    >
      <div className="p-5 sm:p-6">
        <div className="flex flex-col gap-5 lg:flex-row lg:items-start lg:justify-between">

          {/* Left: lesson meta */}
          <div className="flex-1 min-w-0">
            <div className="flex flex-wrap items-center gap-2 mb-3">
              <span className={`rounded-full px-2.5 py-1 text-[10px] font-bold uppercase tracking-wider ${cfg.badge}`}>
                {item.subject}
              </span>
              <span className="rounded-full bg-slate-100 px-2.5 py-1 text-[10px] font-bold uppercase tracking-wider text-slate-600">
                {item.quarter} | Week {item.week}
              </span>
              <span className="rounded-full bg-slate-100 px-2.5 py-1 text-[10px] font-mono text-slate-500">
                {item.melcCode}
              </span>
            </div>

            <p className="text-[10px] font-semibold uppercase tracking-wider text-slate-400 mb-1.5">
              {item.folderName}
            </p>
            <h3 className="text-lg font-bold text-slate-950 mb-2 leading-snug">{item.title}</h3>
            <p className="text-sm text-slate-600 leading-relaxed mb-4">{item.summary}</p>

            <div className="rounded-xl bg-slate-50 border border-slate-100 px-4 py-3">
              <p className="text-[10px] font-bold uppercase tracking-wider text-slate-400 mb-1">Essential Question</p>
              <p className="text-sm font-medium text-slate-700 italic leading-relaxed">
                &ldquo;{item.essentialQuestion}&rdquo;
              </p>
            </div>
          </div>

          {/* Right: dark info + PDF button */}
          <div className="glass-dark rounded-2xl p-5 text-white lg:w-52 flex-shrink-0">
            <p className="text-[10px] font-bold uppercase tracking-widest text-blue-300 mb-2">{item.courseCode}</p>
            <p className="text-lg font-bold mb-1">{item.subject}</p>
            <div className="space-y-1 text-xs text-slate-300 mb-5">
              <p>{item.gradeLevel}</p>
              <p>{item.quarter} | Week {item.week}</p>
            </div>
            <a
              href={item.pdfUrl}
              target="_blank"
              rel="noreferrer"
              className="btn-touch flex items-center justify-center gap-1.5 w-full rounded-xl bg-danilo-gold px-4 py-2.5 text-xs font-bold text-slate-950 hover:brightness-110 transition-all"
            >
              <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2.5}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M12 10v6m0 0l-3-3m3 3l3-3M3 17V7a2 2 0 012-2h6l2 2h6a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2z" />
              </svg>
              Open PDF Lesson
            </a>
          </div>
        </div>
      </div>
    </article>
  );
}

export default function ContentView({ items, search, onSearchChange, quarter, onQuarterChange, subject, onSubjectChange }) {
  const subjects = [...new Set(items.map((item) => item.subject))];

  return (
    <section className="space-y-5">
      <div>
        <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-danilo-blue mb-1">Content Folder</p>
        <h2 className="text-2xl font-bold text-slate-950">MELC-Aligned Lessons</h2>
        <p className="text-sm text-slate-500 mt-1">Structured PDF modules for offline classroom delivery.</p>
      </div>

      {/* Filter bar */}
      <div className="glass rounded-2xl p-4">
        <div className="grid gap-3 sm:grid-cols-3">
          <div className="relative">
            <svg className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
            <input
              value={search}
              onChange={onSearchChange}
              placeholder="Search lessons..."
              className="btn-touch w-full rounded-xl border border-slate-200 bg-white/70 pl-9 pr-4 py-2.5 text-sm outline-none focus:border-danilo-blue focus:ring-2 focus:ring-blue-500/15 focus:bg-white transition-all"
            />
          </div>
          <select
            value={quarter}
            onChange={onQuarterChange}
            className="btn-touch w-full rounded-xl border border-slate-200 bg-white/70 px-4 py-2.5 text-sm outline-none focus:border-danilo-blue focus:ring-2 focus:ring-blue-500/15 transition-all"
          >
            <option value="">All Quarters</option>
            <option value="Q1">Q1</option>
            <option value="Q2">Q2</option>
            <option value="Q3">Q3</option>
            <option value="Q4">Q4</option>
          </select>
          <select
            value={subject}
            onChange={onSubjectChange}
            className="btn-touch w-full rounded-xl border border-slate-200 bg-white/70 px-4 py-2.5 text-sm outline-none focus:border-danilo-blue focus:ring-2 focus:ring-blue-500/15 transition-all"
          >
            <option value="">All Subjects</option>
            {subjects.map((s) => <option key={s} value={s}>{s}</option>)}
          </select>
        </div>
      </div>

      {items.length === 0 ? (
        <div className="glass rounded-[1.75rem] p-10 text-center">
          <p className="text-sm text-slate-500">No modules match your filters.</p>
        </div>
      ) : (
        <div className="space-y-4">
          {items.map((item, i) => (
            <ModuleCard key={item.id} item={item} delay={i * 50} />
          ))}
        </div>
      )}
    </section>
  );
}
EOF

  #  GradesView.jsx 
  cat > "${APP_ROOT}/frontend/src/components/GradesView.jsx" <<'EOF'
function gradeColor(score) {
  if (score >= 90) return { bar: "bg-danilo-emerald", text: "text-emerald-700", bg: "bg-emerald-50" };
  if (score >= 75) return { bar: "bg-danilo-blue",    text: "text-danilo-blue", bg: "bg-blue-50"   };
  if (score >= 60) return { bar: "bg-danilo-gold",    text: "text-amber-700",   bg: "bg-amber-50"  };
  return                   { bar: "bg-red-400",        text: "text-red-700",     bg: "bg-red-50"    };
}

export default function GradesView({ grades }) {
  return (
    <section className="space-y-5">
      <div>
        <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-danilo-blue mb-1">Grades</p>
        <h2 className="text-2xl font-bold text-slate-950">Performance Summary</h2>
        <p className="text-sm text-slate-500 mt-1">Four-quarter weighted grade view per subject.</p>
      </div>

      {!grades || grades.length === 0 ? (
        <div className="glass rounded-[1.75rem] border-2 border-dashed border-slate-200 p-10 text-center">
          <div className="w-12 h-12 rounded-2xl bg-slate-100 flex items-center justify-center mx-auto mb-4">
            <svg className="w-6 h-6 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z" />
            </svg>
          </div>
          <p className="text-sm font-semibold text-slate-600 mb-1">No grades available</p>
          <p className="text-xs text-slate-400">Grade summaries are only shown for student accounts.</p>
        </div>
      ) : (
        <div className="space-y-4">
          {grades.map((grade, i) => {
            const gc = gradeColor(grade.finalGrade);
            return (
              <article
                key={`${grade.courseId}-${grade.quarter}`}
                className="fade-up glass rounded-[1.75rem] overflow-hidden"
                style={{ animationDelay: `${i * 60}ms` }}
              >
                <div className="p-5 sm:p-6">
                  {/* Card header */}
                  <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between mb-5">
                    <div className="flex-1 min-w-0">
                      <p className="text-[10px] font-bold uppercase tracking-wider text-danilo-gold mb-1">{grade.subject}</p>
                      <h3 className="text-lg font-bold text-slate-950 leading-snug">{grade.courseTitle}</h3>
                      <p className="text-xs text-slate-500 mt-1">{grade.courseCode} | Quarter {grade.quarter}</p>
                      {grade.teacher && (
                        <p className="text-xs text-slate-400 mt-0.5">Teacher: {grade.teacher}</p>
                      )}
                    </div>

                    {/* Final grade badge */}
                    <div className={`rounded-2xl ${gc.bg} px-5 py-4 text-center flex-shrink-0 sm:min-w-[90px]`}>
                      <p className={`text-[10px] font-bold uppercase tracking-wider ${gc.text} mb-1`}>Final Grade</p>
                      <p className={`text-3xl font-bold ${gc.text}`}>{grade.finalGrade}</p>
                    </div>
                  </div>

                  {/* Grade bar */}
                  <div className="mb-5">
                    <div className="w-full h-2 rounded-full bg-slate-100 overflow-hidden">
                      <div
                        className={`h-full rounded-full ${gc.bar} transition-all duration-700`}
                        style={{ width: `${Math.min(100, grade.finalGrade)}%` }}
                      />
                    </div>
                    <div className="flex justify-between mt-1.5 text-[10px] text-slate-400">
                      <span>0</span>
                      <span>75 (passing)</span>
                      <span>100</span>
                    </div>
                  </div>

                  {/* Components table */}
                  <div className="overflow-hidden rounded-xl border border-slate-100">
                    <table className="min-w-full divide-y divide-slate-100 text-sm">
                      <thead>
                        <tr className="bg-slate-50">
                          <th className="px-4 py-2.5 text-left text-[10px] font-bold uppercase tracking-wider text-slate-500">Component</th>
                          <th className="px-4 py-2.5 text-left text-[10px] font-bold uppercase tracking-wider text-slate-500">Score</th>
                          <th className="px-4 py-2.5 text-left text-[10px] font-bold uppercase tracking-wider text-slate-500">Weight</th>
                          <th className="px-4 py-2.5 text-left text-[10px] font-bold uppercase tracking-wider text-slate-500 hidden sm:table-cell">Remarks</th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-slate-100 bg-white">
                        {grade.components.map((c) => (
                          <tr key={`${grade.courseId}-${grade.quarter}-${c.component}`}>
                            <td className="px-4 py-3 font-semibold text-slate-800">{c.component}</td>
                            <td className="px-4 py-3 text-slate-600">
                              {c.score}/{c.maxScore}
                              <span className="text-slate-400 text-xs ml-1">({c.percentage}%)</span>
                            </td>
                            <td className="px-4 py-3 text-slate-600">{Math.round(c.weight * 100)}%</td>
                            <td className="px-4 py-3 text-slate-500 italic text-xs hidden sm:table-cell">{c.remarks}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </article>
            );
          })}
        </div>
      )}
    </section>
  );
}
EOF

  #  TutorView.jsx  PREMIUM DARK AI CHAT INTERFACE 
  cat > "${APP_ROOT}/frontend/src/components/TutorView.jsx" <<'EOF'
function SparkleIcon() {
  return (
    <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.75}>
      <path strokeLinecap="round" strokeLinejoin="round"
        d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09z" />
    </svg>
  );
}

function TypingIndicator() {
  return (
    <div className="flex items-center gap-3 py-2">
      <div className="flex items-center gap-1.5">
        <span className="typing-dot" />
        <span className="typing-dot" />
        <span className="typing-dot" />
      </div>
      <p className="text-sm text-slate-400 italic">DANILO is thinking...</p>
    </div>
  );
}

export default function TutorView({ modules, form, onChange, onSubmit, loading, answer }) {
  return (
    <section className="grid gap-5 xl:grid-cols-[1fr_1.15fr]">

      {/*  Left: Input panel  */}
      <div className="glass rounded-[2rem] p-6">

        {/* Header */}
        <div className="flex items-center gap-3 mb-1">
          <div className="w-10 h-10 rounded-2xl bg-danilo-blue flex items-center justify-center text-white flex-shrink-0 shadow-soft">
            <SparkleIcon />
          </div>
          <div className="flex-1 min-w-0">
            <p className="text-[10px] font-bold uppercase tracking-[0.18em] text-danilo-blue">AI Tutor</p>
            <h2 className="text-xl font-bold text-slate-950 leading-tight">DANILO Tutor</h2>
          </div>
          <div className="rounded-xl border border-amber-200 bg-amber-50 px-2.5 py-1.5 text-center flex-shrink-0">
            <p className="text-[10px] font-bold text-amber-800 uppercase tracking-wider leading-none">Offline</p>
            <p className="text-[10px] font-semibold text-amber-700 mt-0.5">Ready</p>
          </div>
        </div>

        <p className="text-sm text-slate-500 leading-relaxed mb-6 mt-3">
          Blends your grade data, lesson context, and MELC code before sending a
          context-rich prompt to the local Ollama model. No internet required.
        </p>

        {/* Network status */}
        <div className="flex items-center gap-2.5 glass rounded-xl px-4 py-2.5 mb-6">
          <span className="status-dot status-dot-pulse" />
          <div>
            <p className="text-xs font-semibold text-slate-700 leading-none">Local School Network</p>
            <p className="text-[10px] text-slate-500 mt-0.5">AI model running on this device</p>
          </div>
        </div>

        <form onSubmit={onSubmit} className="space-y-4">
          <div>
            <label className="block text-[10px] font-bold uppercase tracking-[0.18em] text-slate-500 mb-2">
              Lesson Context
            </label>
            <select
              name="moduleId"
              value={form.moduleId}
              onChange={onChange}
              className="btn-touch w-full rounded-xl border border-slate-200 bg-white/70 px-4 py-3 text-sm text-slate-900 outline-none focus:border-danilo-blue focus:ring-2 focus:ring-blue-500/15 transition-all"
            >
              <option value="">Choose a module (optional)</option>
              {modules.map((module) => (
                <option key={module.id} value={module.id}>
                  {module.subject} | {module.title}
                </option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-[10px] font-bold uppercase tracking-[0.18em] text-slate-500 mb-2">
              Your Question
            </label>
            <textarea
              name="question"
              value={form.question}
              onChange={onChange}
              rows={5}
              className="w-full rounded-xl border border-slate-200 bg-white/70 px-4 py-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none resize-none focus:border-danilo-blue focus:ring-2 focus:ring-blue-500/15 focus:bg-white transition-all"
              placeholder="Explain this lesson in simpler words and give me one practice item."
            />
          </div>

          <button
            type="submit"
            disabled={loading || !form.question.trim()}
            className="btn-touch w-full rounded-xl bg-danilo-blue px-5 py-3.5 text-sm font-bold text-white tracking-wide transition-all hover:brightness-110 hover:shadow-card-hover active:scale-[0.98] disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? (
              <span className="flex items-center justify-center gap-2">
                <span className="w-4 h-4 rounded-full border-2 border-white/30 border-t-white animate-spin" />
                Consulting local model...
              </span>
            ) : (
              <span className="flex items-center justify-center gap-2">
                <SparkleIcon />
                Ask DANILO Tutor
              </span>
            )}
          </button>
        </form>
      </div>

      {/*  Right: Response panel (dark glass)  */}
      <div className="glass-dark rounded-[2rem] p-6 min-h-80 flex flex-col">

        {/* Panel header */}
        <div className="flex items-center justify-between mb-5 pb-4 border-b border-white/10">
          <div className="flex items-center gap-2.5">
            <div className="w-7 h-7 rounded-lg bg-white/10 flex items-center justify-center">
              <SparkleIcon />
            </div>
            <p className="text-xs font-bold uppercase tracking-widest text-blue-300">Response</p>
          </div>
          {answer?.context?.moduleTitle && (
            <span className="text-xs text-slate-400 truncate max-w-32">{answer.context.moduleTitle}</span>
          )}
        </div>

        {/* Content area */}
        <div className="flex-1">
          {loading ? (
            <TypingIndicator />
          ) : answer ? (
            <div className="slide-up space-y-4">
              {/* Answer bubble */}
              <div className="rounded-2xl bg-white/8 border border-white/12 p-5">
                <p className="text-sm text-slate-100 leading-relaxed whitespace-pre-wrap">
                  {answer.answer}
                </p>
              </div>

              {/* Grade signals */}
              {answer.context?.gradeSignals?.length > 0 && (
                <div>
                  <p className="text-[10px] font-bold uppercase tracking-[0.18em] text-slate-500 mb-2.5">
                    Grade Context Used
                  </p>
                  <div className="flex flex-wrap gap-2">
                    {answer.context.gradeSignals.map((signal) => (
                      <span
                        key={signal}
                        className="rounded-full bg-white/8 border border-white/12 px-3 py-1 text-xs text-slate-300"
                      >
                        {signal}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          ) : (
            /* Empty state */
            <div className="flex flex-col items-center justify-center h-full min-h-48 text-center py-8">
              <div className="w-14 h-14 rounded-2xl bg-white/6 border border-white/10 flex items-center justify-center mb-5 text-blue-300">
                <SparkleIcon />
              </div>
              <p className="text-sm font-semibold text-slate-300 mb-2">Ready to help</p>
              <p className="text-xs text-slate-500 max-w-48 leading-relaxed">
                Pick a lesson module and ask a question. The AI runs fully offline on this device.
              </p>
              <div className="mt-6 inline-flex items-center gap-2 rounded-full bg-white/6 border border-white/10 px-3 py-1.5">
                <span className="status-dot status-dot-pulse" />
                <span className="text-[10px] font-semibold text-slate-400">Ollama | Offline-Ready</span>
              </div>
            </div>
          )}
        </div>
      </div>
    </section>
  );
}
EOF

  #  App.jsx  FULL OVERHAUL  Sidebar (desktop) + Bottom Nav (mobile) 
  cat > "${APP_ROOT}/frontend/src/App.jsx" <<'EOF'
import { startTransition, useDeferredValue, useEffect, useState } from "react";

import { apiRequest } from "./api";
import ContentView from "./components/ContentView";
import GradesView from "./components/GradesView";
import InstallBanner from "./components/InstallBanner";
import LoginView from "./components/LoginView";
import StreamView from "./components/StreamView";
import TutorView from "./components/TutorView";

/*  Inline SVG tab icons  */
const Icons = {
  stream: (
    <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.75}>
      <path strokeLinecap="round" strokeLinejoin="round"
        d="M7 8h10M7 12h6m-6 4h10M5 3h14a2 2 0 012 2v14a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2z" />
    </svg>
  ),
  content: (
    <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.75}>
      <path strokeLinecap="round" strokeLinejoin="round"
        d="M3 7a2 2 0 012-2h4l2 2h8a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2V7z" />
    </svg>
  ),
  grades: (
    <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.75}>
      <path strokeLinecap="round" strokeLinejoin="round"
        d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z" />
    </svg>
  ),
  tutor: (
    <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.75}>
      <path strokeLinecap="round" strokeLinejoin="round"
        d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09z" />
    </svg>
  ),
  logout: (
    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
      <path strokeLinecap="round" strokeLinejoin="round"
        d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15M12 9l-3 3m0 0l3 3m-3-3h12.75" />
    </svg>
  ),
};

const TABS = [
  { id: "stream",  label: "Stream",         shortLabel: "Stream",  icon: Icons.stream  },
  { id: "content", label: "Content Folder", shortLabel: "Lessons", icon: Icons.content },
  { id: "grades",  label: "Grades",         shortLabel: "Grades",  icon: Icons.grades  },
  { id: "tutor",   label: "AI Tutor",       shortLabel: "Tutor",   icon: Icons.tutor   },
];

const initialLogin = { username: "", password: "" };
const initialTutor = { moduleId: "", question: "" };

function createBootstrapDashboard(user) {
  return {
    user,
    stream: [],
    courses: [],
    contentFolders: [],
    grades: [],
    network: {
      ssid: "PROJECT-DANILO",
      portal: "http://danilo.local",
      mode: "offline-first captive portal",
    },
    operationsHighlights: [
      { label: "Portal", value: "http://danilo.local" },
      { label: "SSID", value: "PROJECT-DANILO" },
      { label: "AI Model", value: "llama3.2:3b-instruct-q4_K_M" },
    ],
  };
}

/*  Sidebar (desktop)  */
function Sidebar({ user, activeTab, onChangeTab, onLogout, dashboard }) {
  const initials = user.fullName ? user.fullName.split(" ").map((n) => n[0]).slice(0, 2).join("") : "?";
  return (
    <aside className="hidden lg:flex lg:flex-col lg:fixed lg:inset-y-0 lg:left-0 lg:z-40 lg:w-56">
      <div className="flex flex-col h-full glass border-r border-white/40 p-4 gap-4">

        {/* Logo */}
        <div className="flex items-center gap-3 px-1 pt-1 pb-3 border-b border-white/30">
          <div className="w-9 h-9 rounded-xl bg-danilo-blue flex items-center justify-center flex-shrink-0 shadow-soft">
            <svg className="w-5 h-5 text-white" fill="none" viewBox="0 0 24 24">
              <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"
                stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
          </div>
          <div>
            <p className="text-[10px] font-bold uppercase tracking-widest text-danilo-blue leading-none">Project</p>
            <p className="text-sm font-bold text-slate-950">DANILO</p>
          </div>
        </div>

        {/* Network status pill */}
        <div className="rounded-xl bg-emerald-50 border border-emerald-100 px-3 py-2.5">
          <div className="flex items-center gap-2 mb-0.5">
            <span className="status-dot status-dot-pulse" />
            <span className="text-xs font-bold text-emerald-800">School Network</span>
          </div>
          <p className="text-[10px] text-emerald-700 ml-[18px]">AI Tutor Offline-Ready</p>
        </div>

        {/* Navigation */}
        <nav className="flex-1 space-y-1">
          {TABS.map((tab) => (
            <button
              key={tab.id}
              type="button"
              onClick={() => onChangeTab(tab.id)}
              className={`btn-touch w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-semibold transition-all text-left ${
                activeTab === tab.id
                  ? "bg-danilo-blue text-white shadow-soft"
                  : "text-slate-600 hover:bg-white/70 hover:text-slate-900"
              }`}
            >
              {tab.icon}
              {tab.label}
            </button>
          ))}
        </nav>

        {/* Highlights (portal + ssid) */}
        {dashboard?.operationsHighlights && (
          <div className="rounded-xl bg-slate-50 border border-slate-100 px-3 py-2.5 space-y-1.5">
            {dashboard.operationsHighlights.slice(0, 2).map((item) => (
              <div key={item.label}>
                <p className="text-[9px] font-bold uppercase tracking-wider text-slate-400">{item.label}</p>
                <p className="text-xs font-semibold text-slate-700 truncate">{item.value}</p>
              </div>
            ))}
          </div>
        )}

        {/* User + logout */}
        <div className="border-t border-white/30 pt-3">
          <div className="flex items-center gap-2.5 px-1 mb-3">
            <div className="w-8 h-8 rounded-full bg-danilo-gold flex items-center justify-center flex-shrink-0">
              <span className="text-xs font-bold text-slate-950">{initials}</span>
            </div>
            <div className="flex-1 min-w-0">
              <p className="text-xs font-bold text-slate-900 truncate">{user.fullName}</p>
              <p className="text-[10px] text-slate-500 capitalize">{user.role}</p>
            </div>
          </div>
          <button
            type="button"
            onClick={onLogout}
            className="btn-touch w-full flex items-center justify-center gap-1.5 rounded-xl border border-slate-200 bg-white/60 px-3 py-2 text-xs font-semibold text-slate-600 hover:bg-white hover:text-slate-900 transition-all"
          >
            {Icons.logout}
            Sign Out
          </button>
        </div>
      </div>
    </aside>
  );
}

/*  Mobile top bar  */
function MobileTopBar({ user, onLogout }) {
  const initials = user.fullName ? user.fullName.split(" ").map((n) => n[0]).slice(0, 2).join("") : "?";
  return (
    <header className="lg:hidden fixed top-0 inset-x-0 z-40 glass border-b border-white/40">
      <div className="flex items-center justify-between px-4 py-3">
        <div className="flex items-center gap-2.5">
          <div className="w-8 h-8 rounded-xl bg-danilo-blue flex items-center justify-center">
            <svg className="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24">
              <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"
                stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
          </div>
          <p className="text-sm font-bold text-slate-900">Project DANILO</p>
        </div>
        <div className="flex items-center gap-2">
          <div className="inline-flex items-center gap-1.5 rounded-full bg-emerald-50 border border-emerald-100 px-2.5 py-1">
            <span className="status-dot w-1.5 h-1.5" />
            <span className="text-[10px] font-bold text-emerald-700 uppercase tracking-wide hidden xs:inline">Online</span>
          </div>
          <button
            type="button"
            onClick={onLogout}
            className="btn-touch w-8 h-8 rounded-full bg-danilo-gold flex items-center justify-center"
            title={`Sign out (${user.fullName})`}
          >
            <span className="text-xs font-bold text-slate-950">{initials}</span>
          </button>
        </div>
      </div>
    </header>
  );
}

/*  Mobile bottom nav  */
function MobileBottomNav({ activeTab, onChangeTab }) {
  return (
    <nav className="lg:hidden fixed bottom-0 inset-x-0 z-40 glass border-t border-white/40">
      <div
        className="flex items-stretch justify-around px-1"
        style={{ paddingBottom: "calc(8px + env(safe-area-inset-bottom, 0px))", paddingTop: "6px" }}
      >
        {TABS.map((tab) => (
          <button
            key={tab.id}
            type="button"
            onClick={() => onChangeTab(tab.id)}
            className={`btn-touch flex flex-col items-center gap-1 px-3 py-1 rounded-xl flex-1 transition-all ${
              activeTab === tab.id ? "text-danilo-blue" : "text-slate-400"
            }`}
          >
            <div className={`p-1.5 rounded-xl transition-all ${activeTab === tab.id ? "bg-blue-50" : ""}`}>
              {tab.icon}
            </div>
            <span className="text-[10px] font-bold leading-none">{tab.shortLabel}</span>
          </button>
        ))}
      </div>
    </nav>
  );
}

/*  Dashboard hero card  */
function HeroCard({ user, dashboard }) {
  const roleColors = {
    admin:   "bg-slate-700 text-slate-100",
    teacher: "bg-danilo-gold text-slate-950",
    student: "bg-danilo-blue text-white",
  };
  const roleStyle = roleColors[user.role] || "bg-slate-600 text-white";

  return (
    <section className="fade-up glass-dark rounded-[2rem] p-6 text-white">
      <div className="flex flex-col gap-5 lg:flex-row lg:items-center lg:justify-between">
        <div>
          <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-blue-300 mb-2">School Workspace</p>
          <h2 className="text-2xl font-bold leading-tight mb-1">
            Welcome back, {user.fullName.split(" ")[0]}
          </h2>
          <p className="text-sm text-slate-400">
            {dashboard.network.ssid} | {dashboard.network.portal}
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-3">
          <span className={`rounded-full px-3 py-1.5 text-xs font-bold uppercase tracking-wider ${roleStyle}`}>
            {user.role}
          </span>
          {dashboard.operationsHighlights.map((item) => (
            <div key={item.label} className="rounded-xl border border-white/10 bg-white/5 px-4 py-2.5 text-center min-w-24">
              <p className="text-[9px] font-bold uppercase tracking-wider text-danilo-gold">{item.label}</p>
              <p className="text-xs font-semibold mt-0.5 truncate">{item.value}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/*  Main App  */
export default function App() {
  const [token,       setToken]       = useState(() => localStorage.getItem("danilo.token") || "");
  const [user,        setUser]        = useState(null);
  const [dashboard,   setDashboard]   = useState(null);
  const [activeTab,   setActiveTab]   = useState("stream");
  const [loading,     setLoading]     = useState(false);
  const [loginError,  setLoginError]  = useState("");
  const [loginForm,   setLoginForm]   = useState(initialLogin);
  const [promptEvent, setPromptEvent] = useState(null);
  const [search,      setSearch]      = useState("");
  const [quarter,     setQuarter]     = useState("");
  const [subject,     setSubject]     = useState("");
  const [tutorForm,   setTutorForm]   = useState(initialTutor);
  const [tutorLoading,setTutorLoading]= useState(false);
  const [tutorAnswer, setTutorAnswer] = useState(null);

  const deferredSearch = useDeferredValue(search);

  useEffect(() => {
    const handler = (event) => { event.preventDefault(); setPromptEvent(event); };
    window.addEventListener("beforeinstallprompt", handler);
    return () => window.removeEventListener("beforeinstallprompt", handler);
  }, []);

  useEffect(() => {
    if (!token) return;
    let active = true;
    Promise.all([apiRequest("/me", { token }), apiRequest("/dashboard", { token })])
      .then(([profile, data]) => {
        if (!active) return;
        setUser(profile);
        setDashboard(data);
      })
      .catch(() => {
        localStorage.removeItem("danilo.token");
        setToken("");
      });
    return () => { active = false; };
  }, [token]);

  const filteredContent = (dashboard?.contentFolders || []).filter((item) => {
    const matchesSearch = !deferredSearch ||
      [item.title, item.summary, item.folderName, item.subject].join(" ").toLowerCase()
        .includes(deferredSearch.toLowerCase());
    const matchesQuarter = !quarter || item.quarter === quarter;
    const matchesSubject = !subject || item.subject === subject;
    return matchesSearch && matchesQuarter && matchesSubject;
  });

  const handleLoginChange  = (e) => { const { name, value } = e.target; setLoginForm((c) => ({ ...c, [name]: value })); };
  const handleTutorChange  = (e) => { const { name, value } = e.target; setTutorForm((c) => ({ ...c, [name]: value })); };
  const changeTab = (next) => startTransition(() => { setActiveTab(next); });

  const handleLoginSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setLoginError("");
    try {
      const response = await apiRequest("/auth/login", { method: "POST", body: loginForm });
      if (!response?.accessToken || !response?.user) {
        throw new Error("Invalid username or password");
      }
      localStorage.setItem("danilo.token", response.accessToken);
      setToken(response.accessToken);
      setUser(response.user);
      setDashboard(createBootstrapDashboard(response.user));
      apiRequest("/dashboard", { token: response.accessToken })
        .then((nextDashboard) => {
          setDashboard(nextDashboard);
        })
        .catch(() => {
          localStorage.removeItem("danilo.token");
          setToken("");
          setUser(null);
          setDashboard(null);
          setLoginError("Invalid username or password");
        });
    } catch (error) {
      localStorage.removeItem("danilo.token");
      setToken("");
      setUser(null);
      setDashboard(null);
      setLoginError("Invalid username or password");
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("danilo.token");
    setToken(""); setUser(null); setDashboard(null); setTutorAnswer(null);
  };

  const handleTutorSubmit = async (e) => {
    e.preventDefault();
    if (!token) return;
    setTutorLoading(true);
    try {
      const response = await apiRequest("/ai/tutor", {
        method: "POST", token,
        body: { question: tutorForm.question, module_id: tutorForm.moduleId ? Number(tutorForm.moduleId) : null }
      });
      setTutorAnswer(response);
    } catch (error) {
      setTutorAnswer({ answer: error.message, context: { gradeSignals: [] } });
    } finally {
      setTutorLoading(false);
    }
  };

  const installApp = async () => {
    if (!promptEvent) return;
    await promptEvent.prompt();
    setPromptEvent(null);
  };

  /* Not logged in */
  if (!token || !dashboard || !user) {
    return (
      <LoginView
        form={loginForm}
        onChange={handleLoginChange}
        onSubmit={handleLoginSubmit}
        loading={loading}
        error={loginError}
      />
    );
  }

  /* Logged in full layout */
  return (
    <div className="min-h-screen">

      {/* Desktop sidebar */}
      <Sidebar
        user={user}
        activeTab={activeTab}
        onChangeTab={changeTab}
        onLogout={handleLogout}
        dashboard={dashboard}
      />

      {/* Mobile top bar */}
      <MobileTopBar user={user} onLogout={handleLogout} />

      {/* Main content */}
      <main className="lg:pl-56">
        <div className="min-h-screen pt-16 lg:pt-0 pb-safe-nav lg:pb-10 px-4 sm:px-6 lg:px-8 py-4 lg:py-8 max-w-5xl mx-auto space-y-5">

          {/* PWA install banner */}
          <InstallBanner
            promptEvent={promptEvent}
            onInstall={installApp}
            onDismiss={() => setPromptEvent(null)}
          />

          {/* Hero card */}
          <HeroCard user={user} dashboard={dashboard} />

          {/* Desktop tab bar */}
          <nav className="hidden lg:flex gap-2">
            {TABS.map((tab) => (
              <button
                key={tab.id}
                type="button"
                onClick={() => changeTab(tab.id)}
                className={`btn-touch flex items-center gap-2 rounded-xl px-4 py-2.5 text-sm font-semibold transition-all ${
                  activeTab === tab.id
                    ? "bg-danilo-blue text-white shadow-soft"
                    : "glass text-slate-600 hover:text-slate-900"
                }`}
              >
                {tab.icon}
                {tab.label}
              </button>
            ))}
          </nav>

          {/* Tab content */}
          <div className="fade-up" key={activeTab}>
            {activeTab === "stream" ? (
              <StreamView items={dashboard.stream} />
            ) : null}

            {activeTab === "content" ? (
              <ContentView
                items={filteredContent}
                search={search}
                onSearchChange={(e) => setSearch(e.target.value)}
                quarter={quarter}
                onQuarterChange={(e) => setQuarter(e.target.value)}
                subject={subject}
                onSubjectChange={(e) => setSubject(e.target.value)}
              />
            ) : null}

            {activeTab === "grades" ? (
              <GradesView grades={dashboard.grades} />
            ) : null}

            {activeTab === "tutor" ? (
              <TutorView
                modules={dashboard.contentFolders}
                form={tutorForm}
                onChange={handleTutorChange}
                onSubmit={handleTutorSubmit}
                loading={tutorLoading}
                answer={tutorAnswer}
              />
            ) : null}
          </div>

        </div>
      </main>

      {/* Mobile bottom nav */}
      <MobileBottomNav activeTab={activeTab} onChangeTab={changeTab} />
    </div>
  );
}
EOF
}

# =============================================================================
write_gateway_files() {
  mkdir -p "${APP_ROOT}/gateway" "${APP_ROOT}/infra/nginx"

  #  gateway/Dockerfile  multi-stage, optimized for Beelink mini PC 
  cat > "${APP_ROOT}/gateway/Dockerfile" <<'EOF'
#  Stage 1: Build the React PWA 
FROM node:22-alpine AS build

WORKDIR /workspace/frontend

# Install deps first (layer cache)
COPY frontend/package.json ./
RUN npm install --prefer-offline --no-audit --no-fund

# Copy source and build
COPY frontend/ ./
RUN npm run build

#  Stage 2: Lean Nginx runtime 
FROM nginx:1.27-alpine

# Copy our custom config and built assets
COPY infra/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /workspace/frontend/dist /usr/share/nginx/html

# Ensure Nginx can serve without elevated privileges on restricted containers
RUN chown -R nginx:nginx /usr/share/nginx/html && \
    chmod -R 755 /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
EOF

  #  infra/nginx/default.conf  enhanced captive portal + perf + proxy 
  cat > "${APP_ROOT}/infra/nginx/default.conf" <<'EOF'
# Project DANILO - Nginx Gateway Configuration
# Handles: captive portal, SPA serving, API proxying, PWA caching

upstream danilo_backend {
  server backend:8000;
  keepalive 32;
}

#  Global: Gzip compression 
gzip            on;
gzip_comp_level 5;
gzip_min_length 512;
gzip_proxied    any;
gzip_vary       on;
gzip_types
  text/plain text/css text/xml text/javascript
  application/javascript application/json application/xml
  application/rss+xml image/svg+xml font/woff2;

#  Primary server: danilo.local 
server {
  listen 80 default_server;
  server_name danilo.local;
  root  /usr/share/nginx/html;
  index index.html;

  # Security headers
  add_header X-Content-Type-Options  "nosniff"        always;
  add_header X-Frame-Options         "SAMEORIGIN"     always;
  add_header Referrer-Policy         "no-referrer"    always;
  add_header X-XSS-Protection        "1; mode=block"  always;

  #  Captive portal detection  iOS / macOS 
  location = /hotspot-detect.html             { return 302 http://danilo.local/; }
  location = /library/test/success.html       { return 302 http://danilo.local/; }

  #  Captive portal detection  Android / Chrome OS 
  location = /generate_204                    { return 302 http://danilo.local/; }
  location = /gen_204                         { return 302 http://danilo.local/; }

  #  Captive portal detection  Windows (NCSI) 
  location = /ncsi.txt                        { return 302 http://danilo.local/; }
  location = /connecttest.txt                 { return 302 http://danilo.local/; }

  #  Captive portal detection  Firefox / Ubuntu 
  location = /success.txt                     { return 302 http://danilo.local/; }
  location = /canonical.html                  { return 302 http://danilo.local/; }

  #  Captive portal detection  Amazon Kindle 
  location = /kindle-wifi/wifistub.html       { return 302 http://danilo.local/; }

  #  API proxy  FastAPI backend 
  location /api/ {
    proxy_pass             http://danilo_backend/api/;
    proxy_http_version     1.1;
    proxy_set_header       Connection          "";
    proxy_set_header       Host               $host;
    proxy_set_header       X-Real-IP          $remote_addr;
    proxy_set_header       X-Forwarded-For    $proxy_add_x_forwarded_for;
    proxy_set_header       X-Forwarded-Proto  $scheme;

    # AI tutor endpoint can take up to ~3 minutes on a cold Llama model
    proxy_read_timeout     200s;
    proxy_send_timeout     60s;
    proxy_connect_timeout  10s;

    proxy_buffer_size      16k;
    proxy_buffers          8 32k;
  }

  #  Vite asset bundles  aggressive cache (filenames are content-hashed) 
  location /assets/ {
    expires            1y;
    add_header Cache-Control "public, max-age=31536000, immutable";
    try_files          $uri =404;
  }

  #  PWA manifest  short cache 
  location ~* \.(webmanifest|json)$ {
    expires            1h;
    add_header Cache-Control "public, max-age=3600";
  }

  #  Service worker  must never be cached 
  location = /sw.js {
    expires            -1;
    add_header Cache-Control "no-store, no-cache, must-revalidate, proxy-revalidate";
  }

  #  SVG icons  medium cache 
  location /icons/ {
    expires            7d;
    add_header Cache-Control "public, max-age=604800";
    try_files          $uri =404;
  }

  #  SPA fallback  all unknown paths serve index.html 
  location / {
    try_files $uri $uri/ /index.html;
  }
}

#  Wildcard catch-all  redirect to DANILO portal 
# Covers any unrecognized hostname that arrives on port 80 (captive portal trap)
server {
  listen 80;
  server_name _;
  return 302 http://danilo.local$request_uri;
}

#  Google / Android captive check domains 
server {
  listen 80;
  server_name connectivitycheck.gstatic.com
              clients3.google.com
              connectivity-check.ubuntu.com;
  return 302 http://danilo.local/;
}

#  Xiaomi / MIUI captive domains 
server {
  listen 80;
  server_name connect.rom.miui.com
              captive.v2.rom.miui.com;
  return 302 http://danilo.local/;
}

#  Huawei / HarmonyOS captive domains 
server {
  listen 80;
  server_name connectivitycheck.platform.hicloud.com
              connectivitycheck.cloud.huawei.com;
  return 302 http://danilo.local/;
}

#  Samsung / OPPO / Vivo / Realme via Microsoft NCSI 
server {
  listen 80;
  server_name www.msftncsi.com
              msftncsi.com
              dns.msftncsi.com;
  return 302 http://danilo.local/;
}
EOF

  #  docker-compose.yml 
  cat > "${APP_ROOT}/docker-compose.yml" <<'EOF'
services:
  postgres:
    image: postgres:16-alpine
    restart: unless-stopped
    env_file:
      - .env
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 10s
      timeout: 5s
      retries: 12

  backend:
    build:
      context: ./backend
    restart: unless-stopped
    env_file:
      - .env
    depends_on:
      postgres:
        condition: service_healthy
    healthcheck:
      test: ["CMD-SHELL", "python -c \"import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/api/health')\""]
      interval: 20s
      timeout: 5s
      retries: 12

  ollama:
    image: ollama/ollama:latest
    restart: unless-stopped
    volumes:
      - ollama_data:/root/.ollama
    healthcheck:
      test: ["CMD", "ollama", "list"]
      interval: 20s
      timeout: 10s
      retries: 18

  gateway:
    build:
      context: .
      dockerfile: ./gateway/Dockerfile
    restart: unless-stopped
    depends_on:
      backend:
        condition: service_healthy
    ports:
      - "80:80"
    healthcheck:
      test: ["CMD-SHELL", "wget -qO- http://127.0.0.1/ >/dev/null"]
      interval: 20s
      timeout: 5s
      retries: 12

volumes:
  postgres_data:
  ollama_data:
EOF
}
prefetch_container_assets() {
  local build_args=()

  note "Starting Docker for pre-pull operations"
  systemctl enable --now docker

  note "Pulling compose-managed service images"
  if ! docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" pull --ignore-pull-failures; then
    note "Some service images could not be refreshed remotely; continuing with cached images"
  fi

  note "Pulling builder base images for local Docker builds"
  docker pull python:3.12-slim >/dev/null 2>&1 || note "Using cached python:3.12-slim image"
  docker pull node:22-alpine >/dev/null 2>&1 || note "Using cached node:22-alpine image"
  docker pull nginx:1.27-alpine >/dev/null 2>&1 || note "Using cached nginx:1.27-alpine image"

  if [[ "${CLEAN_BUILD}" -eq 1 ]]; then
    build_args+=(--no-cache)
    note "Running Docker build without cache"
  fi

  note "Building local application images while internet is still available"
  docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" build "${build_args[@]}" backend gateway

  note "Preloading the Ollama model into the persistent stack volume"
  docker volume create "${STACK_NAME}_ollama_data" >/dev/null
  docker rm -f "${TEMP_OLLAMA_CONTAINER}" >/dev/null 2>&1 || true
  docker run -d \
    --name "${TEMP_OLLAMA_CONTAINER}" \
    -v "${STACK_NAME}_ollama_data:/root/.ollama" \
    ollama/ollama:latest >/dev/null

  local attempts=0
  until docker exec "${TEMP_OLLAMA_CONTAINER}" ollama list >/dev/null 2>&1; do
    attempts=$((attempts + 1))
    if [[ "${attempts}" -gt 60 ]]; then
      echo "Temporary Ollama service did not become ready in time."
      docker logs "${TEMP_OLLAMA_CONTAINER}" || true
      exit 1
    fi
    sleep 2
  done

  if docker exec "${TEMP_OLLAMA_CONTAINER}" ollama list | awk 'NR > 1 { print $1 }' | grep -Fx "${OLLAMA_MODEL}" >/dev/null 2>&1; then
    note "Ollama model ${OLLAMA_MODEL} is already cached; skipping pull"
  else
    note "Pulling Ollama model ${OLLAMA_MODEL}"
    docker exec "${TEMP_OLLAMA_CONTAINER}" ollama pull "${OLLAMA_MODEL}"
  fi
  docker rm -f "${TEMP_OLLAMA_CONTAINER}" >/dev/null
}

# -----------------------------------------------------------------------------
# Captive portal networking and systemd units
# -----------------------------------------------------------------------------

# Rebuild the dnsmasq master config from scratch so the daemon cannot inherit a
# stale bind address such as 10.0.0.1 from previous installs.
reset_dnsmasq_master_config() {
  note "Preparing dnsmasq for DANILO captive DNS"
  backup_managed_file /etc/dnsmasq.conf
  if [[ -f /etc/dnsmasq.conf ]] && grep -q '^conf-dir=/etc/dnsmasq.d/,\*.conf' /etc/dnsmasq.conf; then
    :
  else
    echo "conf-dir=/etc/dnsmasq.d/,*.conf" > /etc/dnsmasq.conf
  fi
  backup_managed_file /etc/dnsmasq.d/danilo.conf
  rm -f /etc/dnsmasq.d/danilo.conf
}

write_network_scripts() {
  reset_dnsmasq_master_config

  backup_managed_file /etc/NetworkManager/conf.d/99-danilo.conf
  cat > /etc/NetworkManager/conf.d/99-danilo.conf <<EOF
[device-danilo-unmanaged]
match-device=mac:${WIFI_MAC}
managed=0
EOF
  systemctl restart NetworkManager >/dev/null 2>&1 || true

  mkdir -p /etc/dnsmasq.d /etc/hostapd
  backup_managed_file /etc/dnsmasq.d/danilo.conf
  cat > /etc/dnsmasq.d/danilo.conf <<EOF
interface=${WIFI_IFACE}
bind-dynamic
listen-address=${LAN_IP}
domain-needed
bogus-priv
dhcp-range=10.10.0.10,10.10.0.200,255.255.255.0,12h
dhcp-option=3,${LAN_IP}
dhcp-option=6,${LAN_IP}
dhcp-option=114,"http://${PORTAL_DOMAIN}/"
address=/#/${LAN_IP}
address=/${PORTAL_DOMAIN}/${LAN_IP}
address=/connectivitycheck.gstatic.com/${LAN_IP}
address=/clients3.google.com/${LAN_IP}
log-queries
log-dhcp
EOF

  backup_managed_file /etc/hostapd/danilo.conf
  cat > /etc/hostapd/danilo.conf <<EOF
country_code=PH
interface=${WIFI_IFACE}
ssid=${SSID}
hw_mode=g
channel=6
ieee80211n=1
wmm_enabled=1
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=${WIFI_PASSPHRASE}
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
EOF

  backup_managed_file /etc/default/hostapd
  cat >/etc/default/hostapd <<'EOF'
DAEMON_CONF="/etc/hostapd/danilo.conf"
EOF

  backup_managed_file /etc/sysctl.d/98-danilo-ipforward.conf
  cat >/etc/sysctl.d/98-danilo-ipforward.conf <<'EOF'
net.ipv4.ip_forward=1
EOF

  backup_managed_file /usr/local/bin/danilo-network-up.sh
  cat > /usr/local/bin/danilo-network-up.sh <<EOF
#!/usr/bin/env bash
set -Eeuo pipefail

WIFI_IFACE="\$(cat "${RUNTIME_ROOT}/wifi_iface")"
UPLINK_WIFI_IFACE="\$(cat "${RUNTIME_ROOT}/internal_wifi_iface" 2>/dev/null || true)"
LAN_IP="${LAN_IP}"
LAN_PREFIX="${LAN_PREFIX}"

rfkill unblock wifi || true
nmcli radio wifi on >/dev/null 2>&1 || true
systemctl restart NetworkManager
sleep 2

systemctl stop dnsmasq >/dev/null 2>&1 || true

if [[ -n "\${UPLINK_WIFI_IFACE}" ]]; then
  ip link set dev "\${UPLINK_WIFI_IFACE}" down >/dev/null 2>&1 || true
fi

nmcli dev set "\${WIFI_IFACE}" managed no >/dev/null 2>&1 || true
ip link set "\${WIFI_IFACE}" down || true
ip addr flush dev "\${WIFI_IFACE}" || true
ip link set "\${WIFI_IFACE}" up
ip addr add "\${LAN_IP}/\${LAN_PREFIX}" dev "\${WIFI_IFACE}"

# Realtek rtw88 adapters are slow to settle into AP mode. Give the USB Archer
# a full 10 seconds before hostapd and dnsmasq start serving clients.
sleep 10

sysctl --system >/dev/null 2>&1

iptables -t nat -C PREROUTING -i "\${WIFI_IFACE}" -p udp --dport 53 -j REDIRECT --to-ports 53 >/dev/null 2>&1 || \
  iptables -t nat -A PREROUTING -i "\${WIFI_IFACE}" -p udp --dport 53 -j REDIRECT --to-ports 53
iptables -t nat -C PREROUTING -i "\${WIFI_IFACE}" -p tcp --dport 53 -j REDIRECT --to-ports 53 >/dev/null 2>&1 || \
  iptables -t nat -A PREROUTING -i "\${WIFI_IFACE}" -p tcp --dport 53 -j REDIRECT --to-ports 53
iptables -t nat -C PREROUTING -i "\${WIFI_IFACE}" -p tcp --dport 80 -j REDIRECT --to-ports 80 >/dev/null 2>&1 || \
  iptables -t nat -A PREROUTING -i "\${WIFI_IFACE}" -p tcp --dport 80 -j REDIRECT --to-ports 80
iptables -C INPUT -i "\${WIFI_IFACE}" -p udp -m multiport --dports 53,67,68 -j ACCEPT >/dev/null 2>&1 || \
  iptables -A INPUT -i "\${WIFI_IFACE}" -p udp -m multiport --dports 53,67,68 -j ACCEPT
iptables -C OUTPUT -o "\${WIFI_IFACE}" -p udp -m multiport --sports 53,67,68 -j ACCEPT >/dev/null 2>&1 || \
  iptables -A OUTPUT -o "\${WIFI_IFACE}" -p udp -m multiport --sports 53,67,68 -j ACCEPT
iptables -C INPUT -i "\${WIFI_IFACE}" -p tcp --dport 53 -j ACCEPT >/dev/null 2>&1 || \
  iptables -A INPUT -i "\${WIFI_IFACE}" -p tcp --dport 53 -j ACCEPT
iptables -C OUTPUT -o "\${WIFI_IFACE}" -p tcp --sport 53 -j ACCEPT >/dev/null 2>&1 || \
  iptables -A OUTPUT -o "\${WIFI_IFACE}" -p tcp --sport 53 -j ACCEPT
iptables -C INPUT -i "\${WIFI_IFACE}" -p tcp --dport 80 -j ACCEPT >/dev/null 2>&1 || \
  iptables -A INPUT -i "\${WIFI_IFACE}" -p tcp --dport 80 -j ACCEPT
iptables -C OUTPUT -o "\${WIFI_IFACE}" -p tcp --sport 80 -j ACCEPT >/dev/null 2>&1 || \
  iptables -A OUTPUT -o "\${WIFI_IFACE}" -p tcp --sport 80 -j ACCEPT

netfilter-persistent save >/dev/null 2>&1 || true

systemctl restart dnsmasq
systemctl restart hostapd
EOF
  chmod +x /usr/local/bin/danilo-network-up.sh

  backup_managed_file /usr/local/bin/danilo-network-down.sh
  cat > /usr/local/bin/danilo-network-down.sh <<EOF
#!/usr/bin/env bash
set -Eeuo pipefail

WIFI_IFACE="\$(cat "${RUNTIME_ROOT}/wifi_iface")"
UPLINK_WIFI_IFACE="\$(cat "${RUNTIME_ROOT}/internal_wifi_iface" 2>/dev/null || true)"

systemctl stop hostapd >/dev/null 2>&1 || true
systemctl stop dnsmasq >/dev/null 2>&1 || true

iptables -t nat -D PREROUTING -i "\${WIFI_IFACE}" -p udp --dport 53 -j REDIRECT --to-ports 53 >/dev/null 2>&1 || true
iptables -t nat -D PREROUTING -i "\${WIFI_IFACE}" -p tcp --dport 53 -j REDIRECT --to-ports 53 >/dev/null 2>&1 || true
iptables -t nat -D PREROUTING -i "\${WIFI_IFACE}" -p tcp --dport 80 -j REDIRECT --to-ports 80 >/dev/null 2>&1 || true
iptables -D INPUT -i "\${WIFI_IFACE}" -p udp -m multiport --dports 53,67,68 -j ACCEPT >/dev/null 2>&1 || true
iptables -D OUTPUT -o "\${WIFI_IFACE}" -p udp -m multiport --sports 53,67,68 -j ACCEPT >/dev/null 2>&1 || true
iptables -D INPUT -i "\${WIFI_IFACE}" -p tcp --dport 53 -j ACCEPT >/dev/null 2>&1 || true
iptables -D OUTPUT -o "\${WIFI_IFACE}" -p tcp --sport 53 -j ACCEPT >/dev/null 2>&1 || true
iptables -D INPUT -i "\${WIFI_IFACE}" -p tcp --dport 80 -j ACCEPT >/dev/null 2>&1 || true
iptables -D OUTPUT -o "\${WIFI_IFACE}" -p tcp --sport 80 -j ACCEPT >/dev/null 2>&1 || true

ip addr flush dev "\${WIFI_IFACE}" >/dev/null 2>&1 || true
ip link set "\${WIFI_IFACE}" down >/dev/null 2>&1 || true
nmcli dev set "\${WIFI_IFACE}" managed yes >/dev/null 2>&1 || true
if [[ -n "\${UPLINK_WIFI_IFACE}" ]]; then
  ip link set dev "\${UPLINK_WIFI_IFACE}" up >/dev/null 2>&1 || true
fi
EOF
  chmod +x /usr/local/bin/danilo-network-down.sh
}

write_systemd_units() {
  backup_managed_file /etc/systemd/system/danilo-ap.service
  cat >/etc/systemd/system/danilo-ap.service <<'EOF'
[Unit]
Description=Project DANILO Access Point and Captive Networking
After=NetworkManager.service network-online.target
Wants=network-online.target
Before=danilo-stack.service

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/usr/local/bin/danilo-network-up.sh
ExecStop=/usr/local/bin/danilo-network-down.sh

[Install]
WantedBy=multi-user.target
EOF

  backup_managed_file /etc/systemd/system/danilo-stack.service
  cat >/etc/systemd/system/danilo-stack.service <<EOF
[Unit]
Description=Project DANILO Application Stack
Requires=docker.service danilo-ap.service
BindsTo=docker.service
After=docker.service danilo-ap.service

[Service]
Type=oneshot
RemainAfterExit=yes
Environment=COMPOSE_PROJECT_NAME=danilo
WorkingDirectory=${APP_ROOT}
ExecStart=/usr/bin/docker compose -p danilo -f ${APP_ROOT}/docker-compose.yml up -d --no-build
ExecStop=/usr/bin/docker compose -p danilo -f ${APP_ROOT}/docker-compose.yml down

[Install]
WantedBy=multi-user.target
EOF

  systemctl daemon-reload
  systemctl enable danilo-ap.service danilo-stack.service >/dev/null 2>&1
}

# -----------------------------------------------------------------------------
# Final readiness gates and operator summary
# -----------------------------------------------------------------------------

wait_for_stack_readiness() {
  local attempts=0

  note "Running final end-to-end readiness checks"
  note "Checking Docker daemon readiness"
  until docker info >/dev/null 2>&1; do
    attempts=$((attempts + 1))
    if [[ "${attempts}" -gt 30 ]]; then
      echo "Docker daemon did not become ready. Check: systemctl status docker"
      exit 1
    fi
    sleep 2
  done

  note "Checking compose services are running"
  wait_for_service_running postgres
  wait_for_service_running backend
  wait_for_service_running ollama
  wait_for_service_running gateway

  note "Checking compose health status"
  wait_for_container_healthy postgres "Postgres healthcheck"
  wait_for_container_healthy backend "Backend healthcheck"
  wait_for_container_healthy ollama "Ollama service readiness"
  wait_for_container_healthy gateway "Gateway/frontend healthcheck"

  note "Checking Ollama model availability"
  attempts=0
  until docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" exec -T ollama ollama list 2>/dev/null | awk 'NR > 1 { print $1 }' | grep -Fx "${OLLAMA_MODEL}" >/dev/null 2>&1; do
    attempts=$((attempts + 1))
    if [[ "${attempts}" -gt 60 ]]; then
      echo "Ollama is ready, but the configured model is not available locally: ${OLLAMA_MODEL}"
      echo "Reconnect temporary internet or preload the model, then re-run the installer."
      docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" logs --tail=80 ollama || true
      exit 1
    fi
    sleep 3
  done

  note "Checking backend API through gateway"
  attempts=0
  until curl -fsS -H "Host: ${PORTAL_DOMAIN}" "http://127.0.0.1/api/health" >/dev/null 2>&1; do
    attempts=$((attempts + 1))
    if [[ "${attempts}" -gt 60 ]]; then
      echo "Backend /api/health did not respond successfully through the gateway."
      echo "The portal is not usable yet; check backend and gateway logs below."
      docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" ps || true
      docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" logs --tail=120 gateway backend || true
      exit 1
    fi
    sleep 5
  done

  note "Checking frontend HTTP response"
  attempts=0
  until curl -fsS -H "Host: ${PORTAL_DOMAIN}" "http://127.0.0.1/" >/dev/null 2>&1; do
    attempts=$((attempts + 1))
    if [[ "${attempts}" -gt 60 ]]; then
      echo "Gateway/frontend HTTP check did not respond successfully."
      echo "The learner portal did not serve its front page on port 80."
      docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" ps || true
      docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" logs --tail=120 gateway || true
      exit 1
    fi
    sleep 5
  done
}

wait_for_systemd_active() {
  local unit="$1"
  local attempts=0

  note "Checking systemd unit is active: ${unit}"
  until systemctl is-active --quiet "${unit}"; do
    attempts=$((attempts + 1))
    if [[ "${attempts}" -gt 30 ]]; then
      echo "Systemd unit did not become active: ${unit}"
      systemctl status "${unit}" --no-pager || true
      exit 1
    fi
    sleep 2
  done
}

wait_for_service_running() {
  local service="$1"
  local attempts=0
  local container_id=""
  local running=""

  note "Checking ${service} container is running"
  while true; do
    container_id="$(docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" ps -q "${service}" 2>/dev/null | head -n1 || true)"
    if [[ -n "${container_id}" ]]; then
      running="$(docker inspect --format '{{.State.Running}}' "${container_id}" 2>/dev/null || true)"
      [[ "${running}" == "true" ]] && return 0
    fi

    attempts=$((attempts + 1))
    if [[ "${attempts}" -gt 60 ]]; then
      echo "DANILO service did not reach running state: ${service}"
      docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" ps || true
      docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" logs --tail=80 "${service}" || true
      exit 1
    fi
    sleep 3
  done
}

wait_for_container_healthy() {
  local service="$1"
  local label="$2"
  local attempts=0
  local container_id=""
  local health_status=""

  note "Checking ${label}"
  while true; do
    container_id="$(docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" ps -q "${service}" 2>/dev/null | head -n1 || true)"
    if [[ -n "${container_id}" ]]; then
      health_status="$(docker inspect --format '{{if .State.Health}}{{.State.Health.Status}}{{else}}{{.State.Status}}{{end}}' "${container_id}" 2>/dev/null || true)"
      if [[ "${health_status}" == "healthy" ]]; then
        return 0
      fi
      if [[ "${health_status}" == "unhealthy" ]]; then
        echo "${label} reported unhealthy for service: ${service}"
        docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" logs --tail=120 "${service}" || true
        exit 1
      fi
    fi

    attempts=$((attempts + 1))
    if [[ "${attempts}" -gt 90 ]]; then
      echo "${label} did not become healthy for service: ${service}"
      docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" ps || true
      docker compose -f "${APP_ROOT}/docker-compose.yml" -p "${STACK_NAME}" logs --tail=120 "${service}" || true
      exit 1
    fi
    sleep 3
  done
}

# Start the captive networking only after every required image and model asset
# is already present locally. The final compose up runs fully offline.
bring_up_offline_stack() {
  note "Starting the captive portal network services"
  systemctl start danilo-ap.service
  wait_for_systemd_active danilo-ap.service
  wait_for_systemd_active dnsmasq.service
  wait_for_systemd_active hostapd.service

  note "Applying Docker image tag fallback for systemd compose startup"
  docker tag danilo-backend:latest app-backend:latest || true
  docker tag danilo-gateway:latest app-gateway:latest || true

  note "Launching the offline DANILO application stack"
  systemctl start danilo-stack.service
  wait_for_systemd_active danilo-stack.service

  wait_for_stack_readiness

  netfilter-persistent save >/dev/null 2>&1 || true
}

print_success() {
  local elapsed=0
  elapsed=$(( $(date +%s) - INSTALL_STARTED_AT ))

  cat >&3 <<EOF

[ok] Project DANILO is live.
$(rule)
${BOLD}wifi${RESET}      ${SSID}
${BOLD}password${RESET}  ${WIFI_PASSPHRASE}
${BOLD}portal${RESET}    http://${PORTAL_DOMAIN}
${BOLD}elapsed${RESET}   $(format_duration "${elapsed}")
${DIM}log${RESET}       ${LOG_FILE}

${BOLD}access flow${RESET}
1. Join the Wi-Fi network shown above.
2. Enter the password exactly as written above if prompted.
3. Open ${BOLD}http://${PORTAL_DOMAIN}${RESET} if the portal does not appear automatically.

${BOLD}logins${RESET}
- Admin: ${BOLD}${ADMIN_USERNAME} / ${ADMIN_PASSWORD}${RESET}
${BOLD}important${RESET} Record this admin password now. It is printed only on this operator console after a successful install and is not written to the install log.

${BOLD}services${RESET}
- Gateway IP: ${LAN_IP}
- Access Point interface: ${AP_WIFI_IFACE}
- Internet download interface used during install: ${UPLINK_WIFI_IFACE:-current system uplink}
- Installed stack root: ${PROJECT_ROOT}
EOF
}

finalize_success() {
  INSTALL_SUCCEEDED=1
  trap - ERR
  note "All readiness checks passed; printing final deployment summary to the operator console"
  print_success
}

main() {
  parse_args "$@"
  require_root

  if [[ "${SYNC_ONLY}" -eq 1 ]]; then
    run_sync_mode
    return 0
  fi

  print_install_intro

  step 1 6 "System checks"
  preflight_checks
  prepare_apt
  install_docker
  install_node
  install_logrotate_config
  deep_clean
  clear_port_53_and_restore_upstream_dns
  prepare_wifi_hardware

  step 2 6 "Backend files"
  mkdir -p "${APP_ROOT}"
  generate_secrets
  write_env_file
  write_backend_files

  step 3 6 "Frontend files"
  write_frontend_files
  write_gateway_files

  step 4 6 "Docker assets"
  prefetch_container_assets

  step 5 6 "Network setup"
  write_network_scripts
  write_systemd_units

  step 6 6 "Launch stack"
  bring_up_offline_stack
  finalize_success
}

main "$@"

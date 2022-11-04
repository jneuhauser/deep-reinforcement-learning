#!/bin/bash

set -euo pipefail

SAFE_IP_REGEX='^192\.168\.[0-9]+\.[0-9]+$'

SAFE_IP=$(hostname -I | tr ' ' '\n' | sort | grep -E "${SAFE_IP_REGEX}" | head)
SAFE_IP=${SAFE_IP:-"127.0.0.1"}
WORK_DIR=$(dirname -- "$( readlink -f -- "$0")")

if [ ! -e "${WORK_DIR}"/.venv/bin/activate ]; then
    echo "Install first the virtual environment with setup_venv.sh"
    exit 1
fi

. "${WORK_DIR}"/.venv/bin/activate

jupyter notebook --no-browser --notebook-dir="${WORK_DIR}" --ip="${SAFE_IP}"

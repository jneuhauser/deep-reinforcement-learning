#!/bin/bash

set -euo pipefail

WORK_DIR=$(dirname -- "$( readlink -f -- "$0")")

if [ ! -e "${WORK_DIR}"/.venv/bin/activate ]; then
    python3 -m venv --prompt dqn "${WORK_DIR}"/.venv
fi

. "${WORK_DIR}"/.venv/bin/activate
pip install --upgrade pip
pip install -r "${WORK_DIR}"/requirements.txt

echo "Activate virtual environment with:"
echo " . ${WORK_DIR}/.venv/bin/activate"

echo "Start notebook with:"
echo " jupyter notebook --no-browser --notebook-dir=\"${WORK_DIR}\" --ip=0.0.0.0"

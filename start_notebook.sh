#!/bin/bash

set -euxo pipefail

WORK_DIR=$(dirname -- "$( readlink -f -- "$0")")

cd "${WORK_DIR}"

if [ -e "${WORK_DIR}"/venv/bin/activate ]; then
    . venv/bin/activate
else
    python3 -m venv --prompt drlnd venv
    . venv/bin/activate
    pip install --upgrade pip
    cd python
    pip install .
fi

jupyter notebook --no-browser --notebook-dir="${WORK_DIR}" --ip=0.0.0.0

deactivate

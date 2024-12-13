#! /bin/bash

set -ue

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
#
#exec python "$SCRIPT_DIR/../local_start.py"

cd "$SCRIPT_DIR/../"

exec python3 wsgi_start.py
#waitress-serve --port=5000 app.initial:app


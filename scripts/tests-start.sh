#! /usr/bin/env bash

bash scripts/lint.sh
bash scripts/format.sh

set -e
set -x

python app/tests_pre_start.py

bash scripts/test.sh "$@"

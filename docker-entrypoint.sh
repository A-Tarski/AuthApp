#!/bin/bash
set -e

echo "*****Running DB migration*****"

flask db migrate
flask db upgrade

exec "$@"
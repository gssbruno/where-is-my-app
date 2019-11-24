#!/bin/bash

set -m

# Realizar migrações
/usr/local/bin/python /app/manage.py migrate &

# Realiza a transferencia dos arquivos estáticos
/usr/local/bin/python /app/manage.py collectstatic --no-input &

# Inicio do processo primário e envio para o background
/usr/local/bin/gunicorn --config /app/gunicorn_cfg.py app.wsgi &

fg %3
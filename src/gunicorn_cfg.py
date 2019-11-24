"""
Arquivo de configuração do serviço Gunicorn
"""
import os
from multiprocessing import cpu_count

LOG_DIR = '/app/logs'
if not os.path.isdir(LOG_DIR):
    os.makedirs(LOG_DIR)

bind = '0.0.0.0:8080'
accesslog = os.path.join(LOG_DIR, 'access.log')
errorlog = os.path.join(LOG_DIR, 'error.log')
loglevel = 'debug'
workers = int(os.getenv('QTD_WORKERS', cpu_count()))
capture_output = True
reload = True if os.getenv('DJANGO_RELOAD', 0) == '1' else False
timeout = 120

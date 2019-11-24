# Django Template

Este repositório possui os arquivos e configurações necessárias para a disponibilização
de uma stack Django, Postgres e Nginx. 

## Prerrequisitos

* docker
* docker-compose

## Setup

1. Realize o fork do repositório.

2. Copie o arquivo `.env.template` para `.env` e altere as variáveis conforme o ambiente.

3. Crie um usuário para o admin do django: 

```bash
$ docker-compose exec django bash

$ python manage.py createsuperuser
```

4. Inicie seu novo app e o adicione à lista de apps instalados em settings.py:
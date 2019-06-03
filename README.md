A partir do diretorio raiz deste projeto, execute os seguintes comandos:

$ docker-compose create

$ docker-compose run web python /app/fontes/manage.py migrate

Execute entao o cadastro de um usuario admin para cadastrar/modificar produtos:

$ docker-compose run web python /app/fontes/manage.py createsuperuser

Finalmente execute:

$ docker compose up

Apos isso o app estara disponivel em http://127.0.0.1:8000/

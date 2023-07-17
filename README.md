Steps taken

1 - pip install flask
2 - pip install psycopg2
2 - pip install Flask-SQLAlchemy
3 - create route to use Api and methods
4 - Create a port and host to use my API
4 - config the api to connect with database PostgreSQL
5 - Connect SQLAlchemy to my App
6 - Create a Table Characters
7 - create a class to insert items into character
8 - utilizando o metodo **init** e atribui os parametros para meu objeto character
9 - dentro da minha rota primaria, eu faço meu JSON ser lido, os dados necessários são extraídos e usados ​​para criar um novo Characters objeto.
10 - criei um For para adicionar os dados do JSON lido no meu banco de dados como um Looping
11 - Importar o Request e Marshmallow

Após os dados inseridos proximo passo foi criar

1 - Criei as instancias (ma) para utilizar o Marshmallow e coloquei como parametro ele dentro do APP
2 - Criei uma class CharacterSchema para definir o objeto Character para ser serializados/desserializados com marshmallow
3 - Criei os parametros de consulta e defini a paginação utilizando OffSet e filtrei as paginas de busca por nome
4 - Apos isso retorna os dados em JSON

acessar a pesquisa de personagem no banco de dados (http://localhost:105/characters?page=1&per_page=20&name=nome)

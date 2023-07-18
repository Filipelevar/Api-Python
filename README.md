steps taken

1 - pip install flask
2 - pip install psycopg2
2 - pip install Flask-SQLAlchemy
3 - create route to use Api and methods
4 - Create a port and host to use my API
4 - config the api to connect with PostgreSQL database
5 - Connect SQLAlchemy to my App
6 - Create a Table Characters
7 - create a class to insert items into character
8 - using the **init** method and assign the parameters to my character object
9 - inside my primary route, I make my JSON read, the necessary data is extracted and used to create a new Characters object.
10 - I created a For to add the JSON data read in my database as a Looping
11 - Import the Request and Marshmallow

After entering the data, the next step was to create

1 - I created the instances (ma) to use Marshmallow and put it as a parameter within the APP
2 - I created a CharacterSchema class to define the Character object to be serialized/deserialized with marshmallow
3 - I created the query parameters and defined the pagination using OffSet and filtered the search pages by name
4 - After that returns the data in JSON
5 - I created .env to store the database link and the requirements.txt to deploy the API
6 - Install gunicorn to be able to deploy and work in Render
7 - import the .env

access the character search in the database (http://localhost:105/characters?page=1&per_page=20&name=name) in local,

Deploy to database and API, everything working

## Cinema rest api app

####Application was created to improve skills in Python programming using the Django framework.

####This particular application was used to create a REST API type site using the 'djangorestframework' package.

The application has a root view ('Api Root'). From here you can:
- add people (directors, actors) = 'person' tab,
- view and add movies = 'movies' tab,
- view and add cinemas = 'cinemas' tab,
- view and add screenings for each cinema = 'screenings' tab.

The project also includes unit tests of the application functionality.

### Running project locally

First, clone the repository to your local machine:

```
git clone git@github.com:mefiuea/cinema_app.git
or
https://github.com/mefiuea/cinema_app.git
```

Install the requirements:

```
pip install -r requirements.txt
or 
pipenv install -r path/to/requirements.txt
```

Set all environment variables. 
Go to the env folder, then create an .env file and copy the contents of the .env-default file into it. 
Once this is done, fill the .env file with the appropriate data. 
In the terminal, load the environment variables from this file with the command:

```
source env/.env
```

Change DEBUG mode in settings.py:

```
DEBUG = True
```

Apply the migrations:

```
python manage.py migrate
```

Finally, run the development server:

```
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.

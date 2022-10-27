# Portfolio-App
This app displays the users location as part of their profile
# Documentation
 
### Getting start with this project

##### Download the project

```bash
https://github.com/Ofucho/Portfolio-App.git
```

Make sure to change the database connection parameters from `portfolioApp/settings.py` file,

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'portfolioApp',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

##### Installation of dependencies

In windows the gdal can be installed by following method;
```bash
# Gdal installations
install conda
Follow the tutorial below to install geopandas which comes with gdal
https://medium.com/analytics-vidhya/fastest-way-to-install-geopandas-in-jupyter-notebook-on-windows-8f734e11fa2b
```
 

Now you can install the other dependencies as mentioned in requirements.txt
```bash
# Other dependencies
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

Create the django superuser

```bash
python manage.py createsuperuser
```

##### Run server
Now you can run the django server using following command,

```bash
python manage.py runserver
```

Now your site will be running in this url: http://localhost:8000/

 

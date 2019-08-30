from . import *

SECRET_KEY = '4i&u(!%shd*0-3$ls)fohsjsd48t(gu%1-ch_wyzk7@#n3bd8e'
DEBUG = False
ALLOWED_HOSTS = ['51.158.76.250']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # on utilise l'adaptateur postgresql
        'NAME': 'disquaire', # le nom de notre base de données créée précédemment
        'USER': 'stud', # attention  remplacez par votre nom d'utilisateur !!
        'PASSWORD': 'Fidelite',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


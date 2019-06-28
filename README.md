Version française

# Develop-a-website-by-Django
Développement d'un site web de gestion de données de projets par Django
Tous les codes que nous avons écris sont dans la fiche 'src'.

Baser sur `python3.7.0` et `Django2.1.7`   

IDE:Pycharm, MySQL


# Fonctions principaux：
- Ajouter/Modifier/Supprimer Direction, Member, Personal Project
- Distribuer des gens aux groupes différentes.
- Fixer des droits différents aux groupes différentes. 

# Infromations utils:

- Django : Le plus pratique lien d'apprendre Django pour les débutants: https://www.youtube.com/watch?v=F5mRW0jo-U4 
    Regardez les 20 premières minutes de cette vidéo, alors vous savez comment créer l'environnement pour Django. Et installez MySQL aussi. 

- MySQL : Le plus pratique lien d'apprendre MySQL pour les débutants : https://www.tutorialspoint.com/mysql/index.htm


- HTML/CSS/JAVASCRIPT : Le plus pratique lien d'apprendre HTML/CSS/JAVASCRIPT pour les débutants :
  https://getbootstrap.com/docs/4.3/getting-started/introduction/
  https://www.udemy.com/the-web-developer-bootcamp/
  https://developer.mozilla.org/fr/docs/Web

Remarques importantes: Pour utiliser la base de données mysql, il convient de modifier les paramètres au début.

Après install PyCharm, Django, commencer un projet de Djang dans IDE PyCharm par :

    django-admin startproject final

## Créer database
Dans terminal d'ordinateur, allez dans l'environnement MySQL, et faites-le dans mysql:
```sql
CREATE DATABASE `final_database` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
```

## Excuter database

Dans le terminal de Pycharm

    pip3 install pymysql

Ajoutez-les dans 'final/__init__.py'

    import pymysql
    pymysql.install_as_MySQLdb()

 Ajoutez-les dans `final/setting.py` :

     DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'final_database',
            'USER': 'root',
            'PASSWORD': 'password',
            'HOST': 'host',
            'PORT': 3306,
        }
    }

Cliquez le button '+' en haut à droite, et connectez à MySQL

Excutez-le dans le terminal de Pycharm:

    python3 manage.py makemigrations
    python3 manage.py migrate

Créer un 'app' qu'il s'appele feuillederoute par:

    python3 manage.py startapp feuillederoute

Rengistrer cet app dans `final/setting.py`:
    
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'feuillederoute',
    ]

## Informarions Pratiques:

Dans un app, models.py et views.py sont fournies. Dans model.py, il faut écrire des parametres de cet app, et l'engistrer à feuillederoute/admin.py. Après excuter le models.py, django va faire des tables de base de donnée. S'il y a un class se trouve à feuillederoute/model.py, un table correspondant existe automatiquement. (Vous pouvez changer des informations de tables par rédiger la fiche de la table.) Views.py fait partie de recevoir des infromations qui vient de front-end, et consulte MySQL pour avoir des informations et lui rendre. Il faut créer un forms.py et urls.p. En utilisant froms.py pour designer comment presenter des formules de parametres qui sont dans models.py. Il faut enregistrer des liens à chaque app à urls.py. 

Suivi le lien sur Django pour apprendre comment écrire models.py/views.py/forms.py/urls.py

Après finir le premier app:

### Créer un superadmin
Dans le terminal de PyCharm:

    python3 manage.py createsuperuser

### Excutez le projet:
 Dans le terminal de PyCharm:

    python3 manage.py runserver

Se connecter par le nom de superuser et son mot de pass



English Version:

# Develop-a-website-by-Django
Development of a project data management website by Django

Base on `python3.7.0` and `Django2.1.7`   

IDE:Pycharm, MySQL


# Main functions：
- Add/Eidt/Delete Direction, Member, Personal Project
- Divide different groups for different members.
- set different right to different groups.


# Practical infromations:

- Django : a useful link to study django from zero: https://www.youtube.com/watch?v=F5mRW0jo-U4 
    please watch the first 20 minutes of this video, then you know how to build up the environment for Django. And install MySQL too. 

- MySQL : a useful link to study myqsl: https://www.tutorialspoint.com/mysql/index.htm


- HTML/CSS/JAVASCRIPT : some useful links to study HTML/CSS/JAVASCRIPT : 
  https://getbootstrap.com/docs/4.3/getting-started/introduction/
  https://www.udemy.com/the-web-developer-bootcamp/
  https://developer.mozilla.org/fr/docs/Web


Important notes: To use MySQL, it should change it at the beginning, please look at ## Run database.

After installing PyCharm, Django, start a project of Django in IDE PyCharm by:

    django-admin startproject final


## Create database
In terminal, go to MySQL environment, and do this in mysql:
```sql
CREATE DATABASE `final_database` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
```
## Excuter database

Dans le terminal de Pycharm

    pip3 install pymysql

Ajoutez-les dans 'final/__init__.py'

    import pymysql
    pymysql.install_as_MySQLdb()

 Ajoutez-les dans `final/setting.py` :

     DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'final_database',
            'USER': 'root',
            'PASSWORD': 'password',
            'HOST': 'host',
            'PORT': 3306,
        }
    }

Cliquez le button '+' en haut à droite, et connectez à MySQL

Excutez-le dans le terminal de Pycharm:

    python3 manage.py makemigrations
    python3 manage.py migrate

Créer un 'app' qu'il s'appele feuillederoute par:

    python3 manage.py startapp feuillederoute

Rengistrer cet app dans `final/setting.py`:
    
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'feuillederoute',
    ]


## Run databse

In Pycharm's terminal

    pip3 install pymysql

 Add this `final/setting.py` :

     DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'final_database',
            'USER': 'root',
            'PASSWORD': 'password',
            'HOST': 'host',
            'PORT': 3306,
        }
    }

Add this to 'final/__init__.py'

    import pymysql
    pymysql.install_as_MySQLdb()

Click the '+' button in the top right, connect to mysql

Then run this in the terminal of Pycharm:

    python3 manage.py makemigrations
    python3 manage.py migrate

## Useful notes:

In an app, model.py and views.py are offered. In model.py, write some parameters about this app, and save it in feuillederoute/admin.py. Once run this project, if there is one class in models.py, one mysql table which correspond to the parameters of models.py will exist automatiquely. (You can change informations of the mysql table by a file of mysql which is in the top right corner) Views.py is able to receive requires and search informations in the database of mysql, and then send back to front-end to users. There also need to be a forms.py and a urls.py. Using forms.py to design how to present the parameters that have written in models.py, that's to say, decide how big the blank is, what type the blank is. For each app, it should have a urls.py to manage their urls.

Following the link which is written in #Practical informations -Django for studing how to write models.py/views.py/forms.py/ursl.py


After finishing all the python files needed in an app:

### create a superadmin
 Do this in the terminal of Pycharm:

    python3 manage.py createsuperuser

### Run the project:

 Do this in the terminal of Pycharm:

    python3 manage.py runserver

Login in by superuser name and password.



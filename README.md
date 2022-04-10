# PythonDjango_UserWalletApp_DRF
## Developement details
  - Python 3.10.1
  - asgiref==3.5.0
  - Django==4.0.3
  - djangorestframework==3.13.1
  - pytz==2022.1
  - sqlparse==0.4.2
  - tzdata==2022.1

# App Screenshot
 - Create Account
  ![image](https://user-images.githubusercontent.com/35606236/162618743-4c576f58-cc11-432b-961d-074c9b11530a.png)

 - Login
   ![image](https://user-images.githubusercontent.com/35606236/162618786-ade54cba-9384-47be-8193-baa24050b15e.png)
 
 - User Wallet Details page includes add amount, remove amount, and transaction history
   ![image](https://user-images.githubusercontent.com/35606236/162618885-fb34244b-4c1c-41f2-8c09-d5e41ffc991f.png)
 
 - APIs Overview
   ![image](https://user-images.githubusercontent.com/35606236/162618915-8f8af555-4991-4953-ad62-19b9e6961ca7.png)

### Rough steps that, I used to develop the App
> virtualenv envuser
    - create virtual env
> envuser\scripts\activate
    - activate env
> pip install django
    - install django
> django-admin startproject userWallet
    - create project
> django-admin startproject userWallet
    - create project
> cd .\userWallet\
    change directory
> django-admin startapp app_userWallet
    - create app
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\api_userWallet\views.py
    - create views
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\userWallet\settings.py
    - install app in INSTALLED_APPS['app_userWallet']
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\app_userWallet\templates\app_userWallet\main.html
    - create templates files
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\app_userWallet\views.py
    - create views
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\app_userWallet\urls.py
    - create urls
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\userWallet\urls.py
    - include urls
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\app_userWallet\models.py
    - create models User with pass, this will just get all the default attributs of User model
        from django.contrib.auth.models import AbstractUser
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\app_userWallet\admin.py
    - register models User
        admin.site.register(User)

> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\userWallet\settings.py
    - refer auth user
        AUTH_USER_MODEL = 'app_userWallet.User'
> python manage.py makemigrations
> python manage.py migrate
> python manage.py createsuperuser
    - usename: nitish
    - email: bnitish101@gmail.com
    - pass: nitish
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\api_userWallet\models.py
    - update user table with 
        email = models.EmailField(unique=True, null=True) 
        USERNAME_FIELD = 'email'
> python manage.py makemigrations
> python manage.py migrate 
> Admin login with email id
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\api_userWallet\admin.py
    - register User modeles
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\api_userWallet\models.py
    - create following table
        UserWallet
        UserTransactionHistory
> python manage.py makemigrations
> python manage.py migrate 
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\api_userWallet\admin.py
    - register new modeles
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\static\css\main.css
    - create static files
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\userWallet\settings.py
    - config static files
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR / 'static')
        ]
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\app_userWallet\templates\app_userWallet\login_register.html
    - create login register form
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\app_userWallet\views.py
    - create views method
        loginPage

> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\app_userWallet\templates\app_userWallet\login_register.html
    - create login register page
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\app_userWallet\views.py
    - add view methods
        login and logout
> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\app_userWallet\form.py
    - create user form

> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\app_userWallet\templates\app_userWallet\wallet.html
    - create wallet UI includes
        add wallet, remove wallet, transaction history, logout button

> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\app_userWallet\views.py
    - add view methods
        add wallet, remove wallet, transaction history
> pip install djangorestframework

> C:\PythonPractice\PythonFramowrk\PythonDjango_UserWallet\userWallet\userWallet\settings.py
    - install app in INSTALLED_APPS['rest_framework']
> Create new directory inside the app (app_userWallet) named as <api> to create all rest apis
    __init__.py, serializer.py, views.py, urls.py

Admin login
    username: bnitish101@gmail.com
    pass: nitish
User login
    username: bnitish104@gmail.com
    pass: abc123$%123

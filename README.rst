===============
Bond Calculator
===============

Bond Calculator is a simple web based bond calculator based on the mortgate formula found at
​https://en.wikipedia.org/wiki/Mortgage_calculator​. User is asked to input, purchase price, deposit price, bond term
and interest rate and the results are computed. The user also has an option to input name to which results will be
saved with.

--------------
Quick start
--------------

Woking with just the app folder 'calculator'
--------------------------------------------

1. Start a django project 'django-admin startproject' and in the django project folder copy the 'calculator' app
   to it.

2. Add "calculator" to your INSTALLED_APPS setting (in the settings.py file):

  INSTALLED_APP = [
      'calculator.contib.CalculatorConfig',
        ...
  ]

3. include the polls URLconf in your project urls.py:

  path('calculator/', include('calculator.urls')),

4. Run 'python3 manage.py migrate' to create calculator models.

5. Start the development server 'python3 manage.py runserver' and visit http://127.0.0.1:8000
  to do your calculations.

Working with the whole project folder 'webapp'
---------------------------------------------

1. You just need to be in the folder 'webapp/' and run the server (5. from above).

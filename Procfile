web: gunicorn labs.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn labs.wsgi
web: gunicorn Products.wsgi
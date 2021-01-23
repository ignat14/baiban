import os


def run_it():
    os.system('python manage.py migrate --noinput')
    os.system('python manage.py collectstatic --noinput')
    os.system('python manage.py compilemessages')
    os.system('python manage.py create_dev_superuser')
    os.system('python manage.py runserver 0.0.0.0:8000')


run_it()

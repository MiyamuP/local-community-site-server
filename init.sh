pip install -r requirements.txt
python manage.py makemigrations memorymap
python manage.py migrate memorymap
python manage.py create_prefecture
python manage.py runserver
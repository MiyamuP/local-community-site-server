pip instal -r requirements.txt
python manage.py makemigration memorymap
python manage.py migrate memorymap
python manage.py runserver
pip install -r requirements.txt
python3 manage.py makemigrations memorymap
python3 manage.py migrate memorymap
python3 manage.py create_prefecture
python3 manage.py runserver
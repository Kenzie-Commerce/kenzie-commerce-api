set -o errexit

poetry install
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py create_admin
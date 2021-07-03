FROM python:3.6

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_USERNAME=superadmin
ENV DJANGO_SUPERUSER_PASSWORD=superadmin@123

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY src /code/

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py compress

RUN echo "from django.contrib.auth.models import User; \
    User.objects.create_superuser('admin', 'admin@example.com', 'pass')" \
    | python manage.py shell


CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

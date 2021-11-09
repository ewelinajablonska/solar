FROM python:3.8
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY my_app.py .
CMD python /my_app/manage.py runserver 0.0.0.0:8080

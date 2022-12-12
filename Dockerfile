FROM python:3.10-buster
COPY . /app
WORKDIR /app
EXPOSE 8000
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0:8000"]
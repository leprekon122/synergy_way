FROM python

WORKDIR /usr/projects/
COPY . /requirments.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirments.txt

EXPOSE "8000:80"

COPY . / synergy ./
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
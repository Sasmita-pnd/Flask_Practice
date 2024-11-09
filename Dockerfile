#we will get pre-build image of OS and python

from python:3.9.10-slim-buster 
#We can use any OS this slim-buster is for linux

WORKDIR D:\Git\Flask_Practice/docker

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 

COPY . .

CMD ["python", "-m", "flask", "--app", "loan_app", "run", "--host=0.0.0.0"]
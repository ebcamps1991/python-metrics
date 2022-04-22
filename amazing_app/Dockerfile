FROM python:3.8

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app /opt/app

WORKDIR /opt/app

CMD python run.py
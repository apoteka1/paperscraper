FROM python:3.10-alpine3.15

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py greq.py ./

EXPOSE 5000

CMD [ "python", "app.py"]
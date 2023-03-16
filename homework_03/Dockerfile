FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /fastapi
#
#RUN apt update -y && apt upgrade -y

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /fastapi/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


## Комментарий о запуске контейнера
## docker run -d -p 8000:8000 backend
## где -d - фоновый режим, -p 8000:80 проброс портов

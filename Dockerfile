FROM python:latest

RUN pip install pyTelegrambotApi
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app

COPY . /usr/src/app/

CMD ["python", "bot.py"]
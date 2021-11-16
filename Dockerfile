FROM python:latest
LABEL authors="Paul Marquereau"

RUN python3 -m venv /opt/venv
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

COPY ./bot /bot
COPY ./images /images
CMD python ./bot/bot.py
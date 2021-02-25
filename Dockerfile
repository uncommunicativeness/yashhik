FROM python:3.9

ENV DEBIAN_FRONTEND=noninteractive

ENV PYTHONUNBUFFERED 1

COPY . /usr/bot/

WORKDIR /usr/bot/

RUN pip --disable-pip-version-check --no-cache-dir install -r /usr/bot/requirements.txt \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

ENV DEBIAN_FRONTEND=dialog

CMD ["python", "bot.py"]
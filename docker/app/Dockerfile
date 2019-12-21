FROM python:3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /opt/django_container

RUN apt-get update \
 && apt-get install --no-install-recommends -y \
        ca-certificates \
        apt-utils \
        apt-transport-https \
        gettext \
        curl \
        rsync \
 && apt-get -y autoremove --purge \
 && rm -rf /var/lib/apt/lists/* \
 && pip install --upgrade pip \
 && pip install --no-cache-dir psycopg2-binary uwsgi

COPY ./requirements .

RUN pip install --no-cache-dir -r dev.txt

COPY ./docker/app/launch.sh /bin/

CMD [ "/bin/launch.sh" ]

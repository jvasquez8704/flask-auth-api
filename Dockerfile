FROM rackspacedot/python37

ARG ENV=
ENV ENV=${ENV}

RUN  apt-get update && apt-get install -y --force-yes jq

RUN pip3 install --upgrade pip

WORKDIR /api

COPY . /api

RUN pip --no-cache-dir install -r requirements.txt

WORKDIR /api/src
EXPOSE 443
# CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
CMD ["gunicorn", "-b", "0.0.0.0:443", "--timeout", "180", "--certfile", "./certs/cert1.pem", "--keyfile", "./certs/privkey1.pem", "app:app" ]


FROM rackspacedot/python37
RUN  apt-get update && apt-get install -y --force-yes jq

RUN pip3 install --upgrade pip

EXPOSE 443
WORKDIR /api

COPY . /api

RUN pip --no-cache-dir install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:443", "--timeout", "180", "--certfile", "./certs/cert1.pem", "--keyfile", "./certs/privkey1.pem", "app:app" ]


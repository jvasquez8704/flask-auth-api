FROM rackspacedot/python37
RUN  apt-get update && apt-get install -y --force-yes jq

RUN pip3 install --upgrade pip

WORKDIR /api

COPY . /api

RUN pip --no-cache-dir install -r requirements.txt

WORKDIR /api/src
EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]


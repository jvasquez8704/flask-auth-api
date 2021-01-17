FROM rackspacedot/python37
RUN  apt-get update && apt-get install -y --force-yes jq

RUN pip3 install --upgrade pip

WORKDIR /api

COPY . /api

RUN pip --no-cache-dir install -r requirements.txt

CMD ["python", "app.py"]


# katch-auth-api

## Enviroment
    * Python: 3.8.4 || 2.7.16


### Dependencies

```aniso8601==8.1.0
CacheControl==0.12.6
cachetools==4.2.0
certifi==2020.12.5
cffi==1.14.4
chardet==4.0.0
click==7.1.2
cryptography==3.3.1
firebase-admin==4.5.1
Flask==1.1.2
Flask-Cors==3.0.10
Flask-JWT-Extended==3.25.0
Flask-RESTful==0.3.8
google-api-core==1.25.0
google-api-python-client==1.12.8
google-auth==1.24.0
google-auth-httplib2==0.0.4
google-cloud-core==1.5.0
google-cloud-firestore==2.0.2
google-cloud-storage==1.35.0
google-crc32c==1.1.2
google-resumable-media==1.2.0
googleapis-common-protos==1.52.0
grpcio==1.35.0
gunicorn==20.0.4
httplib2==0.18.1
idna==2.10
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
msgpack==1.0.2
proto-plus==1.13.0
protobuf==3.14.0
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycparser==2.20
PyJWT==1.7.1
pyOpenSSL==20.0.1
python-dotenv==0.15.0
pytz==2020.5
requests==2.25.1
rsa==4.7
six==1.15.0
uritemplate==3.0.1
urllib3==1.26.2
Werkzeug==1.0.1
```

# Doc resources
    `<link>` : <https://docs.authlib.org/en/latest/basic/install.html#pip-install-authlib>
    `<link>` : <https://flask.palletsprojects.com/en/1.1.x/quickstart/>


# Notes
```
// commando para forwarding de servicio en el cloud
kubectl port-forward -n dev svc/katch-user-api 4001:80

//conectarse directo al pod
kubectl exec -n <namespace> --stdin --tty katch-user-api-67f696bf9-5phbv -- /bin/bash

//Comando aplicar servicio y desplegar and ingress
kubectl apply -f <.yml>

//Listado de pods
kubectl get pods -n <namespace>

//Listado de servicios
kubectl get svc -n <namespace>

//Obtener credenciales de cluster, previamente correr gcloud auth login && gcloud auth configure-docker
gcloud container clusters get-credentials katchplus-cluster --region=us-west1-a

// Lista containers detenidos
docker ps -a

//Lista containers los que estan corriendo
docker ps

//Borrar contenedor
docker rm <nombre>

//Borrar imagenes
docker rmi <nombre>

//Create Secret TLS
kubectl create secret tls wildcard-katchplus-certificate --cert ./fullchain.pem --key ./privkey.pem 

//Comando PATCH para recontruir los pods
kubectl patch deployment katch-user-api [-n dev] -p "{\"spec\":{\"template\":{\"metadata\":{\"labels\":{\"date\":\"19012021\"}}}}}"
```
#Gunicorn
```
Added "certs" forlder to root, not pushed.

Anotations for ingress fiel to supports ssl/https with gunicorn deployer API, set timeout for request.

    nginx.ingress.kubernetes.io/backend-protocol: HTTPS
    nginx.ingress.kubernetes.io/rewrite-target: /$2
    nginx.ingress.kubernetes.io/proxy-ssl-ciphers: 'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA:ECDHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:DES-CBC3-SHA'
    nginx.ingress.kubernetes.io/proxy-ssl-protocols: 'TLSv1 TLSv1.1 TLSv1.2 TLSv1.3'
    nginx.ingress.kubernetes.io/proxy-connect-timeout: "180"
    nginx.ingress.kubernetes.io/proxy-read-timeout: "180"
    nginx.ingress.kubernetes.io/proxy-send-timeout: "180"

```










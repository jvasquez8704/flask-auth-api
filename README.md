# katch-auth-api

# Enviroment
    * Python: 3.8.4 || 2.7.16


## Its you are using Windows
# Dependencies
    * run `pip install -U python-dotenv`
    * run `pip install -U firebase-admin`
    * run `pip install -U Flask`
    * run `pip install -U request`

## Its you are using MacOS or Linux
# Dependencies
    * run `$ pip3 install Authlib`
    * run `$ pip3 install Authlib requests` 
    * run `$ pip3 install Authlib Flask`
    * run `$ pip3 install Flask` 
    * run `$ pip3 install request` 
    * run `$ pip3 install firebase_admin` 
    * run `$ pip3 install -U python-dotenv` 

# Doc resources
    `<link>` : <https://docs.authlib.org/en/latest/basic/install.html#pip-install-authlib>
    `<link>` : <https://flask.palletsprojects.com/en/1.1.x/quickstart/>


# Notes
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

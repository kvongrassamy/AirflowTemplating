# AirflowTemplating
The goal of this project is to build docker containers that provides an Airflow UI to help users that know little code to use the Jinja Templates to create Airflow DAGs

# Steps to Activate Container
1. cd into the templating folder with `cd templating`

2. Build the Docker Image with `docker-compose build`

3. Then `docker-compose up` will initiate the container to http://localhost:8080/

4. Open http://localhost:8080/ in web

# Dag Generator from Templating

1. We will add in 2 inputs that will take the jinja file and replace the owners name and dag name and generate a new dag in Airflow.  This should be used for typical DAGs that users will need but are will be reused constantly.  
![alt text](images/template_inputs.jpg)
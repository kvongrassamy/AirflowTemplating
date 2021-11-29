FROM postgres 
#RUN apt install docker.io
COPY create_db.sh .
ENV POSTGRESQL_USERNAME=airflow
ENV POSTGRESQL_PASSWORD=airflow
ENV POSTGRESQL_DATABASE=airflow_db
ENV POSTGRES_PASSWORD=airflow
ENV POSTGRES_HOST_AUTH_METHOD=trust
USER postgres
#RUN chmod +x create_db.sh
#RUN su postgres
#USER postgres
#CMD psql -U postgres
#     psql && \
#     ["psql", "--command", "CREATE USER user WITH PASSWORD 'userpassword';"] && \
#     ["psql", "--command", "CREATE DATABASE userdb;"] && \
#     ["psql", "--command", "GRANT ALL PRIVILEGES ON DATABASE userdb to user;" ]&& \
#     ["psql", "--command", "\q;"]
# #COPY create_db.sh /docker-entrypoint-initdb.d/
#CMD psql && \
#    C
#ENV POSTGRES_USER airflow
#ENV POSTGRES_PASSWORD airflow 
#ENV POSTGRES_DB airflow 
# COPY ./postgresql/14/data/. /var/run/postgresql/.
# COPY init.sql /docker-entrypoint-initdb.d/
# USER airflow
#RUN --name some-postgres -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=test postgres

FROM python:3.8
RUN pip3 install 'apache-airflow'
RUN pip install apache-airflow['postgresql']
COPY ./dags/. /root/airflow/dags/.
RUN pip install apache-airflow-providers-microsoft-mssql \
    && pip install Flask-Admin \
    && pip install shelljob\
    && pip install psycopg2
RUN airflow db init
COPY ./plugins/. /root/airflow/plugins/.
COPY ./plugins/ /usr/local/lib/python3.8/site-packages/airflow/plugins/
RUN airflow db init
CMD airflow db upgrade \
    && airflow users create --role Admin --username airflow --email admin@admin.com --firstname admin --lastname admin --password airflow \
    && (airflow scheduler &) && airflow webserver


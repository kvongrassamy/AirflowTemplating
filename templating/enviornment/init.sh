airflow db upgrade
airflow users create --role Admin --username airflow --email admin@admin.com --firstname admin --lastname admin --password airflow
airflow db init
(airflow scheduler &) && airflow webserver
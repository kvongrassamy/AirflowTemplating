FROM python:3.8
RUN pip3 install 'apache-airflow'
RUN pip install apache-airflow['postgresql']
COPY ./dags/. /root/airflow/dags/.
RUN pip install apache-airflow-providers-microsoft-mssql \
    && pip install Flask-Admin \
    && pip install shelljob\
    && pip install psycopg2\
    && pip install bs4\
    && pip install selenium
RUN airflow db init
COPY ./plugins/. /root/airflow/plugins/.
COPY ./plugins/ /usr/local/lib/python3.8/site-packages/airflow/plugins/

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable
# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

RUN airflow db init
CMD airflow db upgrade \
    && airflow users create --role Admin --username airflow --email admin@admin.com --firstname admin --lastname admin --password airflow \
    && (airflow scheduler &) && airflow webserver


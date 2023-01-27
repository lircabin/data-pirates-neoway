FROM apache/airflow:2.5.1-python3.8
COPY ./scrapper/requirements.txt .
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary==2.9.5
RUN pip install sqlalchemy==1.4.46
RUN pip install pandas==1.5.3
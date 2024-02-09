FROM jupyter/pyspark-notebook:latest

# Install additional dependencies
WORKDIR /home/jovyan/work/
RUN mkdir extras

COPY requirements.txt extras/
RUN pip install -r extras/requirements.txt
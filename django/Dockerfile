FROM python:3.10

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       postgresql-client sudo \
    && rm -rf /var/lib/apt/lists/*


COPY ./ /app
RUN pip install --upgrade pip 
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org -r /app/requirements.txt

WORKDIR /app
# RUN django-admin startproject dj .
EXPOSE 80

# RUN useradd -p $(openssl passwd -1 godnseo) -ms /bin/bash -u 1000 kes 
# RUN usermod -aG sudo kes 
# USER kes

# ENTRYPOINT ["/app/start"]

# CMD ["gunicorn", "--bind", ":80", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "dj.asgi:application"]

CMD ["bash", "-c", "while true; do echo 'kes'; sleep 10; done"]

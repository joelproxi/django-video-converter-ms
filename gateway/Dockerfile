FROM python:3.11-slim-bullseye

RUN <<EOF
    apt-get update
    apt-get install --no-install-suggests --no-install-recommends -y build-essential
    pip install --no-cache-dir -U pip
EOF

WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app

EXPOSE 8000

ENTRYPOINT [ "python manage.py" ]
CMD [ "runserver", "0.0.0.0:8000" ]

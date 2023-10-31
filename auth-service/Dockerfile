FROM python:3.11-slim-bullseye

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends --no-install-suggests \
#     build-essential \
#     && pip install --no-cache-dir -U pip


RUN    <<EOF
        apt-get update
        apt-install -y --no-install-recommends --no-install-suggests \
        build-essential
        pip install -U pip
EOF

WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app

EXPOSE 8001

ENTRYPOINT [ "python manage.py" ]
CMD [ "runserver", "0.0.0.0:8001" ]

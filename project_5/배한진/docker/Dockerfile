FROM python:3.10-slim-bullseye


COPY . ./docker

RUN pip install -r ./docker/requirements.txt

EXPOSE 5000

CMD ["python", "./docker/app.py"]


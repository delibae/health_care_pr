FROM python:3.10-slim-bullseye


COPY . ./docker

RUN pip install -r ./docker/requirements.txt

# RUN pip3 install -U flask-cors

# RUN  pip3 install -U scikit-learn

# RUN pip3 install numpy

# RUN pip3 install pandas

EXPOSE 5000

CMD ["python", "./docker/app.py"]


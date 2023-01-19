FROM python:3.10-slim-bullseye


COPY . ./docker

RUN pip install -r ./docker/requirements.txt

RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

EXPOSE 8021

CMD ["python", "./docker/app.py"]


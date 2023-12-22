FROM python:3.10-rc-slim

RUN apt update && mkdir "/sonata_textile_shop"

WORKDIR /sonata_textile_shop

COPY ./src ./src
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip && pip install -r ./requirements.txt

CMD ["python", "src/manage.py", "runserver", "8008"]
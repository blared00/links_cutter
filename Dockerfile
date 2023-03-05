FROM python:3.11

WORKDIR /usr/src/app/web

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN chmod +x entrypoint.sh


COPY . .

ENTRYPOINT ["/usr/src/app/web/entrypoint.sh"]

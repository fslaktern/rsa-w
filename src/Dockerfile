FROM python:3.13-slim

RUN apt-get update && apt-get install -y socat && apt-get clean

RUN pip install pycryptodome

COPY rsa-w.py /rsa-w.py

RUN addgroup ctf && adduser ctf --system
USER ctf

CMD ["sh", "-c", "socat 'TCP-LISTEN:9999,reuseaddr,fork' 'EXEC:/usr/local/bin/python rsa-w.py,pty,setsid'"]



FROM python
LABEL maintainer="Laurent Raufaste <analogue@glop.org>"
LABEL version="0.1"

COPY main.py main.py
COPY requirements.txt requirements.txt
RUN pip install --requirement requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "main.py"]

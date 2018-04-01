FROM python
LABEL maintainer="Laurent Raufaste <analogue@glop.org>"
LABEL version="0.1"

COPY main.py main.py
RUN pip install docopt

EXPOSE 8000

ENTRYPOINT ["python", "main.py"]

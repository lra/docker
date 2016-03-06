FROM debian
MAINTAINER Laurent Raufaste <analogue@glop.org>

COPY geth /usr/local/bin/geth
RUN useradd --create-home ethereum

EXPOSE 30303
USER ethereum
VOLUME /home/ethereum
WORKDIR /home/ethereum

CMD /usr/local/bin/geth

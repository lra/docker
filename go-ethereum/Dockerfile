FROM debian
MAINTAINER Laurent Raufaste <analogue@glop.org>

COPY geth /usr/local/bin/geth
RUN useradd ethereum
RUN mkdir /var/lib/ethereum
RUN chown ethereum /var/lib/ethereum

EXPOSE 8545
EXPOSE 30303

USER ethereum
VOLUME /var/lib/ethereum
WORKDIR /var/lib/ethereum

ENTRYPOINT ["/usr/local/bin/geth", "--datadir", "/var/lib/ethereum"]

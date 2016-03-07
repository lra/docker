FROM debian
MAINTAINER Laurent Raufaste <analogue@glop.org>
LABEL version=1.3.5

COPY geth /usr/local/bin/geth
RUN useradd ethereum
RUN mkdir /var/lib/ethereum
RUN chown ethereum /var/lib/ethereum

EXPOSE 8545 30303

VOLUME /var/lib/ethereum

USER ethereum
WORKDIR /var/lib/ethereum

ENTRYPOINT ["/usr/local/bin/geth", "--rpc", "--datadir", "/var/lib/ethereum"]

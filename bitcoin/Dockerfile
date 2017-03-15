FROM debian
MAINTAINER Laurent Raufaste <analogue@glop.org>
LABEL version=0.14.0

COPY bin/bitcoin-cli /usr/local/bin/bitcoin-cli
COPY bin/bitcoind /usr/local/bin/bitcoind
RUN useradd bitcoin
RUN mkdir /var/lib/bitcoin
RUN chown bitcoin /var/lib/bitcoin

EXPOSE 8333

VOLUME /var/lib/bitcoin

USER bitcoin
WORKDIR /var/lib/bitcoin

ENTRYPOINT ["/usr/local/bin/bitcoind", "--datadir", "/var/lib/bitcoin"]

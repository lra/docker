# Docker

[![Circle CI](https://circleci.com/gh/lra/docker.svg?style=svg)](https://circleci.com/gh/lra/docker)

Some Docker stuff I use.

## go-ethereum

Official golang implementation of the Ethereum protocol.

### Features

- Don't run `geth` as root
- Persist ethereum blockchain data between stop/start

### Usage

```
# Create the persistent volume that will persist the Ethereum blockchain.
docker volume create --name ethereum-data

# Launch the Go Ethereum container with ports forwarded to the host, and the
# ethereum-data volume mounted
docker run -P -v ethereum-data:/var/lib/ethereum lolo/go-ethereum
```

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

# Launch the Go Ethereum in a container named ethereum, lauched in the
# background (-d), with its ports forwarded to the host (-P), and the
# ethereum-data volume mounted (-v)
docker run --name ethereum -d -P -v ethereum-data:/var/lib/ethereum lolo/go-ethereum
```

## Requirements

- Docker 1.10.2+

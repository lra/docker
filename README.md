# Docker

Some Docker stuff I use.

## go-ethereum

Official golang implementation of the Ethereum protocol.

### Features

- Don't run `geth` as root
- Persist ethereum blockchain data between stop/start

### Usage

```docker run -d -P lolo/go-ethereum```

# Docker

Some Docker stuff I use.

## go-ethereum

### Features

- Don't run `geth` as root
- Persist ethereum blockchain data between stop/start

### Usage

```docker run -d -P lolo/go-ethereum```

# NiFTy-Smart-Contract

Initial recipe borrowed from [nft-mix](https://github.com/PatrickAlphaC/nft-mix). 

## Dependencies


- [Brownie](https://github.com/eth-brownie/brownie#installation)
- [ganache-cli](https://github.com/trufflesuite/ganache#command-line-use) 

## Prerequisites 

- An account with [Infura](https://infura.io/)
- Some kind of wallet (e.g. [Metamask](https://metamask.io/)) to accept test tokens from a [faucet](https://faucets.chain.link)


## Building 

This won't run out of the box. The contracts must be compiled first: 

```
$ brownie compile 
``` 

## Running 

The test run requires `WEB3_INFURA_PROJECT_ID` and `PRIVATE_KEY` env vars to execute. They are defined in the `.env` file:

```
# .env
export WEB3_INFURA_PROJECT_ID="your project's ID string" 
export PRIVATE_KEY="your wallet's private key (don't let anyone else see this)"
```

```
$ source .env 
```

See nft-mix's [documentation](https://github.com/PatrickAlphaC/nft-mix#for-the-simple-erc721) on how to create the testnet token. Since we don't expect the content creators' NFT to interact with other NFTs in any meaningful way (this isn't Pokemon), we can more or less stick with the "simple" token example: 

```
$ brownie run scripts/simple_collectible/deploy_simple.py --network rinkeby
$ brownie run scripts/simple_collectible/create_collectible.py --network rinkeby
```

## Projected Project Structure 

### Components Overview 

![Project structure](docs/img/project.png) 

### Miniting Process 

![Minting process](docs/img/minting.png)

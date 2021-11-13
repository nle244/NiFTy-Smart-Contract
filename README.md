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

The test run requires `WEB3_INFURA_PROJECT_ID` and `PRIVATE_KEY` env vars to execute. 

Make a copy of the `.env-template` file as `.env`: 

```
$ cp .env-template .env
```

Store your credentials in the `.env` file:

```
# .env
export WEB3_INFURA_PROJECT_ID="your project's ID string" 
export PRIVATE_KEY="your wallet's private key (don't let anyone else see this)"
```

The `brownie-config.yaml` file includes an entry that looks for the `.env` file for credentials. If it doesn't happen automatically for some reason, source the `.env` file manually:

```
$ source .env 
```


Once properly set-up, run `main.py` to test it out: 

``` 
$ ./main.py
testing...
Transaction sent: 0x304ad3fb15bb42869de79a61721858eb157d5f4674dac0f796743eabac354c83
  Gas price: 1.000000015 gwei   Gas limit: 2017541   Nonce: 16
  ArtistPicture.constructor confirmed   Block: 9610829   Gas used: 1834129 (90.91%)
  ArtistPicture deployed at: 0x3c16fb87AE40997fC46082B12FDB243F9FA0A564

Transaction sent: 0x247711b1550cf588d46b505ca51e0e6168d441cae51f6630d3a56018c12462c3
  Gas price: 1.000000014 gwei   Gas limit: 279320   Nonce: 17
  ArtistPicture.createCollectible confirmed   Block: 9610830   Gas used: 253928 (90.91%)

Minting complete: https://testnets.opensea.io/assets/0x3c16fb87AE40997fC46082B12FDB243F9FA0A564/<Transaction '0x247711b1550cf588d46b505ca51e0e6168d441cae51f6630d3a56018c12462c3'>
```

I've pinned a couple of different metadata files to be tested out: 
- https://ipfs.io/ipfs/QmPwpUKU1KAxbuTCNBCLfE6N4EPWvyY7g2oBCjfLvtHvof?filename=picture.json (this is already the default)
- https://ipfs.io/ipfs/QmPhJ3LYLc7u3AGzbNEvPaa9TWAVuPkUtv7GCNmoRjUVgJ?filename=tree.json (an image of a binary tree)


## IMPORTANT: `.env` file

Originally, this subsection contained instructions on how to "ignore" changes to the `.env` file, referenced from [here](https://stackoverflow.com/questions/936249/how-to-stop-tracking-and-ignore-changes-to-a-file-in-git/40272289#40272289). Unfortunately, this gets in the way of checking out different branches. 

The recommended way as per Git's official documentation ([link](https://www.git-scm.com/docs/git-update-index#_notes)) is to just not use that feature for untracking config files.

**Perform the following actions only if you've followed the instruction that was listed here before.**

Undo the `--skip-worktree` flag:

```
$ git update-index --no-skip-worktree .env
```

Make a backup of the exiting `.env` file if you already have credentials stored there: 

```
$ cp .env .env-bak 
```

Pull from the repo: 

```
$ git pull
```

That should've removed your local `.env` file. 

Restore your credentials if you had it backed up: 

```
$ mv .env-bak .env
```

## Diagrams for Future Deliverables 

See [docs/README.md](docs/README.md). 

## Projected Project Structure 

### Components Overview 

![Project structure](docs/img/project.png) 

### Miniting Process 

![Minting process](docs/img/minting.png)

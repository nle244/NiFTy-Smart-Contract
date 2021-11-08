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

### Tell git to Ignore `.env` file modifications 

*Answer pulled from [here](https://stackoverflow.com/questions/936249/how-to-stop-tracking-and-ignore-changes-to-a-file-in-git/40272289#40272289)*

If you modify your `.env` file to run demos, git is going to complain about it having uncommitted changes despite it being listed in `.gitignore`:

```
$ git status
On branch development
Your branch is up to date with 'origin/development'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   .env

no changes added to commit (use "git add" and/or "git commit -a")
```

Tell git that you want to keep your own version of the file without polluting the repository (you definitely don't want your wallet's private key showing up on the repo):

```
$ git update-index --skip-worktree .env
```

## Diagrams for Future Deliverables 

See [docs/README.md](docs/README.md). 

## Projected Project Structure 

### Components Overview 

![Project structure](docs/img/project.png) 

### Miniting Process 

![Minting process](docs/img/minting.png)

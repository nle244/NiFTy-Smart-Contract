# NFT Demo

*(This section was migrated here from the root README. We don't need to use nft-mix's demo anymore, but it's here for the record.)*

Since we don't expect the content creators' NFT to interact with other NFTs in any meaningful way (this isn't Pokemon), we can more or less stick with the "simple" token example: 

```
$ brownie run scripts/simple_collectible/deploy_simple.py --network rinkeby
$ brownie run scripts/simple_collectible/create_collectible.py --network rinkeby
```


#!/usr/bin/env python3

from brownie import accounts, network, project, config

OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"
sample_token_uri = "https://ipfs.io/ipfs/QmPwpUKU1KAxbuTCNBCLfE6N4EPWvyY7g2oBCjfLvtHvof?filename=picture.json"

def main():
    print("testing...")
    proj = project.load('./', name='NFT')
    proj.load_config()

    from brownie.project.NFT import ArtistPicture
    minter_wallet = accounts.add(config['wallets']['from_key'])

    network.connect('rinkeby')


    picture_nft = ArtistPicture.deploy({'from': minter_wallet})


    picture_nft.createCollectible(sample_token_uri, {'from': minter_wallet})


    print("Minting complete: {}".format(
        OPENSEA_FORMAT.format(picture_nft.address, 0)
        ))

    
if __name__ == "__main__": 
    main()

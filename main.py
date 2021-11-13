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

    if len(ArtistPicture) == 0:
        picture_nft = ArtistPicture.deploy({'from': minter_wallet})
    else:
        picture_nft = ArtistPicture[-1]

    token_id = picture_nft.tokenCounter()


    transaction = picture_nft.createCollectible(sample_token_uri, {'from': minter_wallet})
    transaction.wait(1)


    print("Minting complete: {}".format(
        OPENSEA_FORMAT.format(picture_nft.address, token_id)
        ))

    
if __name__ == "__main__": 
    main()

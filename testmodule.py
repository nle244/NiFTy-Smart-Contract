#!/usr/bin/env python3

from brownie import accounts, network, project, config
import requests
import os
from pathlib import Path
import json

# name for the project
NFT='NFT'

# Pinata API base URL
PINATA_BASE_URL = 'https://api.pinata.cloud/'

# Pinata pinning endpoints
PINATA_ENDPOINT = 'pinning/pinFileToIPFS'
PINATA_JSON_ENDPOINT = 'pinning/pinJSONToIPFS'

# ipfs base url
IPFS_BASE_URL = 'https://ipfs.io/ipfs/'

# opensea url format
OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"

class ContractError(Exception):
    pass

def load_project():
    """
    Load the project, let Brownie instantiate its singletons,
    and import the ArtistPicture contract.

    Parameters:
        nothing

    Returns:
        proj (Project): the Project singleton instance
    """
    proj = project.load('./', name=NFT)
    proj.load_config()
    return proj

def load_account():
    '''
    Load the wallet defined in the .env file.

    Parameters:
        nothing

    Returns:
        minter_wallet (Account): an Account instance representing the wallet.
    '''
    minter_wallet = accounts.add(config['wallets']['from_key'])
    #print('load_account(): Wallet loaded -- ', minter_wallet)
    return minter_wallet


def connect_to_blockchain():
    '''
    Connect to the Rinkeby testnet.

    Parameters:
        nohting

    Returns:
        nothing
    '''
    network.connect('rinkeby')


def pin_to_pinata(filepath):
    '''
    Upload a file to Pinata.

    Params:
        filepath (str): path to the file to be uploaded.

    Returns:
        json_response (dict): a JSON response from Pinata
    '''
    filename = filepath.split('/')[-1:][0]
    headers = {'pinata_api_key': os.getenv('PINATA_API_KEY'),
                      'pinata_secret_api_key': os.getenv('PINATA_API_SECRET')}

    with Path(filepath).open('rb') as fp:
        image_binary = fp.read()
        response = requests.post(PINATA_BASE_URL + PINATA_ENDPOINT,
                                 files={'file': (filename, image_binary)},
                                 headers=headers)
    #print('pin_to_pinata(): Got response -- ', response.json())

    # json = {'IpfsHash': 'some hash as string', 'PinSize': 1234, 'Timestamp': '2021-11-23T06:03:31.248Z'}
    return response.json()


def pin_json(img_url):
    '''
    Create a JSON that encapsulates img_url and other data, then pins it to Pinata.

    Params:
        img_url (str) : URL to image on Pinata

    Returns:
        json_response (dict): a JSON response from Pinata
    '''
    headers = {'pinata_api_key': os.getenv('PINATA_API_KEY'),
                      'pinata_secret_api_key': os.getenv('PINATA_API_SECRET')}
    ipfs_hash = img_url.split('/')[-1:][0]
    json_data = {
        "name": "Artist Picture",
        "description" : "Hey! This is my selfie.",
        "image" : IPFS_BASE_URL + ipfs_hash,
        "attributes": [
            {
                "trait_type": "Signed to",
                "value": "SuperBigFan1967"
            },
            {
                "trait_type": "Message",
                "value": "Take it easy, keep it classy!"
            }
        ]
    }
    response = requests.post(PINATA_BASE_URL + PINATA_JSON_ENDPOINT,
                             data=json_data,
                             headers=headers)
    print(response.json())
    return response.json()


def load_contract(minter_wallet=None):
    '''
    Load the most recent contract of ArtistPicture type, or
    deploy a new one if no contracts exist.

    Parameters:
        minter_wallet (Account): an Account object.

    Returns:
        picture_nft (ProjectContract): a contract instance
    '''
    from brownie.project.NFT import ArtistPicture

    if len(ArtistPicture) == 0:
        if minter_wallet != None:
            picture_nft = ArtistPicture.deploy({'from': minter_wallet})
            print('load_contract(): deployed new contract -- ', picture_nft)
        else:
            raise ContractError('No existing contract found')
    else:
        # load the most recent contract
        picture_nft = ArtistPicture[-1]
        print("load_contract(): loaded existing contract -- ", picture_nft)
    return picture_nft


def mint_nft(json_url, contract, wallet):
    '''
    Mint the NFT.

    Params:
        json_url (str): IPFS link to the JSON file
        wallet (Account): wallet object returned from load_account()

    Returns:
        transaction, url : finished transaction and an OpenSea link
    '''
    token_id = contract.tokenCounter()

    transaction = contract.createCollectible(json_url, {'from': wallet})
    transaction.wait(1)

    url = OPENSEA_FORMAT.format(contract.address, token_id)

    return transaction, url

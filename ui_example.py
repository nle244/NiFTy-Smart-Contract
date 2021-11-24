#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox

from pathlib import Path
import webbrowser

import testmodule as api_demo

PINATA_BASE_URL = 'https://gateway.pinata.cloud/ipfs/'
IPFS_BASE_URL = 'https://ipfs.io/ipfs/'

def click_link_callback(url):
    '''
    Callback for clicking on URL labels
    '''
    webbrowser.open_new(url)

class NFTApp:
    def __init__(self, root):
        '''
        Initializes the NFTApp testing UI.

        Parameters:
            root (Frame): top-levle Tk() frame.
        '''
        root.title('NFT UI Example')

        mainframe = ttk.Frame(root, padding=10)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ##################################################
        # UI elements for file operations
        ##################################################
        # file path
        self._file_path = StringVar()

        # label for displaying the filepath of the chosen file
        self._filepath_label = ttk.Label(
            mainframe,
            textvariable=self._file_path,
            width=40
        )
        self._filepath_label.grid(column=0, row=0, sticky=(W,E))

        # button for invoking load_filepath()
        self._filepath_button = ttk.Button(
            mainframe,
            text='Load',
            command=self.load_filepath
        )
        self._filepath_button.grid(column=1, row=0, sticky=(W,E))

        ##################################################
        # UI elements for Pinata image
        ##################################################
        # Pinata link
        self._pinata_link = StringVar()

        # label for Pinata link
        self._pinata_label = ttk.Label(
            mainframe,
            textvariable=self._pinata_link,
            cursor='hand2',
            foreground='blue'
        )
        self._pinata_label.grid(column=0, row=1, sticky=(W,E))

        # open a browser on label link click
        self._pinata_label.bind(
            '<Button-1>',
            lambda e : click_link_callback(self._pinata_link.get())
        )

        # button for uploading an image to Pinata
        self._pinata_button = ttk.Button(
            mainframe,
            text='Pin to Pinata',
            command=self.pin_to_pinata
        )
        self._pinata_button.grid(column=1, row=1, sticky=(W,E))

        ##################################################
        # UI elements for generating and pinning JSON to Pinata
        ##################################################
        # link to pinned JSON
        self._json_link = StringVar()

        # label for JSON link
        self._json_label = ttk.Label(
            mainframe,
            textvariable=self._json_link,
            cursor='hand2',
            foreground='blue'
        )
        self._json_label.grid(column=0, row=2, sticky=(W,E))

        # open a browser window on link click
        self._json_label.bind(
            '<Button-1>',
            lambda e : click_link_callback(self._json_link.get())
        )

        # button for uploading json to Pinata
        self._json_button = ttk.Button(
            mainframe,
            text='Generate JSON & Pin it',
            command=self.pin_json
        )
        self._json_button.grid(column=1, row=2, sticky=(W,E))

        ##################################################
        # UI elements for minting
        ##################################################
        # link to minted NFT
        self._nft_link = StringVar()

        # label for nft link
        self._nft_label = ttk.Label(
            mainframe,
            textvariable=self._nft_link,
            cursor='hand2',
            foreground='blue'
        )
        self._nft_label.grid(column=0, row=3, sticky=(W,E))

        # open a browser window on click
        self._nft_label.bind(
            '<Button-1>',
            lambda e : click_link_callback(self._nft_link.get())
        )

        # button for minting
        self._nft_button = ttk.Button(
            mainframe,
            text='Mint NFT',
            command=self.mint_nft
        )
        self._nft_button.grid(column=1, row=3, sticky=(W,E))


        ##################################################
        # Adjustments
        ##################################################
        # padding between elements
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)





    def load_filepath(self, *args):
        '''
        Spawns a filepicker dialog that lets the user choose a file.
        The chosen file's full path is stored in self._file_path.

        Parameters:
            *args : Tkinter callback args.

        Returns:
            nothing
        '''
        filetypes = (
            ('image files', '*.jpg *.png'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Choose a file',
            initialdir=Path.home(),
            filetypes=filetypes
        )
        self._file_path.set(filename)


    def pin_to_pinata(self, *args):
        '''
        Pins the file pointed by self._file_path to Pinata.

        Parameters:
            *args : Tkinter callback args.

        Returns:
            nothing
        '''
        response = api_demo.pin_to_pinata(self._file_path.get())
        try:
            pinned_url = PINATA_BASE_URL + response['IpfsHash']
        except KeyError:
            messagebox.showinfo(
                'Error',
                'Error while pinning!\nMaybe missing Pinata API keys?'
            )
        self._pinata_link.set(pinned_url)


    def pin_json(self, *args):
        '''
        Generate and pin JSON.

        Params:
            *args : Tkinter callback args.

        Returns:
            nothing
        '''
        response = api_demo.pin_json(self._pinata_link.get())
        pinned_url = IPFS_BASE_URL + response['IpfsHash']
        self._json_link.set(pinned_url)


    def mint_nft(self, *args):
        '''
        Mint the NFT.

        Parameters:
            *args: Tkinter callback args.

        Returns:
            nothing
        '''
        # load up the Brownie project
        proj = api_demo.load_project()

        # connect to Rinkeby testnet
        api_demo.connect_to_blockchain()

        # load up wallet info from .env file
        wallet = api_demo.load_account()
        print(wallet)

        # load up existing contract, or create a new one
        contract = api_demo.load_contract(wallet)

        # mint the nft
        transaction, url = api_demo.mint_nft(self._json_link.get(), contract, wallet)
        self._nft_link.set(url)



if __name__ == '__main__':
    root = Tk()
    NFTApp(root)
    root.mainloop()



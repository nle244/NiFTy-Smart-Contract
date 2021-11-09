pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract ArtistPicture is ERC721 {
    uint256 public tokenCounter;
    enum TreeType{BINARY, MEME}

    constructor() public ERC721("Artist's Picture", "ARTIST") {
        tokenCounter = 0;
    }

    function createCollectible(string memory tokenURI) public returns (uint256) {
        uint256 newItemID = tokenCounter;

        _safeMint(msg.sender, newItemID);
        _setTokenURI(newItemID, tokenURI);
        tokenCounter += 1;

        return newItemID;
    }
}

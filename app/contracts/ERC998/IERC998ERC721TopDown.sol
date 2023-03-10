// SPDX-License-Identifier: MIT

pragma solidity 0.8.1;

interface IERC998ERC721TopDown {
    event ReceivedChild(address indexed _from, uint256 indexed _tokenId, address indexed _childContract, uint256 _childTokenId);
    event TransferChild(uint256 indexed tokenId, address indexed _to, address indexed _childContract, uint256 _childTokenId);

    function rootOwnerOf(uint256 _tokenId) external view returns (address rootOwner);
    function rootOwnerOfChild(address _childContract, uint256 _childTokenId) external view returns (address rootOwner);
    function ownerOfChild(address _childContract, uint256 _childTokenId) external view returns (address parentTokenOwner, uint256 parentTokenId);
    function onERC721Received(address _operator, address _from, uint256 _childTokenId, bytes calldata _data) external returns (bytes4);

    // getChild function enables older contracts like cryptokitties to be transferred into a composable
    // The _childContract must approve this contract. Then getChild can be called.
    function getChild(address _from, uint256 _tokenId, address _childContract, uint256 _childTokenId) external;
}

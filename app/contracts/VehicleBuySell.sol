pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract VehicleBuySell is ERC721Full{
    constructor() public ERC721Full("vehicle","CAR") {

    }
    struct vehicleData {
        string make;
        string model;
        uint year;
        string veh_color;
        string veh_title;
    }
    struct participant{
        string seller_name;
        string buyer_name;
        string currencyType;
        uint256 appraisalValue;
    }

    mapping(uint256 => vehicleData) public vehicleCollection;
    mapping(uint256 => participant) public ParticipantCollection;

    function registerVehicle(
        address payable owner, 
        string memory VIN,
        string memory make,
        string memory model,
        uint year,
        string memory veh_color,
        string memory veh_title,
        string memory seller_name,
        string memory buyer_name,
        string memory currencyType,
        uint256 appraisalValue
    ) payable public returns(uint256) {
        uint256 tokenId = totalSupply();
        _mint(owner, tokenId);
        _setTokenURI(tokenId, VIN); //used VIN number as TokenURI
        vehicleCollection[tokenId] = vehicleData(
            make, 
            model, 
            year, 
            veh_color, 
            veh_title
            );
        ParticipantCollection[tokenId] = participant(
            seller_name, 
            buyer_name, 
            currencyType, 
            appraisalValue
            );
        return tokenId;
    }

}
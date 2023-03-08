pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract VehicleBuySell is ERC721Full{
    constructor() public ERC721Full("vehicle","CAR") {

    }
    struct vehicleData {
        string make;
        string model;
        uint year;
        uint mileage;
        string currencyType;
        uint256 appraisalValue;
    }
    mapping(uint256 => vehicleData) public vehicleCollection;

    function registerVehicle(
        address payable owner, 
        string memory VIN,
        string memory make,
        string memory model,
        uint year,
        uint mileage,
        string memory currencyType,
        uint256 appraisalValue
    ) payable public returns(uint256) {
        uint256 tokenId = totalSupply();
        _mint(owner, tokenId);
        _setTokenURI(tokenId, VIN); //used VIN number as TokenURI
        vehicleCollection[tokenId] = vehicleData(make, model, year, mileage, currencyType, appraisalValue);
        //_mint(owner, VIN);
        //vehicleCollection[VIN] = vehicleData(make, model, year, mileage, currencyType, appraisalValue);
        return tokenId;
    }
}
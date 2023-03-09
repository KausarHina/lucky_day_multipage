pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract MotoBuySell is ERC721Full{
    constructor() public ERC721Full("Motorcycle","MOT") {

    }
    struct motoData {
        string moto_make;
        string moto_model;
        uint moto_year;
        string motor_size;
        string moto_color;
    }
    struct participant{
        string seller_name;
        string buyer_name;
        string currencyType;
        uint256 appraisalValue;
    }

    mapping(uint256 => motoData) public motoCollection;
    mapping(uint256 => participant) public ParticipantCollection;

    function registerVehicle(
        address payable owner, 
        string memory moto_vin,
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
        _setTokenURI(tokenId, moto_vin); //used VIN number as TokenURI
        motoCollection[tokenId] = motoData(
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
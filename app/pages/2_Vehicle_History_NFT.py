import streamlit as st
import json
from web3 import Web3
from pathlib import Path
import os
import pathlib
from bip44 import Wallet
from eth_account import Account

w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

def load_vehicle_contract():

    parent_path = pathlib.Path(__file__).parent.parent.resolve() 
    compiled_contract_path = os.path.join(parent_path, "contracts/compiled/vehicle_abi.json")
   
    # Load the contract ABI
    with open(Path(compiled_contract_path)) as f:
        contract_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("VEHICLE_SMART_CONTRACT_ADDRESS")

    # Get the contract
    vehicle_contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return vehicle_contract

def load_accesscontrols_contract():

    parent_path = pathlib.Path(__file__).parent.parent.resolve() 
    compiled_contract_path = os.path.join(parent_path, "contracts/compiled/accesscontrols_abi.json")
   
    # Load the contract ABI
    with open(Path(compiled_contract_path)) as f:
        contract_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("ACCESSCONTROLS_SMART_CONTRACT_ADDRESS")

    # Get the contract
    accesscontrols_contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return accesscontrols_contract

def load_mothistory_contract():

    parent_path = pathlib.Path(__file__).parent.parent.resolve() 
    compiled_contract_path = os.path.join(parent_path, "contracts/compiled/mothistory_abi.json")
   
    # Load the contract ABI
    with open(Path(compiled_contract_path)) as f:
        contract_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("MOTHISTORY_SMART_CONTRACT_ADDRESS")

    # Get the contract
    mothistory_contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return mothistory_contract



def load_service_history_contract():

    parent_path = pathlib.Path(__file__).parent.parent.resolve() 
    compiled_contract_path = os.path.join(parent_path, "contracts/compiled/service_history_abi.json")
   
    # Load the contract ABI
    with open(Path(compiled_contract_path)) as f:
        contract_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SERVICE_HISTORY_SMART_CONTRACT_ADDRESS")

    # Get the contract
    service_history_contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return service_history_contract


def vehicle_history_NFT():
   
    st.set_page_config(page_title="Vehicle History NFT", page_icon="📈", layout="wide")
    st.markdown("# Vehicle History NFT")
    st.sidebar.header("Vehicle History NFT")
    st.write(
        """Vehicle History NFT"""
    )

    #Load accesscontrols_contract
    accesscontrols_contract = load_accesscontrols_contract()
    st.write("accesscontrols_contract address", accesscontrols_contract.address)

    #Load vehicle_contract
    vehicle_contract = load_vehicle_contract()
    st.write("vehicle_contract address", vehicle_contract.address)

    #Load mothistory_contract
    mothistory_contract = load_mothistory_contract()
    st.write("mothistory_contract address", mothistory_contract.address)

    #Load service_history_contract
    service_history_contract = load_service_history_contract()
    st.write("service_history_contract address", service_history_contract.address)

    vehicle_uri = st.text_input("Vehicle URI", max_chars=20)

    vehicle_vin = st.text_input("Vehicle VIN",max_chars=20)

    accounts = w3.eth.accounts
    account = '0x9BfAe49cf5ADBa070c23fF6dED65741817a8D325'

    recipient_address = st.selectbox("Select Recipient Address ", options=accounts)

    sender_account_info = f"Sender Account Address is {account} "
    st.write(sender_account_info)

    if st.button("Mint Vehicle token"):
        transaction_hash = vehicle_contract.functions.mint(vehicle_uri, vehicle_vin, recipient_address ).transact({'from': account, 'gas': 1000000})
        st.write("transaction_hash", transaction_hash)
       
        stored_token_id = vehicle_contract.functions.vinToTokenId(vehicle_vin).call()
        stored_owner_of = vehicle_contract.functions.ownerOf(stored_token_id).call()
        stored_vin = vehicle_contract.functions.tokenIdToVIN(stored_token_id).call() 
        stored_token_uri = vehicle_contract.functions.tokenURI(stored_token_id).call() 
   
        st.write("Successfully Minted Vehicle Token")
        st.write("token_id = ", stored_token_id)
        st.write("vehicle_vin = ", stored_vin)
        st.write("token_uri = ", stored_token_uri)
        st.write("owner_of = ", stored_owner_of)
   



vehicle_history_NFT()


import streamlit as st
import json
from web3 import Web3
from pathlib import Path
import os
import pathlib
from bip44 import Wallet
from eth_account import Account
import pandas as pd

w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

#########################################################################################################################################
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

#########################################################################################################################################
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

#########################################################################################################################################
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

#########################################################################################################################################
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

#########################################################################################################################################
def load_vehicle_history_search(accesscontrols_contract, vehicle_contract, mothistory_contract , service_history_contract) :

    st.write("------------------------------------------------------------------------------------------------------")
    st.markdown("## Vehicle History Search")

    token_id_to_vin_list = []
    token_id_list = []
    i = 1
    token_id_to_vin = search_vehicle_token_id = vehicle_contract.functions.tokenIdToVIN(i).call()

    if len(token_id_to_vin) > 0 :
        token_id_to_vin_list.append(token_id_to_vin)
        token_id_list.append(i)
    
    while len(token_id_to_vin) > 0:
        token_id_to_vin = search_vehicle_token_id = vehicle_contract.functions.tokenIdToVIN(i).call()    
        if len(token_id_to_vin) > 0 :
            i = i + 1
            token_id_to_vin_list.append(token_id_to_vin)
            token_id_list.append(i)

    st.write("Total Vehicle Tokens ", len(token_id_list))
    search_vehicle_token_id = st.selectbox('Select Vehicle token ID ', token_id_list )
   
    st.write("Selected Vehicle Token ID : ", search_vehicle_token_id)
    selected_token_id_to_vin = vehicle_contract.functions.tokenIdToVIN(search_vehicle_token_id).call()   
    st.write("VIN Number of Selected Vehicle Token ID : ", selected_token_id_to_vin) 
        
    mot_address = mothistory_contract.address
    total_child_tokens = vehicle_contract.functions.totalChildTokens( search_vehicle_token_id,  mot_address ).call() 
    
    children = []
    for number in range(total_child_tokens):
        child_token_id = vehicle_contract.functions.childTokenByIndex(search_vehicle_token_id, mot_address, number ).call() 
        child_info = mothistory_contract.functions.getMOTByTokenId(child_token_id).call()
        children.append(child_info)

    df = pd.DataFrame(children, columns =['Mileage', 'Date', 'Garage Address', 'Emission Test', 'Advisories'])

    df['Date'] = pd.to_datetime(df['Date'], unit='s')
    st.write(df)

#########################################################################################################################################
def load_vehicle_nft_mint_section(account, accesscontrols_contract, vehicle_contract, mothistory_contract , service_history_contract) :

    st.write("------------------------------------------------------------------------------------------------------")
    st.markdown("## Vehicle NFT Mint Section")

    vehicle_uri = st.text_input("Vehicle URI", max_chars=20)

    vehicle_vin = st.text_input("Vehicle VIN",max_chars=20)

    accounts = w3.eth.accounts
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

#########################################################################################################################################   
def load_emission_test_nft_mint_section(account, accesscontrols_contract, vehicle_contract, mothistory_contract , service_history_contract) :

    st.write("------------------------------------------------------------------------------------------------------")
    st.markdown("## Emission Test NFT Mint Section")

    emission_test_result = st.radio("What\'s vehicle emission test result", ('Pass', 'Fail'))

    pass_result = False
    if emission_test_result == 'Pass':
        st.write('Your selected emission test Pass')
        pass_result = True
    else:
        st.write('Your selected emission test Fail')

    mileage = st.number_input('Insert vehicle mileage number', min_value=1000, max_value=100000, value=30000, step=1000)

    emission_test_vehicle_token_id = st.number_input('Insert vehicle Token ID', min_value=1, max_value=100, value=2, step=1)

    mileage_number = int(mileage)

    if st.button("Mint Vehicle Emission Test Token"):
        emission_test_vehicle_token_uri = vehicle_contract.functions.tokenURI(emission_test_vehicle_token_id).call() 
        if len(emission_test_vehicle_token_uri) > 0 :
            #mint mot nft to specific vehicle
            transaction_hash = mothistory_contract.functions.mint(vehicle_contract.address, 
                                                                emission_test_vehicle_token_id, 
                                                                emission_test_vehicle_token_uri,
                                                                mileage_number,
                                                                pass_result,
                                                                "" ).transact({'from': account, 'gas': 1000000})
            st.write("transaction_hash", transaction_hash)
        

#########################################################################################################################################
def vehicle_history_NFT():
   
    st.set_page_config(page_title="Vehicle History NFT", page_icon="📈", layout="wide")
    st.markdown("# Vehicle History Report on LuckyDay Blockchain")

    #Load accesscontrols_contract
    accesscontrols_contract = load_accesscontrols_contract()
    if accesscontrols_contract is None :
        return
    #st.write("accesscontrols_contract address", accesscontrols_contract.address)

    #Load vehicle_contract
    vehicle_contract = load_vehicle_contract()
    if vehicle_contract is None :
        return
    
    #st.write("vehicle_contract address", vehicle_contract.address)

    #Load mothistory_contract
    mothistory_contract = load_mothistory_contract()
    if mothistory_contract is None :
        return
    #st.write("mothistory_contract address", mothistory_contract.address)

    #Load service_history_contract
    service_history_contract = load_service_history_contract()
    if service_history_contract is None :
        return
    #st.write("service_history_contract address", service_history_contract.address)

    #Need to modify to select different account
    account = '0x9BfAe49cf5ADBa070c23fF6dED65741817a8D325'

    #Load Vehicle history search section
    load_vehicle_history_search(accesscontrols_contract, vehicle_contract, mothistory_contract , service_history_contract) 

    #Load Vehicle NFT mint section
    load_vehicle_nft_mint_section(account, accesscontrols_contract, vehicle_contract, mothistory_contract , service_history_contract) 

    #Load Emission Test NFT mint section
    load_emission_test_nft_mint_section(account, accesscontrols_contract, vehicle_contract, mothistory_contract , service_history_contract) 

    
#########################################################################################################################################
#########################################################################################################################################


vehicle_history_NFT()


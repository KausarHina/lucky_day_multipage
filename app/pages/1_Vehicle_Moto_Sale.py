# Lucky Day Blockchain Application
################################################################################

################################################################################
# Imports
import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path
from utils import getnums, get_price, send_transaction
from wallet import generate_account, get_balance
from bip44 import Wallet
from eth_account import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

def load_contract(json_path, envpara):
    
    # Load Art Gallery ABI
    #with open(Path('./contracts/compiled/certificate_abi.json')) as f:
    with open(json_path) as f:
        certificate_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv(envpara)

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=certificate_abi
    )
    # Return the contract from the function
    return contract

def form2_callback():
    print("form2_callback executed")
    st.session_state['submit2'] = True

def form3_callback():
    print("form3_callback executed")
    st.session_state['submit3'] = True


def reset_form2_session_state():    
    if 'submit2' not in st.session_state:
        st.session_state['submit2'] = False   

    if 'priceETH' not in st.session_state:
        st.session_state.priceETH=''  

    if 'seller_wallet_address' not in st.session_state:
        st.session_state.seller_wallet_address=''        

    if 'seller_address' not in st.session_state:
        st.session_state.seller_address=''    
       
    if 'veh_price' not in st.session_state:
        st.session_state.veh_price=''     

    if 'veh_pmtCOIN' not in st.session_state:
        st.session_state.veh_pmtCOIN='' 

    if 'veh_make' not in st.session_state:
        st.session_state.veh_make='' 

    if 'veh_model' not in st.session_state:
        st.session_state.veh_model=''    
    
def reset_form3_session_state():    
    if 'submit3' not in st.session_state:
        st.session_state['submit3'] = False

    if 'priceETH' not in st.session_state:
        st.session_state.priceETH='' 
    
    if 'seller_wallet_address' not in st.session_state:
        st.session_state.seller_wallet_address=''     

    if 'seller_address' not in st.session_state:
        st.session_state.seller_address='' 
 
    if 'moto_price' not in st.session_state:
        st.session_state.moto_price=''     

    if 'moto_price' not in st.session_state:
        st.session_state.moto_price=''  

    if 'moto_make' not in st.session_state:
        st.session_state.moto_make=''   

    if 'veh_model' not in st.session_state:
        st.session_state.veh_model=''  

def load_Vehicle_Moto_sale() :
    ################################################################################
    # Step 1:
    # Streamlit Code for Header

    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown("# Lucky Day")
        st.markdown("## Blockchain Smart Contract App")
    with col2:
        clover_image = Image.open(Path('app/Images/clover.png'))
        st.image(clover_image, caption = "")

    # st.markdown("# Lucky Day")
    # st.markdown("## Blockchain Smart Contract App")
    st.markdown("**Conduct your transactions via a transparent, trustworthy decentralized network**")

    ################################################################################
    # Step 2:
    # Get Buyer Wallet data and balance for sidebar
    account = generate_account()
    walletETH = get_balance(w3, account.address)
    buyer_address = account.address

    st.sidebar.markdown("**It's Your Lucky Day to Buy**")
    st.sidebar.write("Your (buyer) Account")
    st.sidebar.write(f"Account Address : {buyer_address}")
    st.sidebar.write(f"Balance: {walletETH}")
    
    def get_wallet():
        walletETH = get_balance(w3, account.address)
        st.sidebar.write(f":blue[your new account balance: {walletETH}]")
        

    ################################################################################
    # Step 3:
    # Streamlit Main Page  - Form for data capture to set up additional form expanders

    #sets up first data collection form
    st.write("")
    form = st.form(key="form_settings", clear_on_submit=False)
    col1, col2, col3 = form.columns([2, 2, 1])

    #1st column dropdown options
    contract_options=["Vehicle", "Motorcycle"]
    type = col1.selectbox(
        "Purchase Type",
        options=contract_options,
        key="type",
    )
    #2nd column dropdown options
    level_options=["Smart Contract Enabled", "Simple Transaction Record"]
    level = col2.radio(
        "Transaction Level",
        options=level_options,
        key="level",
    )

    #3rd column slider option
    excitement = col3.slider(
        "Excitement Level",
        0,
        100,
        key="excitement",
    )

    submit = form.form_submit_button(label="Transaction Type")

    ################################################################################
    # Step 4:
    # Sets up data customization Form 2, with expander for Vehicle, or Form 3 for Motorcycle 

    reset_form2_session_state()
    reset_form3_session_state()
    priceUSD = '' 
    priceETH = '' 
    priceWEI = ''   
    
    
        #connects with Ganache testing addresses to use for seller in this beta version
        # all_ganach_addresses = w3.eth.accounts
    # seller_list = []
    # all_addresses = w3.eth.accounts 
    # for i in range (1,10):
    #     next_address = all_addresses[i]
    #     seller_addresses = seller_list.append(next_address)
    
    # seller_addresses = seller_addresses.pop(0)
        
    seller_addresses = w3.eth.accounts
    seller_addresses = [seller_addresses[1], seller_addresses[2], seller_addresses[3], seller_addresses[4], seller_addresses[5], seller_addresses[6], seller_addresses[7]]
    veh_vin = ""
    veh_make = ""
    veh_model = ""
    veh_year = 0
    ##### Sets up form 2 #####
    if submit == True and type == "Vehicle":
        form2 = st.form(key="form2_settings", clear_on_submit=False)
        reset_form2_session_state()
        
        # Expander opens and collapses the form with 3 columns
        expander = form2.expander("Customize Your Transaction")
        col1style, col2style, col3style = expander.columns([2, 2, 1])
            
    # ---------
    #col 1 data input -Vehicle
        veh_make = col1style.text_input(
            "Vehicle Make",
            max_chars=20,
            key="veh_make",
        )

        veh_model = col1style.text_input(
            "Vehicle Model",
            max_chars=20,
            key="veh_model",
        )

        veh_year = col1style.selectbox(
            "Vehicle Year",
            options=getnums(1980,2023,1),
            key="veh_year"
        )

        veh_vin = col1style.text_input(
            "Vehicle VIN",
            max_chars=17,
            key="veh_vin",
        )
        
        col1style.markdown("---")
        
        seller_name = col1style.text_input(
            "Seller Name",
            max_chars=40,
            key="seller_name",
        )

        # seller addresses from Ganache for beta testing
        seller_address = col1style.selectbox(
            "Seller Wallet Address",
            options = seller_addresses,
            key="seller_address",
        )
        
        # # for real-time use: need this text imput for the seller to enter their wallet address
        # seller_address = col1style.text_input(
        #     "Seller Wallet Address",
        #     max_chars=42,
        #     key="seller_address",
        # )

        
        
    # ---------
    #col 2 data input- Vehicle
        veh_color_options = ["black", "white", "silver", "grey", "beige", "blue", "red", "green", "gold", "other"]
        veh_color = col2style.radio(
            "Vehicle Color",
            options=veh_color_options,
            key="veh_color",
        )
        
        col2style.write(" ")
        
        col2style.write(" ")
        
        col2style.markdown("---")

        buyer_name = col2style.text_input(
            "Your (buyer) Name",
            max_chars=40,
            key="buyer_name",
        )

        
        
    # ---------    
    #col 3 data input- Vehicle
        veh_title_options = ["clean/clear", "lienholder", "electronic", "salvage", "flood/water damage", "rebuilt", "parts"]
        veh_title = col3style.radio(
            "Vehicle Title",
            options=veh_title_options,
            key="veh_title",
        )
        
        col3style.write(" ")
        col3style.write(" ")
        col3style.write(" ") 
        col3style.write(" ") 
        col3style.write(" ")  
        col3style.markdown("---")
        
        pmtCOIN_options =["USD", "ETH"]
        pmtCOIN = col2style.radio(
            "Sale Transaction Coin",
            options=pmtCOIN_options,
            help="This is the coin of choice for the sale transaction",
            key="veh_pmtCOIN"
        )
        
        price = col2style.text_input(
            label="Sale Transaction Price",
            help="This is agreed sale price in the coin of choice listed above",
            key="veh_price"
        )

        
        gas = col3style.text_input(
            "Gas",
            help="Price offering for gas",
            key="veh_gas",
        )
        
        # col3style.write ("Current Avg Gas Price")
        # avg_gas_price = get_gas_price()
        # col3style.write (f"{avg_gas_price}")
        
    # Final Form2 submittal of data to of Transaction Details
        submit_button_form2 = form2.form_submit_button(label='Review Transaction Details', on_click=form2_callback)
        print(f"submit2 = {st.session_state.submit2}")

    # ----------------------------
    # ----------------------------
    seller_address = ""
    ##### Sets up form 3 ####
    if submit == True and type == "Motorcycle":
        form3 = st.form(key="form3_settings", clear_on_submit=False)
        reset_form3_session_state()

        # Expander opens and collapses the form with 3 columns
        expander = form3.expander("Customize Your Transaction")
        col1style, col2style, col3style = expander.columns([2, 2, 1])

    # ---------
        #col 1 data input -Motorcycle
        moto_make = col1style.text_input(
            "Motorcycle Make",
            max_chars=20,
            key="moto_make",
        )

        moto_model = col1style.text_input(
            "Motorcycle Model",
            max_chars=20,
            key="moto_model",
        )

        moto_year = col1style.selectbox(
            "Motorcycle Year",
            options=getnums(1980,2023,1),
            key="moto_year"
        )

        moto_vin = col1style.text_input(
            "Motorcycle VIN",
            max_chars=17,
            key="moto_vin",
        )
        
        col1style.write(" ") 
        
        col1style.markdown("---")
        
        seller_name = col1style.text_input(
            "Seller Name",
            max_chars=40,
            key="seller_name",
        )

        # seller addresses from Ganache for beta testing
        seller_address = col1style.selectbox(
            "Seller Wallet Address",
            options = seller_addresses,
            key="seller_address",
        )
        
        # # for real-time use: need this text imput for the seller to enter their wallet address
        # seller_address = col1style.text_input(
        #     "Seller Wallet Address",
        #     max_chars=42,
        #     key="seller_address"
        # )
        
        
    # ---------
        #col 2 data input- Motorcycle
        motor_size = col2style.text_input(
            "Engine Size",
            max_chars=40,
            key="motor_size",
        )
        
    
        moto_color_options = ["black", "white", "silver", "yellow", "orange", "blue", "red", "green", "gold", "other"]
        moto_color = col2style.radio(
            "Motorcycle Color",
            options=moto_color_options,
            key="moto_color",
        )
        
        col2style.markdown("---")

        buyer_name = col2style.text_input(
            "Buyer Name",
            max_chars=40,
            key="buyer_name",
        )


        pmtCOIN_options =["USD", "ETH"]
        pmtCOIN = col2style.radio(
            "Sale Transaction Coin",
            options=pmtCOIN_options,
            help="This is the coin of choice for the sale transaction",
            key="moto_pmtCOIN"
        )
        
        price = col2style.text_input(
            label="Sale Transaction Price",
            help="This is agreed sale price in the coin of choice listed above",
            key="moto_price"
        )

        
        
    # --------- 
        #col 3 data input- Motorcycle
        moto_title_options = ["clean/clear", "lienholder", "electronic", "salvage", "flood/water damage", "rebuilt", "parts"]
        moto_title = col3style.radio(
            "Motorcycle Title",
            options=moto_title_options,
            key="moto_title",
        )
        
        col3style.write(" ") 
        col3style.write(" ") 
        col3style.write(" ")
        col3style.write(" ")
        col3style.write(" ") 
        col3style.write(" ") 
        col3style.write(" ")  
        col3style.markdown("---")
        
        gas = col3style.text_input(
            "Gas price in wei",
            help="Price offering for gas in wei",
            key="moto_gas",
        )
        
        # col3style.write ("Current Avg Gas Price")
        # avg_gas_price = get_gas_price()
        # col3style.write (f"{avg_gas_price}")

        # Final Form3 submittal of data to of Transaction Details
        submit_button_form3 = form3.form_submit_button(label='Review Transaction Details', on_click=form3_callback)
        print(f"submit3 = {st.session_state.submit3}")

    ################################################################################
    # Step 5: User Review of transaction details before committing to the Blockchain
                
    # ******* need to include code from line 124-129 about contract level == Simple Transaction Record *** 

    if st.session_state.submit2 == True or st.session_state.submit3 == True:       
        
        print(f"st.session_state.submit2={st.session_state.submit2} st.session_state.submit3={st.session_state.submit3}")

        #calculate price here
        if type == "Vehicle":
            price = st.session_state.veh_price 
            pmtCOIN = st.session_state.veh_pmtCOIN
        else:
            price = st.session_state.moto_price
            pmtCOIN = st.session_state.moto_pmtCOIN

        if price != '' : 
            priceUSD, priceETH, priceWEI = get_price(w3, pmtCOIN, price)
        else:
            priceUSD = '' 
            priceETH = '' 
            priceWEI = ''   
    
        # Establish wallet has enough eth for transaction, and print sidebar balance if transaction would go through
        print(f"priceETH={priceETH} walletETH={walletETH}")
        if priceETH != '' and float(priceETH) <= float(walletETH):
            new_balance = float(walletETH) - float(priceETH)
            
            st.markdown("---")
            st.write("**The blockchain sale transaction will be in wei**")
            st.write("current market price of Ethereum")                  
            st.write(f"${priceUSD} USD = {priceETH} ETH = {priceWEI} wei")
            st.markdown("---")
            
            st.session_state.priceETH=priceETH
            st.session_state.seller_wallet_address=st.session_state.seller_address

            #print(f"st.session_state.seller_address={st.session_state.seller_address}, st.session_state.priceETH={st.session_state.priceETH}")
            
            st.sidebar.write(" ")
            st.sidebar.write(" ")
            if type == "Vehicle":
                st.sidebar.write(f":blue[If you buy this {st.session_state.veh_make} {st.session_state.veh_model} for, {priceETH} ETH]")
                st.sidebar.write(f":blue[your new balance: {new_balance}]")
            else:
                st.sidebar.write(f":blue[If you buy this {st.session_state.moto_make} {st.session_state.moto_model} for, {priceETH} ETH]")
                st.sidebar.write(f":blue[your new balance: {new_balance}]")
            
            
              #Text propmting user to review transaction details before execution
            st.write(" ")
            st.markdown("---")
            st.markdown("### If this sale record looks correct, press the button below")
            st.markdown("### to complete the transaction and record it to the Blockchain")    
            st.write(" ")
            
            buyer_name_address=f"<p style=\"color:Red;\" > BUYER INFO : {st.session_state.buyer_name} @ {buyer_address} </p>"
            st.markdown( buyer_name_address, unsafe_allow_html=True)

            price_pmtCOIN=f"<p style=\"color:Red;\" > {price} @ {pmtCOIN} =  {priceWEI} @ wei </p>"
            st.markdown( price_pmtCOIN, unsafe_allow_html=True)

            to_str=f"<p style=\"color:Red;\" > <b>TO </b> </p>"
            st.markdown( to_str, unsafe_allow_html=True)

            seller_name_address=  f"<p style=\"color:Red;\" > SELLER INFO : {st.session_state.seller_name} @ {st.session_state.seller_address} </p>"
            st.markdown( seller_name_address, unsafe_allow_html=True)

            #st.markdown(f":red[*paying {price}{pmtCOIN}*]")
            #st.markdown(f":red[*to*]")
            #st.markdown(f":red[*{st.session_state.seller_name} @ {st.session_state.seller_address}*]")

            if type =="Vehicle":

                veh_info=f"<p style=\"color:Red;\" > for the {st.session_state.veh_year} {st.session_state.veh_make}, {st.session_state.veh_model} </p>"
                #st.write(f":red[*for the {st.session_state.veh_year} {st.session_state.veh_make}, {st.session_state.veh_model}*]")
                st.markdown( veh_info, unsafe_allow_html=True)

            else:
                moto_info=f"<p style=\"color:Red;\" > for the {st.session_state.moto_year}, {st.session_state.moto_make}, {st.session_state.moto_model} </p>"
                #st.write(f":red[*for the {st.session_state.moto_year}, {st.session_state.moto_make}, {st.session_state.moto_model}*]")
                st.markdown( moto_info, unsafe_allow_html=True)                     
         
        # else statement if wallet balance from line 450 is less than the sales transaction amount
        else:
            if type == "Vehicle":
                print(f"veh_make={st.session_state.veh_make}")
                st.write(f"With a balance of {walletETH} ether in your wallet, you can't afford this {st.session_state.veh_make} {st.session_state.veh_model} for, {priceETH} ETH.")
            else:
                st.write(f"With a balance of {walletETH} ether in your wallet, you can't afford this {st.session_state.moto_make} {st.session_state.moto_model} for, {priceETH} ETH.")
    
    
  ################################################################################
    # Step 6:
    # Link Smart Contract
    # ******* neet to include code from line 124-129 about contract level == Smart Contract Enabled
    if (st.session_state.submit2 == True or st.session_state.submit3 == True) and level == "Smart Contract Enabled":
        parent_path = pathlib.Path(__file__).parent.parent.resolve() 
        compiled_contract_path = os.path.join(parent_path, "contracts/compiled/vehicle_buysell.json")
        contract = load_contract(compiled_contract_path, "SMART_CONTRACT_VEHICLE")
        print("vin:",veh_vin)
        tx_hash = contract.functions.registerVehicle(
                    buyer_address, 
                    veh_vin,
                    veh_make,
                    veh_model,
                    veh_year, #veh_color
                    10000,
                    pmtCOIN,
                    int(price)
                ).transact({'from':buyer_address, 'value': w3.toWei(int(price), "ether"), 'gas':1000000})
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        st.write("Transaction Receipt Mined:")
        st.write(dict(receipt))

    ###############################################################################
    # Step 7:
    # Streamlit “Complete Transaction” button code so that when someone clicks the
    # button, the transaction is added to the blockchain.

    st.session_state['submit2'] = False
    st.session_state['submit3'] = False

    if st.button("Complete Transaction"):
        print(f"st.session_state.seller_wallet_address={st.session_state.seller_wallet_address}, st.session_state.priceETH={st.session_state.priceETH}")
        transaction_complete = send_transaction(w3, account, st.session_state.seller_wallet_address, st.session_state.priceETH)
        st.write("Your transaction on the Ganache Blockchain tester is complete!")
        st.write("Here is the hash code confirming your transaction")
        st.write(f"{transaction_complete}")
        st.write("/n")
        get_wallet()
        if type == "Vehicle":
            st.markdown("## Congratulations on buying your vehicle!")
            st.balloons()
        else:
            st.markdown("## Congratulations on buying your motorcycle!")
            st.balloons()
        
        

    ################################################################################
##################
    # Step 8:
    # App github link and notes
    st.markdown("---")

    st.write(
        " "
    )

    share_msg=f"<p style=\"color:Blue;\"> <b> Share with your friends and make buying and selling your lucky day! </b> </p>"
    st.markdown(share_msg, unsafe_allow_html=True)

    st.write(
        " "
    )
    st.markdown("If you liked this app give us a :thumbsup: it keeps us creating more great tools for the future of Blockchain!")

    st.write("More infos and :star: at [github.com/KausarHina/lucky_day_multipage](https://github.com/KausarHina/lucky_day_multipage)")

    ################################################################################



load_Vehicle_Moto_sale()
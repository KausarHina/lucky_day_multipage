# lucky_day

---

## Blockchain Buy/Sell App

This project is a 2-page Streamlit app built to handle private and public blockchain sales transactions. 

Page 1: Private transactions of vehicle/motorcycle sales can be handled with user input data to complete the sale via a simple blockchain wei transaction or using a smart contract for tokenization of the VIN and tracking of all transactions with that token in addition to the monetary transaction.

Page 2: A second functionality of the app interface uses a smart contract, built using Solidity and ERC721 standards, to tokenize NFT assets and handle the auction of those tokens via a public blockchain network. 

The user can choose a page for which type of transaction they wish to use: buying a vehicle/motorcycle or auctioning their assets.

This project leverages the program Ganache to connect the user's crypto wallet, RemixIDE to compile the Solidity smart contracts, MetaMask to connect Remix to Ganache. ChainLink, Pinata and Photoshop are also utilized for the auction house functionality.

## Blockchain Vehicle History Report

Page 3: LuckyDay Vehicle History Report is a development beta function of the LuckyDay web app , for storing vehicle history records on the blockchain. Right now the vehicle history records are distributed among dealers, insurance companies, collision centers, and DMVs etc. The main purpose of the LuckyDay Vehicle History report is to bring all scattered records to one place and give a role based access to different parties to add the different history records in the LuckyDay blockchain. For example: the records for emission tests , repair works, Oil changes etc. can be added to the blockchain by different parties and can not be altered later. The successive buyer will have unaltered and complete history of the vehicle before buying it. 


---

# Technologies
python 3.8

Streamlit 1.17.0

Web3 5.17

mnemonic 0.20

bip44 0.1.3

os-sys 2.1.4

python-dotenv 0.21.1

ethereum 2.3.2

solidity 0.8.1

https://trufflesuite.com/ganache/

www.metamask.io

www.remix.ethereum.org

www.pinata.cloud

---

# Installation Overview
Step 1 - Create new conda environment & install required Technologies

Step 2 - Download/ Open necessary 3rd party applications

Step 3 - Gather mneumonic, API keys to create new .env file

Step 4 - Deploy Smart Contract for Vehicle/ Moto Sale

Step 5 - Follow link to Set-up and User Guide for **NFT Auction**

Step 6 - Follow links to Set-up and User Guide for **Vehicle History Records**


---

### Step 1 - Conda Environment and Technologies installation
1. Open your terminal and start a new dev env

    ```
    `conda create -n dev python=3.8 anaconda`
    ```

2. Activate your dev envnironment
    ```
    `conda activate dev`
    ```

3. Install required Technologies in development environment
    ```
    pip install streamlit
    pip install web3
    pip install mnemonic
    pip install bip44
    pip install os-sys
    pip install python-dotenv
    pip install ethereum
    ```

4. In the directory of your choice, clone this repository
    ```
    `git clone git@github.com:KausarHina/lucky_day_multipage.git`
    ```

### Step 2 - Download/ Open Browser Applications
1. Download Ganache to local system
    www.https://trufflesuite.com/ganache/
    
    - click on download to your local system
    
    - open Ganache using a Quick Start button
    
2. Download MetaMask to local system
    www.metamask.io
    
    - click on Download button and follow instructions to set up account

3. Open ReMix browser application
    www.remix.ethereum.org
    
    
4. Open Pinata browser application
    www.pinata.cloud
    
    - create Log in account
    
### Step 3 - Gather Data for .env  file    
1. Navigate to Ganache Dashboard for mneumonic string
    At top of the dasboard under the "Accounts" Tab, will be a mnemonic string

    <img  src="./app/Images/mnemonic_ex.png"  width="600" />

    - copy the string to your clipboard
    
    -
    
2. Navigate to the sample.env file in your lucky_day cloned directory 

    open the IDE of your choice and navigate into the app folder, copy  `sample.env` in a new file

    paste the string value saved on your clipboard to the MNEMONIC variable 

    ```
    MNEMONIC=''
    VEHICLE_SMART_CONTRACT_ADDRESS=''
    ACCESSCONTROLS_SMART_CONTRACT_ADDRESS=''
    MOTHISTORY_SMART_CONTRACT_ADDRESS=''
    SERVICE_HISTORY_SMART_CONTRACT_ADDRESS=''
    WEB3_PROVIDER_URI='HTTP://127.0.0.1:7545'
    PINATA_API_KEY=''
    PINATA_SECRET_API_KEY=''
    JWT=''
    ```
    
    - save the file as simply '.env

    
    -
    
    <img  src="./app/Images/directory.png"  width="200" />
    
    - **this mnemonic will be used to create a wallet with public and private key for you use on the local Ganache testing Blockchain**
    
    -
    
3. Navigate back to Pinata browser window to get API keys

    - click "API Keys" on the left sidebar menu
    
    - click on "+ New Key" button
    
    - turn slidebar in 'Admin' section to 'ON"
    
    - enter a name for your keys 
    
    - click "Create Key"
    
    - Save all key information to a safe place
    
    <img  src="./app/Images/pinata_API_keys.png"  width="600" /> 
    
    - return to the repo .env file you created, and copy the API keys and JWT values here
    ```
    PINATA_API_KEY=''
    PINATA_SECRET_API_KEY=''
    JWT=''
    ```
    -
    
4. Connect Metamask account to Ganache

    - open Ganache and copy RPC Server listed in the top
    
    <img  src="./app/Images/RPC_Server.png"  width="600" />  
    
    - Open Metamask from Chrome Extensions menu top Right of browser window
    
    - Click on Ethereum Mainnet Network dropdown, choose Add Network or Custom RPC, which ever shows up
    
        <img  src="./app/Images/meta_mask_network.png"  width="200" /> 
    
    - Fill in Network Name: "Ganache TestNetwork", RPC Url: paste RPC Server value from clipboard, Chain ID: "1337", click Save Icon
    
    - Click on circular My Account Icon, and choose "Import Account" from dropdown
    
    - Navigate back to Ganache to get account key choose any account (not the first listed), click on the key icon (far right) and copy the private key value
    
    - Navigate back to MetaMask screen and paste the private key value, then choose "Import"
    
    - You can repeat this process for as many accounts as you would like to have for your test network, and rename them as you like
    

### Step 4 - Deploy Smart Contract for Vehicle/ Moto Sale

```
    
```
    
    
### Step 5 - Link to Set-up & User Guide - NFT Auction
1. Follow the 'LD_README.pdf' for detailed set-up steps and User Guide

    ![NFT_Auction_Instructions ](./LD_README.pdf)


### Step 6 - Link to Set-up & User Guide - Vehicle History Report
1. Follow the 'VehicleHistoryReport_SmartContracts_Setup.pdf' for detailed setting up steps

    ![Vehicle History Report Smart Contracts Setup ](./VehicleHistoryReport_SmartContracts_Setup.pdf)

2. Follow the 'VehicleHistoryReport_UserGuide.pdf' for detailed user guide steps

    ![Vehicle History Report UserGuide ](./VehicleHistoryReport_UserGuide.pdf)

---

## Run lucky_day

1. Navigate to your terminal, then to the directory where you cloned the lucky_day repository
    ```
        - run `streamlit run app/app.py` 

        or 

        execute `./run.sh`
    ```   
2. Navigate to streamlit page running locally in browser window

3. In the sidebar menu, select the type of transaction you would like to conduct
    - "Vehicle Moto Sale"
    - "Lucky Day Auction NFT"
    - "Vehicle_History_Report"
    
    <img  src="./app/Images/LuckyDayMainPage.png"  width="600" />   

4. You will be directed to your page of choice.

---

## Vehicle / Motorcycle Sale
    
*Note*
    *your wallet and public address will be listed as the first address on the Ganache dashboard*
    *as described below in step 4*
    <img  src="./app/Images/address.png"  width="600" />  
   

1. Enter the data appropriate for the sale type, and choose whether you wish to have the transaction remain a 'Simple       Blockchain Transaction' where only the wei transaction and the addresses of buyer and seller will be recorded, or if "Smart Contract Enabled" is your preferance, where a token is created for your VIN and all sale transaction information is recorded to your vin/token.

2. Hit the "Transaction Type" button, to register your preferences.

    <img  src="./app/Images/sale_main_page.png"  width="600" /> 

3. An expandable menu will appear. Click the "Customize Your Transaction" button.
    
    <img  src="./app/Images/customize_transaction.png"  width="600" />     
    
4. Enter the specific information about the vehicle or motorcycle you are buying, the seller name and address, and enter your name, and gas for the transaction.

    
    <img  src="./app/Images/data_form_top.png"  width="600" /> 
    <img  src="./app/Images/data_form_bottom.png"  width="600" /> 

5. Hit the "Review Transaction Details" button on the bottom of the expander
        - the current USD to ETH to wei equivalents are listed
        - the details you entered about the transaction are listed as a transaction record for final review
    
    <img  src="./app/Images/transaction_review.png"  width="600" /> 
    
6. Hit the "Complete Transaction" button on the bottom of the expander
    -see the transactions hash code printed below the button verifying the hash code added to the block as the transaction was processed. Your new wallet balance will appear on the sidebar.
    <img  src="./app/Images/sale_hash.png"  width="600" />  

7. You can verify this transaction by navigating to your Ganache dashboard and clicking on the "Transactions" tab

    <img  src="./app/Images/ganache_transaction.png"  width="600" />

    <img  src="./app/Images/transaction_detail.png"  width="600" />

8. The amount paid will also be subtracted from your wallet balance, listed next to your wallet address on the "Accounts" page
    - (you can also see the transaction price added to the seller's Address that you listed in the app because for this beta version the seller addresses are in your Ganache test network)

    <img  src="./app/Images/my_gan_acct.png"  width="600" />


---


# Limitations
1. Solidity Smart Contract for NFT Auction created, but will not compile without errors. See code here
![Artifacts_AuctionContract](./Artifacts/Auction.sol)

---


# Contributors

Jodi Artman.  *github.com/Arty-j*

Kausar Hina.  *github.com/KausarHina*

Marissa Gonzalas.  *github.com/Marissagonzales468*

Edith Chou.   *github.com/wf880180*

---

# License

licensed in accordance with UC Berkeley policy
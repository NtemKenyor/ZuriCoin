from transactions.transaction_arena import Transactions
from wallets.wallet_ import Wallet
import random
from blocks.block_area import Block
from mining.zuri_mine import Minable
from wallet_Address.create_address import Address_Creator
from filing.create_file import FileCoins
from filing.retrive_filed import turnfile2Zuri
from coin_balance.check_wal_bal import wallet_balance
import requests
import hashlib
import sys
#import "wallets/wallet.py"

def SHA256(text):
    return hashlib.sha256(text.encode('ascii')).hexdigest()

def mine_side():
    minable_blocks = Minable()
    pending = minable_blocks.get_all()
    print("To mine you need to have a Zuri Wallet Address. You also need upto a minimum amount of Zuri coins in your Wallet. \n \
         This is to help the community understand that you have invested your financial resource on this project. Before trying to Mine.")
    reward_address = input("Where should the reward for mining Zuri be sent to? \n")
    for i in pending:
        print(i)
        for nonce in range(100, 201):
            past_hash = i.get("previous_hash")
            previous_hash = ""
            if past_hash is not "#WAZIRI#":
                print("Block Number: {}".format(str(i.get("count"))))
                previous_hash = past_hash.split("#WAZIRI#")[0]
            Tblock = Block(i.get("count"), i.get("sender_address"), i.get("receiver_address"), i.get("amount"), previous_hash, nonce)
            hashed = Tblock._hash_area()
            """ print(str(nonce) + "->" + i.get("sender_address") + "->" + i.get("receiver_address") + "->" + str(float(i.get("amount"))) + "->" + previous_hash )
            downtown = SHA256(str(nonce) + "->" + i.get("sender_address") + "->" + i.get("receiver_address") + "->" + str(float(i.get("amount"))) + "->" + previous_hash)
            print(downtown)  """
            data = {"miner_address": reward_address,
            "block_count":  i.get("count"),
            "nonce": nonce,
            "transaction_py": hashed,
            }
            ch = requests.post("https://a1in1.com/Zuri Coin/Waziri_Coin/mining_leges.php", data=data)
            print("Hashed Value: {}".format(hashed))
            print(ch.text)
            the_out = dict(ch.json())

            if (the_out.get("status") == "true"):
                print("GoodNews You have mined Zuri")
                break
        #print(i.get("count"))

if(len(sys.argv) > 1):
    passed_lst = sys.argv
    dir_digit = passed_lst[1]
    if(dir_digit.isdigit() == True):
        #print(passed_lst[1])
        dir_digit = int(dir_digit)
        if dir_digit == 1:
            wallet = Wallet()
            wallet.create_keys()
            wallet.save_keys()
        elif dir_digit == 3:
            print("No wallet can have up to 1,000,000 addresses \n")
            print("Your Wallet Address would look like:")
            print("Zuri + Random(000000) + access_token_modified + public_key_modified ")
            print("So any random number within this range belongs to you.")
            print("You can manually create your own address as to receive Zuricoin.")
            pub_key_dat = passed_lst[2]
            access_tok = passed_lst[3]
            
            if (pub_key_dat is not None and access_tok is not None ):
                print("one of your 999,999 Wallet Address is: ")
                address = Address_Creator(access_tok, pub_key_dat).rand()
                print(address)
else:
    menu = "1 to create your Zuri Wallet \n2 to send ZuriCoin \n3 to Receive a List of all your Possible wallet Addresses \n4 to mine Zuri Coin \n5 to File Zuri Coin \n6 to Retrieve Zuri coin \n7 to Get instructions  \n8 Repeat Menu \n9 Check Wallet Balance \n10 Exit \nTo back-up your wallets, you would need to save wallet.txt in the cloud, on a card reader or on an external disk drive.\n You can also write your keys on paper and store somewhere save. "
    print(menu)

    exit = 1
    while(exit):
        #print(BLAKE2B_("Hello Dear"))
        #print(SHA256("Hello Dear"))
        x = input("Please Enter a Number from 1-9 as Described Above\n")
        if( x.isdigit() == True ):
            x = int(x)
            if (x == 1):
                wallet = Wallet()
                wallet.create_keys()
                wallet.save_keys()
                #wallet.load_keys()
            elif (x == 2):
                trans = Transactions()
            elif (x == 3):
                print("No wallet can have up to 1,000,000 addresses \n")
                print("Your Wallet Address would look like:")
                print("Zuri + Random(000000) + access_token_modified + public_key_modified ")
                print("So any random number within this range belongs to you.")
                print("You can manually create your own address as to receive Zuricoin.")
                pub_key_dat = input("Enter a public key \n")
                access_tok = input("Enter a Access token \n")
                
                if (pub_key_dat is not None and access_tok is not None ):
                    print("one of your 999,999 Wallet Address is: ")
                    address = Address_Creator(access_tok, pub_key_dat).rand()
                    print(address)

                #wallet = Wallet()
                #wallet.print_keys()

            elif (x == 4):
                mine_side()
            elif (x == 5):
                #file zuri coin
                FileCoins()
            elif (x == 6):
                #retrieve the filed zuri coin...
                turnfile2Zuri()
            elif (x == 7):
                print("All Generated keys are in Wallet.txt...\n")
                print("Please save your wallet.txt offline or write the keys down and hide them. \n")
                print("Please do not expose your private keys...\nYou can clone ZuriCoin from Github and use the entire software to create and store your coins. It is easy and simple. You only need Python installed")
            elif(x == 8):
                print(menu)
            elif(x == 9):
                wallet_addr = input("Please Enter your Wallet Address: ")
                wallet_balance(wallet_addr)
            elif(x == 10):
                exit = 0
                
        else:
            print("Only integers are allowed.")

#Zuri327592fdc525166aee28cd6bad2af5702a6c6002d792cbc3f47bbea041
#Zuri586680fdc525166aee28cd6bad2af5702a6c6002d792cbc3f47bbea041
#Zuri797879fdc525166aee28cd6bad2af5702a6c6002d792cbc3f47bbea041

#vD9hL1mC7aL8oO0sF4dP3yI1iV5kC3gA4rV1tV8lC1eB0nE034
#$2y$10$elxCwHrsgEQrToJy5IBIT.hfxhvdDBcZy9QC\/ElOn6vJY9u8pP1vC
#45

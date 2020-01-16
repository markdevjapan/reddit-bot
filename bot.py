import praw
import config
import time
import os
import requests

def bot_login():
	print("Loggin in...")
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "The IOTA YourFriendlyIOTABOT by pmayall")
	print("Logged in!")

	return r

def get_usd():
	r = requests.get('https://api.cryptonator.com/api/ticker/iot-usd')
	return r.json()

def run_bot(r, comments_replied_to):

	for comment in r.subreddit('iota+CryptoCurrency+IOTAmarkets+CryptoMarkets+altcoin+CoinBase+Best_of_Crypto+BitcoinMarkets+Blockchain+BitcoinMining+Bitcoin_Unlimited+BitcoinXT+Crypto+CryptoMarkets+CryptoTrade+DoItForTheCoin+EthTrader+Jobs4Crypto+Liberland+LitecoinMarkets+LitecoinMining+XMRtrader+GPUmining').comments(limit=5):

		if comment.id not in comments_replied_to:
			print(comment.id + " is not in the comments ---------------- ")
			if comment.author != r.user.me() and comment.author != "iotaTipBot":
				print(str(comment.author) + " is not the commemt author -------------")

				if "iota --define" in comment.body or "What is Iota" in comment.body or "what is Iota" in comment.body or "what is iota" in comment.body or "What is iota" in comment.body or "what is IOTA" in comment.body or "What is IOTA" in comment.body:
					print("found one of the phrases ----------------")
					comment.reply("IOTA is the revolutionary new CryptoCurrency built on Tangle (read: [Whitepaper](https://iota.org/IOTA_Whitepaper.pdf)). A blockless distributed ledger which is scalable, lightweight and for the first time ever makes it possible to transfer value without any fees. \n\n You can type `iota --buy` as a comment reply for information on buying IOTA")
					comments_replied_to.append(comment.id)
				elif "iota --buy" in comment.body or "how to buy iota" in comment.body.lower() or "where to buy iota" in comment.body.lower() or "how do i buy iota" in comment.body.lower():
					print("second statement found ------------")
					comment.reply("You can buy IOTA by visiting: [How to Buy IOTA](https://howtobuyiota.co.uk) \n\n *If this bot has fired incorrectly, please send me a message /u/pmayall. This bot is very new and is still a work in progress. Thank you for your understanding* \n\n[IOTA Dashboard](https://iota.guide/dashboard) | [Wiki](https://iota.guide/reddit-bot/wiki/)")
					comments_replied_to.append(comment.id)
				elif "iota --seed" in comment.body or "generate iota seed" in comment.body or "Generate Seed" in comment.body:
					comment.reply("Check out the [How To Generate My IOTA Wallet Seed](https://iota.guide/seed/how-to-generate-iota-wallet-seed/). You might also want to give [A Guide to Setting up Cold Storage for IOTA](https://iota.guide/seed/how-to-set-up-cold-storage/) a glance")
					comments_replied_to.append(comment.id)
				elif "iota --help" in comment.body:
					comment.reply("You can type the following commands in the comments for help with IOTA: \n\n `iota --define` : This will give a quick definition of what IOTA is. \n\n`iota --buy` : This will link you to intructions on how to buy IOTA \n\n `iota --seed` : This will tell you what an IOTA seed is and how to generate your own. \n\n More will be added shortly.")
					comments_replied_to.append(comment.id)

				with open ("comments_replied_to.txt", "a") as f:
					f.write(comment.id + "\n")

					print("added  " + str(comment.id)  + " id to text file")


	print ("Sleeping for 10 seconds...")
	#Sleep for 10 seconds...
	time.sleep(10)

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = list(filter(None, comments_replied_to))
	return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print (comments_replied_to)

count = 0
while (count < 5):
   print ('The count is:', count)
   count = count + 1
   run_bot(r, comments_replied_to)

print("Good bye!")
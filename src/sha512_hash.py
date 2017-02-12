import argparse
from Crypto.Hash import SHA512

#Create the help menu
parser = argparse.ArgumentParser(description='Hashes arguments into sha512')
parser.add_argument('text', metavar='\"Text\"', type=str,
                    help='Input the text that is going to be hashed, use quotations \" followed by text and close with another quotation \" if you are going to be including spaces')

#Parse the arguments that are being passed through
args = parser.parse_args()

#Function that hashes any text that is being passed to it
def hashing(message):
  print 'hashing:', message
  hasher = SHA512.new()
  hasher.update(message)
  print hasher.hexdigest()

#Calling the hash function and grabs the text argument from the command
hashing(args.text)
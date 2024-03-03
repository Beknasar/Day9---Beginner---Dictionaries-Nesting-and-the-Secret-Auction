from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
bidders = {}
print(logo)
print("Welcome to the secret auction program.")
end = False

while not end:
  name = input("What is your name?: ").strip().lower()
  bid = int(input("What's your bid?: $"))
  
  bidders[name] = bid
  
  answer = input("Are there any other bidders? Type 'yes' or 'no'. ").strip().lower()
  if answer == "no":
    max = 0
    winner = ""
    #finding max bid
    for bidder in bidders:
      bidder_bid = bidders[bidder]
      if bidder_bid > max:
        max = bidder_bid
        winner = bidder
    print(f"The winner is {winner.capitalize()} with a bid of ${max}")
    end = True
  elif answer == "yes":
    clear()

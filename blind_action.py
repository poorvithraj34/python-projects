def find_highest_bidder(bidding_dictinory):
    winner=""
    highest_bit=0

    for bidder in bidding_dictinory:
        bid_amount=bidding_dictinory[bidder]
        if bid_amount>highest_bit:
            highest_bit=bid_amount
            winner=bidder
    

    print(f"The winner is : {winner} with a bid of ${highest_bit}")
        

bids={}
continue_bidding=True
while continue_bidding:
    name=input("enter the name?:")
    bid_price=int(input("what is  the bid price:"))
    bids[name]=bid_price
    should_continue=input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        continue_bidding=False
        find_highest_bidder(bids)
    elif should_continue =="yes":
        print("\n"*20)

            






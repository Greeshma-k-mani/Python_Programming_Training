#Inheritance

class VISACARD:
    def __init__(self,holder_name,card_number):
        self.holder_name=holder_name
        self.card_number=card_number
    def display_details(self):
        print(self.holder_name)
        print(self.card_number)
    def compute_rewards(self,amount):
        reward=amount*0.01
        print("The reward for VISA is:",reward)

class HPVISACARD(VISACARD):
    def compute_reward(self,purchase_type,amount):
        reward=amount*0.01
        if purchase_type=="Fuel":
            reward=reward+10
        print("The reward for HPVISA is:",reward)

#Input
card_type=input("Enter the card_type:").strip()
if card_type not in ["VISA","HPVISA"]:
    print("Invalid card_type")
else:
    holder_name=input("Enter the name:").strip()
    card_number=input("Enter the number:").strip()
    amount=float(input("Enter the amount:"))
    purchase_type=input("Enter the purchase_type:").strip()

    if card_type=="VISA":
        card=VISACARD(holder_name,card_number)
        card.display_details()
        card.compute_rewards(amount)
    else:
        card=HPVISACARD(holder_name,card_number)
        card.display_details()
        card.compute_rewards(purchase_type,amount)
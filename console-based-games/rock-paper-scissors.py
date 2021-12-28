import random 

rule_dict = {"rock": {
    "win" : ["scissors"],
    "lose" : ["paper"]
},
"paper":{
    "win" : ["rock"],
    "loose" : ["scissors"]
},
"scissors":{
    "win" : ["paper"],
    "lose" : ["rock"]
}}

class RockPaperScissors:
    
    def __init__(self):
        print("Initializing Components")
        
    def computer_selection(self):
        choice_list = ['rock', 'paper', 'scissors']
        return random.choice(choice_list)
        
    def check_rule(self,user_selection,computer_selection):
        reduced_dict = rule_dict[user_selection]
        return "User has won by selecting :: "+user_selection+" against :: "+computer_selection if computer_selection in reduced_dict["win"] else "Compter has won by selecting :: "+computer_selection+" against :: "+user_selection

        
    def take_decision(self,user_selection,computer_selection):
        return "Its a Tie" if user_selection == computer_selection else self.check_rule(user_selection,computer_selection)
    
play_instance = RockPaperScissors()
user_selection = input("Enter user choice !!! ")
computer_selection = play_instance.computer_selection()
print(play_instance.take_decision(user_selection,computer_selection))
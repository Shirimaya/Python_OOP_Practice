from basic_actions.actions import walk
from basic_actions.actions import questions
from basic_actions.actions import display
import os
#Ask user where to go
#class 1 from basic actions
class Asking_where_to_go(questions, display):
    def __init__ (self):
        pass

    #Asking Where to go
    def going_to():
        num_choice = 5
        while (True):          
            try:              
                
                questions.where_to_go() #asks the question
                display.disp_location() #displays list of locations
                num_choice = int(input('Please Input a Number: ')) #asking for input choice                
            except ValueError:
                print('Please enter a number: ')
            else:
                return num_choice #returns choice of number in int               

    #Asking if wanting to continue shopping
    def Stop_shopping():
        questions.continue_shopping() #asks the question
        choice = str(input("Yes or No? ")) #asking for Yes or No intput
        return choice #returns choice in string

#Display user is walking to location
#class 2 from basic actions
class user_walking(walk):
    #initialization
    def __init__():
        pass
    #walking to location function
    def walk_to_location(location):
        os.system('cls')
        walk.walking_to_location(location) #displays walking to location   

#Display all products in the shop
#class 3 from basic actions
class Disp_products(questions, display):
    #initialization
    def __init__(self):
        pass
    #function to show products
    def show_products(choice):
        os.system('cls')
        questions.what_to_buy() #asks what to buy
        display.disp_products(choice) #displays list of products
        num_choice = int(input('Please Input a Number: ')) #asking for input choice
        return num_choice #returns choice of number in int

#Display user walking home
#class 4 inherit from basic actions
class home(walk):
    def __init__(self):
        pass
    def walk_home():
            walk.walking_home()
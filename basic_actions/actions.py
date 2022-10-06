from _data.products import store
from time import sleep

#ask questions
class questions:
    #initialization
    def __init__(self):
        pass
    #where to go question
    def where_to_go():
        print("Hello! Where do you want to go? ")
    #what do you want to buy question
    def what_to_buy():
        print("What do you want to buy? ")
    #Continue shopping question
    def continue_shopping():
        print("Do you want to continue shopping? ")

#display class
class display:
    #initialization
    def __init__(self):
        pass
    #Display the list of locations for shopping
    def disp_location():
        i = 0
        #loop to display stores in numbered order
        for w in store.keys(): #grabs the Keys from the dictionary
            i += 1 #iteration
            y = w.replace("_", " ") #remove _
            print(f"{i}. {y}") #Display line per line
    #Display the products
    def disp_products(choice):
        location = list(store.keys())[choice - 1]
        inchoice = store.get(location) #grab the internal dictionary from the choice
        i = 0 #iteration
        list_values = [] #list to put the data values in         
        for r in store[location].values():
            list_values.append(r) #creating the list of prices
        for w in inchoice: #loop to display products
                a = list_values[i]
                i += 1                        
                print(f"{i}. {w} = ${a}") #Display products in numbered order
    

#walk class
class walk:
    #initialization
    def __init__(self):
        pass
    #Walking to location
    def walking_to_location(location):
        go_to_location = list(store.keys())[location - 1] #grabs the specific key from the list according to choice
        gtl = go_to_location.replace("_", " ") #removes underscore if displayed
        print(f"You are walking to {gtl}") #display you are walking to area
        sleep(3) # sleep for loading effect, not really necessary
    #Displays when user chooses to go home
    def walking_home():
        print("Thank you for shopping you are now walking home")
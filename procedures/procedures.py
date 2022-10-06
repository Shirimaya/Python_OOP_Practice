#start shopping section
from steps.steps import Asking_where_to_go
from steps.steps import user_walking
from steps.steps import Disp_products
from steps.steps import home

class shopping(Asking_where_to_go, user_walking, Disp_products, home):    
    def First_section():                  
        choice = Asking_where_to_go.going_to()         
        user_walking.walk_to_location(choice)
        Disp_products.show_products(choice)
        
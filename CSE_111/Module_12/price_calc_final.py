def main():
    # ask user for the price of the frames that they picked out.
    frame_price = float(input("What is the price of the frames? "))

    # ask user what type of lens they need: (Single Vision or Progressive)
    lens_type = input("What type of lens do you need? (Single Vision / Progressive)").lower()

    # ask user if they require a thinner lens based on their RX.
    lens_thinkness = input("Do you need a thinner lens based on your prescription? (Y / N) ").lower()


def get_lens_price(lens_type, thickness):
    """This function will take the type of lens that the user has chosen as 
        well as the thickness and determine the cost of the lens based on 
        those parameters.
        
        Parameters 
            type: The tupe of lens that the user chose
            thickness: if the user chose the thinner lens
        Return: price of the lens based on the parameters"""

    if lens_type == "single vision" and thickness == "y":
        price = 79.99
    elif lens_type == "single vision" and thickness == "n":
        price = 59.99
    elif lens_type == "progressive" and thickness == "n":
        price = 129.99
    else:
        price = 159.99
    
    return price

def get_combined_price(lens_price, frame_price):
    """This function will take the price of the lens that we get from
        the get_lens_price() function and the price of the frames that
        the user input and add them together to give us our subtotal.
        
        Parameters 
            lens_price: The price of lens that was calculated from the function
            frame_price: price of the frames the user input.
        Return: The sum of the two parameters to give us the subtotal of this set
                of glasses"""
    
    subtotal = lens_price + frame_price
    return subtotal

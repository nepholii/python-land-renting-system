from read import read_details as rd
from write import make_invoice as mi
from write import update_data as ud
from write import make_return_invoice
import datetime
present=0
selected_kitta_no=[]
selected_city_name=[]
selected_land_faced=[]
selected_area_of_land=[]
selected_customer_name=[]
selected_duration_of_rent=[]
selected_amount=[]
selected_rented_for=[]
selected_returned_in=[]

def display():
    """
    Displays the land information in a tabular format.

    This method prints the land information stored in the file in a tabular format.
    It includes columns for Serial Number (S.N), Kitta Number, City/District, Land Faced,
    Area of land, Price in Nepalese Rupees (NRs), and Availability. The data is fetched
    using the `rd()` function.

    Parameters:
        None

    Returns:
        None
    """
    print("""----------------------------------------------------------------------------------------------""")
    print("""|S.N |Kitta Number | City/District | Land Faced | Area of land | Price (NRs) | Availability  |""")
    print("""----------------------------------------------------------------------------------------------""")# Printing each element of the row i in a formatted table cell
    for i in rd():
        print(f"""|{i[0]:<4}| {i[1]:<12}| {i[2]:<14}| {i[3]:<11}|{i[4]:<14}| {i[5]:<12}| {i[6]:<14}|""")
    
    print("""----------------------------------------------------------------------------------------------""")# Print a horizontal line to separate rows in the table
def to_rent(customer_name=None,phone_no=None,address=None):
    """
    Allows a customer to rent a piece of land.

    This method does the process of renting a piece of land by displaying available land options,
    prompting the customer to select a kitta number, and collecting necessary information such as the 
    customer's name, phone number, address, and duration of rent. If the selected land is available, the
    customer's details along with the rental information are recorded. The process continues until the
    customer decides not to rent more lands.

    Parameters:
        customer_name (str): The first name of the customer. Defaults to None.
        phone_no (str): The phone number of the customer. Defaults to None.
        address (str): The address of the customer. Defaults to None.

    Returns:
        None
    """
    display()
    kitta_no=input("Select the kitta.no of the land that you want to rent>>")
    data=rd()# Getting data from the details file
   
    try:
        row_no=get_row_from_kitta(kitta_no,data)#to get the row number corresponding to the selected kitta number
        print(data[row_no])
    
    
        if str(data[row_no][6]) =='Not Available': # Checking if the selected land is available
            print("The land you want to rent is currently not available")
            again=input("do you want to select again")# Recursively calling to_rent function to select land again
            if(again.upper()=="Y"):
                to_rent()
                return 0
            else:
                return 0
    except:
        print("Please enter valid kitta no")
        to_rent() 
        return 0   
    
    else:
        if customer_name is None:# If customer details are not provided,prompt the customer to enter details
            while True:
                customer_name=input("Please enter your name>>")
                if customer_name.isalpha() or " " in customer_name:#accpet the name only if it contains alphabet or space
                    break
                else:
                    print("Your name contains non-alphabet characters.")
            while True:
                try:
                    phone_no=input("Enter your phone no>>")
                    if phone_no.isdigit() and len(phone_no) == 10:#accept the number only if it is a numerical value of length 10
                        break
                    else:
                        print("Please enter exactly 10 digits with no alphabets.")
                except:
                    print("Please enter valid phone no")

            while True:
                address=input("Please enter your address>>")
                break

        while True:
            try:
                duration_of_rent=int(input("How long do you want to rent the land for?(in months)>>"))
                if duration_of_rent <30 and duration_of_rent>0:
                    break
                else:
                    print("Please enter a duration less than 30 months.")
            except:
                print("Please enter a valid integer value for the duration.")

        present=(datetime.datetime.now())#updating the present variable with current date and time
        selected_kitta_no.append(kitta_no)#updating the selected land details in respective fields
        selected_city_name.append(data[row_no][2])
        selected_land_faced.append(data[row_no][3])
        selected_area_of_land.append(data[row_no][4])
        selected_customer_name.append(customer_name)
        selected_duration_of_rent.append(duration_of_rent)
        selected_amount.append(data[row_no][5])
        selected_customer_name.append(customer_name)
        rent_more=input("do you want to rent more lands?(Y for yes/N for no)")
        ud(int(kitta_no)) # Update the rental details in details file
        if(rent_more.upper()=="Y" or rent_more.upper()=="YES"):
            to_rent(customer_name,phone_no,address)# Recursively call to_rent function to rent more lands 
        else:
            mi(present,selected_kitta_no,selected_city_name,selected_land_faced,selected_area_of_land,selected_customer_name,
               selected_duration_of_rent,selected_amount,phone_no,address)#calling in make_invoice function by calling in the right parameter
            selected_kitta_no.clear()
            selected_city_name.clear()
            selected_land_faced.clear()
            selected_area_of_land.clear()
            selected_customer_name.clear()
            selected_duration_of_rent.clear()
            selected_amount.clear()
            # Clear the lists containing selected land details

def to_return(customer_name=None,phone_no=None,address=None):
    """
    Allows a customer to return a piece of land.

    This method does the process of returning a piece of land by displaying available land options,
    prompting the customer to select a kitta number, and collecting necessary information such as the 
    customer's name, phone number, address, and duration rented for and duration returned in. If the selected land is available, the
    customer's details along with the rental information are recorded. The process continues until the
    customer decides not to rent more lands.

    Parameters:
        customer_name (str): The first name of the customer. Defaults to None.
        phone_no (str): The phone number of the customer. Defaults to None.
        address (str): The address of the customer. Defaults to None.

    Returns:
        None
    """
    display()
    try: 
        kitta_no=input("Select the kitta.no of the land that you want to return>>")
        data=rd()
        row_no=get_row_from_kitta(kitta_no,data)#to get the row number corresponding to the selected kitta number
        print(data[row_no])
        if str(data[row_no][6]) =="Available":
            print("The land you want to return has already been returned")
            again=str(input("do you want to select again"))
            if(again.upper()=="Y"):
                to_return()
                return 0
    except:
        print("Please enter valid kitta no")
        to_return() 
        return 0   
    else:
        if customer_name is None:
            while True:
                customer_name=input("Please enter your name>>")
                if customer_name.isalpha() or " " in customer_name:#accpet the name only if it contains alphabet or space
                    break
                else:
                    print("Your name contains non-alphabet characters.")
            while True:
                try:
                    phone_no=input("Enter your phone no>>")
                    if phone_no.isdigit() and len(phone_no) == 10:#accept the number only if it is a numerical value of length 10
                        break
                    else:
                        print("Please enter exactly 10 digits with no alphabets.")
                except:
                    print("Please enter valid phone no")
            
            while True:
                address=input("please enter your address")
                break 

        while True:
            try:
                rented_for=int(input("How long did you  rent the land for?(in months)>>"))
                if rented_for < 30 and rented_for>0:#accept the number only if it is less than 30 and greater than 0
                    break
                else:
                    print("Please enter a duration less than 30 months ")
            except:
                print("Please enter a valid integer value for the duration.")

        while True:
            try:
                returned_in=int(input("After how long are you returning the land?(in months)"))
                if returned_in>0:#accept the number only if it is greater than 0
                    break
                else:
                    print("please enter positive integer")
            except:
                print("Please enter a valid integer value for the duration.") 
        present=(datetime.datetime.now())
        #updating the selected land details in respective fields
        selected_kitta_no.append(kitta_no)
        selected_city_name.append(data[row_no][2])
        selected_land_faced.append(data[row_no][3])
        selected_area_of_land.append(data[row_no][4])
        selected_amount.append(data[row_no][5])
        selected_returned_in.append(returned_in)
        selected_rented_for.append(rented_for)

        renturn_more=input("do you want to return more lands?(Y for yes/N for no)")
        ud(int(kitta_no))
        if(renturn_more.upper()=="Y"):# check for first letter
            to_return(customer_name,phone_no,address)# Recursively call to_rent function to rent more lands 
        else:
            make_return_invoice(present,selected_kitta_no,selected_city_name,selected_land_faced,selected_area_of_land,customer_name,
               selected_rented_for,selected_returned_in,selected_amount,phone_no,address)#calling in make_return_invoice function by calling in the right parameter
            selected_kitta_no.clear()
            selected_city_name.clear()
            selected_land_faced.clear()
            selected_area_of_land.clear()
            selected_rented_for.clear()
            selected_returned_in.clear()
            selected_amount.clear()
            # Clear the lists containing selected land details
            
def get_row_from_kitta(kitta_no,data):
    """
    Get the row index from the given kitta number in the data.

    Args:
        kitta_no (int): The kitta number to search for.
        data (list): The list of data where kitta number is searched.
    Returns:
        int: The index of the row where the kitta number is found.
        """   
    for i in range(len(data)): # Iterate through each row in the data
        if(kitta_no == data[i][1]):# Check if the kitta number matches the one in the current row
            row = i# Assign the index of the row where kitta number is found
            return row # Return the index of the row where kitta number is found

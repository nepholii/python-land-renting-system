import datetime #import current date and time
from read import read_details as rd
fine_amount=0


def make_invoice(present,selected_kitta_no,selected_city_name,selected_land_faced,selected_area_of_land,selected_customer_name,
               selected_duration_of_rent,selected_amount,phone_no,address):
    """
    Generate an invoice based on provided details and save it to a file and prints it.

    Args:
        present (str): The current date and time.
        selected_kitta_no (list): List of kitta numbers.
        selected_city_name (list): List of city/district names.
        selected_land_faced (list): List of land faced details.
        selected_area_of_land (list): List of land area details.
        selected_customer_name (str): Name of the customer.
        selected_duration_of_rent (list): List of durations for rent.
        selected_amount (list): List of amounts for rent.
        phone_no (str): Phone number of the customer.
        address (str): Address of the customer.
    """

    date=str(present)
    date=date.replace(":","-") #Convert present datetime to string format and replace ":" with "-" for filename
    #Creating the header of the invoice
    note1=f"""
-----------------------------------------------------------------------------------------
|  PAN NO:612474496             TechnoPropertyNepal                    Mob:9843705806   |
|                            BuddhaChowk-10, Pokhara Kaski                              |
---------------------------------------Note----------------------------------------------
|        Name:{selected_customer_name[0]:<15}                                                           |
|        Date:{date:<30}                                            |
|        Phone no:{phone_no:<10}                                                            |
|        Address:{address:<10}                                                             |
-----------------------------------------------------------------------------------------  
|Kitta Number | City/District | Land Faced | Area of land | Duration(In months) | Amount|
-----------------------------------------------------------------------------------------     
"""
    note2=""
    total_amount=0
   #looping through each selected land and accumulate total amount
    for i in range(len(selected_kitta_no)):
     total_amount=int(selected_amount[i])*int(selected_duration_of_rent[i])+int(total_amount) #since selected amount is in string
     vat_amount=total_amount*0.13
     grand_total=vat_amount+total_amount# Calculate grand total

     note2+=f"""|{selected_kitta_no[i]:<13}| {selected_city_name[i]:<14}| {selected_land_faced[i]:<11}| {selected_area_of_land[i]:<13}| {selected_duration_of_rent[i]:<20}|{selected_amount[i]:<7}|
"""
     # Generating the footer of the invoice including total, VAT, grand total, and terms & conditions
    note3= f"""-----------------------------------------------------------------------------------------                                                             
|                                                              Total:Nrs{total_amount:<10}      |
|                                                              VAT 13%:{vat_amount:<15}  |
|                                                            Grand Total:{grand_total:<15}|
-----------------------------------------------------------------------------------------          
| Terms & Conditions:                                                                   |
| - Late payments are subject to a monthly interest charge.                             |
| - All disputes are subject to Pokhara jurisdiction.                                   |
|***************************************************************************************|
| Thank you for choosing TechnoPropertyNepal. For inquiries, please contact us at:      |
| Phone: 9843705806 | Email: info@technoproperty.com                                    |
-----------------------------------------------------------------------------------------"""

    note=note1+note2+note3#joining the bill
    date=str(present)
    date=date.replace(":","-")
    note_file_name =f"Note_{selected_customer_name[0]} {date}.txt" # Generate filename for the invoice note
    file=open(f"{note_file_name}","w")# Write the invoice to a file
    file.write(note)
    file.close()
    print(f"Note saved as: {note_file_name}") #Print the filename where the invoice is saved and the invoice itself
    print(note)


def make_return_invoice(present,selected_kitta_no,selected_city_name,selected_land_faced,selected_area_of_land,customer_name,
               selected_rented_for,selected_returned_in,selected_amount,phone_no,address):
       """ 
    Generate a return invoice based on provided details and save it to a file and prints it.

    Args:
        present (str): The current date and time.
        selected_kitta_no (list): List of kitta numbers.
        selected_city_name (list): List of city/district names.
        selected_land_faced (list): List of land faced details.
        selected_area_of_land (list): List of land area details.
        customer_name (str): Name of the customer.
        selected_rented_for (list): List of durations the land was rented for.
        selected_returned_in (list): List of durations the land was returned in.
        selected_amount (list): List of amounts for rent.
        phone_no (str): Phone number of the customer.
        address (str): Address of the customer.
       """
       vat_amount=0
       date=str(present)
       date=date.replace(":","-")#Convert present datetime to string format and replace ":" with "-" for filename
       note1=f"""
------------------------------------------------------------------------------------------------------------------------------------
|  PAN NO:612474496                                           TechnoPropertyNepal                    Mob:9843705806                |
|                                                        BuddhaChowk-10, Pokhara Kaski                                             |
------------------------------------------------------------------Invoice-----------------------------------------------------------
|        Name:{customer_name:<15}                                                                                                      |
|        Date:{date:<30}                                                                                       |
|        Phone no:{phone_no:<10}                                                                                                       |
|        Address:{address:<10}                                                                                                        |
------------------------------------------------------------------------------------------------------------------------------------ 
|Kitta Number | City/District | Land Faced | Area of land | Duration rented for(In months) |Duration returned in(In months)| Amount|
------------------------------------------------------------------------------------------------------------------------------------     
"""
       note2=""
       total_amount=0
       #looping through each selected land and accumulate total amount
       for i in range((len(selected_kitta_no))): 
          
           total_amount=int(selected_amount[i])*int(selected_returned_in[i])+total_amount
           months_late=int(selected_returned_in[i])-int(selected_rented_for[i])
           if months_late>0:
               fine_amount=total_amount*0.05#5% fine for returning late
           elif months_late>3:
               fine_amount=total_amount*0.1 #10% fine for returning late more than 3 months
           elif months_late>7:
               fine_amount=total_amount*0.25 #25% fine for returning late more than 7 months
           else:
               fine_amount=0  
           vat_amount=0.13*(total_amount+fine_amount) #adding vat to total amount
           grand_total=total_amount+fine_amount+vat_amount
                
               
           note2+=f"""|{selected_kitta_no[i]:<13}| {selected_city_name[i]:<14}| {selected_land_faced[i]:<11}| {selected_area_of_land[i]:<13}| {selected_rented_for[i]:<31}|{selected_returned_in[i]:<31}|{selected_amount[i]:<7}|
"""
       note3= f"""------------------------------------------------------------------------------------------------------------------------------------                                                                
|                                                                                            Total(Nrs):{total_amount:<10}                 |
|                                                                                            Late Fine:{fine_amount:<15}             |
|                                                                                            Grand Total(After_Vat):{grand_total:<15}|
------------------------------------------------------------------------------------------------------------------------------------        
| Terms & Conditions:                                                                                                              |
| - Late payments are subject to a monthly interest charge.                                                                        |
| - All disputes are subject to Pokhara jurisdiction.                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------|      
| Thank you for choosing TechnoPropertyNepal. For inquiries, please contact us at:                                                 |
| Phone: 9843705806 | Email: info@technoproperty.com | Follow us on Twitter: @TechnoPropertyNepal                                  |
------------------------------------------------------------------------------------------------------------------------------------"""
       note=note1+note2+note3
       date=str(present)
       date=date.replace(":","-")
       note_file_name =f"Returned_Note_{customer_name} {date}.txt"# Generate filename for the invoice note
    
  
       file=open(f"{note_file_name}","w")
       file.write(note)
       file.close()
       print(f"Returned_Note saved as: {note_file_name}") #Print the filename where the invoice is saved and the invoice itself
       print(note)
      



def update_data(kitta_no):
     """
    Update data based on a given kitta number.

    Args:
        kitta_no (int): The kitta number to update data for.
    """
     data=rd()# Read data from the details file
     updated_details=""# Initialize string to store updated details
     for row in data:#looping through each row in the data
         del row[0] 
         if (int(row[0])==kitta_no):# Check if the kitta number matches the one provided
             if (row[5]=="Available"):# Toggle the availability status of the land
                 row[5]="Not Available"
             else:
                row[5]="Available"
         
        
         line=",".join(row)+"\n"# Convert the row to a string and append to updated_details
         updated_details+=line 
       
     details=open("details.txt","w")
     details.write(updated_details)# Write the updated details to the file
     details.close()

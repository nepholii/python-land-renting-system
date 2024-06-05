import operations
def main():
    """
    Main function to manage the land rental system.

    This function displays a menu of options to the user and calls corresponding functions from the operations module
    based on the user's selection. The function continues to display the menu until the user chooses to exit.

    Returns:
        None
    """
    while True:
        # Printing the company name
        print(r'''
 _____         _                   ____                            _           _   _                  _ 
|_   _|__  ___| |__  _ __   ___   |  _ \ _ __ ___  _ __   ___ _ __| |_ _   _  | \ | | ___ _ __   __ _| |
  | |/ _ \/ __| '_ \| '_ \ / _ \  | |_) | '__/ _ \| '_ \ / _ \ '__| __| | | | |  \| |/ _ \ '_ \ / _` | |
  | |  __/ (__| | | | | | | (_) | |  __/| | | (_) | |_) |  __/ |  | |_| |_| | | |\  |  __/ |_) | (_| | |
  |_|\___|\___|_| |_|_| |_|\___/  |_|   |_|  \___/| .__/ \___|_|   \__|\__, | |_| \_|\___| .__/ \__,_|_|
                                                  |_|                  |___/             |_|            ''')

        # Display the menu options
        print("""
    ******************1. Show details of the land***********
    ------------------------------------------------------------
    ***********************2. Rent land*********************
    ------------------------------------------------------------
    **********************3. Return land********************
    ------------------------------------------------------------
    *************************4. Exit************************
    ------------------------------------------------------------""")

        try:
            # Prompt the user to select an option
            number_selected = int(input('''---------------------Select a Number--------------------->>>>'''))
            
            # Execute corresponding operation based on the selected option
            if number_selected == 1:
                operations.display()
            elif number_selected == 2:
                operations.to_rent()
            elif number_selected == 3:
                operations.to_return()
            elif number_selected == 4:
                # Exit the program
                print(r""" _____                                                                                                   _____ 
    ( ___ )-------------------------------------------------------------------------------------------------( ___ )
    |   |                                                                                                   |   | 
    |   | _    _ _____ _______ _____ _______      _     _ _______      _______  ______ _______ _____ __   _ |   | 
    |   |  \  /    |   |______   |      |         |     | |______      |_____| |  ____ |_____|   |   | \  | |   | 
    |   |   \/   __|__ ______| __|__    |         |_____| ______|      |     | |_____| |     | __|__ |  \_| |   | 
    |___|                                                                                                   |___| 
    (_____)-------------------------------------------------------------------------------------------------(_____)
    """)
                print(r"""
        |)          ,_    _|   _ _  |   
        | |`()(||`(||||  (_|()_\(/_(|   
            _|             """)
                break
            else:
                print("Please enter a valid number")
        except:
            print("Please enter a valid integer")

# Call the main function
main()

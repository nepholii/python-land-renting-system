def read_details(path="details.txt"):
    '''method reads details file and returns details in list
    Args:
        path (str, optional): The path to the details file. Defaults to "details.txt".
    Returns:
        list: A list containing details read from the file. Each element in the list represents a row of details.
    '''
    details=open(path)# Open the details file
    single_details=details.readlines()# Reads all lines from the file
    land_list=[]
    clean_list=[]
    for i in range(len(single_details)):# looping through each line in the file
        clean_list=[str(i+1)]#to add S.N no
        clean_list.extend(single_details[i].strip().split(","))# Split the line by comma and adding to the clean_list
        land_list.append(clean_list)
    land_list[0][0]="1"#first row to have S.N no 1
    details.close()   
    return land_list # Returning the list containing all details
from book import AddressBook
#user interface functions, these are independent of the AddressBook class.
def prompt_for_record():
    
    try:
        name     = str(input("Please provide a name *: ")) 
        surname  = str(input("Please provide a surname *: ")) 
        addr1    = str(input("Address Line 1 *: "))
        addr2    = str(input("Address Line 2: "))
        postcode = str(input("Postcode *: "))
        country  = str(input("Country: "))

        contact = {"name": name,"surname":surname, "addr1": addr1, "addr2": addr2, "postcode":postcode, "country":country}

        if (AddressBook.is_valid_record(contact)):
            return contact
    except:
        return {}
    
    return {}
        
    
def prompt_for_user():
    try:
        surname = str(input("Surname:"))
        return surname
    except:
        return ""

def wait_for_keypress():
    input("[press any key]")

def menu():

        print("What would you like to do?\n") 
        print("1. Add a new contact") 
        print("2. Remove an existing contact")
        print("3. Search for a contact")
        print("4. Display all contacts") 
        print("5. Exit") 
        print ("\n\n\n")
        try:
            choice = int(input("Please enter your choice: ")) 
        except:
            return 0
        return choice 


def start():
        
        prompting = True

        #1 = create
        #2 = delete
        #3 = read
        #4 = list all
        #5 = exit
        ab = AddressBook()

        while prompting: 
            ab.summary()
            ch = menu() 
        
            if (ch == 1):
                record = prompt_for_record()
                ab.create_contact(record)
                
            elif (ch==2):
                userkey = prompt_for_user()
                ab.delete_contact(userkey)
                
            elif (ch==3):
                userkey = prompt_for_user()
                ab.print_contact(userkey)
                wait_for_keypress()

            elif (ch==4):
                ab.list_contacts()
                wait_for_keypress()
            
            elif (ch==5):
                prompting=False
        
start()

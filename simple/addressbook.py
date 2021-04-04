addressbook = {}

def is_valid_record(record):
    #TODO: check record validity -- this could be done in one line: return all (k in record for k in ("name","surname", "addr1", "postcode")):
    for k in ("name","surname","addr1","postcode"):
        if k not in record:
            return False
    return True

def is_valid_key(key):
    #TODO: check key validity
    return True

# create a new contact and return True on success, False otherwise
def create_contact(record):
    if is_valid_record(record):
        key = record["surname"]
        if key not in addressbook:
            addressbook[key] = record
            return True
    return False

#return contact or empty dict if contact does not exist
def read_contact(key=""):
    if is_valid_key(key):
      if key in addressbook:
        return addressbook[key]
    return {}

#update item if exists, return True on success, fail otherwise
def update_contact(record):
    if is_valid_record(record):
        key = record["surname"]
        if key in addressbook:
            addressbook[key] = record
            return True
    return False

def delete_contact(key):
    if is_valid_key(key):
      if key in addressbook:
        del addressbook[key]
        return True    
    return False


def print_contact(key):
    contact = read_contact(key)
    if is_valid_record(contact):
        print (f"-- {contact['name']} --")
        for key in ["surname", "addr1", "addr2", "postcode", "country"]:
          print (f"{contact[key]}")
        print()
    else:   
        print (f"contact does not exist\n")

def list_contacts():   
    print ("************** your contacts ****************")
    for key in sorted(addressbook.keys()):
        print_contact(key)
    print ("*********************************************\n")

def summary():
    print("\n\n\nYou have {} contacts in your contact list.".format(len(addressbook.keys())))

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


def fetch_phonebook():
    return 


def prompt_for_record():
    
    try:
        name     = str(input("Please provide a name *: ")) 
        surname    = str(input("Please provide a surname *: ")) 
        addr1    = str(input("Address Line 1 *: "))
        addr2    = str(input("Address Line 2: "))
        postcode = str(input("Postcode *: "))
        country  = str(input("Country: "))

        contact = {"name": name,"surname":surname, "addr1": addr1, "addr2": addr2, "postcode":postcode, "country":country}

        if (is_valid_record(contact)):
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

def start():
    
    prompting = True

    #1 = create
    #2 = delete
    #3 = read
    #4 = list all
    #5 = exit

    while prompting: 
        summary()
        ch = menu() 
    
        if (ch == 1):
            record = prompt_for_record()
            create_contact(record)
            
        elif (ch==2):
            userkey = prompt_for_user()
            delete_contact(userkey)
               
        elif (ch==3):
            userkey = prompt_for_user()
            print_contact(userkey)
            wait_for_keypress()

        elif (ch==4):
            list_contacts()
            wait_for_keypress()
           
        elif (ch==5):
            prompting=False
        
start()

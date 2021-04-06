class AddressBook:

    def __init__(self):
        self.addressbook = {}

    @staticmethod
    def is_valid_record(record):
        #TODO: check record validity -- this could be done in one line: return all (k in record for k in ("name","surname", "addr1", "postcode")):
        for k in ("name","surname","addr1","postcode"):
            if k not in record:
                return False
        return True
    
    @staticmethod
    def is_valid_key(key):
        #TODO: check key validity
        return True

    # create a new contact and return True on success, False otherwise
    def create_contact(self, record):
        if AddressBook.is_valid_record(record):
            key = record["surname"]
            if key not in self.addressbook:
                self.addressbook[key] = record
                return True
        return False

    #return contact or empty dict if contact does not exist
    def read_contact(self, key=""):
        if AddressBook.is_valid_key(key):
          if key in self.addressbook:
            return self.addressbook[key]
        return {}

    #update item if exists, return True on success, fail otherwise
    def update_contact(self, record):
        if AddressBook.is_valid_record(record):
            key = record["surname"]
            if key in self.addressbook:
                self.addressbook[key] = record
                return True
        return False

    def delete_contact(self, key):
        if AddressBook.is_valid_key(key):
          if key in self.addressbook:
            del self.addressbook[key]
            return True    
        return False


    def print_contact(self, key):
        contact = self.read_contact(key)
        if AddressBook.is_valid_record(contact):
            print (f"-- {contact['name']} --")
            for key in ["surname", "addr1", "addr2", "postcode", "country"]:
              print (f"{contact[key]}")
            print()
        else:   
            print (f"contact does not exist\n")

    def list_contacts(self):   
        print ("************** your contacts ****************")
        for key in sorted(self.addressbook.keys()):
            self.print_contact(key)
        print ("*********************************************\n")

    def summary(self):
        print("\n\n\nYou have {} contacts in your contact list.".format(len(self.addressbook.keys())))

    
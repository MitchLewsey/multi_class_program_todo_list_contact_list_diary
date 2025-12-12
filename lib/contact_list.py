class ContactList():
    def __init__(self):
        self.all_contacts = []
    
    def add(self, contact: "Contact"):
        self.all_contacts.append(contact)
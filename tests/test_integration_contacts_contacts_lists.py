from lib.contact import *
from lib.contact_list import *
# Contact and Contact List Integration Tests
"""
Given a contact list with two added contacts
all_contacts returns a list of added contact objects
"""
def test_add_contacts_updates_all_contacts_list():
    contact1 = Contact("07111111111")
    contact2 = Contact("07111111112")
    contactlist1 = ContactList()
    contactlist1.add(contact1)
    contactlist1.add(contact2)
    actual = contactlist1.all_contacts
    expected = [contact1, contact2]
    assert actual == expected
from lib.contact_list import *

# class Contact List Unit Tests
"""
Given a Contact List
An empty list called all_contacts is initialized
"""
def test_instantiating_class_initializes_empty_all_contacts_list():
    contactlist1 = ContactList()
    actual = contactlist1.all_contacts
    expected = []
    assert actual == expected
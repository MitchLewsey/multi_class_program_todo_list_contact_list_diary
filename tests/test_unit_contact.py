from lib.contact import *

"""
Given a contact with a number
The number is associated with the number property
"""
def test_contact_phone_property_set():
    contact1 = Contact("07111111111")
    actual = contact1.phone
    expected = "07111111111"
    assert actual == expected


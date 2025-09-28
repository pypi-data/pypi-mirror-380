from pynetbox.core.response import Record

class Emails(Record):
    pass

class Contacts(Record):
    pass

class ContactRoles(Record):
    pass

class ContactAssignments(Record):
    contact = Contacts
    role = ContactRoles
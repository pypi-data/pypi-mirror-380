from pynetbox.core.response import Record
from pypeeringmanager.models.peering import InternetExchanges


class Synchronizations(Record):
    pass


class Organizations(Record):
    pass


class Campuses(Record):
    org = Organizations


class Facilities(Record):
    org = Organizations


class IternetExchangeFacilities(Record):
    ix = InternetExchanges
    fac = Facilities


class InternetExchanges(Record):
    org = Organizations


class Ixlans(Record):
    ix = InternetExchanges


class IxlanPrefixes(Record):
    ixlan = Ixlans


class Networks(Record):
    org = Organizations


class NetworkContacts(Record):
    net = Networks


class NetworkFacilities(Record):
    net = Networks
    fac = Facilities


class NetworkIxlans(Record):
    pass


from pynetbox.core.response import Record

from pypeeringmanager.models.bgp import Relationships
from pypeeringmanager.models.devices import Routers
from pypeeringmanager.models.net import Connections
from pypeeringmanager.models.extras import Tags

class RoutingPolicies(Record):
    pass


class Communities(Record):
    tags = Tags


class AutonomousSystems(Record):
    import_routing_policies = RoutingPolicies
    export_routing_policies = RoutingPolicies
    tags = Tags


class BGPGroups(Record):
    import_routing_policies = RoutingPolicies
    export_routing_policies = RoutingPolicies
    communities = Communities
    tags = Tags


class InternetExchanges(Record):
    import_routing_policies = RoutingPolicies
    export_routing_policies = RoutingPolicies
    communities = Communities
    local_autonomous_system = AutonomousSystems
    tags = Tags

class DirectPeeringSessions(Record):
    autonomous_system = AutonomousSystems
    bgp_group = BGPGroups
    import_routing_policies = RoutingPolicies
    export_routing_policies = RoutingPolicies
    local_autonomous_system = AutonomousSystems
    tags = Tags
    router = Routers
    relationship = Relationships
    connection = Connections

    def __str__(self):
        return self.ip_address


class InternetExchangePeeringSessions(Record):
    autonomous_system = AutonomousSystems
    import_routing_policies = RoutingPolicies
    export_routing_policies = RoutingPolicies
    tags = Tags
    ixp_connection = Connections

    def __str__(self):
        return self.ip_address

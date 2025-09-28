try:
    from pynetbox.core.app import App as PyNetboxApp
except ImportError:
    raise ImportError("pynetbox is not installed. Please install it with 'pip install pynetbox'.")

from pypeeringmanager.models import bgp, devices, extras, messaging, net, peering, peeringdb

class App(PyNetboxApp):
    """ Represents apps in Peering-Manager.
    Calls to attributes are returned as Endpoint objects.
    :returns: :py:class:`.Endpoint` matching requested attribute.
    :raises: :py:class:`.RequestError`
        if requested endpoint doesn't exist.
    """

    models = {
        "bgp": bgp,
        "devices": devices,
        "extras": extras,
        "messaging": messaging,
        "peering": peering,
        "peeringdb": peeringdb,
        "net": net,
    }

    def _setmodel(self):
        self.model = self.__class__.models[self.name] if self.name in self.__class__.models else None
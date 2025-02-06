from utils.logger.logger import Logger

class NetworkManager:
    """
    Manages network operations and handles logging related to network events.
    """
    # NETWORKMANAGER INITIALIZATION
    def __init__(self):
        """
        Initializes the NetworkManager instance
        """
        Logger.log(f"start NetworkManager __init__(self)")
        self.network = []
        Logger.log(f"end NetworkManager __init__(self)")

    # SET NETWORK
    def set_network(self, network):
        """
        Sets the network attribtue to network. 

        Args: 
        network: this is a Network object. 
        """
        Logger.log(f"start set_network(self, {network})")
        self.network = network
        Logger.log(f"end set_network_(self, network)")

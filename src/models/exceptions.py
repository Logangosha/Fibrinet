class StateTransitionError(Exception):
    """
    Raised when an invalid state transition is attempted.
    """
    # INITIALIZES THE STATE TRANSITION ERROR WITH A CUSTOM MESSAGE.
    def __init__(self, message="Invalid state transition attempted."):
        super().__init__(message)
    
class InvalidInputDataError(Exception):
    """
    Exception raised for invalid input data.
    """
    # INITIALIZES THE INVALID INPUT DATA ERROR WITH A CUSTOM MESSAGE.
    def __init__(self, message="Unable to validate input data."):
        super().__init__(message)

class UnsupportedFileTypeError(Exception):
    """
    Exception raised for invalid file type.
    """
    # INITIALIZES THE UNSUPPORTED FILE TYPE ERROR ERROR WITH A CUSTOM MESSAGE.
    def __init__(self, message="File type not supported."):
        super().__init__(message)

class InvalidNetworkError(Exception):
    """
    Exception raised for invalid network types.
    Example: tkinter_view expects a Network2D if a network 2D is not provided this will be raised. 
    """
    # INITIALIZES THE UNSUPPORTED FILE TYPE ERROR ERROR WITH A CUSTOM MESSAGE.
    def __init__(self, message="Invalid Network Type."):
        super().__init__(message)
        
class NodeNotFoundError(Exception):
    """Raised when a node ID is not found in the network."""
    def __init__(self, message="Node ID not found in network."):
        super().__init__(message)

class EdgeNotFoundError(Exception):
    """Raised when an edge ID is not found in the network."""
    def __init__(self, message="Edge ID not found in network."):
        super().__init__(message)
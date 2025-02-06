class Observer:
    """
    Abstract base class for defining observer pattern.
    Subclasses must implement the `update` method to handle updates.
    """
    # OBSERVER INTERFACE METHOD FOR RECEIVING UPDATES.
    def update(self, event_type, data):
        """Observer interface method for receiving updates."""
        raise NotImplementedError("Subclasses must implement `update` method.")

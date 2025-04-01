from utils.logger.logger import Logger

class BaseNode:
    """
    Represents a node in a network with attributes and validation.
    """

    schema = {"n_id"}

    def __init__(self, attributes):
        """
        Initializes a Node with the given attributes.

        Params:
            attributes: Dictionary of attributes for the node.

        Raises:
            ValueError: If attributes do not conform to the schema.
        """
        Logger.log(f"start Node __init__(self)")

        # INITIALIZE ATTRIBUTES LIST
        self.attributes = []

        # SET ATTRIBUTES FROM INPUT DICTIONARY
        for key, value in attributes.items():
            setattr(self, key, value)
            self.attributes.append(key)
            Logger.log(f"Node attribute added {key}={value}")

        # VALIDATE ATTRIBUTES AGAINST SCHEMA
        if not self.validate_attributes():
            raise ValueError("Invalid node attributes according to schema.")

        Logger.log(f"end Node __init__(self)")

    def get_id(self):
        """
        Returns the ID of the node.
        """
        return getattr(self, "n_id", None)

    def get_attributes(self):
        """
        Returns all attributes of the node as a dictionary.
        """
        return self.__dict__

    def get_attribute(self, attribute_name):
        """
        Retrieves the value of a specific attribute.

        Params:
            attribute_name: Name of the attribute to retrieve.

        Returns:
            Value of the requested attribute or None if not found.
        """
        return getattr(self, attribute_name, None)

    def set_attribute(self, attribute_name, value):
        """
        Sets an attribute value, ensuring it follows the schema.

        Params:
            attribute_name: Name of the attribute to set.
            value: New value for the attribute.

        Raises:
            ValueError: If the attribute is not allowed by the schema.
        """
        # VALIDATE ATTRIBUTE AGAINST SCHEMA
        if self.schema and attribute_name not in self.schema:
            raise ValueError(f"Invalid attribute '{attribute_name}' according to schema.")

        # SET ATTRIBUTE VALUE
        setattr(self, attribute_name, value)

        # ADD ATTRIBUTE TO LIST IF NOT ALREADY PRESENT
        if attribute_name not in self.attributes:
            self.attributes.append(attribute_name)

    def validate_attributes(self):
        """
        Validates if all attributes conform to the schema.

        Returns:
            True if attributes are valid, False otherwise.
        """
        for attr in self.attributes:
            if self.schema and attr not in self.schema:
                return False
        return True
    
    @classmethod
    def get_schema(cls):
        """
        Returns the schema of the node class.

        Returns:
            Set containing valid attribute names.
        """
        return cls.schema

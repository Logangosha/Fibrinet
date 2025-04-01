from utils.logger.logger import Logger

class BaseEdge:
    """
    Represents an edge in a network with attributes and validation.
    """

    schema = {"e_id"}

    def __init__(self, attributes):
        """
        Initializes an Edge with the given attributes.

        Params:
            attributes: Dictionary of attributes for the edge.

        Raises:
            ValueError: If attributes do not conform to the schema.
        """
        Logger.log(f"start Edge __init__(self)")

        # INITIALIZE ATTRIBUTES LIST
        self.attributes = []

        # SET ATTRIBUTES FROM INPUT DICTIONARY
        for key, value in attributes.items():
            setattr(self, key, value)
            self.attributes.append(key)
            Logger.log(f"Edge attribute added {key}={value}")

        # VALIDATE ATTRIBUTES AGAINST SCHEMA
        if not self.validate_attributes():
            raise ValueError("Invalid Edge attributes according to schema.")

        Logger.log(f"end Edge __init__(self)")

    def get_id(self):
        """
        Returns the ID of the edge.
        """
        return getattr(self, "e_id", None)

    def get_attributes(self):
        """
        Returns all attributes of the edge as a dictionary.
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
        Logger.log(f"start set_attribute(self, {attribute_name}, {value})")
        # VALIDATE ATTRIBUTE AGAINST SCHEMA
        if self.schema and attribute_name not in self.schema:
            raise ValueError(f"Invalid attribute '{attribute_name}' according to schema.")

        # SET ATTRIBUTE VALUE
        setattr(self, attribute_name, value)

        # ADD ATTRIBUTE TO LIST IF NOT ALREADY PRESENT
        if attribute_name not in self.attributes:
            self.attributes.append(attribute_name)
        Logger.log("end set_attribute(self, attribute_name, value)")


    def validate_attributes(self):
        """
        Validates if all attributes conform to the schema.

        Returns:
            True if attributes are valid, False otherwise.
        """
        Logger.log(f"start validate_attributes(self)")
        for attr in self.attributes:
            if self.schema and attr not in self.schema:
                Logger.log(f"end validate_attributes(self)")
                return False
        Logger.log(f"end validate_attributes(self)")
        return True
    
    @classmethod
    def get_schema(cls):
        """
        Returns the schema of the edge class.

        Returns:
            Set containing valid attribute names.
        """
        return cls.schema

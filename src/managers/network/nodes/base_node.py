from utils.logger.logger import Logger

class BaseNode:
    """
    Represents a node in a network with attributes and validation.
    """

    schema = {"n_id": int}

    def __init__(self, attributes):
        """
        Initializes a Node with the given attributes.

        Params:
            attributes (dict): Dictionary of attributes for the node.

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
            attribute_name (str): Name of the attribute to retrieve.

        Returns:
            Value of the requested attribute or None if not found.
        """
        return getattr(self, attribute_name, None)

    @staticmethod
    def safe_cast(value, expected_type):
        """
        Attempts to cast value to the expected type.

        Params:
            value: The value to cast.
            expected_type: The type to cast to.

        Returns:
            The casted value.

        Raises:
            ValueError: If casting fails.
        """
        # HANDLE BOOLEAN SPECIAL CASE
        try:
            if expected_type == bool:
                return str(value).strip().lower() in ["true", "1", "yes"]
            return expected_type(value)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid value: '{value}' is not of type {expected_type.__name__}")

    def set_attribute(self, attribute_name, value):
        """
        Sets an attribute value, ensuring it follows the schema and types.

        Params:
            attribute_name (str): Name of the attribute to set.
            value: New value for the attribute.

        Raises:
            ValueError: If attribute is not in schema or value type is invalid.
        """
        # VALIDATE ATTRIBUTE AGAINST SCHEMA
        if self.schema and attribute_name not in self.schema:
            raise ValueError(f"Invalid attribute '{attribute_name}' according to schema.")

        # GET EXPECTED TYPE FROM SCHEMA OR DEFAULT TO str
        expected_type = self.schema.get(attribute_name, str)

        # CAST VALUE TO EXPECTED TYPE
        value = self.safe_cast(value, expected_type)

        # SET ATTRIBUTE VALUE
        setattr(self, attribute_name, value)

        # ADD ATTRIBUTE TO LIST IF NOT ALREADY PRESENT
        if attribute_name not in self.attributes:
            self.attributes.append(attribute_name)

    def validate_attributes(self):
        """
        Validates if all attributes conform to the schema.

        Returns:
            bool: True if attributes are valid, False otherwise.
        """
        Logger.log("Starting attribute validation.")
        Logger.log(f"Schema: {self.schema}")

        for attr in self.attributes:
            Logger.log(f"Validating attribute: {attr}")
            if self.schema and attr not in self.schema:
                Logger.log(f"Attribute '{attr}' not in schema. Validation failed.")
                return False

        Logger.log("All attributes are valid.")
        return True

    @classmethod
    def get_schema(cls):
        """
        Returns the schema of the node class.

        Returns:
            dict: The schema dictionary mapping attribute names to types.
        """
        return cls.schema

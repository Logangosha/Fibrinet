from utils.logger.logger import Logger

class BaseEdge:
    """
    Represents an edge in a network with attributes and validation.
    """

    # SCHEMA DICTIONARY WITH ATTRIBUTE TYPES (e.g. {"e_id": int})
    schema = {"e_id": int, "n_from": int, "n_to":int}

    def __init__(self, attributes):
        """
        Initializes an Edge with the given attributes.

        Params:
            attributes (dict): Dictionary of attributes for the edge.

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
        Logger.log(f"start set_attribute(self, {attribute_name}, {value})")

        # VALIDATE ATTRIBUTE EXISTS IN SCHEMA
        if self.schema and attribute_name not in self.schema:
            raise ValueError(f"Invalid attribute '{attribute_name}' according to schema.")

        # GET EXPECTED TYPE FROM SCHEMA (DEFAULT TO str IF NOT SPECIFIED)
        expected_type = self.schema.get(attribute_name, str)

        # SAFE CAST VALUE TO EXPECTED TYPE
        value = self.safe_cast(value, expected_type)

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
            bool: True if attributes are valid, False otherwise.
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
            dict: The schema dictionary mapping attribute names to types.
        """
        return cls.schema

#!/usr/bin/python3
"""
User class
"""


class User():
    """
    User class represents a user object.
    """

    def __init__(self):
        """
        Initializes a User instance with None email.
        """
        self.__email = None

    @property
    def email(self):
        """
        Getter method for email property.
        """
        return self.__email

    @email.setter
    def email(self, value):
        """
        Setter method for email property.
        """
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        self.__email = value


if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)

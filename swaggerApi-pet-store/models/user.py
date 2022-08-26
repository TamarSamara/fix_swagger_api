from models.baseObj import baseObj


class User(baseObj):
    def __init__(self, id, userName, firstName, lastName, email, password, phone, userStatus=0):
        self._id = id
        self._username = userName
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._password = password
        self._phone = phone
        self._userStatus = userStatus

    @property
    def id(self):
        """Gets the id of this User.
        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.
        :param id: The id of this User.
        :type: int
        """
        self._id = id

    @property
    def username(self):
        """Gets the username of this User.
        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.
        :param username: The username of this User.
        :type: str
        """
        self._username = username

    @property
    def firstName(self):
        """Gets the firstName of this User.
        :return: The firstName of this User.
        :rtype: str
        """
        return self._firstName

    @firstName.setter
    def firstName(self, firstName):
        """Sets the firstName of this User.
        :param firstName: The firstName of this User.
        :type: str
        """
        self._firstName = firstName

    @property
    def lastName(self):
        """Gets the lastName of this User.
        :return: The lastName of this User.
        :rtype: str
        """
        return self._lastName

    @lastName.setter
    def lastName(self, lastName):
        """Sets the lastName of this User.
        :param lastName: The lastName of this User.
        :type: str
        """
        self._lastName = lastName

    @property
    def email(self):
        """Gets the email of this User.
        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.
        :param email: The email of this User.
        :type: str
        """
        self._email = email

    @property
    def password(self):
        """Gets the password of this User.
        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this User.
        :param password: The password of this User.
        :type: str
        """
        self._password = password

    @property
    def phone(self):
        """Gets the phone of this User.
        :return: The phone of this User.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this User.
        :param phone: The phone of this User.
        :type: str
        """
        self._phone = phone

    @property
    def userStatus(self):
        """Gets the userStatus of this User.
        :return: The userStatus of this User.
        :rtype: int
        """
        return self._userStatus

    @userStatus.setter
    def userStatus(self, userStatus):
        """Sets the userStatus of this User.
        :param userStatus: The userStatus of this User.
        :type: int
        """
        self._userStatus = userStatus

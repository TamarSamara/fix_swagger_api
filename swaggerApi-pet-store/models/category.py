# coding: utf-8
from models.baseObj import baseObj


class Category(baseObj):

    def __init__(self, id=None, name=None):
        self._id = None
        self._name = None
        if id is not None:
            self._id = id
        if name is not None:
            self._name = name

    @property
    def id(self):
        """Gets the id of this Category.  # noqa: E501
        :return: The id of this Category.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Category.
        :param id: The id of this Category.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Category.  # noqa: E501
        :return: The name of this Category.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Category.
        :param name: The name of this Category.  # noqa: E501
        :type: str
        """

        self._name = name

from models.baseObj import baseObj
from enum import Enum


class Status(Enum):
    available = "available"
    pending = "pending"
    sold = "sold"


class Pet(baseObj):

    def __init__(self, id, name, category=None, photoUrls=None, tags=None, status=Status.available):
        self._photo_urls = None
        self._tags = None
        self._status = None
        self._id = id
        self._name = name
        self._category = category
        if photoUrls is not None:
            self._photo_urls = photoUrls
        if tags is not None:
            self._tags = tags
        if status is not None:
            self._status = status

    @property
    def id(self):
        """Gets the id of this Pet.  # noqa: E501
        :return: The id of this Pet.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Pet.
        :param id: The id of this Pet.  # noqa: E501
        :type: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Pet.  # noqa: E501
        :return: The name of this Pet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Pet.
        :param name: The name of this Pet.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        self._name = name

    @property
    def category(self):
        """Gets the category of this Pet.  # noqa: E501
        :return: The category of this Pet.  # noqa: E501
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Pet.
        :param category: The category of this Pet.  # noqa: E501
        :type: Category
        """
        self._category = category

    @property
    def status(self):
        """Gets the status of this Pet.  # noqa: E501
        :return: The status of this Pet.  # noqa: E501
        :rtype: status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Pet.
        :param status: The status of this Pet.  # noqa: E501
        :type: status
        """
        self._status = status

    @property
    def tags(self):
        """Gets the tags of this Pet.  # noqa: E501
        :return: The tags of this Pet.  # noqa: E501
        :rtype: tags
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Pet.
        :param tags: The tags of this Pet.  # noqa: E501
        :type: tags
        """
        self._tags = tags

    @property
    def photourls(self):
        """Gets the photo urls of this Pet.  # noqa: E501
        :return: The photo urls of this Pet.  # noqa: E501
        :rtype: photo urls
        """
        return self._photo_urls

    @photourls.setter
    def photourls(self, photo_urls):
        """Sets the photo urls of this Pet.
        :param photo_urls: The photo urls of this Pet.  # noqa: E501
        :type: photo urls
        """
        self._photo_urls = photo_urls

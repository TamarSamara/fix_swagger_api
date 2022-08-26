from models.baseObj import BaseObj


class BookStore(BaseObj):

    def __init__(self, isbn: str, title: str, subTitle: str = None, author: str = None, publish_date: str = None,
                 publisher: str = None, pages: int = None, description: str = None,
                 website: str = None):
        self._isbn = isbn
        self._title = title
        self._subTitle = subTitle
        self._author = author
        self._publish_date = publish_date
        self._publisher = publisher
        self._pages = pages
        self._description = description
        self._website = website

    @property
    def isbn(self) -> str:
        return self._isbn


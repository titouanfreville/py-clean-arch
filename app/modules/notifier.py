from abc import ABC, abstractmethod
from app import domains


class Notify(ABC):
    """Manage notification"""

    @abstractmethod
    def new_user(self, user: domains.User):
        """Notify user created an acount"""

    @abstractmethod
    def new_book(self):
        """Notify book creation"""
        ...

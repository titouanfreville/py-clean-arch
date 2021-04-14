from app import domains


class Users:
    """Manager users features"""

    def __init__(self):
        self.__user = None
        self.__notify = None

    def register(self, user: domains.User):
        """Register user"""
        self.__user.validate(user)
        self.__user.create(user)
        self.__notify.new_user(user)

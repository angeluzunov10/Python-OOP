from project1.library import Library
from project1.user import User


class Registration:
    def add_user(self, user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        else:
            library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id, new_username, library: Library):
        for user in library.user_records:
            if user.user_id == user_id:
                if user.username != new_username:
                    user.username = new_username
                    return f"Username successfully changed to: {new_username} for user with id: {user_id}"
                else:
                    return "Please check again the provided username - " \
                           "it should be different than the username used so far!"

        return f"There is no user with id = {user_id}!"


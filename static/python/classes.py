from flask_login import UserMixin


class Accounts(UserMixin):
    def __init__(self, user_id, email, forename, surname, username, school_id, is_school, carbon_emission, password):
        self.id = user_id
        self.email = email
        self.forename = forename
        self.surname = surname
        self.username = username
        self.school_id = school_id
        self.is_school = is_school
        self.carbon_emission = carbon_emission
        self.password = password
        self.authenticated = False

    def is_active(self):
        return self.is_active()

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def get_id(self):
        return self.id

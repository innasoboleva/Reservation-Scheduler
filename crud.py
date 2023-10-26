from model import User, Reservation

def check_user_login(email, password):
    user = User.query.get(email)
    if user and user.password == password:
        return True
    else:
        return False

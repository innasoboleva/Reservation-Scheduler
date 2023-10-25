from model import User, Reservation

def check_user_login(email, password):
    user = User.get(email)
    if user and user.password == password:
        return True
    else:
        return False

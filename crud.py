from model import User, Reservation

def check_user_login(email, password):
    """Checks if email and password are correct"""

    user = User.query.get(email)
    if user and user.password == password:
        return True
    else:
        return False
    

def get_time(start, end):
    """Converts time to a list while getting it to a closer 20-min span (30 min) or (00 min)"""

    s_time = start.split(':')
    e_time = end.split(':')
    try:
        start_time_return = "30" if 15 < int(s_time[1]) < 45 else "00"
        print(start_time_return)
        if int(s_time[1]) > 45:
            s_time[0] = str(int(s_time[0]) + 1)
        end_time_return = "30" if 15 < int(e_time[1]) < 45 else "00" 
        if int(e_time[1]) > 45:
            e_time[0] = str(int(e_time[0]) + 1)
    except:
        return { "status": "error" }
    return { "status": "success", "start": (s_time[0], start_time_return), "end": (e_time[0], end_time_return) }


def get_available_times(day, time):
    """Returns all available times for this period"""
    
    users_date = None
    booked = Reservation.query.filter(Reservation.date == users_date).all()
    print(booked)
    not_booked = Reservation.query.filter(Reservation.date != users_date).all()
    pass
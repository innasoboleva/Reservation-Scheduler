from model import User, Reservation
from datetime import datetime, time, timedelta
from dateutil import parser

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
        return None
    return { "start": (s_time[0], start_time_return), "end": (e_time[0], end_time_return) }


def get_available_times(day, start, end):
    """Returns all available times for this period except already booked ones"""
    result = []
    parsed_day = parser.parse(day)
    all_available_times = []
    time_list = get_time(start, end)
    if time_list:
        s = time_list['start']
        e = time_list['end']
        all_available_times = get_times(parsed_day, s, e)

    start_datetime = datetime.combine(parsed_day.date(), time(int(start[0]),int(start[1])))
    end_datetime = datetime.combine(parsed_day.date(), time(int(end[0]),int(end[1])))

    list_of_booked = Reservation.query.filter(Reservation.date > start_datetime, Reservation.date < end_datetime).all()
    list_of_booked_set = set(list_of_booked)
    print(list_of_booked)
    for each_time in all_available_times:
        if each_time not in list_of_booked_set:
            result.append(each_time.time())
    print(result)

    return result

def get_times(day, start, end):
    """Returns all available times for this period"""

    start_time = time(int(start[0]), int(start[1]))
    end_time = time(int(end[0]), int(end[1]))

    all_times = []
    current_time = datetime.combine(day, start_time)

    while current_time.time() <= end_time or start_time > end_time:
        # all_times.append((current_time.time()))
        all_times.append(current_time)
        
        current_time += timedelta(minutes=30)
       
        if current_time.time() < start_time:
            current_time = datetime.combine(current_time.date() + timedelta(days=1), time(0, 0))

    print(all_times)
    return all_times
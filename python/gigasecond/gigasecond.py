import datetime as dt

def add(moment : dt) -> dt:
    return moment + dt.timedelta(seconds = 1000000000)

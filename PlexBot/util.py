from time import gmtime, strftime
def format_time(duration):
    return strftime("%M:%S", gmtime(duration / 1000))
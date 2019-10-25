from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API

PEOPLE = {
    "Farrel": {
        "fname": "William",
        "lname": "Farrel",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Easter",
        "lname": "Bunny",
        "timestamp": get_timestamp()
    }
}

def read():
    """
    This request responds to a request for /api/people
    with the complete lists of people

    :return: sorted list of people
    """
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


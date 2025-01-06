#payloads

#create booking
#update booking
#Auth-Token


def payload_create_booking():
    pay_load={
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
    return pay_load


def payload_update_booking():
    pay_load={
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
    return pay_load

def create_token():
    pay_load={
        "username":"admin",
        "password":"password123"
    }
    return pay_load
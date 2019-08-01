import sys
from core.API.FonoAPI import *
from core.Smartphone import Smartphone
from .GraphDBRequests import SmartphoneRequest as SmartphoneRequest


def main(argv=None):
    phone = retrieve_phone_information(argv)

    if phone == null:
        msg_error("The telephone has not been found")

    smartphone = Smartphone(phone["DeviceName"])
    smartphone.format(phone)

    smartphone.display()
    #SmartphoneRequest.insert_phone(smartphone)


if __name__ == "__main__":
    main(sys.argv)

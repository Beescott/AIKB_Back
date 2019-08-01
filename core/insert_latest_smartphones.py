import sys
from core.Smartphone import Smartphone
from core.API.FonoAPI import *
import core.GraphDBRequests.SmartphoneRequest as SmartphoneRequest

def main(argv=None):
    # Get the 100 latest phone from FonoApi
    phones = get_all_phone()

    for phone in phones:
        try:
            # Create a Smartphone object
            smartphone = Smartphone(phone["DeviceName"])
            # Format the smartphone to match the OWL file
            smartphone.format(phone)
            smartphone.format_version()

    #         # Insert smartphone inside GraphDB
            SmartphoneRequest.insert_phone(smartphone)

            print("Smartphone successfully added to database")
        except Exception as e:
            print(e)

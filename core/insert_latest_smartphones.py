import sys
from core.Smartphone import Smartphone
from core.API.FonoAPI import *
import core.GraphDBRequests.SmartphoneRequest as SmartphoneRequest

def main(argv=None):
    # Get the 100 latest phone from FonoApi
    phones = get_all_phone()
    n = 5
    i=0
    for phone in phones:
        i += 1
        if i < n:
            try:
                # Create a Smartphone object
                smartphone = Smartphone(phone["DeviceName"])
                # Format the smartphone to match the OWL file
                smartphone.format(phone)
                smartphone.format_version()

        #         # Insert smartphone inside GraphDB
                SmartphoneRequest.insert_phone(smartphone)

                print(phone["DeviceName"] + " successfully added to database")
            except Exception as e:
                print(e)

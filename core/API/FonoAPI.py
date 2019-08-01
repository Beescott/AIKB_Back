from .fonAPI import FonApi
import null
import core.config as config

def msg_error(str):
    """
    :param str:
    :return:
    """
    print(str)
    exit(0)


def print_phone_information(phone):
    """
    Print the phone information
    :param phone: dictionnary of strings
    :return:
    """
    print("Device Name :" + phone['DeviceName'])
    print("Bluetooth :" + phone['bluetooth'])
    print("GPS :" + phone['gps'])
    print("Jack :" + phone['_3_5mm_jack_'])
    print("Wifi :" + phone['wlan'])
    print("Edge :" + phone['_3g_bands'])
    print("4g :" + phone['_4g_bands'])
    print("Radio :" + phone['radio'])
    print("USB :" + phone['usb'])
    print("OS :" + phone['os'])


def retrieve_phone_information(argv):
    """
    Get the requested phone from argv, use the FonAPI and returns the phone's information
    :param argv:
    :return phone: dictionnary of string
    """
    # Send error if the user has input wrong arguments
    if len(argv) < 2 or len(argv) > 3:
        msg_error('The program takes one or two arguments. \nPlease type py get_device.py "telephone_name brand" '
                  '(brand is optional).')

    # Use the FonApi
    fon = FonApi(config.API_key)

    # Get the required device
    device = argv[2]
    brand = None
    if len(argv) == 3:
        brand = argv[1]

    # Use the API to retrieve the information about the required device
    # fon.getdevice returns a list of smartphones with similar name the user has input
    # position='0' allow us to only take the closest name from the user input
    phones = fon.getdevice(device, position='0', brand=brand)
    requested_phone = phones[0]

    if requested_phone == 'N':
        requested_phone = null

    return requested_phone


def get_all_phone():
    fon = FonApi(config.API_key)
    return fon.getlatest()

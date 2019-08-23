class Smartphone:
    def __init__(self, name):
        self.name = name
        self.formated_connectivities = {}
        self.formated_version = {}
        self.edge = False
        self.lte = False

    def smartphone_has(self, key):
        if self.formated_connectivities[key] != 'No':
            return True
        return False

    def format(self, unformated_api):
        self.formated_connectivities['GPS'] = unformated_api['gps'] if 'gps' in unformated_api else 'No'
        self.formated_connectivities['Bluetooth'] = unformated_api['bluetooth'] if 'bluetooth' in unformated_api else 'No'

        edge_4g = ""
        if '_3g_bands' in unformated_api and unformated_api['_3g_bands'] != 'No':
            edge_4g += unformated_api['_3g_bands']
            self.edge = True
        if '_4g_bands' in unformated_api and unformated_api['_4g_bands'] != 'No':
            edge_4g += "/" + unformated_api['_4g_bands']
            self.lte = True
        if edge_4g == "":
            self.formated_connectivities['Edge_4G'] = 'No'
        else:
            self.formated_connectivities['Edge_4G'] = edge_4g

        self.formated_connectivities['USB_cable'] = unformated_api['usb'] if 'usb' in unformated_api else 'No'
        self.formated_connectivities['Radio'] = unformated_api['radio'] if 'radio' in unformated_api else 'No'
        self.formated_connectivities['OS'] = unformated_api['os'] if 'os' in unformated_api else 'No'
        self.formated_connectivities['NFC'] = unformated_api['nfc'] if 'nfc' in unformated_api else 'No'
        for i in self.formated_connectivities:
            if self.formated_connectivities[i] == '':
                self.formated_connectivities[i] = 'No'

    def format_version(self):
        # Format bluetooth to get only the version
        if self.smartphone_has("Bluetooth"):
            bluetooth_version = self.formated_connectivities['Bluetooth'].split(",")[0]
            self.formated_version['Bluetooth'] = "Bluetooth_" + bluetooth_version

        # Format usb_cable
        if self.smartphone_has("USB_cable"):
            usb_cable_version = self.formated_connectivities['USB_cable'].split(",")[0]
            usb_cable_version = usb_cable_version.replace(' ', '_')
            usb_cable_version = usb_cable_version.replace('(', '')
            usb_cable_version = usb_cable_version.replace(')', '')
            self.formated_version['USB_cable'] = "USB_" + usb_cable_version

        # Format GPS
        if self.smartphone_has("GPS"):
            gps_version = self.formated_connectivities['GPS'].split(",")
            gps_version = gps_version[1:]
            string_gps_version = ''.join(gps_version)[6:]
            string_gps_version = string_gps_version.replace(' ', '_')
            string_gps_version = string_gps_version.replace('(', '')
            string_gps_version = string_gps_version.replace(')', '')
            string_gps_version = string_gps_version.replace('+', '_')
            string_gps_version = string_gps_version.replace(';', '')
            string_gps_version = string_gps_version.replace('/', '_')
            string_gps_version = string_gps_version.replace('&', '')
            string_gps_version = string_gps_version.replace('#', '')
            string_gps_version = string_gps_version.replace('8209', '')
            self.formated_version['GPS'] = string_gps_version

        # Format OS
        if self.smartphone_has("OS"):
            os_version = self.formated_connectivities['OS'].split(';')[0]
            os_version = os_version.replace(' ', '_')
            os_version = os_version.replace('(', '')
            os_version = os_version.replace(')', '')
            os_version = os_version.replace(',', '_')
            self.formated_version['OS'] = os_version

        if self.smartphone_has("Edge_4G"):
            if self.edge and self.lte:
                self.formated_version['Edge_4G'] = '3G_4G'
            elif self.edge:
                self.formated_version['Edge_4G'] = '3G'
            elif self.lte:
                self.formated_version['Edge_4G'] = '4G'

    def display(self):
        print("######################################################################################################")
        print("Smartphone name : " + self.name)
        for information in self.formated_connectivities:
            print(information, self.formated_connectivities[information])

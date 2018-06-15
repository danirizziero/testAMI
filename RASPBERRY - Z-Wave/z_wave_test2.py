# Used for sensing the motion in the environment
from requests import request, RequestException
import time


# Getting the info for the url and putting them into a dictionary
def send(method='GET', url=None, data=None, headers={}, auth=None):
    response = dict()

    # check that the URL is not empty
    if url is not None:
        result = None
        try:
            # Authentication phase
            if auth is not None:
                result = request(method, url, data=data, headers=headers, auth=auth)

        # If there is an error in the procedure, print the error
        except RequestException as auth_error:
            print("Authentication error encountered: " + auth_error)

        # check result
        if result is not None:
            # consider the response content as JSON and put it in the dictionary
            try:
                response = result.json()
            except ValueError as value_error:
                # no JSON, return the plain result
                print("Value error encountered: " + value_error)
                response = result
    return response


def get(method='GET', url=None, data=None, headers={}, auth=None):
    updating_data = dict()

    # check that the URL is not empty
    if url is not None:
        result = None
        try:
            # Authentication phase
            if auth is not None:
                result = request(method, url, data=data, headers=headers, auth=auth)

        # If there is an error in the procedure, print the error
        except RequestException as auth_error:
            print("Authentication error encountered: " + auth_error)

        # check result
        if result is not None:
            # consider the response content as JSON and put it in the dictionary
            try:
                updating_data = result.json()
            except ValueError as value_error:
                # no JSON, return the plain result
                print("Value error encountered: " + value_error)
                updating_data = result

    return updating_data


DEBUG = True


def user_detected():
    # main url: login before the access (could be done without authentication).
    main_url = 'http://192.168.0.202:8083'

    # Setting of the login credentials
    username = 'admin'
    password = 'ami-zwave'

    # get z-wave devices. We pop out the z-way controller from the list
    Devices = send(url=main_url + '/ZWaveAPI/Data/0', auth=(username, password))
    Devices = Devices['devices']
    Devices.pop('1')


    device_id = 12  # X = ID del nostro sensore/device, da verificare sull'interfaccia web
    # FOR INUTILE MA NECESSARIO PER IL FUNZIONAMENTO, NON SI SA PERCHè.
    # PROVARE PER CREDERE
    for device_id in Devices:
        pass

# D E B U G
    if DEBUG:
        #print("Devices:", Devices)
        for device_id in Devices:
            print(device_id)

    # URL for reaching the device
    device_url = main_url + '/ZWaveAPI/Run/devices[{}].instances[{}].commandClasses[{}]'
    # Command class used
    sensor_binary = '48'  # Sensor responsible for the motion, has two states

    # C O N T R O L L O    dello stato
    for instance in Devices[device_id]['instances']:
        if sensor_binary in Devices[device_id]['instances'][instance]['commandClasses']:

# D E B U G
            if DEBUG:
                print('Device %s is a binary sensor detecting the motion' % device_id)

            # AGGIORNAMENTO FORZATO DEL SENSORE
            update = get(url=main_url + '/ZAutomation/api/v1/devices/ZWayVDev_zway_11-0-48-1',
                         auth=(username, password))
            url_to_call = device_url.format(device_id, instance, sensor_binary)
            response = send(url=url_to_call, auth=(username, password))
            val = response['data']['1']['level']['value']

# D E B U G
            if DEBUG:  # Which values does it return?
                print("Value is ", val)

            print('Motion: ' + str(val))
            if val == True:
                return True
            else:
                return False


if __name__ == '__main__':
    user_detected()

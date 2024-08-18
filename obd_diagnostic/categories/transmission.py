from obd_diagnostic.obd_reader import OBDTool

def read_transmission_data():
    reader =OBDTool(interface='usb')
    temp = reader.read_data('TRANSMISSION_TEMP')
    print(f'Transmission Temperature: {temp}')
    reader.disconnect()
    return f'Transmission Temperature: {temp}'
from obd_diagnostic.obd_reader import OBDTool

def read_engine_data():
    reader = OBDTool(interface= 'usb')
    rpm = reader.read_data('RPM')
    print(f'Engine RPM:{rpm}')
    reader.disconnected()
    return f'Engine RPM:{rpm}'



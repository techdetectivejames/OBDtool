import argparse
from obd_diagnostic.categories.engine import read_engine_data
from obd_diagnostic.categories.transmission import read_transmission_data

def main():
    parser =argparse.ArgumentParser(description= 'Run OBD Diagnostics.')
    parser.add_argument('category', choices=['engine', 'transmission'], help='Category of Diagnostics to run')
    args = parser.parse_args()

    if args.category == 'engine':
        read_engine_data()
    if args.category =='transmission':
        read_transmission_data()

if _name_== '_main_':
    main()
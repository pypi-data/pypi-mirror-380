"""Main module for IPMI monitoring command-line tool.

This module provides the entry point for the IPMI monitoring command-line
interface, handling argument parsing and sensor data display.
"""

import sys
import time
import json
import dataclasses
from prettytable import PrettyTable
from enum import Enum

from .arguments import *

def make_json(records, indent):
    a = []
    for record in records:
        d = {}
        for k, v in dataclasses.asdict(record).items():
            if isinstance(v, Enum):
                v = v.name
            d[k] = v
        a.append(d)
    return json.dumps(a, indent = indent)

def make_table(records):
    table = PrettyTable()

    table.field_names = [
        "Num",
        "Event",
        "Sensor",
        "Sensor Name",
        "Sensor Type",
        "State",
        "Reading",
        "Units",
        "Type",
        "Bitmask",
        "Bitmask Type",
        "Bitmask Strings",
    ]

    table.align = 'l'
    table.align["Num"] = 'r'
    table.align["Event"] = 'r'
    table.align["Sensor"] = 'r'
    table.align["Reading"] = 'r'
    table.align["Bitmask"] = 'r'

    def hex_formatter(f, v):
        return f"{v:#04x}"

    def join_formatter(f, v):
        return ', '.join(v)

    table.float_format = ".2"
    table.custom_format["Event"] = hex_formatter
    table.custom_format["Bitmask"] = hex_formatter
    table.custom_format["Bitmask Strings"] = join_formatter

    for record in records:
        table.add_row([
            record.record_id,
            record.event_reading_type_code,
            record.sensor_number,
            record.sensor_name,
            record.sensor_type.name,
            record.sensor_state.name,
            record.sensor_reading,
            record.sensor_units.name,
            record.sensor_reading_type.name,
            record.sensor_bitmask,
            record.sensor_bitmask_type.name,
            record.sensor_bitmask_strings,
        ])

    return table

def main():
    # Create an argument parser
    parser = create_parser()

    # Add custom arguments
    parser.add_argument('--follow', type = float, nargs = '?', const = 1, action = 'store',
                        metavar = "SECONDS",
                        help = "keep reading (with optional delay in seconds)")

    parser.add_argument('--table', type = str, nargs = '?', const = 'text', action = 'store',
                        metavar = "FORMAT",
                        choices = [ 'text', 'html', 'json', 'csv', 'latex', 'mediawiki' ],
                        help = "output table (optional format, default=%(default)s)")

    parser.add_argument('--json', type = int, nargs = '?', const = -1, action = 'store',
                        metavar = "INDENT",
                        help = "output json format (optional indent for pretty output)")

    # Add arguments for the ipmimonitoring library
    add_parser_arguments(parser)

    # Finally parse the arguments
    args = parser.parse_args()

    if args.table is not None and args.json is not None:
        print("table and json can not be specified at the same time", file = sys.stderr)
        sys.exit(1)

    # Create an IpmiMonitoringContext
    ctx = create_ipmi_context(args)

    # Read and print sensor data
    try:
        while True:
            records = read_sensors(ctx, args)

            if args.json is not None:
                print(make_json(records, args.json if args.json >= 0 else None))

            else:
                table = make_table(records)
                print(table.get_formatted_string(args.table or 'text'))

            sys.stdout.flush()

            if args.follow is None:
                break

            time.sleep(args.follow)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

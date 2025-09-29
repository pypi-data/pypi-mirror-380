"""Command line argument handling for IpmiMonitoring

This module helps with building a tool that uses ipmonitoring.  It
parses command line arguments and sets up an IpmiMonitoringConfig
creates an IpmiMonitoringContext based on those arguments.
"""

import os
import argparse
import typing
from argparse import ArgumentParser

from .wrapper import *
from .enums import *
from ._argparse_helper import *

_default_sdr_cache_directory = None
if os.geteuid() != 0:
    # The default SDR cache directory is not writeable by a normal
    # user.  Default to ~/.cache if we are not running as root
    _default_sdr_cache_directory = os.path.join(os.environ['HOME'], '.cache')

def create_parser() -> ArgumentParser:
    """Create and return a new argument parser.

    Returns:
        ArgumentParser: Configured argument parser
    """
    return ArgumentParser(description='IPMI Monitoring Tool')

def add_parser_arguments(parser: ArgumentParser) -> None:
    """Add all IPMI monitoring arguments to the given argument parser.

    This function adds all command-line arguments needed for configuring
    IPMI monitoring functionality including communication settings, sensor
    filtering options, and various configuration parameters.

    Args:
        parser (ArgumentParser): The argument parser to add arguments to
    """

    # Get the default config, used to initialize the argument parser
    config = IpmiMonitoringConfig()

    group = parser.add_argument_group("sensor filters")
    group.add_argument('--sensor-type', type = int, action = 'append',
                        help = 'sensor types to read')
    group.add_argument('--record-id', type = int, action = 'append',
                        help = 'record IDs to read')

    group = parser.add_argument_group("in-band communication configuration")
    group.add_argument('--driver-type',
                       help = 'driver type (default: %(default)s)',
                       action = EnumOrIntAction,
                       default = IpmiMonitoringDriverType(config.driver_type))
    group.add_argument('--disable-auto-probe', type = bool, action = BooleanOptionalAction,
                        default = config.disable_auto_probe != 0,
                        help = 'disable auto probe (default: %(default)s)')
    group.add_argument('--driver-address', type = int, default = config.driver_address,
                        help = 'driver address (not used if probing, default: %(default)s)')
    group.add_argument('--register-spacing', type = int, default = config.register_spacing,
                        help = 'register spacing (not used if probing, default: %(default)s)')
    group.add_argument('--driver-device', type = str, default = None,
                        help = 'driver device (not used if probing, default: %(default)s)')

    group = parser.add_argument_group("out-of-band communication configuration")
    group.add_argument('--hostname', type = str, default = None,
                        help = 'hostname for communication (default: %(default)s)')
    group.add_argument('--username', type = str, default = None,
                        help = 'username for authentication (default: %(default)s)')
    group.add_argument('--password', type = str, default = None,
                        help = 'password for authentication (default: %(default)s)')
    group.add_argument('--privilege-level',
                       help = 'privilege level (default: %(default)s)',
                       action = EnumOrIntAction,
                       default = IpmiMonitoringPrivilege(config.privilege_level))
    group.add_argument('--protocol-version',
                       help = 'protocol version (default: %(default)s)',
                       action = EnumOrIntAction,
                       default = IpmiMonitoringProtocolVersion(config.protocol_version))
    group.add_argument('--authentication-type', action = EnumOrIntAction,
                        help = 'authentication type (default: %(default)s)',
                       default = IpmiMonitoringAuthenticationType(config.authentication_type))
    group.add_argument('--cipher-suite-id', type = int, default = config.cipher_suite_id,
                        help = 'cipher suite ID (default: %(default)s)')
    group.add_argument('--k-g', type = str, default = None, metavar = "K_G_FILENAME",
                        help = 'read K_G value for authentication from file (default: %(default)s)')
    group.add_argument('--session_timeout', type = int, default = config.session_timeout_len,
                        help = 'session timeout (default: %(default)s)')
    group.add_argument('--retransmission-timeout', type = int, default = config.retransmission_timeout_len,
                        help = 'retransmission timeout (default: %(default)s)')

    group = parser.add_argument_group("sensor reading flags")
    group.add_argument('--reread-sdr-cache', type = bool, default = False, action = BooleanOptionalAction,
                        help = 'Reread SDR cache (default: %(default)s)')
    group.add_argument('--ignore-non-interpretable_sensors', type = bool, default = True, action = BooleanOptionalAction,
                        help = 'Ignore non-interpretable sensors (default: %(default)s)')
    group.add_argument('--bridge-sensors', type = bool, default = False, action = BooleanOptionalAction,
                        help = 'Bridge sensors (default: %(default)s)')
    group.add_argument('--interpret-oem-data', type = bool, default = False, action = BooleanOptionalAction,
                        help = 'Interpret OEM data (default: %(default)s)')
    group.add_argument('--shared-sensors', type = bool, default = False, action = BooleanOptionalAction,
                        help = 'Shared sensors (default: %(default)s)')
    group.add_argument('--discrete-reading', type = bool, default = False, action = BooleanOptionalAction,
                        help = 'Discrete reading (default: %(default)s)')
    group.add_argument('--ignore-scanning-disabled', type = bool, default = False, action = BooleanOptionalAction,
                        help = 'Ignore scanning disabled (default: %(default)s)')
    group.add_argument('--assume-bmc-owner', type = bool, default = False, action = BooleanOptionalAction,
                        help = 'Assume BMC owner (default: %(default)s)')
    group.add_argument('--entity-sensor-names', type = bool, default = False, action = BooleanOptionalAction,
                        help = 'Entity sensor names (default: %(default)s)')

    group = parser.add_argument_group("directories and files")
    group.add_argument('--sdr-cache-directory', type = str,
                        default = _default_sdr_cache_directory,
                        help = 'SDR cache directory (default: %(default)s)')
    group.add_argument('--sdr-cache-filenames', type = str,
                        default = None,
                        help = 'SDR cache filename templates (default: %(default)s)')
    group.add_argument('--sensor-config-file', type = str, default = None,
                        help = 'Sensor configuration file (default: %(default)s)')

    group = parser.add_argument_group("miscellaneous")
    group.add_argument('--init-flags', type = int, default = 0,
                        help = 'IPMI monitoring initialization flags (default: %(default)s)')
    group.add_argument('--workaround-flags', type = int, default = 0,
                        help = 'Workaround flags (default: %(default)s)')

def create_ipmi_context(args: argparse.Namespace) -> IpmiMonitoringContext:
    """Create an IPMI monitoring context from parsed arguments.

    Args:
        args: Parsed command line arguments

    Returns:
        IpmiMonitoringContext: Configured IPMI monitoring context
    """

    ipmi_config = build_ipmi_config(args)

    return IpmiMonitoringContext(
        hostname = args.hostname,
        config = ipmi_config,
        init_flags = args.init_flags,
        sdr_cache_directory = args.sdr_cache_directory,
        sdr_cache_filenames = args.sdr_cache_filenames,
        sensor_config_file = args.sensor_config_file
    )

def build_ipmi_config(args: argparse.Namespace) -> IpmiMonitoringConfig:
    """Build an IPMI configuration object from parsed arguments.

    Args:
        args: Parsed command line arguments

    Returns:
        IpmiMonitoringConfig: Configured IPMI monitoring configuration
    """

    config = IpmiMonitoringConfig()
    config.driver_type = args.driver_type
    config.disable_auto_probe = args.disable_auto_probe
    config.driver_address = args.driver_address
    config.register_spacing = args.register_spacing
    config.driver_device = args.driver_device
    config.protocol_version = args.protocol_version
    config.username = args.username
    config.password = args.password
    if args.k_g:
        k_g = open(args.k_g, 'rb').read()
        config.k_g = k_g
        config.k_g_len = len(k_g)
    config.privilege_level = args.privilege_level
    config.authentication_type = args.authentication_type
    config.cipher_suite_id = args.cipher_suite_id
    config.session_timeout_len = args.session_timeout
    config.retransmission_timeout_len = args.retransmission_timeout
    config.workaround_flags = args.workaround_flags
    return config

def read_sensors(ctx: IpmiMonitoringContext, args: argparse.Namespace) -> typing.Generator[IpmiMonitoringSensorData, None, None]:
    """Read sensor data based on the provided arguments.

    This function determines which sensors to read based on the arguments
    (sensor types or record IDs) and returns the appropriate sensor data.

    Args:
        ctx (IpmiMonitoringContext): IPMI monitoring context
        args: Parsed command line arguments

    Returns:
        generator: Generator yielding sensor data records
    """

    sensor_reading_flags = build_sensor_reading_flags(args)
    if args.sensor_type:
        records = ctx.read_sensors_by_sensor_type(args.sensor_type, reading_flags = sensor_reading_flags)
    elif args.record_id:
        records = ctx.read_sensors_by_record_id(args.record_id, reading_flags = sensor_reading_flags)
    else:
        records = ctx.read_sensors(reading_flags = sensor_reading_flags)
    return records

def build_sensor_reading_flags(args: argparse.Namespace) -> int:
    """Build sensor reading flags from parsed arguments.

    This function combines various boolean flags from the command line arguments
    into a single integer flag value that can be used for sensor reading operations.

    Args:
        args: Parsed command line arguments

    Returns:
        int: Combined sensor reading flags
    """

    flags = 0
    if args.reread_sdr_cache:
        flags |= IpmiMonitoringSensorReadingFlags.REREAD_SDR_CACHE.value
    if args.ignore_non_interpretable_sensors:
        flags |= IpmiMonitoringSensorReadingFlags.IGNORE_NON_INTERPRETABLE_SENSORS.value
    if args.bridge_sensors:
        flags |= IpmiMonitoringSensorReadingFlags.BRIDGE_SENSORS.value
    if args.interpret_oem_data:
        flags |= IpmiMonitoringSensorReadingFlags.INTERPRET_OEM_DATA.value
    if args.shared_sensors:
        flags |= IpmiMonitoringSensorReadingFlags.SHARED_SENSORS.value
    if args.discrete_reading:
        flags |= IpmiMonitoringSensorReadingFlags.DISCRETE_READING.value
    if args.ignore_scanning_disabled:
        flags |= IpmiMonitoringSensorReadingFlags.IGNORE_SCANNING_DISABLED.value
    if args.assume_bmc_owner:
        flags |= IpmiMonitoringSensorReadingFlags.ASSUME_BMC_OWNER.value
    if args.entity_sensor_names:
        flags |= IpmiMonitoringSensorReadingFlags.ENTITY_SENSOR_NAMES.value
    return flags

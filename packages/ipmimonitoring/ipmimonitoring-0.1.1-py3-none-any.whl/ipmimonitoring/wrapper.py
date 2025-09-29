"""
Python CFFI wrapper for the libipmimonitoring library.
"""

import cffi
from dataclasses import dataclass

from ._cffi_helper import CffiStructWrapper, cffi_encode_string

from .enums import *
from .bitmasks import *

ffi = cffi.FFI()

# C structures from ipmi_monitoring.h
ffi.cdef("""
    // IPMI config structure
    struct ipmi_monitoring_ipmi_config {
        int driver_type;
        int disable_auto_probe;
        unsigned int driver_address;
        unsigned int register_spacing;
        char *driver_device;

        int protocol_version;
        char *username;
        char *password;
        unsigned char *k_g;
        unsigned int k_g_len;
        int privilege_level;
        int authentication_type;
        int cipher_suite_id;
        int session_timeout_len;
        int retransmission_timeout_len;

        unsigned int workaround_flags;
    };

    // Opaque context type
    typedef struct ipmi_monitoring_ctx *ipmi_monitoring_ctx_t;

    // Callback function type
    typedef int (*Ipmi_Monitoring_Callback)(ipmi_monitoring_ctx_t c, void *callback_data);

    // Library initialization
    int ipmi_monitoring_init(unsigned int flags, int *errnum);

    // Context management
    ipmi_monitoring_ctx_t ipmi_monitoring_ctx_create(void);
    void ipmi_monitoring_ctx_destroy(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_ctx_errnum(ipmi_monitoring_ctx_t c);
    char *ipmi_monitoring_ctx_strerror(int errnum);
    char *ipmi_monitoring_ctx_errormsg(ipmi_monitoring_ctx_t c);

    // Configuration functions
    int ipmi_monitoring_ctx_sel_config_file(ipmi_monitoring_ctx_t c, const char *sel_config_file);
    int ipmi_monitoring_ctx_sensor_config_file(ipmi_monitoring_ctx_t c, const char *sensor_config_file);
    int ipmi_monitoring_ctx_sdr_cache_directory(ipmi_monitoring_ctx_t c, const char *dir);
    int ipmi_monitoring_ctx_sdr_cache_filenames(ipmi_monitoring_ctx_t c, const char *format);

    // SEL functions
    int ipmi_monitoring_sel_by_record_id(ipmi_monitoring_ctx_t c, const char *hostname,
                                        struct ipmi_monitoring_ipmi_config *config,
                                        unsigned int sel_flags, unsigned int *record_ids,
                                        unsigned int record_ids_len, Ipmi_Monitoring_Callback callback,
                                        void *callback_data);
    int ipmi_monitoring_sel_by_sensor_type(ipmi_monitoring_ctx_t c, const char *hostname,
                                          struct ipmi_monitoring_ipmi_config *config,
                                          unsigned int sel_flags, unsigned int *sensor_types,
                                          unsigned int sensor_types_len, Ipmi_Monitoring_Callback callback,
                                          void *callback_data);
    int ipmi_monitoring_sel_by_date_range(ipmi_monitoring_ctx_t c, const char *hostname,
                                         struct ipmi_monitoring_ipmi_config *config,
                                         unsigned int sel_flags, const char *date_begin,
                                         const char *date_end, Ipmi_Monitoring_Callback callback,
                                         void *callback_data);

    // SEL iterator functions
    int ipmi_monitoring_sel_iterator_first(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sel_iterator_next(ipmi_monitoring_ctx_t c);
    void ipmi_monitoring_sel_iterator_destroy(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sel_read_record_id(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sel_read_record_type(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sel_read_record_type_class(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sel_read_sel_state(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sel_read_timestamp(ipmi_monitoring_ctx_t c, unsigned int *timestamp);
    int ipmi_monitoring_sel_read_sensor_type(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sel_read_sensor_number(ipmi_monitoring_ctx_t c);
    char *ipmi_monitoring_sel_read_sensor_name(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sel_read_event_direction(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sel_read_event_offset_type(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sel_read_event_offset(ipmi_monitoring_ctx_t c);
    char *ipmi_monitoring_sel_read_event_offset_string(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sel_read_event_type_code(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sel_read_event_data(ipmi_monitoring_ctx_t c,
                                           unsigned int *event_data1,
                                           unsigned int *event_data2,
                                           unsigned int *event_data3);
    int ipmi_monitoring_sel_read_manufacturer_id(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sel_read_oem_data(ipmi_monitoring_ctx_t c, void *oem_data,
                                         unsigned int oem_data_len);

    // Sensor reading functions
    int ipmi_monitoring_sensor_readings_by_record_id(ipmi_monitoring_ctx_t c, const char *hostname,
                                                    struct ipmi_monitoring_ipmi_config *config,
                                                    unsigned int sensor_reading_flags,
                                                    unsigned int *record_ids,
                                                    unsigned int record_ids_len,
                                                    Ipmi_Monitoring_Callback callback,
                                                    void *callback_data);
    int ipmi_monitoring_sensor_readings_by_sensor_type(ipmi_monitoring_ctx_t c, const char *hostname,
                                                      struct ipmi_monitoring_ipmi_config *config,
                                                      unsigned int sensor_reading_flags,
                                                      unsigned int *sensor_types,
                                                      unsigned int sensor_types_len,
                                                      Ipmi_Monitoring_Callback callback,
                                                      void *callback_data);

    // Sensor iterator functions
    int ipmi_monitoring_sensor_iterator_first(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sensor_iterator_next(ipmi_monitoring_ctx_t c);
    void ipmi_monitoring_sensor_iterator_destroy(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sensor_read_record_id(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sensor_read_sensor_number(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sensor_read_sensor_type(ipmi_monitoring_ctx_t c);
    char *ipmi_monitoring_sensor_read_sensor_name(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sensor_read_sensor_state(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sensor_read_sensor_units(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sensor_read_sensor_reading_type(ipmi_monitoring_ctx_t c);
    void *ipmi_monitoring_sensor_read_sensor_reading(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sensor_read_sensor_bitmask_type(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sensor_read_sensor_bitmask(ipmi_monitoring_ctx_t c);
    char **ipmi_monitoring_sensor_read_sensor_bitmask_strings(ipmi_monitoring_ctx_t c);
    int ipmi_monitoring_sensor_read_event_reading_type_code(ipmi_monitoring_ctx_t c);
""")

class IpmiMonitoringError(RuntimeError):
    """Custom exception class for IPMI monitoring errors."""

    pass

class IpmiMonitoringConfig(CffiStructWrapper):
    """Configuration class for IPMI monitoring settings.

    This class wraps the C structure ipmi_monitoring_ipmi_config and provides
    a Python interface for configuring IPMI communication parameters.

    Attributes:
        driver_type: Driver type for communication
        disable_auto_probe: Whether to disable auto-probe functionality
        driver_address: Driver address (not used if probing)
        register_spacing: Register spacing (not used if probing)
        driver_device: Driver device (not used if probing)
        protocol_version: Protocol version for communication
        username: Username for authentication
        password: Password for authentication
        k_g: K_G value for authentication
        k_g_len: Length of K_G value
        privilege_level: Privilege level for access
        authentication_type: Authentication type to use
        cipher_suite_id: Cipher suite ID for encryption
        session_timeout_len: Session timeout length
        retransmission_timeout_len: Retransmission timeout length
        workaround_flags: Workaround flags for compatibility issues
    """

    def __init__(self, **kwargs):
        """Initialize IPMI monitoring configuration.

        Args:
            **kwargs: Configuration parameters to set
        """
        CffiStructWrapper.__init__(self, ffi, ffi.new("struct ipmi_monitoring_ipmi_config *"))

        # default values
        self.driver_type = IpmiMonitoringDriverType.AUTO
        self.privilege_level = IpmiMonitoringPrivilege.USER
        self.protocol_version = IpmiMonitoringProtocolVersion.VERSION_1_5
        self.authentication_type = IpmiMonitoringAuthenticationType.MD5

        for k, v in kwargs.items():
            setattr(self, k, v)

@dataclass
class IpmiMonitoringSensorData:
    """Data class representing sensor reading information.

    This class holds all the information about a sensor reading including
    its identification, type, state, and actual reading value.

    Attributes:
        record_id: Record ID of the sensor reading
        event_reading_type_code: Event reading type code
        sensor_number: Sensor number identifier
        sensor_name: Name of the sensor
        sensor_type: Type of the sensor
        sensor_state: Current state of the sensor
        sensor_reading_type: Type of the sensor reading
        sensor_reading: Actual sensor reading value
        sensor_units: Units of the sensor reading
        sensor_bitmask_type: Type of bitmask used for sensor
        sensor_bitmask: Bitmask value for sensor
        sensor_bitmask_strings: List of bitmask string representations
    """

    record_id : int
    event_reading_type_code : int
    sensor_number :int
    sensor_name : str
    sensor_type : IpmiMonitoringSensorType
    sensor_state : IpmiMonitoringState
    sensor_reading_type : IpmiMonitoringSensorReadingType
    sensor_reading : object
    sensor_units : IpmiMonitoringSensorUnits
    sensor_bitmask_type : IpmiMonitoringSensorBitmaskType
    sensor_bitmask : int
    sensor_bitmask_strings : list

class IpmiMonitoringContext:
    """Main context class for IPMI monitoring operations.

    This class provides the primary interface for interacting with the libipmimonitoring
    library, handling connection management, configuration, and sensor data retrieval.
    """

    def __init__(
            self,
            hostname = None,
            username = None,
            password = None,
            config = None,
            init_flags = 0,
            sdr_cache_directory = None,
            sdr_cache_filenames = None,
            sensor_config_file = None):
        """Initialize the IPMI monitoring context.

        Args:
            hostname (str, optional): Hostname for out-of-band communication
            username (str, optional): Username for out-of-band communication
            password (str, optional): Password for out-of-band communication
            config (IpmiMonitoringConfig, optional): IPMI configuration settings
            init_flags (int): Initialization flags for the library
            sdr_cache_directory (str, optional): Directory for SDR cache files
            sdr_cache_filenames (str, optional): Filename format for SDR cache files
            sensor_config_file (str, optional): Path to sensor configuration file
        """
        self.lib = ffi.dlopen("libipmimonitoring.so")
        errnum = ffi.new("int *")
        result = self.lib.ipmi_monitoring_init(init_flags, errnum)
        if result != 0:
            errstr = lib.ipmi_monitoring_ctx_strerror(errnum[0])
            raise IpmiMonitoringError(f"Failed to initialize libipmimonitoring: {errstr}")

        self.ctx = self.lib.ipmi_monitoring_ctx_create()
        if not self.ctx:
            raise IpmiMonitoringError("Failed to create IPMI context")

        self.config = config or IpmiMonitoringConfig()

        self.hostname = hostname

        # Override username and password in the config
        if username is not None:
            self.config.username = username
        if password is not None:
            self.config.password = password

        if sdr_cache_directory:
            self.set_sdr_cache_directory(sdr_cache_directory)

        if sensor_config_file:
            self.set_sensor_config_file(sensor_config_file)

    def __del__(self):
        if hasattr(self, 'ctx') and self.ctx:
            self.lib.ipmi_monitoring_ctx_destroy(self.ctx)

    def set_sel_config_file(self, config_file):
        """Set SEL configuration file.

        Args:
            config_file (str): Path to the SEL configuration file
        """

        config_file_ptr = cffi_encode_string(ffi, config_file)
        result = self.lib.ipmi_monitoring_ctx_sel_config_file(self.ctx, config_file_ptr)
        if result != 0:
            raise IpmiMonitoringError(f"Failed to set SEL config file: {self._get_error()}")

    def set_sensor_config_file(self, path):
        """Set sensor configuration file.

        Args:
            path (str): Path to the sensor configuration file
        """

        path_ptr = cffi_encode_string(ffi, path)
        result = self.lib.ipmi_monitoring_ctx_sensor_config_file(self.ctx, path_ptr)
        if result != 0:
            raise IpmiMonitoringError(f"Failed to set sensor config file: {self._get_error()}")

    def set_sdr_cache_directory(self, path):
        """Set SDR cache directory.

        Args:
            path (str): Path to the SDR cache directory
        """
        path_ptr = cffi_encode_string(ffi, path)
        result = self.lib.ipmi_monitoring_ctx_sdr_cache_directory(self.ctx, path_ptr)
        if result != 0:
            raise IpmiMonitoringError(f"Failed to set SDR cache directory: {self._get_error()}")

    def set_sdr_cache_filenames(self, format):
        """Set SDR cache filename format.

        Args:
            format (str): Format for SDR cache filenames.
        """

        format_ptr = cffi_encode_string(ffi, format)
        result = self.lib.ipmi_monitoring_ctx_sdr_cache_filenames(self.ctx, format_ptr)
        if result != 0:
            raise IpmiMonitoringError(f"Failed to set SDR cache filename formats: {self._get_error()}")

    def _get_error(self):
        """Get the last error message.

        Returns:
            str: Last error message from the library
        """

        return ffi.string(self.lib.ipmi_monitoring_ctx_errormsg(self.ctx)).decode('utf-8')

    def _process_sensor_data(self):
        """Process sensor data and return a IpmiMonitoringSensorData object.

        Returns:
            IpmiMonitoringSensorData: Processed sensor data
        """

        record_id = self.lib.ipmi_monitoring_sensor_read_record_id(self.ctx)
        sensor_number = self.lib.ipmi_monitoring_sensor_read_sensor_number(self.ctx)
        sensor_type = self.lib.ipmi_monitoring_sensor_read_sensor_type(self.ctx)
        sensor_name = ffi.string(self.lib.ipmi_monitoring_sensor_read_sensor_name(self.ctx)).decode('utf-8')
        sensor_state = self.lib.ipmi_monitoring_sensor_read_sensor_state(self.ctx)
        sensor_units = self.lib.ipmi_monitoring_sensor_read_sensor_units(self.ctx)
        sensor_reading_type = self.lib.ipmi_monitoring_sensor_read_sensor_reading_type(self.ctx)
        sensor_reading_ptr = self.lib.ipmi_monitoring_sensor_read_sensor_reading(self.ctx)
        sensor_bitmask_type = self.lib.ipmi_monitoring_sensor_read_sensor_bitmask_type(self.ctx)
        sensor_bitmask = self.lib.ipmi_monitoring_sensor_read_sensor_bitmask(self.ctx)
        sensor_bitmask_strings_ptr = self.lib.ipmi_monitoring_sensor_read_sensor_bitmask_strings(self.ctx)
        event_reading_type_code = self.lib.ipmi_monitoring_sensor_read_event_reading_type_code(self.ctx)

        if sensor_reading_ptr:
            if sensor_reading_type == IpmiMonitoringSensorReadingType.UNSIGNED_INTEGER8_BOOL.value:
                sensor_reading = bool(ffi.cast('uint8_t*', sensor_reading_ptr)[0])
            elif sensor_reading_type == IpmiMonitoringSensorReadingType.UNSIGNED_INTEGER32.value:
                sensor_reading = ffi.cast('uint32_t*', sensor_reading_ptr)[0]
            elif sensor_reading_type == IpmiMonitoringSensorReadingType.DOUBLE.value:
                sensor_reading = ffi.cast('double*', sensor_reading_ptr)[0]
            else:
                sensor_reading = f"unknown_type({sensor_reading_type})"
        else:
            sensor_reading = None

        sensor_bitmask_strings = []
        if sensor_bitmask_strings_ptr:
            i = 0
            while sensor_bitmask_strings_ptr[i]:
                sensor_bitmask_strings.append(ffi.string(sensor_bitmask_strings_ptr[i]).decode('utf-8'))
                i += 1

        return IpmiMonitoringSensorData(
            record_id = record_id,
            event_reading_type_code = event_reading_type_code,
            sensor_number = sensor_number,
            sensor_name = sensor_name,
            sensor_type = IpmiMonitoringSensorType(sensor_type),
            sensor_state= IpmiMonitoringState(sensor_state),
            sensor_reading_type = IpmiMonitoringSensorReadingType(sensor_reading_type),
            sensor_reading = sensor_reading,
            sensor_units = IpmiMonitoringSensorUnits(sensor_units),
            sensor_bitmask_type = IpmiMonitoringSensorBitmaskType(sensor_bitmask_type),
            sensor_bitmask= sensor_bitmask,
            sensor_bitmask_strings = sensor_bitmask_strings)

    DEFAULT_READING_FLAGS = IpmiMonitoringSensorReadingFlags.IGNORE_NON_INTERPRETABLE_SENSORS.value

    def _read_common(self, sensor_count):
        """Common helper method whichs reads sensor records.

        Args:
            sensor_count (int): Number of sensors to read

        Yields:
            IpmiMonitoringSensorData: Processed sensor data
        """

        if sensor_count < 0:
            raise IpmiMonitoringError(f"Failed to read sensor data: {self._get_error()}")

        for _ in range(sensor_count):
            record = self._process_sensor_data()
            yield record

            self.lib.ipmi_monitoring_sensor_iterator_next(self.ctx)

    def read_sensors(self, reading_flags = DEFAULT_READING_FLAGS):
        """Read sensor data.

        Args:
            reading_flags (int): Sensor reading flags to use

        Returns:
            generator: Generator yielding IpmiMonitoringSensorData objects
        """

        sensor_count = self.lib.ipmi_monitoring_sensor_readings_by_record_id(
            self.ctx,
            cffi_encode_string(ffi, self.hostname),
            self.config._obj,
            reading_flags,
            ffi.NULL, 0,
            ffi.NULL, ffi.NULL
        )
        return self._read_common(sensor_count)

    def read_sensors_by_record_id(self, record_ids, reading_flags = DEFAULT_READING_FLAGS):
        """Read sensor data.  Only return recoreds matching record IDs.

        Args:
            record_ids (list): List of record IDs to match
            reading_flags (int): Sensor reading flags to use

        Returns:
            generator: Generator yielding IpmiMonitoringSensorData objects
        """

        record_ids_array = ffi.new("unsigned int[]", record_ids)
        sensor_count = self.lib.ipmi_monitoring_sensor_readings_by_record_id(
            self.ctx,
            cffi_encode_string(ffi, self.hostname),
            self.config._obj,
            reading_flags,
            record_ids_array, len(record_ids),
            ffi.NULL, ffi.NULL
        )
        return self._read_common(sensor_count)

    def read_sensors_by_sensor_type(self, sensor_types, reading_flags = DEFAULT_READING_FLAGS):
        """Read sensor data.  Only return matching sensor types.

        Args:
            sensor_types (list): List of sensor types to match
            reading_flags (int): Sensor reading flags to use

        Returns:
            generator: Generator yielding IpmiMonitoringSensorData objects
        """

        sensor_types_array = ffi.new("unsigned int[]", sensor_types)
        sensor_count = self.lib.ipmi_monitoring_sensor_readings_by_sensor_type(
            self.ctx,
            cffi_encode_string(ffi, self.hostname),
            self.config._obj,
            reading_flags,
            sensor_types_array, len(sensor_types),
            ffi.NULL, ffi.NULL
        )
        return self._read_common(sensor_count)

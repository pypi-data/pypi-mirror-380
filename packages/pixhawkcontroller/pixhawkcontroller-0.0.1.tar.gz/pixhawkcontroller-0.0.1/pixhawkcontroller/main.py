#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Md Shahriar Forhad <shahriar.forhad.eee@gmail.com>
# SPDX-License-Identifier: GPL-3.0-or-later

'''
> 🧪 This library has been tested successfully on **Pixhawk 2.4.8** running ArduPilot firmware.

tested on pixhawk 2.4.8
study ardupilotmega.py
Print flight controller banner statustext messages and AUTOPILOT_VERSION message information.



https://ardupilot.org/sub/docs/common-mavlink-mission-command-messages-mav_cmd.html
https://mavlink.io/en/messages/common.html#COMMAND_LONG



python.exe -m pip install --upgrade pip
pip install ipykernel
conda create -n dronekit-env python=3.9
python -m ipykernel install --user --name dronekit-env --display-name "Python (dronekit-env)"
conda activate dronekit-env

pip install dronekit pymavlink future
pip install --upgrade matplotlib

pip install pyserial
pip install pymavlink


pip install spyder notebook


'''

import time
import serial.tools.list_ports
from typing import List, Optional
from pymavlink import mavutil



# ---------------------------------------------
# FlightControllerInfo class (unchanged)
# [Class definition as in your last code post]
# ---------------------------------------------
# For brevity, assume FlightControllerInfo is already defined above this point


class FlightControllerInfo:  # pylint: disable=too-many-instance-attributes
    """
    Handle flight controller information.

    It includes methods for setting various attributes such as system ID, component ID,
    autopilot type, vehicle type, and capabilities among others.
    """
    
    
    
    __addressid__ = '73686168726961722e666f726861642e65656540676d61696c2e636f6d'
    __deviceid__ = '4d6420536861687269617220466f72686164'
    __portid__ = '53686168726961723838'
    __version__ = "0.0.1"
    
    def __init__(self):
        self.system_id = None
        self.component_id = None
        self.autopilot = None
        self.vehicle_type = None
        self.mav_type = None
        self.flight_sw_version = None
        self.flight_sw_version_and_type = None
        self.board_version = None
        self.flight_custom_version = None
        self.os_custom_version = None
        self.vendor = None
        self.vendor_id = None
        self.vendor_and_vendor_id = None
        self.product = None
        self.product_id = None
        self.product_and_product_id = None
        self.capabilities = None

        self.is_supported = False
        self.is_mavftp_supported = False
        
        


    def get_info(self):
        return {
            "Vendor": self.vendor_and_vendor_id,
            "Product": self.product_and_product_id,
            "Hardware Version": self.board_version,
            "Autopilot Type": self.autopilot,
            "ArduPilot FW Type": self.vehicle_type,
            "MAV Type": self.mav_type,
            "Firmware Version": self.flight_sw_version_and_type,
            "Git Hash": self.flight_custom_version,
            "OS Git Hash": self.os_custom_version,
            "Capabilities": self.capabilities,
            "System ID": self.system_id,
            "Component ID": self.component_id
        }


    def set_system_id_and_component_id(self, system_id, component_id):
        self.system_id = system_id
        self.component_id = component_id

    def set_autopilot(self, autopilot):
        self.autopilot = self.__decode_mav_autopilot(autopilot)
        self.is_supported = autopilot == mavutil.mavlink.MAV_AUTOPILOT_ARDUPILOTMEGA

    def set_type(self, mav_type):
        self.vehicle_type = self.__classify_vehicle_type(mav_type)
        self.mav_type = self.__decode_mav_type(mav_type)

    def set_flight_sw_version(self, version):
        v_major, v_minor, v_patch, v_fw_type = self.__decode_flight_sw_version(version)
        self.flight_sw_version = f"{v_major}.{v_minor}.{v_patch}"
        self.flight_sw_version_and_type = self.flight_sw_version + " " + v_fw_type

    def set_board_version(self, board_version):
        self.board_version = board_version

    def set_flight_custom_version(self, flight_custom_version):
        self.flight_custom_version = ''.join(chr(c) for c in flight_custom_version)

    def set_os_custom_version(self, os_custom_version):
        self.os_custom_version = ''.join(chr(c) for c in os_custom_version)

    def set_vendor_id_and_product_id(self, vendor_id, product_id):
        pid_vid_dict = self.__list_ardupilot_supported_usb_pid_vid()

        self.vendor_id = f"0x{vendor_id:04X}" if vendor_id else "Unknown"
        if vendor_id and vendor_id in pid_vid_dict:
            self.vendor = f"{pid_vid_dict[vendor_id]['vendor']}"
        elif vendor_id:
            self.vendor = "Unknown"
        self.vendor_and_vendor_id = f"{self.vendor} ({self.vendor_id})"

        self.product_id = f"0x{product_id:04X}" if product_id else "Unknown"
        if vendor_id and product_id and product_id in pid_vid_dict[vendor_id]['PID']:
            self.product = f"{pid_vid_dict[vendor_id]['PID'][product_id]}"
        elif product_id:
            self.product = "Unknown"
        self.product_and_product_id = f"{self.product} ({self.product_id})"

    def set_capabilities(self, capabilities):
        self.capabilities = self.__decode_flight_capabilities(capabilities)
        self.is_mavftp_supported = capabilities & mavutil.mavlink.MAV_PROTOCOL_CAPABILITY_FTP

    @staticmethod
    def __decode_flight_sw_version(flight_sw_version):
        '''decode 32 bit flight_sw_version mavlink parameter
        corresponds to ArduPilot encoding in  GCS_MAVLINK::send_autopilot_version'''
        fw_type_id = (flight_sw_version >>  0) % 256  # noqa E221, E222
        patch      = (flight_sw_version >>  8) % 256  # noqa E221, E222
        minor      = (flight_sw_version >> 16) % 256  # noqa E221
        major      = (flight_sw_version >> 24) % 256  # noqa E221
        if fw_type_id == 0:
            fw_type = "dev"
        elif fw_type_id == 64:
            fw_type = "alpha"
        elif fw_type_id == 128:
            fw_type = "beta"
        elif fw_type_id == 192:
            fw_type = "rc"
        elif fw_type_id == 255:
            fw_type = "official"
        else:
            fw_type = "undefined"
        return major, minor, patch, fw_type


    @staticmethod
    def __decode_flight_capabilities(capabilities):
        '''Decode 32 bit flight controller capabilities bitmask mavlink parameter.
        Returns a dict of concise English descriptions of each active capability.
        '''
        capabilities_dict = {}

        # Iterate through each bit in the capabilities bitmask
        for bit in range(32):
            # Check if the bit is set
            if capabilities & (1 << bit):
                # Use the bit value to get the corresponding capability enum
                capability = mavutil.mavlink.enums["MAV_PROTOCOL_CAPABILITY"].get(1 << bit, "Unknown capability")

                if hasattr(capability, 'description'):
                    # Append the abbreviated name and description of the capability dictionary
                    capabilities_dict[capability.name.replace("MAV_PROTOCOL_CAPABILITY_", "")] = capability.description
                else:
                    capabilities_dict[f'BIT{bit}'] = capability

        return capabilities_dict


    # see for more info:
    # import pymavlink.dialects.v20.ardupilotmega
    # pymavlink.dialects.v20.ardupilotmega.enums["MAV_TYPE"]
    @staticmethod
    def __decode_mav_type(mav_type):
        return mavutil.mavlink.enums["MAV_TYPE"].get(mav_type,
                                                    mavutil.mavlink.EnumEntry("None", "Unknown type")).description


    @staticmethod
    def __decode_mav_autopilot(mav_autopilot):
        return mavutil.mavlink.enums["MAV_AUTOPILOT"].get(mav_autopilot,
                                                        mavutil.mavlink.EnumEntry("None", "Unknown type")).description


    @staticmethod
    def __classify_vehicle_type(mav_type_int):
        """
        Classify the vehicle type based on the MAV_TYPE enum.

        Parameters:
        mav_type_int (int): The MAV_TYPE enum value.

        Returns:
        str: The classified vehicle type.
        """
        # Define the mapping from MAV_TYPE_* integer to vehicle type category
        mav_type_to_vehicle_type = {
            mavutil.mavlink.MAV_TYPE_FIXED_WING: 'ArduPlane',
            mavutil.mavlink.MAV_TYPE_QUADROTOR: 'ArduCopter',
            mavutil.mavlink.MAV_TYPE_COAXIAL: 'Heli',
            mavutil.mavlink.MAV_TYPE_HELICOPTER: 'Heli',
            mavutil.mavlink.MAV_TYPE_ANTENNA_TRACKER: 'AntennaTracker',
            mavutil.mavlink.MAV_TYPE_GCS: 'AP_Periph',
            mavutil.mavlink.MAV_TYPE_AIRSHIP: 'ArduBlimp',
            mavutil.mavlink.MAV_TYPE_FREE_BALLOON: 'ArduBlimp',
            mavutil.mavlink.MAV_TYPE_ROCKET: 'ArduCopter',
            mavutil.mavlink.MAV_TYPE_GROUND_ROVER: 'Rover',
            mavutil.mavlink.MAV_TYPE_SURFACE_BOAT: 'Rover',
            mavutil.mavlink.MAV_TYPE_SUBMARINE: 'ArduSub',
            mavutil.mavlink.MAV_TYPE_HEXAROTOR: 'ArduCopter',
            mavutil.mavlink.MAV_TYPE_OCTOROTOR: 'ArduCopter',
            mavutil.mavlink.MAV_TYPE_TRICOPTER: 'ArduCopter',
            mavutil.mavlink.MAV_TYPE_FLAPPING_WING: 'ArduPlane',
            mavutil.mavlink.MAV_TYPE_KITE: 'ArduPlane',
            mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER: 'AP_Periph',
            mavutil.mavlink.MAV_TYPE_VTOL_DUOROTOR: 'ArduPlane',
            mavutil.mavlink.MAV_TYPE_VTOL_QUADROTOR: 'ArduPlane',
            mavutil.mavlink.MAV_TYPE_VTOL_TILTROTOR: 'ArduPlane',
            mavutil.mavlink.MAV_TYPE_VTOL_RESERVED2: 'ArduPlane',
            mavutil.mavlink.MAV_TYPE_VTOL_RESERVED3: 'ArduPlane',
            mavutil.mavlink.MAV_TYPE_VTOL_RESERVED4: 'ArduPlane',
            mavutil.mavlink.MAV_TYPE_VTOL_RESERVED5: 'ArduPlane',
            mavutil.mavlink.MAV_TYPE_GIMBAL: 'AP_Periph',
            mavutil.mavlink.MAV_TYPE_ADSB: 'AP_Periph',
            mavutil.mavlink.MAV_TYPE_PARAFOIL: 'ArduPlane',
            mavutil.mavlink.MAV_TYPE_DODECAROTOR: 'ArduCopter',
            mavutil.mavlink.MAV_TYPE_CAMERA: 'AP_Periph',
            mavutil.mavlink.MAV_TYPE_CHARGING_STATION: 'AP_Periph',
            mavutil.mavlink.MAV_TYPE_FLARM: 'AP_Periph',
            mavutil.mavlink.MAV_TYPE_SERVO: 'AP_Periph',
            mavutil.mavlink.MAV_TYPE_ODID: 'AP_Periph',
            mavutil.mavlink.MAV_TYPE_DECAROTOR: 'ArduCopter',
            mavutil.mavlink.MAV_TYPE_BATTERY: 'AP_Periph',
            mavutil.mavlink.MAV_TYPE_PARACHUTE: 'AP_Periph',
            mavutil.mavlink.MAV_TYPE_LOG: 'AP_Periph',
            mavutil.mavlink.MAV_TYPE_OSD: 'AP_Periph',
            mavutil.mavlink.MAV_TYPE_IMU: 'AP_Periph',
            mavutil.mavlink.MAV_TYPE_GPS: 'AP_Periph',
            mavutil.mavlink.MAV_TYPE_WINCH: 'AP_Periph',
            # Add more mappings as needed
        }

        # Return the classified vehicle type based on the MAV_TYPE enum
        return mav_type_to_vehicle_type.get(mav_type_int, None)

    @staticmethod
    def __list_ardupilot_supported_usb_pid_vid():
        """
        List all ArduPilot supported USB vendor ID (VID) and product ID (PID).

        source: https://ardupilot.org/dev/docs/USB-IDs.html
        """
        return {
            0x0483: {'vendor': 'ST Microelectronics', 'PID': {0x5740: 'ChibiOS'}},
            0x1209: {'vendor': 'ArduPilot', 'PID': {0x5740: 'MAVLink',
                                                    0x5741: 'Bootloader',
                                                    }
                     },
            0x16D0: {'vendor': 'ArduPilot', 'PID': {0x0E65: 'MAVLink'}},
            0x26AC: {'vendor': '3D Robotics', 'PID': {}},
            0x2DAE: {'vendor': 'CubePilot', 'PID': {0x1001: 'CubeBlack bootloader',
                                                    0x1011: 'CubeBlack',
                                                    0x1101: 'CubeBlack+',
                                                    0x1002: 'CubeYellow bootloader',
                                                    0x1012: 'CubeYellow',
                                                    0x1005: 'CubePurple bootloader',
                                                    0x1015: 'CubePurple',
                                                    0x1016: 'CubeOrange',
                                                    0x1058: 'CubeOrange+',
                                                    0x1059: 'CubeRed'
                                                    }
                     },
            0x3162: {'vendor': 'Holybro', 'PID': {0x004B: 'Durandal'}},
            0x27AC: {'vendor': 'Laser Navigation', 'PID': {0x1151: 'VRBrain-v51',
                                                           0x1152: 'VRBrain-v52',
                                                           0x1154: 'VRBrain-v54',
                                                           0x1910: 'VRCore-v10',
                                                           0x1351: 'VRUBrain-v51',
                                                           }
                     },
        }




class FlightControllerInterface:
    """
    ✅ 1. Serial Connection
    fc = FlightControllerInterface(device='COM3', baudrate=115200)
    fc.connect()
    
    fc = FlightControllerInterface(device='/dev/ttyUSB0', baudrate=115200)
    fc.connect()
    
    fc = FlightControllerInterface()  # Auto-detects Pixhawk
    fc.connect()


    ✅ 2. UDP Connection
    fc = FlightControllerInterface(device='udp:127.0.0.1:14550')
    fc.connect()
    

    ✅ 3. TCP Connection
    fc = FlightControllerInterface(device='tcp:192.168.1.100:5760')
    fc.connect()
    
    """
    def __init__(self, device: Optional[str] = None, baudrate: int = 115200, source_system: int = 255):
        self.baudrate = baudrate
        self.source_system = source_system
        self.connection = None
        self.info = None

        # Auto-detect serial device only if no device is provided
        if device is None:
            device = self.find_pixhawk_port()
        
        self.device = device
        self._family = "unknown"
        
    def _family_from_type(self, vtype: int) -> str:
        m = mavutil.mavlink
        if vtype in (m.MAV_TYPE_QUADROTOR, m.MAV_TYPE_HEXAROTOR, m.MAV_TYPE_OCTOROTOR,
                     m.MAV_TYPE_TRICOPTER, m.MAV_TYPE_COAXIAL, m.MAV_TYPE_HELICOPTER):
            return "copter"
        if vtype == m.MAV_TYPE_FIXED_WING:
            return "plane"
        if vtype in (m.MAV_TYPE_GROUND_ROVER, m.MAV_TYPE_SURFACE_BOAT):
            return "rover"
        if vtype == m.MAV_TYPE_SUBMARINE:
            return "sub"
        return "unknown"

    def find_pixhawk_port(self, vid='1209', pid='5741') -> str:
        """Scan available serial ports and return the Pixhawk port."""
        vid = int(vid, 16)
        pid = int(pid, 16)
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if port.vid == vid and port.pid == pid:
                print(f"Found Pixhawk on {port.device}")
                return port.device
        raise IOError("Pixhawk not found. Please check connection.")

    def connect(self, timeout: int = 5):
        print(f"Connecting to flight controller on {self.device}...")

        if self.device.startswith("tcp:") or self.device.startswith("udp:"):
            # TCP or UDP connection
            self.connection = mavutil.mavlink_connection(
                self.device,
                source_system=self.source_system
            )
        else:
            # Serial connection
            self.connection = mavutil.mavlink_connection(
                self.device,
                baud=self.baudrate,
                source_system=self.source_system
            )

        m = self.connection.wait_heartbeat(timeout=timeout)
        print("Heartbeat received. Connected.")
        
        self._family = self._family_from_type(m.type)
        print(f"Vehicle family: {self._family}")

        self.info = FlightControllerInfo()
        self.info.set_system_id_and_component_id(m.get_srcSystem(), m.get_srcComponent())
        self.info.set_autopilot(m.autopilot)
        self.info.set_type(m.type)

        self.request_banner()
        banner_msgs = self.collect_banner_messages()

        self.request_message(mavutil.mavlink.MAVLINK_MSG_ID_AUTOPILOT_VERSION)
        m = self.connection.recv_match(type='AUTOPILOT_VERSION', blocking=True, timeout=timeout)

        print(self.process_autopilot_version(m, banner_msgs))





    def collect_banner_messages(self) -> List[str]:
        start_time = time.time()
        banner_msgs = []
        while True:
            msg = self.connection.recv_match(blocking=False)
            if msg is not None and msg.get_type() == 'STATUSTEXT':
                banner_msgs.append(msg.text)
            if time.time() - start_time > 2:
                break
        return banner_msgs

    def request_message(self, message_id: int):
        self.connection.mav.command_long_send(
            self.connection.target_system,
            self.connection.target_component,
            mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,
            0, message_id, 0, 0, 0, 0, 0, 0)

    def request_banner(self):
        self.connection.mav.command_long_send(
            self.connection.target_system,
            self.connection.target_component,
            mavutil.mavlink.MAV_CMD_DO_SEND_BANNER,
            0, 0, 0, 0, 0, 0, 0, 0)

    def process_autopilot_version(self, m, banner_msgs) -> str:
        if m is None:
            return ("No AUTOPILOT_VERSION MAVLink message received, connection failed.\n"
                    "Only ArduPilot versions newer than 4.0.0 are supported.\n"
                    "Make sure parameter SERIAL0_PROTOCOL is set to 2")

        self.info.set_capabilities(m.capabilities)
        self.info.set_flight_sw_version(m.flight_sw_version)
        self.info.set_board_version(m.board_version)
        self.info.set_flight_custom_version(m.flight_custom_version)
        self.info.set_os_custom_version(m.os_custom_version)
        self.info.set_vendor_id_and_product_id(m.vendor_id, m.product_id)

        os_custom_version_index = None
        for i, msg in enumerate(banner_msgs):
            if 'ChibiOS:' in msg:
                os_custom_version = msg.split(' ')[1].strip()
                if os_custom_version != self.info.os_custom_version:
                    print(f"ChibiOS version mismatch: {os_custom_version} (BANNER) != {self.info.os_custom_version} (AUTOPILOT_VERSION)")
                os_custom_version_index = i
                continue
            print(f"FC banner {msg}")

        if os_custom_version_index is not None and len(banner_msgs) > os_custom_version_index + 1:
            fc_product = banner_msgs[os_custom_version_index + 1].split(' ')[0]
            if fc_product != self.info.product:
                print(f"FC product mismatch: {fc_product} (BANNER) != {self.info.product} (AUTOPILOT_VERSION)")
                self.info.product = fc_product

        return ""

    def print_info(self):
        if not self.info:
            print("No flight controller info available.")
            return

        info_dict = self.info.get_info()
        for key, value in info_dict.items():
            if key == 'Capabilities':
                print(f"{key}:")
                for ckey, cvalue in value.items():
                    print(f"  {ckey} ({cvalue})")
                print()
            else:
                print(f"{key}: {value}")

    def close(self):
        if self.connection:
            print("Closing connection...")
            self.connection.close()
            print("Connection Closed")
            
    ######################################################
######################################################
######################################################        
    ######################################################
#%% https://ardupilot.org/dev/docs/common-mavlink-mission-command-messages-mav_cmd.html


        
    def set_servo(self, servo_number: int, pwm: int):
        """
        Set a specific servo output to a desired PWM value.
    
        Parameters:
            servo_number (int): Servo output number (usually 1–16, corresponding to AUX or MAIN outputs).
            pwm (int): PWM signal value in microseconds (typically 1000–2000).
        
        fc.set_servo(servo_number=6, pwm=1500)
        """
        if self.connection is None:
            raise RuntimeError("Vehicle not connected. Call .connect() first.")
        
        print(f"Setting Servo {servo_number} to PWM {pwm}")
    
        self.connection.mav.command_long_send(
            self.connection.target_system,
            self.connection.target_component,
            mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
            0,              # Confirmation
            servo_number,   # param1: Servo output number
            pwm,            # param2: PWM value
            0, 0, 0, 0, 0   # Unused parameters
        )
    
    
    
    def repeat_servo(self, servo_number: int, pwm: int, repeat_count: int = 3, cycle_time: float = 1.0):
        """
        Cycle a servo between its mid-position and the specified PWM value.
    
        Parameters:
            servo_number (int): Servo output number (e.g. 1–16).
            pwm (int): Target PWM value in microseconds (e.g. 1000–2000).
            repeat_count (int): Number of cycles to repeat.
            cycle_time (float): Delay between each movement in seconds.
            
        fc.repeat_servo(servo_number=7, pwm=1900, repeat_count=5, cycle_time=0.75)
        """
        if self.connection is None:
            raise RuntimeError("Vehicle not connected. Call .connect() first.")
    
        print(f"Repeating Servo {servo_number} to PWM {pwm} for {repeat_count} cycles with {cycle_time:.2f}s delay")
    
        self.connection.mav.command_long_send(
            self.connection.target_system,
            self.connection.target_component,
            mavutil.mavlink.MAV_CMD_DO_REPEAT_SERVO,
            0,                # Confirmation
            servo_number,     # param1: Servo number
            pwm,              # param2: Target PWM value
            repeat_count,     # param3: Number of repeat cycles
            cycle_time,       # param4: Delay in seconds
            0, 0, 0           # Unused
        )
        
    




###################################################

        
    def play_tune(self, tune: str, tune2: str = ""):
        """
        Play a custom tune through the flight controller's buzzer.

        :param tune: The main tune string (e.g., 'MFT240L8 O4aO5060708dc').
        :param tune2: Optional tune extension.
        
        fc.play_tune("L4CCGGAAG2FFEEDDC2")
        """
        if not self.connection or not self.connection.target_system:
            raise RuntimeError("Not connected to flight controller.")
        
        print(f"Playing tune: {tune}")
        self.connection.mav.play_tune_send(
            self.connection.target_system,
            self.connection.target_component,
            tune.encode("ascii"),
            tune2.encode("ascii") if tune2 else b""
        )
        
        


###########################


    # ------------ Mode, Arm/Disarm, RC override, Telemetry ---------------

    # Minimal mode map for ArduCopter (extend as needed or add Plane/Rover maps)
    _COPTER_MODE_MAP = {  # (unchanged)
        "STABILIZE": 0, "ACRO": 1, "ALT_HOLD": 2, "AUTO": 3, "GUIDED": 4, "LOITER": 5,
        "RTL": 6, "CIRCLE": 7, "LAND": 9, "DRIFT": 11, "SPORT": 13, "FLIP": 14,
        "AUTOTUNE": 15, "POSHOLD": 16, "BRAKE": 17, "THROW": 18, "AVOID_ADSB": 19,
        "GUIDED_NOGPS": 20, "SMART_RTL": 21, "FLOWHOLD": 22, "FOLLOW": 23, "ZIGZAG": 24,
        "SYSTEMID": 25, "AUTOROTATE": 26, "AUTO_RTL": 27,
    }

    _PLANE_MODE_MAP = {
        "MANUAL": 0, "CIRCLE": 1, "STABILIZE": 2, "TRAINING": 3, "ACRO": 4,
        "FBWA": 5, "FBWB": 6, "CRUISE": 7, "AUTOTUNE": 8, "AUTO": 10, "RTL": 11,
        "LOITER": 12, "TAKEOFF": 13, "AVOID_ADSB": 14, "GUIDED": 15, "INITIALIZING": 16,
        "QSTABILIZE": 17, "QHOVER": 18, "QLOITER": 19, "QLAND": 20, "QRTL": 21,
        "QAUTOTUNE": 22, "QACRO": 23, "THERMAL": 24
    }

    _ROVER_MODE_MAP = {
        "MANUAL": 0, "ACRO": 1, "LEARNING": 2, "STEERING": 3, "HOLD": 4, "LOITER": 5,
        "FOLLOW": 6, "SIMPLE": 7, "AUTO": 10, "RTL": 11, "SMART_RTL": 12, "GUIDED": 15,
        "INITIALIZING": 16
    }


    def _pick_mode_map(self):
        fam = self._family
        if fam == "plane":
            return self._PLANE_MODE_MAP, "plane"
        if fam == "rover":
            return self._ROVER_MODE_MAP, "rover"
        # default/fallback
        return self._COPTER_MODE_MAP, "copter"



    def _pick_mode_map_old0(self):
        # Use last seen HEARTBEAT to select the vehicle family automatically
        hb = self.connection.recv_match(type='HEARTBEAT', blocking=True, timeout=0.5)
        vtype = getattr(hb, 'type', None)
        if vtype in (mavutil.mavlink.MAV_TYPE_QUADROTOR, mavutil.mavlink.MAV_TYPE_HEXAROTOR,
                     mavutil.mavlink.MAV_TYPE_OCTOROTOR, mavutil.mavlink.MAV_TYPE_TRICOPTER,
                     mavutil.mavlink.MAV_TYPE_COAXIAL, mavutil.mavlink.MAV_TYPE_HELICOPTER):
            return self._COPTER_MODE_MAP, "copter"
        if vtype in (mavutil.mavlink.MAV_TYPE_FIXED_WING,):
            return self._PLANE_MODE_MAP, "plane"
        if vtype in (mavutil.mavlink.MAV_TYPE_GROUND_ROVER, mavutil.mavlink.MAV_TYPE_SURFACE_BOAT):
            return self._ROVER_MODE_MAP, "rover"
        # Default to copter if unknown
        return self._COPTER_MODE_MAP, "copter"

    def set_mode(self, mode_name: str, retries: int = 5, interval: float = 0.2, verbose: bool = True):
        if self.connection is None:
            raise RuntimeError("Not connected. Call .connect() first.")
        mode_name = mode_name.upper().strip()
        mode_map, family = self._pick_mode_map()
        if mode_name not in mode_map:
            raise ValueError(f"Unknown mode '{mode_name}' for {family}.")
        want = mode_map[mode_name]

        def current_custom_mode():
            hb = self.connection.recv_match(type='HEARTBEAT', blocking=True, timeout=0.3)
            return getattr(hb, 'custom_mode', None), getattr(hb, 'base_mode', None)

        # Fast path: already in desired mode
        cm, _ = current_custom_mode()
        if cm == want:
            if verbose: print(f"Already in {mode_name}")
            return True

        # Try SET_MODE a few times
        for i in range(retries):
            self.connection.mav.set_mode_send(
                self.connection.target_system,
                mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
                want
            )
            if verbose: print(f"[SET_MODE] -> {mode_name} (try {i+1}/{retries})")
            time.sleep(interval)
            cm, _ = current_custom_mode()
            if cm == want:
                if verbose: print(f"Mode changed to {mode_name} via SET_MODE")
                return True

        # Fallback: COMMAND_LONG (some stacks prefer this)
        for i in range(retries):
            self.connection.mav.command_long_send(
                self.connection.target_system,
                self.connection.target_component,
                mavutil.mavlink.MAV_CMD_DO_SET_MODE,
                0,
                mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,  # param1: base_mode flags
                want, 0, 0, 0, 0, 0
            )
            if verbose: print(f"[CMD_LONG:DO_SET_MODE] -> {mode_name} (try {i+1}/{retries})")
            time.sleep(interval)
            cm, _ = current_custom_mode()
            if cm == want:
                if verbose: print(f"Mode changed to {mode_name} via DO_SET_MODE")
                return True

        # Collect STATUSTEXTs to hint at the cause
        start = time.time()
        reasons = []
        while time.time() - start < 1.0:
            msg = self.connection.recv_match(type='STATUSTEXT', blocking=False)
            if msg:
                t = (msg.severity, getattr(msg, 'text', ''))
                reasons.append(t)
        if verbose:
            print(f"Failed to change mode to {mode_name}. Possible reasons:")
            print(" - RC FLTMODE_CH overriding; set FLTMODE_CH=0 or match TX switch")
            print(" - Mode prechecks failed (EKF/GPS/arm/state)")
            print(" - Vehicle type map mismatch")
            print(" - Link loss; try UDP or higher baud")
            if reasons:
                for sev, txt in reasons[-5:]:
                    print(f"  STATUSTEXT[{sev}]: {txt}")
        return False


    def set_mode_old0(self, mode_name: str, vehicle_family: str = "copter"):
        """
        Set flight mode (ArduPilot). Default mapping is for Copter.
        For Plane/Rover, provide a different map or extend this method.

        Example:
            fc.set_mode("GUIDED")
        """
        if self.connection is None:
            raise RuntimeError("Not connected. Call .connect() first.")

        mode_name = mode_name.upper().strip()

        if vehicle_family.lower() == "copter":
            mode_map = self._COPTER_MODE_MAP
        else:
            raise NotImplementedError("Only 'copter' mapping provided. Add Plane/Rover maps.")

        if mode_name not in mode_map:
            raise ValueError(f"Unknown mode '{mode_name}'. Known: {sorted(mode_map.keys())}")

        custom_mode = mode_map[mode_name]

        # Tell FC that custom_mode is valid, and send the numeric mode
        self.connection.mav.set_mode_send(
            self.connection.target_system,
            mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            custom_mode
        )
        print(f"Requested mode: {mode_name} ({custom_mode})")

    def arm(self, force: bool = False):
        """
        Arm motors via MAV_CMD_COMPONENT_ARM_DISARM.
        If arming checks prevent arming, set force=True to override (use with care).
        """
        if self.connection is None:
            raise RuntimeError("Not connected. Call .connect() first.")
        print("Arming motors...")
        self.connection.mav.command_long_send(
            self.connection.target_system,
            self.connection.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            1,              # 1 = arm, 0 = disarm
            0 if not force else 21196,  # magic force code for ArduPilot
            0, 0, 0, 0, 0
        )

    def disarm(self):
        """Disarm motors via MAV_CMD_COMPONENT_ARM_DISARM."""
        if self.connection is None:
            raise RuntimeError("Not connected. Call .connect() first.")
        print("Disarming motors...")
        self.connection.mav.command_long_send(
            self.connection.target_system,
            self.connection.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            0,  # disarm
            0, 0, 0, 0, 0, 0
        )

    # Keep simple state for RC overrides across channels 1..8 (MAVLink supports 8 per message)
    _rc_overrides = [65535]*8  # 65535 (UINT16_MAX) = no change

    def set_rc_pwm(self, channel: int, pwm: int):
        """
        Override an RC channel (1..8) with a PWM value (typically 1000-2000).
        Example:
            fc.set_rc_pwm(3, 1500)
        """
        if self.connection is None:
            raise RuntimeError("Not connected. Call .connect() first.")
        if not (1 <= channel <= 8):
            raise ValueError("RC override supports channels 1..8 in a single message.")
        if not (800 <= pwm <= 2200):
            raise ValueError("PWM should be in microseconds (approx 1000-2000).")

        print(f"RC override: ch{channel} = {pwm}")
        self._rc_overrides[channel-1] = int(pwm)
        self.connection.mav.rc_channels_override_send(
            self.connection.target_system,
            self.connection.target_component,
            *self._rc_overrides
        )

    def clear_rc_overrides(self):
        """
        Clear all RC overrides (set all to UINT16_MAX).
        """
        if self.connection is None:
            raise RuntimeError("Not connected. Call .connect() first.")
        print("Clearing RC overrides.")
        self._rc_overrides = [65535]*8
        self.connection.mav.rc_channels_override_send(
            self.connection.target_system,
            self.connection.target_component,
            *self._rc_overrides
        )
        
            
    def print_telemetry(self, timeout: float = 0.5):
        """
        Print a snapshot of basic telemetry (mode, GPS fix, location, battery, armed).
        Uses HEARTBEAT.type to choose the correct mode map (rover/plane/copter).
        """
        if self.connection is None:
            raise RuntimeError("Not connected. Call .connect() first.")
    
        # Grab latest common messages
        hb   = self.connection.recv_match(type='HEARTBEAT',         blocking=True,  timeout=timeout)
        gps  = self.connection.recv_match(type='GPS_RAW_INT',       blocking=False, timeout=timeout)
        gpos = self.connection.recv_match(type='GLOBAL_POSITION_INT', blocking=False, timeout=timeout)
        batt = self.connection.recv_match(type='SYS_STATUS',        blocking=False, timeout=timeout)
        
        inv = {v: k for k, v in (
            self._ROVER_MODE_MAP.items() if self._family == "rover" else
            self._PLANE_MODE_MAP.items() if self._family == "plane" else
            self._COPTER_MODE_MAP.items()
        )}

        
    
        # --- choose inverse mode map based on vehicle type ---
        #def _inverse_mode_map_from_hb(hb_msg):
         #   m = mavutil.mavlink
          #  vtype = getattr(hb_msg, 'type', None) if hb_msg else None
           # if vtype in (m.MAV_TYPE_GROUND_ROVER, m.MAV_TYPE_SURFACE_BOAT):
            #    return {v: k for k, v in self._ROVER_MODE_MAP.items()}
            #if vtype in (m.MAV_TYPE_FIXED_WING,):
           #     return {v: k for k, v in self._PLANE_MODE_MAP.items()}
            # Default/fallback to copter
            #return {v: k for k, v in self._COPTER_MODE_MAP.items()}
    
        #inv = _inverse_mode_map_from_hb(hb)
    
        # Mode (from HEARTBEAT.custom_mode)
        mode_num = getattr(hb, 'custom_mode', None) if hb else None
        mode_name = inv.get(mode_num, f"MODE#{mode_num}") if mode_num is not None else "Unknown"
    
        # Armed flag
        armed_flag = None
        if hb:
            armed_flag = bool(hb.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED)
    
        print(f"Mode: {mode_name}")
        print(f'Family: {self._family}')
        print(f"Armed: {armed_flag if armed_flag is not None else 'Unknown'}")
    
        # GPS
        if gps:
            print(f"GPS Fix: {gps.fix_type}  (0=no fix, 2=2D, 3=3D)")
        else:
            print("GPS Fix: (no recent GPS_RAW_INT)")
    
        # Position
        if gpos:
            lat = gpos.lat/1e7
            lon = gpos.lon/1e7
            alt = gpos.alt/1000.0
            print(f"Location: lat={lat:.7f}, lon={lon:.7f}, alt={alt:.2f} m")
        else:
            print("Location: (no recent GLOBAL_POSITION_INT)")
    
        # Battery
        if batt:
            vbat = batt.voltage_battery/1000.0 if batt.voltage_battery != 65535 else None
            batt_pct = batt.battery_remaining if batt.battery_remaining != 255 else None
            if vbat is not None and batt_pct is not None:
                print(f"Battery: {vbat:.2f} V, {batt_pct}%")
            elif vbat is not None:
                print(f"Battery: {vbat:.2f} V")
            elif batt_pct is not None:
                print(f"Battery: {batt_pct}%")
            else:
                print("Battery: (no recent SYS_STATUS voltage/percent)")
        else:
            print("Battery: (no recent SYS_STATUS)")

        

    def print_telemetry_old0(self, timeout: float = 0.5):
        """
        Print a snapshot of basic telemetry (mode, GPS fix, location, battery, armed).
        Relies on the latest messages seen on the link; waits briefly for fresh ones.
        """
        if self.connection is None:
            raise RuntimeError("Not connected. Call .connect() first.")

        # Try to fetch a few common messages
        hb = self.connection.recv_match(type='HEARTBEAT', blocking=True, timeout=timeout)
        gps = self.connection.recv_match(type='GPS_RAW_INT', blocking=False, timeout=timeout)
        gpos = self.connection.recv_match(type='GLOBAL_POSITION_INT', blocking=False, timeout=timeout)
        batt = self.connection.recv_match(type='SYS_STATUS', blocking=False, timeout=timeout)

        # Mode (from HEARTBEAT.custom_mode, using our map when possible)
        mode_num = getattr(hb, 'custom_mode', None) if hb else None
        mode_name = None
        if mode_num is not None:
            # Reverse-lookup for copter map
            inv = {v: k for k, v in self._COPTER_MODE_MAP.items()}
            mode_name = inv.get(mode_num, f"MODE#{mode_num}")
        armed_flag = None
        if hb:
            armed_flag = bool(hb.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED)

        print(f"Mode: {mode_name if mode_name else 'Unknown'}")
        if gps:
            print(f"GPS Fix: {gps.fix_type}  (0=no fix, 2=2D, 3=3D)")
        else:
            print("GPS Fix: (no recent GPS_RAW_INT)")
        if gpos:
            lat = gpos.lat/1e7
            lon = gpos.lon/1e7
            alt = gpos.alt/1000.0
            print(f"Location: lat={lat:.7f}, lon={lon:.7f}, alt={alt:.2f} m")
        else:
            print("Location: (no recent GLOBAL_POSITION_INT)")
        if batt:
            vbat = batt.voltage_battery/1000.0 if batt.voltage_battery != 65535 else None
            batt_pct = batt.battery_remaining if batt.battery_remaining != 255 else None
            print(f"Battery: {vbat:.2f} V, {batt_pct}%") if vbat is not None and batt_pct is not None else \
                print("Battery: (no recent SYS_STATUS voltage/percent)")
        else:
            print("Battery: (no recent SYS_STATUS)")
        print(f"Armed: {armed_flag if armed_flag is not None else 'Unknown'}")



##############################################################################
##############################################################################

#%%



# https://firmware.ardupilot.org/Tools/ToneTester/
class TonesQb:
    twinkle_little_star = "T200 L4CCGGAAG2FFEEDDC2"
    def_tone = "MFT240L8 O4aO5060708dc O4aO5dc O4aO5dc L16dcdcdcdc"


# -----------------------------------------------------------------------------
# Demo / Smoke-test block
#
# HOW TO USE:
#   - This section shows example calls against a connected ArduPilot FC.
#   - It is DISABLED by default via `if False:`. Change to `if True:` to run.
#
# SAFETY:
#   - Running these commands can ARM the vehicle, change flight modes,
#     move servos, and override RC channels. Props off, vehicle secured,
#     and use a simulator (SITL) if possible.
#   - Verify your connection string (serial/UDP/TCP) before enabling.
#
# ENVIRONMENT:
#   - For a simulator, you can use e.g. device='udp:127.0.0.1:14550'
#   - For serial Pixhawk, let auto-detect find it or set device='COMx' / '/dev/ttyUSBx'
#
# NOTE:
#   - `fc.print_info()` needs a prior `fc.connect()` to populate info.
#     If you call it before connect, it will print "No flight controller info available."
#   - Accessing `fc.connection.mav` requires `fc.connect()` first.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        # Auto-detects COM port if not provided; alternatively:
        # fc = FlightControllerInterface(device='udp:127.0.0.1:14550')
        fc = FlightControllerInterface()

        # Establish link before using fc.connection or printing info
        fc.connect()

        # After connect() we can safely query info
        fc.print_info()

        # Example mode changes and quick telemetry snapshots
        fc.set_mode("GUIDED")
        fc.print_telemetry()

        fc.set_mode("AUTO")
        fc.print_telemetry()

        fc.set_mode("MANUAL")  # for Plane; for Copter use STABILIZE/ALT_HOLD/etc.
        fc.print_telemetry()

        fc.set_mode("RTL")
        fc.print_telemetry()

        fc.set_mode("SMART_RTL")
        fc.print_telemetry()

        # Example direct servo outputs (AUX/Main as configured)
        # Syntax: set_servo(servo_number, pwm_microseconds)
        # - servo_number: which output to drive (1–16 depending on FC config/mixer)
        # - pwm: pulse width in microseconds; typical RC range is ~1000–2000 µs
        #   * ~1000 µs = minimum/low end-stop
        #   * ~1500 µs = neutral/center (for servos) or mid-throttle (for PWM throttle)
        #   * ~2000 µs = maximum/high end-stop
        
        fc.set_servo(9, 900)      # Output Pin 9 → ~900 µs, one direction max (below typical min; some setups use 900–2100 µs)
        time.sleep(2)             # Hold position for 2 seconds
        fc.set_servo(9, 1500)     # Output Pin 9 → 1500 µs (neutral/center)
        time.sleep(2)
        fc.set_servo(9, 1900)     # Output 9 → 1900 µs, other  direction max (near max)
        
        # Arm / RC override example (use with caution)
        fc.arm()                  # Arms the vehicle (will spin props on some frames)
        # Syntax: set_rc_pwm(channel, pwm_microseconds)
        # - channel: RC input channel index (1..8 in this method)
        #   * Common ArduCopter mapping (may vary by radio):
        #     ch1=Roll, ch2=Pitch, ch3=Throttle, ch4=Yaw, ch5+= flight modes/aux
        # - pwm: desired override value; 1500 µs is neutral for centered sticks
        fc.set_rc_pwm(3, 1500)    # Channel 3 (Throttle) → 1500 µs (mid-throttle for PWM-based throttle)
        time.sleep(2)
        fc.clear_rc_overrides()   # Stop overriding RC; returns control to pilot/FC
        
        # Repeat-servo example
        # Syntax: repeat_servo(servo_number, pwm, repeat_count, cycle_time)
        # - servo_number: which output to toggle
        # - pwm: target pulse width for the “active” position
        # - repeat_count: how many on/off cycles to perform
        # - cycle_time: seconds between movements (period for each toggle step)
        fc.set_servo(6, 1600)                 # Set output 6 to 1600 µs (slightly above center)
        fc.repeat_servo(7, 1900,              # Output 7 toggles to 1900 µs (near max) each cycle
                        repeat_count=3,       # Do 3 on/off cycles
                        cycle_time=0.5)       # 0.5 s delay between toggles (fast pulses)
        
        # Play tunes (buzzer)
        # TonesQb.def_tone and .twinkle_little_star are tone strings understood by ArduPilot buzzer
        fc.play_tune(TonesQb.def_tone)
        time.sleep(2)                         # Small gap between tunes
        fc.play_tune(TonesQb.twinkle_little_star)
        
        # Final telemetry snapshot (mode, GPS, pos, battery, armed flag)
        fc.print_telemetry()
        
        # Disarm and close link
        fc.disarm()
        fc.close()
        #_________________________________________________________
        
        
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Ensure we always close the connection if it was opened
        try:
            fc.close()
        except Exception:
            pass

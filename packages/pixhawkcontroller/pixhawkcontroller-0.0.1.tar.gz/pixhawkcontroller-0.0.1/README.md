# pixhawkcontroller

> Lightweight Python utilities to connect and control **Pixhawk / ArduPilot** flight controllers using [pymavlink](https://github.com/ArduPilot/pymavlink).

[![Build](https://github.com/Shahriar88/pixhawkcontroller/actions/workflows/python-package.yml/badge.svg)](https://github.com/Shahriar88/pixhawkcontroller/actions)
[![PyPI](https://img.shields.io/pypi/v/pixhawkcontroller.svg)](https://pypi.org/project/pixhawkcontroller/)
[![License](https://img.shields.io/badge/license-GPLv3-blue.svg)](LICENSE)
[![Python](https://img.shields.io/pypi/pyversions/pixhawkcontroller.svg)](https://www.python.org/)

---

## ✨ Features

- 🔌 **Auto-detect Pixhawk** on serial ports (Windows, Linux, macOS).
- 🌐 **Supports Serial, UDP, and TCP connections**:
  - `COMx` (Windows), `/dev/ttyUSBx` (Linux), `/dev/tty.usbmodem*` (macOS)
  - `udp:127.0.0.1:14550` for SITL
  - `tcp:192.168.1.100:5760` for network connections
- 🛠 **Servo control**: Set or repeat PWM outputs.
- 🎛 **RC channel override** with safety reset.
- 🎶 **Play tones** via the flight controller buzzer (e.g., Twinkle Twinkle, Mario tune).
- 📡 **Telemetry snapshot** (mode, GPS fix, battery, armed flag, location).
- 🛡 **Vehicle info decoding** (autopilot type, version, board, vendor/product IDs).
- 🚁 **Flight mode switching** (ArduCopter, ArduPlane, Rover supported).

---

## 📦 Installation

```bash
# Recommended: create a fresh virtual environment
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install from PyPI (when released)
pip install pixhawkcontroller

# OR install from source
git clone https://github.com/Shahriar88/pixhawkcontroller.git
cd pixhawkcontroller
pip install -e .
```

Dependencies:

* [pymavlink](https://github.com/ArduPilot/pymavlink) `>=2.4.41`
* [pyserial](https://pypi.org/project/pyserial/)

---

## 🚀 Quick Start

### 1. Import and connect

```python
from pixhawkcontroller import FlightControllerInterface, TonesQb

# Auto-detect Pixhawk (USB VID/PID known)
fc = FlightControllerInterface()
fc.connect()

# Or explicitly:
# fc = FlightControllerInterface(device='udp:127.0.0.1:14550')  # Connect to SITL (simulator)
# fc = FlightControllerInterface(device='COM3', baudrate=115200)  # Windows COM port
# fc = FlightControllerInterface(device='/dev/ttyUSB0', baudrate=115200)  # Linux USB port
```

### 2. Print flight controller info

```python
fc.print_info()
```

This prints firmware, board ID, MAVLink system ID, and more.

---

### 3. Control examples

```python
# Direct servo control:
# - First argument: servo output number (1–16 depending on config)
# - Second argument: PWM microseconds (typical RC range ~1000–2000 µs)
fc.set_servo(9, 1500)

# Repeat servo pulses:
# Toggle a servo output several times with a delay between movements
fc.repeat_servo(7, 1900, repeat_count=3, cycle_time=0.5)

# RC override (use carefully!):
# Temporarily override pilot’s RC input, e.g., throttle at mid-stick
fc.arm()
fc.set_rc_pwm(3, 1500)   # Channel 3 = throttle on many setups
fc.clear_rc_overrides()
fc.disarm()

# Play a tune on the buzzer
fc.play_tune(TonesQb.twinkle_little_star)

# Print a telemetry snapshot (mode, GPS, battery, location, armed state)
fc.print_telemetry()
```

---

### 4. Close connection

```python
fc.close()
```

Always close the MAVLink connection before exiting.

---

## 🎶 Tunes

This project uses **QBasic `PLAY`-style tone strings** (not RTTTL).  
They are directly compatible with the ArduPilot buzzer and can be tested using the official [ToneTester tool](https://firmware.ardupilot.org/Tools/ToneTester/).

Preloaded tunes in `TonesQb`:

```python
class TonesQb:
    twinkle_little_star = "T200 L4CCGGAAG2FFEEDDC2"
    def_tone = "MFT240L8 O4aO5060708dc O4aO5dc O4aO5dc L16dcdcdcdc"
```

👉 Explanation:
- `T200` → Tempo (200 quarter notes per minute)  
- `L4`   → Default note length (quarter notes)  
- `CCGGAAG2` → Sequence of notes (with octaves and lengths)  
- `MFT240`   → Music format / tempo modifier  
- `O4`, `O5` → Set octave (O4 = 4th octave, O5 = 5th)  
- Letters (`a`, `c`, `d`) represent notes; numbers modify duration  

---

### Adding Your Own Tunes

You can extend `TonesQb` or make your own class:

```python
class MyTunes:
    super_mario = (
        "T120 L8 O5 "
        "E6E6P32E6 L4C6E6G6 P G C6 P E A B L16A# A G."
    )
```

---

### Testing Tunes

Copy any string into the [ToneTester](https://firmware.ardupilot.org/Tools/ToneTester/) and press play to preview it on your PC before sending it to your Pixhawk.


---

## 🛡 Safety Notes

⚠️ **Important: Test first in SITL or with propellers removed.**

- Commands like `.arm()`, `.set_servo()`, and `.set_rc_pwm()` **can move motors/servos**.
- Always confirm your vehicle type and wiring before sending commands.
- To run ArduPilot in simulation:

  ```bash
  sim_vehicle.py -v ArduCopter -w --console --map
  ```

---

## 🧩 Project Structure

```
pixhawkcontroller/
├── __init__.py        # Exports FlightControllerInterface, TonesQb
├── main.py            # Core implementation
├── __version__.py    
setup.py
README.md
LICENSE
pyproject.toml
```

---

## 📂 Extended Example

Here’s a full demo script that shows multiple features in one go:

```python
import time
from pixhawkcontroller import FlightControllerInterface, TonesQb

fc = FlightControllerInterface()
fc.connect()

# Print board info
fc.print_info()

# Switch between flight modes (varies by vehicle type)
for mode in ["MANUAL","GUIDED", "AUTO", "RTL"]:
    fc.set_mode(mode)
	time.sleep(1)
    fc.print_telemetry()

# Servo control (PWM ranges)
fc.set_servo(9, 900)   # low end
time.sleep(2)
fc.set_servo(9, 1500)  # neutral
time.sleep(2)
fc.set_servo(9, 1900)  # high end

# RC override (channel 3 = throttle mid)
fc.arm()
fc.set_rc_pwm(3, 1500)
time.sleep(2)
fc.clear_rc_overrides()
fc.disarm()

# Play buzzer tunes
fc.play_tune(TonesQb.def_tone)
time.sleep(1)
fc.play_tune(TonesQb.twinkle_little_star)

# Telemetry snapshot
fc.print_telemetry()

# Clean up
fc.close()
```



---

## ✅ Requirements

- Python 3.8+ (tested on 3.9–3.12)
- ArduPilot firmware (Copter/Plane/Rover/Sub) speaking MAVLink
- Windows, Linux, or macOS with access to the Pixhawk serial device
- ✅ Verified working on **Pixhawk 2.4.8** hardware


---

## 🧪 Supported / Not Supported

- ✅ ArduPilot-based controllers (Pixhawk family) over Serial/UDP/TCP via `pymavlink`
- ❌ PX4 APIs (not targeted; may work for generic MAVLink pieces but not guaranteed)

---

## 🛠 Troubleshooting

**No device found / auto-detect fails**
- On Linux, ensure your user is in the `dialout` (or equivalent) group, then re-login:
  ```bash
  sudo usermod -aG dialout $USER


---

## 📚 References

* [ArduPilot MAVLink Commands](https://ardupilot.org/sub/docs/common-mavlink-mission-command-messages-mav_cmd.html)
* [MAVLink Message Definitions](https://mavlink.io/en/messages/common.html)
* [ToneTester Tool](https://firmware.ardupilot.org/Tools/ToneTester/)

---

## 🤝 Contributing

PRs and issues welcome!  
Open an [issue](https://github.com/Shahriar88/pixhawkcontroller/issues) if you spot a bug or want a feature.

---

## 📜 License

GPL-3.0-or-later © 2025 Md Shahriar Forhad  
See [LICENSE](LICENSE) for details.

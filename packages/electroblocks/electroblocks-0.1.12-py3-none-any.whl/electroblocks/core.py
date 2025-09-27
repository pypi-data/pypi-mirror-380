import serial
import serial.tools.list_ports
import time
from enum import Enum

class ComponentPins(Enum):
    UNKNOWN = 0
    LCD = 1
    RGBLED = 2
    DIGITAL_WRITE = 3
    ANALOG_WRITE = 4
    RGB_LED_STRIP = 5
    SERVO = 6

class ElectroBlocks:

    last_sense_data = ""
    verbose = False
    pins = {}

    def __init__(self, baudrate=115200, timeout=2, verbose = False):
        self.ser = self._auto_connect(baudrate, timeout)
        self.verbose = verbose
        self._wait_for_ready()
    
    def _auto_connect(self, baudrate, timeout):
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            if (p.vid == 9025 and p.pid in (67, 16)) or (p.vid == 6790): # Arduino Uno or Mega and Indian Arduino UNO
                try:
                    ser = serial.Serial(p.device, baudrate, timeout=timeout)
                    time.sleep(2)  # Give Arduino time to reset
                    return ser
                except serial.SerialException as e:
                    print(f"Failed to connect to {e}. Trying next port...")
                    continue
        raise Exception("No Arduino Uno or Mega found.")
    
    def _drain_serial(self):
        """Drains/clears the serial port input buffer of any unread messages."""
        if self.ser and self.ser.is_open:
            self.ser.reset_input_buffer()


    def _add_pin(self, pinType, pin):
        if pinType not in self.pins:
            self.pins[pinType] = [str(pin)]
        else:
            self.pins[pinType].append(str(pin))


    def _wait_for_message(self, message):
        count = 0
        while count < 10:
            if self.ser.in_waiting:
                line = self.ser.readline().decode("utf-8", errors="ignore").strip()
                if message in line:
                    return line
            count += 1
            time.sleep(0.05)
        if self.verbose:
            print(f"DEBUG: MESSAGE NOT FOUND: '{message}'")
        return ""

    def _get_sensor_str(self):
        self.ser.write(b"sense|")
        message = self._wait_for_message("SENSE_COMPLETE")
        if self.verbose:
            print(f"FULL SENSOR MESSSAGE: {message}")
        message = message.replace("SENSE_COMPLETE", "")
        sensorsStr = message.split(";")
        return sensorsStr
    
    # return the result of pin read that is being sensed
    def _find_sensor_str(self, sensorPin, sensorType):
        sensorsStr = self._get_sensor_str()
        for sensor in sensorsStr:
            if len(sensor) == 0:
                continue
            [type, pin, result] = sensor.split(":")
            if (type == sensorType and pin == str(sensorPin)):
                return result

        return ""

    def _wait_for_ready(self):
        self.ser.write(b"IAM_READY|")
        self._wait_for_message("System:READY")

    def _send(self, cmd):
        self.ser.write((cmd + "|\n").encode())
        self._wait_for_message("OK")

    # Digital Write Method
    def config_digital_read(self, pin):
        self._send(f"config:b={pin}")

    def digital_read(self, pin):
        return self._find_sensor_str(pin, "dr") == "1"
    
    # RFID
    def config_rfid(self, rxPin, txPin):
        self._send(f"config:rfid={rxPin},{txPin}")

    def rfid_tag_number(self):
        return self._find_sensor_str("0", "rfid")

    def rfid_sensed_card(self):
        return len(self._find_sensor_str("0", "rfid")) > 0
    
    #IR Remote

    def config_ir_remote(self, pin):
        self._send(f"config:ir={pin}")

    def ir_remote_has_sensed_code(self):
        return len(self._find_sensor_str("0", "ir")) > 0
    
    def ir_remote_get_code(self):
        return self._find_sensor_str("0", "ir")

    # Motion Sensors
    def config_motion_sensor(self, echoPin, trigPin):
        self._send(f"config:m={echoPin},{trigPin}")

    def motion_distance_cm(self):
        return self._find_sensor_str("0", "m")

    # Button Methods
    def config_button(self, pin):
        self._send(f"config:b={pin}")

    def is_button_pressed(self, pin):
        return self._find_sensor_str(pin, "b") == "0"

    # Servo Methods
    def config_servo(self, pin):
        self._send(f"register::servo::{pin}")

    def move_servo(self, pin, angle):
        self._send(f"write::servo::{pin}::{angle}")

    # RGB Methods
    def config_rgbled(self, r_pin, g_pin, b_pin):
        self._add_pin(ComponentPins.RGBLED, r_pin)
        self._add_pin(ComponentPins.RGBLED, g_pin)
        self._add_pin(ComponentPins.RGBLED, b_pin)
        self._send(f"register::rgb::{r_pin}::{g_pin}::{b_pin}")

    def set_color_rgbled(self, r, g, b):
        redpin = self.pins[ComponentPins.RGBLED][0]
        self._send(f"write::rgb::{redpin}::{r}::{g}::{b}")

    # LCD Methods
    def config_lcd(self, rows=2, cols=16, addr=39):
        self._add_pin(ComponentPins.DIGITAL_WRITE, "A5")
        self._add_pin(ComponentPins.DIGITAL_WRITE, "A4")
        self._send(f"register::lcd::{rows}::{cols}::{addr}")

    def lcd_print(self, row, col, message):
        self._send(f"write::lcd::A5::9::{row}::{col}::{message}")

    def lcd_clear(self):
        self._send("write::lcd::A5::1")

    def lcd_toggle_backlight(self, on):
        if on:
            self._send("write::lcd::A5::2")
        else:
            self._send("write::lcd::A5::3")

    def lcd_blink_curor(self, row, col, on):
        if on == True:
            self._send(f"write::lcd::A5::5::{row}::{col}")
        else:
            self._send(f"write::lcd::A5::4")

    def lcd_scrollright(self):
        self._send("write::lcd::A5::6")

    def lcd_scrollleft(self):
        self._send("write::lcd::A5::7")

    # LED Methods

    def digital_config(self, pin):
        self._add_pin(ComponentPins.DIGITAL_WRITE, pin)
        self._send(f"register::dw::{pin}")

    def digital_write(self, pin, value):
        self._send(f"write::dw::{pin}::{value}")

    def analog_write(self, pin, value):
        self._send(f"write::aw::{pin}::{value}")
    
    def analog_config(self, pin):
        self._send(f"register::aw::{pin}")
        self._add_pin(ComponentPins.ANALOG_WRITE, pin)

    # NEO PIXELS

    def config_rgb_strip(self, pin, count, colorOrderString, brightness):
        orderToNumber = {
            "RGB": 128,
            "GRB": 129,
            "RBG": 130,
            "GBR": 131,
            "BRG": 132,
            "BGR": 133,
        }
        colorOrder = orderToNumber.get(colorOrderString) or 128
        self._add_pin(ComponentPins.RGB_LED_STRIP, pin)
        self._send(f"register::leds::{pin}::{count}::{colorOrder}::{brightness}")


    def rgb_strip_set_color(self, position, red, green, blue):
        """Set color for RGB LED strip at specified position"""
        pin = self.pins[ComponentPins.RGB_LED_STRIP][0]
        color = self.rgb_to_hex(red, green, blue)
        self._send(f"write::leds::{pin}::2::{position}::{color}")

    def rgb_strip_show_all(self):
        pin = self.pins[ComponentPins.RGB_LED_STRIP][0]
        self._send(f"write::leds::{pin}::1")

    # Helpers

    def rgb_to_hex(self, red, green, blue):
        """
        Convert RGB values (0-255) to a hex color string format (#RRGGBB)
        
        Args:
            red (int): Red value (0-255)
            green (int): Green value (0-255)  
            blue (int): Blue value (0-255)
            
        Returns:
            str: Hex color string in format RRGGBB
        """
        # Ensure values are within valid range (0-255)
        red = max(0, min(255, int(red)))
        green = max(0, min(255, int(green)))
        blue = max(0, min(255, int(blue)))
        
        # Convert to hex and format with leading zeros if needed
        return f"{red:02x}{green:02x}{blue:02x}".upper()


    def close(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
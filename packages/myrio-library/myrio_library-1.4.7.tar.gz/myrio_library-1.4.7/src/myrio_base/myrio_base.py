"""myRIO_library - a library for working with NI myRIO in Python

This library is an improvement over nifpga, a Python library that
gives access to the FPGA registers of NI targets with FPGA.

In this library, we have created some support functions and a class
named MyRIO.
"""

from nifpga import Session
from typing import Tuple, List
from time import sleep
import ctypes
import pkg_resources


# RGB constants: 1.4.1 added new colors and aliases

GREEN = G = 1
RED = R = 2
YELLOW = Y = 3
BLUE = B = 4
CYAN = C = 5
MAGENTA = M = 6
WHITE = W = 7
RGB_OFF = OFF = BLACK = 0

# Support functions. They are not part of the class MyRIO, but they are used by it.
# Feel free to use them in your own programs.


def u8_to_bits(u8_number: int) -> List[bool]:
    """This function converts u8 values to an array of Booleans"""
    if u8_number < 0 or u8_number > 255:
        raise ValueError("Input number must be in the range 0-255")
    mask = 1
    one_by_one = []
    for i in range(8):
        one_by_one.append(bool((u8_number & mask) != 0))
        mask = mask * 2
    return one_by_one


def only_one_bit_on(bit_number: int, input_number: int = 0) -> int:
    """This function sets the specified bit in a u8 integer, leaving other bits unchanged."""
    if bit_number < 0 or bit_number > 7:
        raise ValueError("Input bit number must be in the range 0-7")
    u8_number = 0
    u8_number = 1 << bit_number
    return input_number | u8_number


def only_one_bit_off(bit_number: int, input_number: int = 0) -> int:
    """This function clears (sets to 0) the specified bit in a u8 integer, leaving other bits unchanged."""
    if bit_number < 0 or bit_number > 7:
        raise ValueError("Input bit number must be in the range 0-7")
    mask = 0xFF ^ (1 << bit_number)
    return input_number & mask



def raw_to_volts_AB(raw: int) -> float:
    """This function converts the raw value
    from myRIO MXP (ports A and B) Analog Input channels to volts
    """

    return raw * 0.001220703


def raw_to_volts_C(raw: int) -> float:
    """This function converts the raw value
    from myRIO MSP (port C) Analog Input channels to volts
    """

    return raw * 0.004882813


def raw_to_volts_audio(raw: int) -> float:
    """This function converts the raw value
    from myRIO Audio Input channels to volts
    """

    return raw * 0.001220703


def volts_to_raw_AB(volts: float) -> int:
    """This function converts values in Volts
    to raw values for myRIO MXP (ports A and B) Analog Output channels
    """

    return int(volts / 0.001220703)


def volts_to_raw_C(volts: float) -> int:
    """This function converts values in Volts
    to raw values for myRIO MSP (port C) Analog Output channels
    """

    signed_value = int(volts / 0.004882813)
    unsigned_value = ctypes.c_uint16(signed_value).value
    return unsigned_value


def volts_to_raw_audio(volts: float) -> int:
    """This function converts values in Volts
    to raw values for Audio Output channels
    """

    signed_value = int(volts / 0.001220703)
    unsigned_value = ctypes.c_uint16(signed_value).value
    return unsigned_value


def volts_to_temperature(volts: float) -> float:
    """This function converts values in Volts
    to temperature in Celsius degrees
    """

    return ((volts - 1.7) * 10 / -0.3) + 20


def volts_to_luminosity(volts: float) -> float:
    """This function converts values in Volts
    to luminosity in percentage (0-100%)
    """

    return 100 - (volts * 30.3)


def extract_waveform_from_csv_file(file_name: str) -> List[int]:
    """This function extracts a stereo waveform from a .csv file
    and returns it as a list of I16 integers.
    The .csv format is very basic for an audio file, but
    the myRIO has memory limitations, so the audio files
    must be mono and quite shorts.
    We have tried the wave library from Python, but it does not work
    properly with the myRIO, so we have used the csv format that
    can be easily generated. We used a simple LabVIEW program for that. 
    You can find the source code in the examples folder (myRIOAudioFile.zip).
    """

    # Open and read a csv file
    with open(file_name, "r") as file:
        data = file.readlines()  # Read all the lines of the file
        waveform = []  # Create an empty list for the waveform
        for line in data:  # Read line by line
            waveform.append(
                volts_to_raw_audio(float(line))
            )  # Append the integer value to the list

    return waveform  # Return the list


class MyRIO:
    """Class MyRIO: class for accessing NI myRIO inputs and outputs using nifgpa

    NI myRIO is a programmable device with digital and analog inputs and outputs.
    It is usually programmed in LabVIEW, but it can be programmed in Python too.
    """

    __session = None

    def __init__(self, session_bitfile="", session_resource="RIO0"):
        """when an instance is created, an nifpga session is created."""
        if session_bitfile == "":
            session_bitfile = pkg_resources.resource_filename(
                "myrio_base", "data/Default.lvbitx"
            )

        self.__session = Session(session_bitfile, session_resource)
        sys_handler = self.__session.registers["SYS.RDY"]

        timeout = 0
        while not sys_handler.read():
            sleep(0.1)
            timeout += 1
            if timeout > 1000:  # 100 seconds timeout
                raise TimeoutError("System not ready after 100 seconds")

    def check_if_ready(self) -> bool:
        """checks if system is ready"""
        sys_handler = self.__session.registers["SYS.RDY"]
        return sys_handler.read()

    def __del__(self):
        """This function closes the session with the myRIO FPGA"""
        self.__session.close()

    def set_DIO_mask(self, mask_low: int = 7, mask_high: int = 0, port: str = "A"):
        """sets the DIO mask for defining the direction (IN/OUT) of the channels
        low 7, high 0 is the default for the design of our current MXP cards
        """

        dir_string_low = "DIO." + port + "_" + "7:0" + ".DIR"
        dir_string_high = "DIO." + port + "_" + "15:8" + ".DIR"
        mask_handler_low = self.__session.registers[dir_string_low]
        mask_handler_high = self.__session.registers[dir_string_high]
        mask_handler_low.write(mask_low)  # 7 is 00000111 where 1 is OUT
        mask_handler_high.write(mask_high)  # 0 is 00000000 where 0 is IN

    def update_DIO_mask(self, channel: int, is_output: bool, port: str = "A"):
        """Updates the current DIO mask to change the behaviour of one channel"""
        dir_string_low = "DIO." + port + "_" + "7:0" + ".DIR"
        dir_string_high = "DIO." + port + "_" + "15:8" + ".DIR"
        mask_handler_low = self.__session.registers[dir_string_low]
        mask_handler_high = self.__session.registers[dir_string_high]
        current_dio_mask_low = mask_handler_low.read()
        current_dio_mask_high = mask_handler_high.read()

        if is_output:  # change channel direction to output
            if channel < 8:
                new_dio_mask_low = only_one_bit_on(channel, current_dio_mask_low)
                mask_handler_low.write(new_dio_mask_low)
            else:
                new_dio_mask_high = only_one_bit_on(channel - 8, current_dio_mask_high)
                mask_handler_high.write(new_dio_mask_high)
        else:
            if channel < 8:
                new_dio_mask_low = only_one_bit_off(channel, current_dio_mask_low)
                mask_handler_low.write(new_dio_mask_low)
            else:
                new_dio_mask_high = only_one_bit_off(channel - 8, current_dio_mask_high)
                mask_handler_high.write(new_dio_mask_high)

    def read_analog_input(self, channel: int, port: str = "A") -> float:
        """returns the value in volts of one of the AI channels (default port: A)"""
        channel_string = "AI." + port + "_" + str(channel) + ".VAL"
        channel_handler = self.__session.registers[channel_string]
        if port == "A" or port == "B":
            return raw_to_volts_AB(channel_handler.read())
        elif port == "C":
            return raw_to_volts_C(channel_handler.read())
        elif port == "AudioIn_L" or port == "AudioIn_R":
            return raw_to_volts_audio(channel_handler.read())
        else:
            raise ValueError("Port name error: correct values are A, B, C, AudioIn_L, or AudioIn_R")

    def read_MXP_temperature(self, channel: int = 0, port: str = "A") -> float:
        """returns the temperature in Celsius degrees of an NTC sensor connected to one of the
        AI channels (default channel:0, default port: A)
        """

        channel_string = "AI." + port + "_" + str(channel) + ".VAL"
        channel_handler = self.__session.registers[channel_string]
        if port == "A" or port == "B":
            return volts_to_temperature(raw_to_volts_AB(channel_handler.read()))
        else:
            raise ValueError("Port name error: correct values are A or B")

    def read_MXP_luminosity(self, channel: int = 1, port: str = "A") -> float:
        """returns the luminosity in percentage of an LDR sensor connected to one of the
        AI channels (default channel:1, default port: A)
        """

        channel_string = "AI." + port + "_" + str(channel) + ".VAL"
        channel_handler = self.__session.registers[channel_string]
        if port == "A" or port == "B":
            return volts_to_luminosity(raw_to_volts_AB(channel_handler.read()))
        else:
            raise ValueError("Port name error: correct values are A or B")

    def read_digital_input(self, channel: int, port: str = "A") -> bool:
        """returns the Boolean value of one of the DIO input channels (default port: A)"""

        if port != "A" and port != "B" and port != "C":
            raise ValueError("Port name error: correct values are A, B, or C")
        if channel < 0 or channel > 15:
            raise ValueError("Channel number error: correct values are 0-15")
        
        # First, check if the function is asking for a channel
        # in the low byte (7:0) or in the high byte (15:8)
        if channel < 8:
            channel_string = "DIO." + port + "_7:0.IN"
            array_index = int(channel)
        else:
            channel_string = "DIO." + port + "_15:8.IN"
            # The length of the array is 8, so the index should be in the 7:0 range
            array_index = channel - 8

        channel_handler = self.__session.registers[channel_string]
        raw_value = channel_handler.read()
        bool_array = u8_to_bits(raw_value)
        return bool_array[array_index]


    def read_digital_port(self, port: str = "A") -> List[bool]:
        """returns the Boolean values of the whole port (default port: A)"""

        if port == "A" or port == "B" or port == "C":

            channel_string_low = "DIO." + port + "_7:0.IN"
            channel_string_high = "DIO." + port + "_15:8.IN"
            channel_handler_low = self.__session.registers[channel_string_low]
            channel_handler_high = self.__session.registers[channel_string_high]
            raw_value_low = channel_handler_low.read()
            raw_value_high = channel_handler_high.read()
            bool_array = u8_to_bits(raw_value_low) + u8_to_bits(raw_value_high)
            return bool_array
        else:
            raise ValueError("Port name error: correct values are A, B, or C")

    def read_MXP_button(self, button: int = 1, port: str = "A") -> bool:
        """returns the Boolean value of one of the MXP buttons that are mounted
        on the MXP card (default port: A) We expect 1 for the first button, 
        and 2 for the second one.
        Most of our cards have a black button first, a white button second.
        """

        if port == "A" or port == "B":
            if button == 1 or button == 2:
                channel_string = "DIO." + port + "_7:0.IN"
                array_index = int(button + 2)
                channel_handler = self.__session.registers[channel_string]
                raw_value = channel_handler.read()
                bool_array = u8_to_bits(raw_value)
                return bool_array[array_index]
            else:
                raise ValueError("Button number error: correct values are 1 (black) or 2 (white)")
        else:
            raise ValueError("Port name error: correct values are A or B")

    def read_button(self) -> bool:
        """returns the Boolean value of the myRIO onboard button"""
        channel_string = "DI.BTN"
        channel_handler = self.__session.registers[channel_string]
        raw_value = channel_handler.read()
        return bool(raw_value)
    
    read_onboard_button = read_button  # alias for simplicity

    def read_analog_accelerometer(self) -> Tuple[float, float, float]:
        """returns the x, y, and z values in Gs of the onboard Accelerometer"""
        channel_string_x = "ACC.X.VAL"
        channel_string_y = "ACC.Y.VAL"
        channel_string_z = "ACC.Z.VAL"
        channel_handler_x = self.__session.registers[channel_string_x]
        channel_handler_y = self.__session.registers[channel_string_y]
        channel_handler_z = self.__session.registers[channel_string_z]
        raw_value_x = channel_handler_x.read()
        raw_value_y = channel_handler_y.read()
        raw_value_z = channel_handler_z.read()

        if raw_value_x & (1 << 15):
            # Perform two's complement conversion for negative numbers
            raw_value_x = raw_value_x - (1 << 16)
        x_value = float(raw_value_x) / 256.0

        if raw_value_y & (1 << 15):
            # Perform two's complement conversion for negative numbers
            raw_value_y = raw_value_y - (1 << 16)
        y_value = float(raw_value_y) / 256.0

        if raw_value_z & (1 << 15):
            # Perform two's complement conversion for negative numbers
            raw_value_z = raw_value_z - (1 << 16)
        z_value = float(raw_value_z) / 256.0

        return x_value, y_value, z_value

    read_onboard_accelerometer = read_analog_accelerometer  # alias for simplicity
    read_accelerometer = read_analog_accelerometer  # alias for simplicity

    def write_leds_integer(self, raw_value: int):
        """changes the state of the myRIO onboard LEDs using an integer value"""

        if raw_value < 0 or raw_value > 15:
            raise ValueError("Input number must be in the range 0-15")
        else:
            channel_string = "DO.LED3:0"
            channel_handler = self.__session.registers[channel_string]
            channel_handler.write(raw_value)

    write_onboard_leds_integer = write_leds_integer  # alias for simplicity

    def write_leds_booleans(self, boolean_values: List[bool]):
        """changes the state of the myRIO onboard LEDs using Booleans"""

        raw_value = 0
        j = 1
        for i in range(4):
            raw_value = raw_value + boolean_values[i] * j
            j = j * 2

        channel_string = "DO.LED3:0"
        channel_handler = self.__session.registers[channel_string]
        channel_handler.write(raw_value)
    
    write_onboard_leds_booleans = write_leds_booleans  # alias for simplicity

    def write_led(self, led_number: int, value: bool):
        """changes the state of one of the myRIO onboard LEDs using a Boolean value"""

        if led_number < 0 or led_number > 3:
            raise ValueError("LED number must be in the range 0-3")
        else:
            channel_string = "DO.LED3:0"
            channel_handler = self.__session.registers[channel_string]
            raw_value = channel_handler.read()
            if value:
                new_value = only_one_bit_on(led_number, raw_value)
            else:
                new_value = only_one_bit_off(led_number, raw_value)
            channel_handler.write(new_value)

    write_onboard_led = write_led  # alias for simplicity
    write_only_one_led = write_led  # alias for simplicity

    def write_digital_output(
        self,
        channel: int,
        value: bool,
        port: str = "A",
        mask_low: int = 7,
        mask_high: int = 0,
    ):
        """writes a Boolean value on one of the DIO output channels (default port: A)
        The defaults are set for the design of our current MXP cards:
        RGB LEDs at channels 0,1,2 (G,R,B) and buttons at channels 3,4. Rest unused.
        """

        if port != "A" and port != "B" and port != "C":
            raise ValueError("Port name error: correct values are A, B, or C")
        if channel < 0 or channel > 15:
            raise ValueError("Channel number error: correct values are 0-15")
        
        self.set_DIO_mask(port=port, mask_low=mask_low, mask_high=mask_high)

        # Check if the function is asking for a channel
        # in the low byte (7:0) or in the high byte (15:8)
        if 0 <= channel <= 7:
            channel_string = "DIO." + port + "_7:0.OUT"
            mask_string = "DIO." + port + "_7:0.DIR"
        elif 8 <= channel <= 15:
            channel_string = "DIO." + port + "_15:8.OUT"
            mask_string = "DIO." + port + "_15:8.DIR"
            channel = channel - 8

        mask_handler = self.__session.registers[mask_string]
        saved_mask = mask_handler.read()
        new_mask = only_one_bit_on(channel, saved_mask)
        mask_handler.write(new_mask)

        channel_handler = self.__session.registers[channel_string]
        saved_value = channel_handler.read()

        if value:
            value_to_be_written = only_one_bit_on(channel, saved_value)
        else:
            value_to_be_written = only_one_bit_off(channel, saved_value)

        channel_handler.write(value_to_be_written)

        mask_handler.write(saved_mask)  # restore original DIR mask

    def write_digital_port(
        self,
        value_low: int,
        value_high: int = 255,
        port: str = "A",
        mask_low: int = 7,
        mask_high: int = 0,
    ):
        """writes integer low and high values on DIO output channels (default port: A)
        The defaults are set for the design of our current MXP cards:
        RGB LEDs at channels 0,1,2 (G,R,B) and buttons at channels 3,4. Rest unused.
        """

        if port != "A" and port != "B" and port != "C":
            raise ValueError("Port name error: correct values are A, B, or C")

        self.set_DIO_mask(port=port, mask_low=mask_low, mask_high=mask_high)

        channel_string_low = "DIO." + port + "_7:0.OUT"
        channel_string_high = "DIO." + port + "_15:8.OUT"
        channel_handler_low = self.__session.registers[channel_string_low]
        channel_handler_high = self.__session.registers[channel_string_high]
        channel_handler_low.write(value_low)
        channel_handler_high.write(value_high)

    def write_MXP_RGB_LED(self, color: int, port: str = "A"):
        """writes a three-bit color on the myRIO MXP RGB LED (default port: A)"""
        if port != "A" and port != "B":
            raise ValueError("Port name error: correct values are A, or B")
        if color < 0 or color > 7:
            raise ValueError("Color value error: correct values are 0-7 (OFF, G, R, Y, B, C, M, W)")

        self.set_DIO_mask(port=port)  # default mask is OK for the RGB LED
        channel_string_low = "DIO." + port + "_7:0.OUT"
        channel_handler_low = self.__session.registers[channel_string_low]
        channel_handler_low.write(color)

    write_RGB = write_MXP_RGB_LED  # alias for simplicity

    def write_only_one_MXP_LED(self, led_color: int, value: bool, port: str = "A"):
        """writes a Boolean value on one of the myRIO MXP RGB LED channels (default port: A)
        led_color: 1 for Green, 2 for Red, 4 for Blue.
        The other combinations are not allowed in this function.
        """

        if port != "A" and port != "B":
            raise ValueError("Port name error: correct values are A, or B")
        if led_color != 1 and led_color != 2 and led_color != 4:
            raise ValueError("LED color error: correct values are 1 (G), 2 (R), or 4 (B)")
  
        self.set_DIO_mask(port=port)  # default mask is OK for the RGB LED
        channel_string_low = "DIO." + port + "_7:0.OUT"
        channel_handler_low = self.__session.registers[channel_string_low]
        saved_value = channel_handler_low.read()

        if led_color == 1: # Green
            channel = 0
        elif led_color == 2: # Red
            channel = 1
        elif led_color == 4: # Blue
            channel = 2

        if value:
            new_value = only_one_bit_on(channel, saved_value)
        else:
            new_value = only_one_bit_off(channel, saved_value)

        channel_handler_low.write(new_value)

    def write_analog_output(self, channel: int, value: float, port: str = "A"):
        """writes a value (in volts) on an AO channel (default port: A)"""
        if port != "A" and port != "B" and port != "C" and port != "AudioOut_L" and port != "AudioOut_R":
            raise ValueError("Port name error: correct values are A, B, C, AudioOut_L, or AudioOut_R")
        if channel < 0 or channel > 15:
            raise ValueError("Channel number error: correct values are 0-15")
        
        channel_string = "AO." + port + "_" + str(channel) + ".VAL"
        channel_handler = self.__session.registers[channel_string]
        if port == "A" or port == "B":
            raw_value = volts_to_raw_AB(value)
        elif port == "C":
            raw_value = volts_to_raw_C(value)
        elif port == "AudioOut_L" or port == "AudioOut_R":
            raw_value = volts_to_raw_audio(value)
        
        channel_handler.write(raw_value)
        go_handler = self.__session.registers["AO.SYS.GO"]
        go_handler.write(True)

    def read_audio_input(self, channel: str = "L") -> float:
        """returns the value in volts of one of the Audio Input channels"""
        if channel == "L" or channel == "R":
            channel_string = "AI.AudioIn_" + str(channel) + ".VAL"
        else:
            raise ValueError("Channel name error: correct values are L or R")

        channel_handler = self.__session.registers[channel_string]
        return raw_to_volts_audio(channel_handler.read())

    def write_audio_output(self, value: float, channel: str = "L"):
        """writes a value (in volts) on an Audio Output channel"""
        if channel == "L" or channel == "R":
            channel_string = "AO.AudioOut_" + str(channel) + ".VAL"
        else:
            raise ValueError("Channel name error: correct values are L or R")

        channel_handler = self.__session.registers[channel_string]
        raw_value = volts_to_raw_audio(value)
        channel_handler.write(raw_value)
        go_handler = self.__session.registers["AO.SYS.GO"]
        go_handler.write(True)

    def play_waveform(self, waveform: List[int]):
        """plays a waveform on the myRIO Audio Output channels"""

        channel_string_left = "AO.AudioOut_L.VAL"
        channel_string_right = "AO.AudioOut_R.VAL"
        channel_handler_left = self.__session.registers[channel_string_left]
        channel_handler_right = self.__session.registers[channel_string_right]

        go_handler = self.__session.registers["AO.SYS.GO"]

        for i in range(len(waveform)):
            channel_handler_left.write(waveform[i])
            channel_handler_right.write(waveform[i])
            go_handler.write(True)

    def read_audio_input_noise_level(self) -> float:
        """returns the noise level % of the Audio Input channels"""
        window_size = 100
        max_volts = 2.5

        channel_string_L = "AI.AudioIn_L.VAL"
        channel_string_R = "AI.AudioIn_R.VAL"

        channel_handler_L = self.__session.registers[channel_string_L]
        channel_handler_R = self.__session.registers[channel_string_R]

        noise_level_sum = 0.0
        for i in range(window_size):
            volume_L = raw_to_volts_audio(channel_handler_L.read())
            volume_R = raw_to_volts_audio(channel_handler_R.read())
            noise_level_sum += abs(volume_L) + abs(volume_R)

        mean_value = noise_level_sum / (2 * window_size)
        return mean_value * 100.0 / max_volts

    def config_PWM_output(
        self, channel: int, frequency: float = 2000.0, port: str = "A"
    ) -> int:
        """configs a PWM output to work with a certain frequency (default port: A)
        The frequency should be expressed in Hz (default 2000 Hz).
        The range of frequency is 40Hz-40KHz
        Returns X (the value of the MAX register)
        """

        if port != "A" and port != "B":
            raise ValueError("Port name error: correct values are A or B")
        if channel < 0 or channel > 7:
            raise ValueError("Channel number error: correct values are 0-7")
            
        BASE_FREQUENCY = 40000000.0

        if (frequency < 40.0) or (frequency > 40000.0):
            raise ValueError("Frequency out of range (40Hz-40KHz)")
        elif frequency < 80.0:
            divider_N = 16
            divider_code = 5
        elif frequency < 160.0:
            divider_N = 8
            divider_code = 4
        elif frequency < 320.0:
            divider_N = 4
            divider_code = 3
        elif frequency < 800.0:
            divider_N = 2
            divider_code = 2
        else:
            divider_N = 1
            divider_code = 1

        max_value_X = int((BASE_FREQUENCY / frequency) / divider_N) - 1

        self.update_DIO_mask(channel=8, is_output=True, port="B")
        self.update_DIO_mask(channel=9, is_output=True, port="B")
        self.update_DIO_mask(channel=10, is_output=True, port="B")

        channel_string_sys = "SYS.SELECT" + port
        channel_handler_sys = self.__session.registers[channel_string_sys]
        current_value = channel_handler_sys.read()
        new_value = only_one_bit_on(bit_number=channel + 2, input_number=current_value)
        channel_handler_sys.write(new_value)

        channel_string_cnfg = "PWM." + port + "_" + str(channel) + ".CNFG"
        channel_handler_cnfg = self.__session.registers[channel_string_cnfg]
        channel_handler_cnfg.write(4)

        channel_string_cs = "PWM." + port + "_" + str(channel) + ".CS"
        channel_handler_cs = self.__session.registers[channel_string_cs]
        channel_handler_cs.write(divider_code)

        channel_string_max = "PWM." + port + "_" + str(channel) + ".MAX"
        channel_handler_max = self.__session.registers[channel_string_max]
        channel_handler_max.write(max_value_X)
        return max_value_X

    def write_PWM_output(
        self, channel: int, duty_cycle: float, X: int = 19999, port: str = "A"
    ):
        """writes a duty cycle value (in percentage) on a PWM channel (default port: A)"""

        if port != "A" and port != "B":
            raise ValueError("Port name error: correct values are A or B")
        if channel < 0 or channel > 7:
            raise ValueError("Channel number error: correct values are 0-7")
        if (duty_cycle < 0.0) or (duty_cycle > 100.0):
            raise ValueError("Duty cycle out of range (0.0-100.0)")
      
        duty_cycle_code = int(
            (duty_cycle / 100) * (X + 1)
        )  # X is the MAX value of the PWM counter

        channel_string_cmp = "PWM." + port + "_" + str(channel) + ".CMP"
        channel_handler_cmp = self.__session.registers[channel_string_cmp]
        channel_handler_cmp.write(duty_cycle_code)

    def display_color_PWM(self, R: int = 0, G: int = 0, B: int = 0, port: str = "A"):
        """This is not a generic function, it is only an example.
        It uses the PWM channels to control the RGB LED display we have on our MXP cards.
        The frequencies of each channel and the resistors
        used in the circuit are specific for each RGB LED display.
        In our case, the RGB LED display is connected to
        channels 0,1,2 (G,R,B). Since PWM channels are mapped to different channels,
        we have to connect PWM0 to the RED pin, PWM1 to the GREEN pin,
        and PWM2 to the BLUE pin of the RGB LED display. Doing so, we must configure
        channels 0 to 2 as inputs. This is done by setting the DIO mask to 00011111 (31).
        The color values should be in the range 0-255.
        """

        if port != "A" and port != "B":
            raise ValueError("Port name error: correct values are A or B")
        if (R < 0) or (R > 255) or (G < 0) or (G > 255) or (B < 0) or (B > 255):
            raise ValueError("Color value error: correct values are 0-255")
        
        self.set_DIO_mask(mask_low=31, mask_high=0, port=port) # 00011111 = 31

        duty_cycle_R = int(R * 100 / 256)
        duty_cycle_G = int(G * 100 / 256)
        duty_cycle_B = int(B * 100 / 256)

        X_0 = self.config_PWM_output(channel=0, frequency=5000.0, port=port)
        X_1 = self.config_PWM_output(channel=1, port=port)
        X_2 = self.config_PWM_output(channel=2, port=port)
        self.write_PWM_output(channel=0, duty_cycle=duty_cycle_R, X=X_0, port=port)
        self.write_PWM_output(channel=1, duty_cycle=duty_cycle_G, X=X_1, port=port)
        self.write_PWM_output(channel=2, duty_cycle=duty_cycle_B, X=X_2, port=port)


if __name__ == "__main__":
    print("This is a library for working with NI myRIO in Python")
    print(
        "It is not intended to be run directly, but to be imported in other programs."
    )
    print("Please, see the documentation for more information.")
    from time import sleep

    myrio1 = MyRIO()

    print("Read digital port A:")
    print(myrio1.read_digital_port(port="A"))
    print("Read temperature from MXP port A, channel 0:")
    print(myrio1.read_MXP_temperature())
    print("Read luminosity from MXP port A, channel 1:")
    print(myrio1.read_MXP_luminosity())
    print("RGB LED in MXP port A: RED")
    myrio1.write_MXP_RGB_LED(RED)
    sleep(1)
    print("RGB LED in MXP port A: GREEN")
    myrio1.write_MXP_RGB_LED(GREEN)
    sleep(1)
    print("RGB LED in MXP port A: BLUE")
    myrio1.write_MXP_RGB_LED(BLUE)
    sleep(1)
    print("RGB LED in MXP port A: OFF")
    myrio1.write_MXP_RGB_LED(RGB_OFF)

    # Play a simple waveform using raw data
    print("Playing a simple waveform")
    csv_file = pkg_resources.resource_filename("myrio_base", "examples/PacManDeath.csv")
    my_waveform = extract_waveform_from_csv_file(csv_file)
    myrio1.play_waveform(my_waveform)

    # Get the noise level of the Audio Input channels
    print("Noise level of the Audio Input channels:")
    print(myrio1.read_audio_input_noise_level())

    # Test the PWM outputs
    print("PWM output test (port B: PWM0, PWM1, PWM2):")
    print("Configuring...")
    X_0 = myrio1.config_PWM_output(channel=0, frequency=5000.0, port="B")
    X_1 = myrio1.config_PWM_output(channel=1, port="B")
    X_2 = myrio1.config_PWM_output(channel=2, port="B")

    print("10% 45% 11,5%")
    myrio1.write_PWM_output(channel=0, duty_cycle=10, X=X_0, port="B")
    myrio1.write_PWM_output(channel=1, duty_cycle=45, X=X_1, port="B")
    myrio1.write_PWM_output(channel=2, duty_cycle=11.5, X=X_2, port="B")
    sleep(2)

    print("0% 0% 0%")
    myrio1.write_PWM_output(channel=0, duty_cycle=0.0, port="B")
    myrio1.write_PWM_output(channel=1, duty_cycle=0.0, port="B")
    myrio1.write_PWM_output(channel=2, duty_cycle=0.0, port="B")

    print("Display RGB color orange (252, 161, 3):")
    myrio1.display_color_PWM(252, 161, 3)
    sleep(10)
    myrio1.display_color_PWM(0, 0, 0)


""" TODO

There are some extra features that we do not cover.
They are interesting, but are not so commonly used, and given
their complexity, we leave them for future development.
The features we did not cover are:
1.-ENC
2.-I2C and SPI
3.-IRQs

It would be interesting too to improve the audio functions.
They are very simple and it does not seem straightforward
to improve them.
"""

""" Credits
This library has been developed from scratch by Aitzol Ezeiza Ramos
from the University of the Basque Country (UPV/EHU)
It is strongly based on nifpga the basic library for accessing the
FPGA on NI RIO devices.

https://github.com/ni/nifpga-python/


First version: 2024/02/28
Current version: 2025/09/25
"""

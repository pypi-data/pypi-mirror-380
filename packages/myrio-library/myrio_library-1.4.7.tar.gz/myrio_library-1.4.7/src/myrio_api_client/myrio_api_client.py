"""myRIO API client: An API client for the myRIO API server

Last update: 2024/03/15 Aitzol Ezeiza Ramos UPV/EHU

This is the client of the myRIO API server. Please refer to the
server documentation for further help.
The basics are:
    · Digital Inputs and Outputs
    · Analog Inputs and Outputs
    · onboard button and LEDs
    · onboard accelerometer
    - mxp board components
The default port is 8080. Some examples of API calls
(using curl) would be the following:

curl -X POST http://172.22.11.2:8080/digital_output/2/1

This turns on the digital output DIO2 on the default MXP port (A)
If you use Windows Powershell, you should replace the -X with -method X

curl -method POST http://172.22.11.2:8080/digital_output/2/1

You can change the default port with a parameter:

curl -X GET http://172.22.11.2:8080/digital_input/3?port=B

Read the examples un the examples folder for more info.
"""

import requests
from typing import Tuple

DEFAULT_HTTP_PORT = 8080
DEFAULT_HOST_IP = "172.22.11.2"


class MyRIO_API_Client:
    """class MyRIO_API_Client
    This is the base class for making requests to the API.
    We define generic methods for further development and
    developer flexibility. Anyway, there will be specific
    methods for each application route of the API server.

    Developer methods:
        make_request
        get_data
        post_data
        put_data
        delete_data

    Basic methods:
        get_digital_input
        set_digital_output
        get_analog_input
        set_analog_output
        get_onboard_button
        set_onboard_leds
        get_onboard_accelerometer

    MXP board methods:
        get_mxp_button
        set_mxp_rgb_color
        get_mxp_temperature
        get_mxp_luminosity

    Extra methods:
        set_pwm_output
    """

    def __init__(
        self, ip_address: str = DEFAULT_HOST_IP, port: int = DEFAULT_HTTP_PORT
    ):
        self.base_url = "http://" + ip_address + ":" + str(DEFAULT_HTTP_PORT)

    def make_request(self, method, endpoint, data=None, params=None):
        url = self.base_url + "/" + endpoint
        response = requests.request(method, url, json=data, params=params)
        response.raise_for_status()
        json_response = response.json()

        # Check if the response is a success message
        if isinstance(json_response, dict) and json_response.get("success") is True:
            return None  # Success message, no need to process
        # Check for a single key-value pair
        if isinstance(json_response, dict) and len(json_response) == 1:
            key, value = next(iter(json_response.items()))
            return value
        # Check for a dict of three key-value pairs (accelerometer)
        if isinstance(json_response, dict) and len(json_response) == 3:
            return list(json_response.values())
        # If none of the above cases match, return the full JSON response
        else:
            return json_response

    def get_data(self, endpoint, params=None):
        return self.make_request("GET", endpoint, params=params)

    def post_data(self, endpoint, data=None):
        return self.make_request("POST", endpoint, data=data)

    def put_data(self, endpoint, data=None):
        return self.make_request("PUT", endpoint, data=data)

    def delete_data(self, endpoint, params=None):
        return self.make_request("DELETE", endpoint, params=params)

    def get_digital_input(self, channel_in: int, port_in: str = "A") -> bool:
        """Returns the value (true/false) of a digital input"""
        if port_in == "A":
            endpoint = "digital_input/" + str(channel_in)
        else:
            endpoint = "digital_input/" + str(channel_in) + "?port=" + port_in

        response = self.get_data(endpoint)
        return response

    def set_digital_output(self, channel_in: int, value_in: int, port_in: str = "A"):
        """Sets the value (true 1, false 0) of a digital output"""
        if port_in == "A":
            endpoint = "digital_output/" + str(channel_in) + "/" + str(value_in)
        else:
            endpoint = (
                "digital_output/"
                + str(channel_in)
                + "/"
                + str(value_in)
                + "?port="
                + port_in
            )
        self.post_data(endpoint)

    def get_analog_input(self, channel_in: int, port_in: str = "A") -> float:
        """Returns the value (volts in float type) of an analog input"""
        if port_in == "A":
            endpoint = "analog_input/" + str(channel_in)
        else:
            endpoint = "analog_input/" + str(channel_in) + "?port=" + port_in
        response = self.get_data(endpoint)
        return float(response)

    def set_analog_output(self, channel_in: int, value_in: float, port_in: str = "A"):
        """Sets the value (volts in float type) of an analog output"""
        if port_in == "A":
            endpoint = "analog_output/" + str(channel_in) + "/" + str(value_in)
        else:
            endpoint = (
                "analog_output/"
                + str(channel_in)
                + "/"
                + str(value_in)
                + "?port="
                + port_in
            )
        self.post_data(endpoint)

    def get_onboard_button(self) -> bool:
        """Returns the value (true/false) of the onboard button"""
        endpoint = "onboard_button"
        response = self.get_data(endpoint)
        return response

    def set_onboard_leds(self, value_in: int):
        """Sets the value (0..15 integer) of the onboard LEDs"""
        endpoint = "onboard_leds/" + str(value_in)
        response = self.post_data(endpoint)

    def get_onboard_accelerometer(self) -> Tuple[float, float, float]:
        """Returns the value (x, y, z floats) of the onboard accelerometer"""
        endpoint = "onboard_accelerometer"
        response = self.get_data(endpoint)
        return response

    """
    MXP board methods:
        get_mxp_button
        set_mxp_rgb_color
        get_mxp_temperature
        get_mxp_luminosity
    """

    def get_mxp_button(self, button_in: int, port_in: str = "A") -> bool:
        """Returns the value (true/false) of one of the MXP buttons"""
        if port_in == "A":
            endpoint = "mxp_button/" + str(button_in)
        else:
            endpoint = "mxp_button/" + str(button_in) + "?port=" + port_in

        response = self.get_data(endpoint)
        return response

    def set_mxp_rgb_color(self, color_in: int):
        """Sets the value (0..7 integer) of the MXP RGB LED"""
        endpoint = "mxp_rgb_color/" + str(color_in)
        response = self.post_data(endpoint)

    def get_mxp_temperature(self, port_in: str = "A") -> float:
        """Returns the temperature (degrees in float type)
        of the MXP NTC temperature sensor (AI0)
        """
        if port_in == "A":
            endpoint = "mxp_temperature"
        else:
            endpoint = "mxp_temperature" + "?port=" + port_in
        response = self.get_data(endpoint)
        return float(response)

    def get_mxp_luminosity(self, port_in: str = "A") -> float:
        """Returns the luminosity (percentage in float type)
        of the MXP LDR light sensor (AI1)
        """
        if port_in == "A":
            endpoint = "mxp_luminosity"
        else:
            endpoint = "mxp_luminosity" + "?port=" + port_in
        response = self.get_data(endpoint)
        return float(response)

    # Extra methods

    def set_pwm_output(self, channel_in: int, value_in: float, port_in: str = "A"):
        """Sets the value (duty cycle in float type) of a PWM output"""
        if port_in == "A":
            endpoint = "pwm_output/" + str(channel_in) + "/" + str(value_in)
        else:
            endpoint = (
                "pwm_output/"
                + str(channel_in)
                + "/"
                + str(value_in)
                + "?port="
                + port_in
            )
        self.post_data(endpoint)


if __name__ == "__main__":
    myRIO = MyRIO_API_Client()
    print("Accelerometer:")
    print(myRIO.get_onboard_accelerometer())
    print("MXP temperature")
    print(myRIO.get_mxp_temperature())
    print("More examples in ./examples/client_examples.py")

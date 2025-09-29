"""myRIO API: A RESTful API server for the myRIO

Last update: 2024/03/14 Aitzol Ezeiza Ramos UPV/EHU

This library uses Flask and Waitress to create an API
based on myRIO_library. Not all the functions are
served this way, but the basics are there:
    · Digital Inputs and Outputs
    · Analog Inputs and Outputs
    · onboard button and LEDs
    · onboard accelerometer
    - MXP board components
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

from flask import Flask, jsonify, request
import myrio_base

DEFAULT_HTTP_PORT = 8080

app = Flask(__name__)


@app.before_first_request
def setup():
    """We need to create a session before any API call
    We use a global handler for that.
    """
    global myrio_handler
    myrio_handler = myRIO_base.MyRIO()


@app.route("/digital_input/<int:channel_in>", methods=["GET"])
def get_digital_input(channel_in: int):
    """Returns the value (true/false) of a digital input"""
    port_in = request.args.get("port", default="A", type=str)
    value = myrio_handler.read_digital_input(channel=channel_in, port=port_in)
    return jsonify({"value": value})


@app.route("/digital_output/<int:channel_in>/<int:value_in>", methods=["POST"])
def set_digital_output(channel_in: int, value_in: int):
    """Sets the value (true 1, false 0) of a digital output"""
    port_in = request.args.get("port", default="A", type=str)
    myrio_handler.write_digital_output(
        channel=channel_in, port=port_in, value=bool(value_in)
    )
    return jsonify({"success": True})


@app.route("/analog_input/<int:channel_in>", methods=["GET"])
def get_analog_input(channel_in: int):
    """Returns the value (volts in float type) of an analog input"""
    port_in = request.args.get("port", default="A", type=str)
    value = myrio_handler.read_analog_input(channel=channel_in, port=port_in)
    return jsonify({"value": value})


@app.route("/analog_output/<int:channel_in>/<float:value_in>", methods=["POST"])
def set_analog_output(channel_in: int, value_in: float):
    """Sets the value (volts in float type) of an analog output"""
    port_in = request.args.get("port", default="A", type=str)
    myrio_handler.write_analog_output(channel=channel_in, port=port_in, value=value_in)
    return jsonify({"success": True})


# Define routes for the onboard inputs and outputs
@app.route("/onboard_button", methods=["GET"])
def get_onboard_button():
    """Returns the value (true/false) of the onboard button"""
    value = myrio_handler.read_button()
    return jsonify({"value": value})


@app.route("/onboard_leds/<int:value_in>", methods=["POST"])
def set_onboard_leds(value_in: int):
    """Sets the value (0..15 integer) of the onboard LEDs"""
    myrio_handler.write_leds_integer(value_in)
    return jsonify({"success": True})


@app.route("/onboard_accelerometer", methods=["GET"])
def get_onboard_accelerometer():
    """Returns the value (x, y, z floats) of the onboard accelerometer"""
    values = myrio_handler.read_analog_accelerometer()
    response_data = {"x": values[0], "y": values[1], "z": values[2]}
    return jsonify(response_data)


# MXP board components: buttons, RGB LED, Temperature sensor, Light sensor


@app.route("/mxp_button/<int:button_in>", methods=["GET"])
def get_mxp_button(button_in: int):
    """Returns the value (true/false) of one of the buttons.
    We expect 1 or 2, first (black) and second (white).
    """
    port_in = request.args.get("port", default="A", type=str)
    value = myrio_handler.read_MXP_button(button=button_in, port=port_in)
    return jsonify({"value": value})


@app.route("/mxp_rgb_color/<int:color_in>", methods=["POST"])
def set_mxp_rgb_color(color_in: int):
    """Sets the color (0 to 7) of the MXP RGB LED
    Remember that the order is G(0)R(1)B(2)
    Green is 1, Red is 2, Blue is 4
    White is 7 and Off is 0.
    """
    port_in = request.args.get("port", default="A", type=str)
    myrio_handler.write_MXP_RGB_LED(color=color_in, port=port_in)
    return jsonify({"success": True})


@app.route("/mxp_temperature", methods=["GET"])
def get_mxp_temperature():
    """Returns the temperature (degrees in float type) of
    the NTC temperature sensor (MXP board)
    """
    port_in = request.args.get("port", default="A", type=str)
    value = myrio_handler.read_MXP_temperature(port=port_in)
    return jsonify({"value": value})


@app.route("/mxp_luminosity", methods=["GET"])
def get_mxp_luminosity():
    """Returns the luminosity (percentage in float type) of
    the LDR light sensor (MXP board)
    """
    port_in = request.args.get("port", default="A", type=str)
    value = myrio_handler.read_MXP_luminosity(port=port_in)
    return jsonify({"value": value})


# Extra functions: set PWM output


@app.route("/pwm_output/<int:channel_in>/<float:value_in>", methods=["POST"])
def set_pwm_output(channel_in: int, value_in: float):
    """Sets the value (duty cycle in float type) of a PWM output"""
    port_in = request.args.get("port", default="A", type=str)
    max_value = myrio_handler.config_PWM_output(channel=channel_in, port=port_in)
    myrio_handler.write_PWM_output(
        channel=channel_in, port=port_in, duty_cycle=value_in, X=max_value
    )
    return jsonify({"success": True})


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=DEFAULT_HTTP_PORT)
    # 0.0.0.0 means it will be served in all network interfaces

    # Instead of serving, you can debug the application
    # using Flask's server
    # app.run(debug=True)

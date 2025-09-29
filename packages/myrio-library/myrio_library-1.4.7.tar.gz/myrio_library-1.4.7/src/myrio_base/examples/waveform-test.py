"""Usage examples of the MyRIO class: play waveform

This example shows how to play a waveform using the MyRIO class.

Playing wav files is not supported in the myRIO library. However,
there is a rudimentary way to play a waveform using raw data.

Last update: 2024/04/10 Aitzol Ezeiza Ramos (UPV/EHU)
"""

import myrio_base as myRIO
import pkg_resources

myrio1 = myRIO.MyRIO()

# Play a simple waveform using raw data
print("Playing a simple waveform")
csv_file = pkg_resources.resource_filename("myRIO_base", "examples/PacManDeath.csv")
print("Waveform file: ", csv_file)
my_waveform = myRIO.extract_waveform_from_csv_file(csv_file)
myrio1.play_waveform(my_waveform)

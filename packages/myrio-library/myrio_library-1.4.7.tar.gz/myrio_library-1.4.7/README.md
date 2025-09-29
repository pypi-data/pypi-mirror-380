# myrio_library - a library for working with NI myRIO in Python

This is a set of tools to program the NI myRIO programmable device using Python. The myRIO is an FPGA-based RT device that is programmed usually in LabVIEW.

In this library, we have created some support functions and a class
named MyRIO. We call it "library" because the aim of this project is
to create a collection of packages for running Python programs in
different environments (multiple myRIOs, for example).

The packages myRIO_base and myRIO_API are designed to work locally, 
inside the myRIO. myRIO runs a reduced version of Linux named NI Linux RT.

https://www.ni.com/en/shop/linux/under-the-hood-of-ni-linux-real-time.html

The main idea is to be able to install the base library inside the myRIO and
to run basic functions easily.

If you want to use the base library, you will need an updated NI Linux RT image,
SSH enabled (it is easy to set in NI MAX, the configuration tool), and Internet
enabled on your myRIO (check the myRIO documentation for that). You will need
a privileged account (in myRIO the default administrator user is admin) if you
want to have access to the FPGA registers (the basic package, nifpga, needs that).

When ready, you should connect (ssh) to the myRIO and ensure that everything
is up-to-date before installing myRIO_library:

https://oldwiki.archive.openwrt.org/doc/techref/opkg

opkg update
opkg install python3 python3-misc python-pip

python -m pip install myrio_library

Check the examples folder inside the site-packages/myRIO_library/examples
folder for further help.

The myRIO_API package creates and serves an API implementation based 
on myRIO_base.

Read its specific documentation and examples for more information.

And finally, the third package of the library, myRIO_API_client,
can run on any computer that supports Python. You can install it
using pip:

pip install myrio_library

This library is an improvement over nifpga, a Python library that
gives access to the FPGA registers of NI targets with FPGA.

https://github.com/ni/nifpga-python

This package is a client implementation for accessing the API.
You will need communication with the myRIO (via USBLAN or WiFi)
in order to use the API. More info in the specific docs about
the myRIO_API_client package.

Last update: 2025/09/26 Aitzol Ezeiza Ramos (University of the Basque Country - EHU)


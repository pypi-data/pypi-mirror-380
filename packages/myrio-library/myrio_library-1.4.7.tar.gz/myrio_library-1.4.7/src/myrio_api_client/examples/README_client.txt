
README notes for the myRIO API client

If you have the myRIO_API application enabled as a service, you just need
to power up the myRIO and connect it via USBLAN. In that case, the example
will work straightforward.

If not, you can run the following command in the myRIO secure shell:

python /usr/lib/python3.5/site-packages/myrio_api/myrio_api.py

If you want to use a remote myRIO or multiple myRIOs, you can pass
the IP Address as a parameter in the class instance definition.

myRIO = MyRIO_API_Client(ip_address='172.22.11.3',port:8080)

Last update: 2025/09/26 Aitzol Ezeiza Ramos UPV/EHU
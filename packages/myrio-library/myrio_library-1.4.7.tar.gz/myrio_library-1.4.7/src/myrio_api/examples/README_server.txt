
README notes for the myRIO API server

If you want to enable the myRIO_API application as a service, you can copy the file named myRIO_API to the /etc/init.d folder

cp /usr/lib/python3.5/site-packages/myRIO_API/myRIO_API /etc/init.d

Ensure that the file has +x permisions:

chmod +x /etc/init.d/myRIO_API

The following commands would be ready to test and use.

/etc/init.d/myRIO_API start
/etc/init.d/myRIO_API stop
/etc/init.d/myRIO_API restart

If you want to start the service on system boot, you should create the soft links in the corresponding folders.

ln -s /etc/init.d/myRIO_API /etc/rc0.d/K01myRIO_API
ln -s /etc/init.d/myRIO_API /etc/rc1.d/K01myRIO_API
ln -s /etc/init.d/myRIO_API /etc/rc2.d/S99myRIO_API
ln -s /etc/init.d/myRIO_API /etc/rc3.d/S99myRIO_API
ln -s /etc/init.d/myRIO_API /etc/rc4.d/S99myRIO_API
ln -s /etc/init.d/myRIO_API /etc/rc5.d/S99myRIO_API
ln -s /etc/init.d/myRIO_API /etc/rc6.d/K01myRIO_API

The server needs some 40 seconds to launch after reboot.

Last update: 2024/03/11 Aitzol Ezeiza Ramos UPV/EHU
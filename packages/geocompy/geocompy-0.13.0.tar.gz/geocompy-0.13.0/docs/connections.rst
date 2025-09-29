.. _page_connections:

Connections
===========

Total stations and digital levels usually support a serial connection
with RS232. Some instruments come with additional connection methods, like
bluetooth as well.

Serial Line
-----------

The RS232 serial line is the main method of connection. The relevant main
primitive is the :class:`~geocompy.communication.SerialConnection` class,
that acts as a wrapper around a :class:`~serial.Serial` object that
implements the actual low level serial communication.

.. code-block:: python
    :caption: Simple serial connection
    :linenos:

    from serial import Serial
    from geocompy.communication import SerialConnection


    port = Serial("COM1", timeout=15)
    com = SerialConnection(port)
    com.send("some message")
    com.close()  # Closes the wrapped serial port

.. caution::
    :class: warning

    It is strongly recommended to set a ``timeout`` on the connection. Without
    a ``timeout`` set, the connection may end up in a perpetual waiting state
    if the instrument becomes unresponsive. A too small value however might
    result in premature timeout issues when using slow commands (e.g.
    motorized functions, measurements).

The :class:`~geocompy.communication.SerialConnection` can also be used as a
context manager, that automatically closes the serial port when the context
is left.

.. code-block:: python
    :caption: Serial connection as context manager
    :linenos:

    from serial import Serial
    from geocompy.communication import SerialConnection


    port = Serial("COM1", timeout=15)
    with SerialConnection(port) as com:
        com.send("some message")

To make the connection creation simpler, a utility function is also included
that can be used similarly to the :func:`open` function of the standard
library.

.. code-block:: python
    :caption: Creating connection with the utility function
    :linenos:

    from geocompy.communication import open_serial


    with open_serial("COM1", timeout=15) as com:
        com.send("some message")

If a time consuming request has to be executed (that might exceed the normal
connection timeout), it is possible to run it with a temporary override.

.. code-block:: python
    :caption: Timeout override for slow requests
    :linenos:

    from geocompy.communication import open_serial


    with open_serial("COM1", timeout=5) as com:
        ans = com.exchage("message")
        # normal operation

        # request that might time out
        with com.timeout_override(20):
            ans = com.exchange("blocking message")
        
        # resumed normal operation

Bluetooth
---------

Newer instruments (particularly robotic total stations) might come with
built-in or attachable bluetooth connection capabilities (e.g. Leica TS15
with radio handle). These instruments communicate over Serial Port Profile
Bluetooth Classic (SPP), that emulates a direct line serial connection.

.. note::

    In case of Leica instruments and GeoCOM, the GeoCOM interface on the
    instrument might have to be manually switched to the bluetooth device,
    before initiating a connection. Make sure to sync the port parameters
    (e.g. speed, parity) between the instrument and the computer!

To initiate a connection like this, the instrument first has to be paired
to the controlling computer, and the bluetooth address of the instrument
must be bound to an RFCOMM port as well.

.. tip::
    :class: hint

    Make sure, that the Bluetooth modem is active on the instrument
    and it is discoverable!

Windows
^^^^^^^

On windows machines the process is relatively straight forward. New SPP devices
can be added through the "Devices and Printers" page of the Control Panel.

1. Right-click on local computer and select the Bluetooth settings

.. image:: controlpanel_devices_and_printers.png

2. Navigate to the COM Ports tab
3. Click on Add
4. Select the Outgoing connection option and click Browse
5. Wait for the device to show up in the discovery window, then press OK
6. Click OK in all the windows

.. image:: add_device.png

If the process is successful, a new device will be added to the list of
devices. To double check, that the COM port binding was successful, open
the properties of the new device, and check, that the SPP service is active
and what port was assigned to it.

.. image:: check_spp.png

The actual device pairing will be initiated when the first actual connection
is attempted. The pairing code is usually ``0000`` or ``1234``.

Linux
^^^^^

.. note::

    The Linux process might vary between systems and distributions. Here the
    steps for setting up a Raspberry Pi will be given.

To add an SPP Bluetooth connection, the Bluetooth service has to be set to
compatibility mode, and the SPP service registered. This can be done by
updating the config of the bluez service.

.. code-block:: shell

    sudo nano /etc/systemd/system/dbus-org.bluez.service

Two lines have to be modified/added in the config:

.. code-block:: text

    ExecStart=/usr/lib/bluetooth/bluetoothd -C
    ExecStartPost=/usr/bin/sdptool add SP

.. caution::
    :class: warning

    On some devices/distributions of the Raspberry Pi OS the Bluetooth
    service executable might be in ``/usr/libexec/...`` instead of
    ``/usr/lib/...``. Make sure to specify the correct path!

After the modifications the Bluetooth service has to be restarted (the
cleanest solution is to simply restart the whole Raspberry Pi).

Once restarted, check, that the service started without issues:

.. code-block:: shell

    service bluetooth status

If the service started without errors, the pairing and binding can be done.

Start the Bluetooth utility:

.. code-block:: shell

    bluetoothctl

Make sure, that the device modem is powered on, the agent is active and
start scanning:

.. code-block:: shell

    power on
    agent on
    scan on

Wait for the device to appear (Bluetooth MAC address and device name), then
turn off the scanning:

.. code-block:: shell

    scan off

Once the MAC address is known, the device can be paired and set to trusted
(the pairing code is usually ``0000`` or ``1234``):

.. code-block:: shell

    pair <MAC address>
    0000
    trust <MAC address>

After the pairing is successful, the devices can be checked:

.. code-block:: shell

    paired-devices

If everything is done, the utility can be closed:

.. code-block:: shell

    quit

The final step is creating the RFCOMM binding, that allows to access the
SPP service connection:

.. code-block:: shell

    sudo rfcomm bind hci0 <MAC address>

The existing RFCOMM bindings can be checked if needed:

.. code-block:: shell

    rfcomm

If the whole process was successful, the device will be accessible on the
``/dev/rfcomm0`` port, and can be used as any direct line serial connection.

.. code-block:: python
    :caption: Opening connection through an RFCOMM port on a Raspberry Pi
    :linenos:

    from geocompy import open_serial


    with open_serial("/dev/rfcomm0") as com:
        com.send("some message")

.. warning::

    The RFCOMM bindings on Linux only exist while the system is running.
    They have to be recreated after every restart either manually, or with
    a startup script.

Simulators
----------

For testing and development purposes it is possible to make a connection to
the Leica Captivate TS simulator (and possibly other older official instrument
simulators). The simulators are available with an existing Captivate license,
or individual request from Leica or a Leica dealer.

.. tip::

    The simulator can be used to generate test data, or test a range of
    commands. It responds to GeoCOM requests with some exceptions.

To communicate with the simulator, a virtual serial port pair needs to be set
up on the computer. An open source solution is to use
`com0com <https://sourceforge.net/projects/com0com/>`_.

.. image:: com0com.png

It installs virtual serial port emulator drivers to simulate connections.
The communication is channeled through the presistent virtual devices.

.. image:: virtual_ports.png

In the settings of the simulator, the cable connection can be set to one end
of the virtual port pair (COM3 in this example), the other end can be used to
connect to the simulator (COM13 here).

.. tip::

    Older instrument simulators are hardwired to use COM1, COM2 and COM3 for
    cable, radio and bluetooth connections in this order. To connect to such
    a simulator, the virtual port pair should be set up between COM1 and a
    suitable second port COM4 or above.

.. image:: captivate_ports.png

The interface settings have to be set accordingly in the simulator itself,
just like on a real instrument.

.. image:: captivate_interface.png

.. warning::

    While purely software related GeoCOM commands are executed fine, the
    simulator might freeze up (serial communication wise) when trying to call
    closely hardware related functions (e.g. motorization). In these cases the
    GeoCOM commands start to time out. To solve it, the simulator has to be
    restarted.

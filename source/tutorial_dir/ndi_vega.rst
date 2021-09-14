NDI Polaris Vega Setup + Plus Server
====================================

written by Aoife Fitton

The NDI Polaris Vega is an optical tracking system for surgical navigation. The group uses the Vega for performing various measurement and registration tasks when evaluating magnetic tracking systems. Reflective markers are used to track objects within the defined field of view of the Vega camera. The optical nature of the device means that its precision and accuracy are unaffected by the presence of metal in the surrounding environment making it ideal for evaluating the performance of magnetic tracking systems in different environments

This tutorial describes how to set up the Vega system using both NDI's standalone software and the open-source PLUS toolkit.

.. image:: ./_images/ndi-vega.png
	:scale: 35%


.. image:: ./_images/ndi-markers.png
	:scale: 35%

NDI Vega camera unit and reflective markers.

|

Camera Setup
------------

1. Open the memory key that comes with the camera – install the windows/mac installer. You will install here NDI Configure, NDI Track and NDI Capture.
2. Once installing process completed, set up the hardware as shown in fig, using the Ethernet cables provided in the box. The computer connects by Ethernet to the PoE block (DATA IN) and the NDI Polaris is connected to the PoE block (DATA AND POWER OUT).
3. Open NDI Configure, open the file tab, select “connect to”, the camera named “P9-*****” or “[cameras IP address]” should be listed here, selected it to connect to. You can browse the cameras functionality configuration in this window.
4. To test the tracking, open NDI Track.
5. Connect to the camera as described in step 3 if it is not already connected.
6. Go to File, add tool, browse files, NDI key folder, CombinedAPIsample, sroms – and select the tool you are using, 38, 39 or, 40. You should see this when you move the tracker in the appropriate volume (Note. The tracking will not work if you are too close to the camera, keep about three feet back to begin):

.. figure:: ./_images/ndi-track.png
	:scale: 60%

	NDI track interface. The blue dot indicates the tracked object. The bounding box establishes the 3D region in which the object may be tracked.


Live Tracking with PLUS Toolkit
-------------------------------

The PLUS Toolkit `https://plustoolkit.github.io/ <https://plustoolkit.github.io/>`_ is an open-source package for connecting to 3rd party navigation devices. The package creates a *server* to which end-user *client* applications such as `Matlab https://github.com/PlusToolkit/PlusMatlabUtils/tree/master/MatlabOpenIGTLinkInterface>`_ and `3DSlicer <https://www.slicer.org/>`_ can connect.

The following tuturial describes how to set up the PLUS toolkit with the NDI Polaris Vega.

1. Download and install Plus Server application from `https://plustoolkit.github.io/download.html <https://plustoolkit.github.io/download.html>`_ - see latest stable release.
2. Copy the sroms folder from the NDI key, CombinedAPIsample to ``C:\Users\[user name]\PlusApp-2.8.0.20191105-Win32\config``.
3. Make sure the Vega is not being utilised by another software program. Check this by opening NDI Track, clicking connections, and seeing that the camera is not connected to that software.
4. Open Plus Server Launcher. Ensure the Device set configuration directory is the location of the config folder (``C:/…./ PlusApp-2.8.0.20190617-Win64/config``). *The Plus config file used is at the end of this document.*
5. From the drop-down menu select “PlusServer: NDI Vega tracker with passive markers”
6. Click “Launch server”. If the connection fails refresh the configuration directory and try again.

Sometimes Plus Server doesn’t connect on the first try or after first turning on the tracker. Click the green (or red) button in the bottom right corner to see the error messages.

.. figure:: ./_images/plus-screen.png
	:scale: 60%

	PLUS toolkit main screen.



XML Config file for Vega
~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: config.xml
	:linenos:
	:language: xml

Data Acquisition
================

Data acquisition refers to how the analog signals of the Anser EMT system are sampled and digitised for demodulation and processing by the position and orientation algorithm. Many data acquisition (DAQ) solutions are on the market ranging from low-cost microcontroller solutions to high performance 'turn-key' hardware solutions.

Anser EMT utilises National Instrument DAQ hardware, though this is not a strict requirement. The NI-USB 6216 DAQ unit (shown below) performs all the sampling operation for the Anser system. This DAQ unit features sixteen analog input channels with 16 bit resolution. A maximum sampling rate of 400kHz can be achieved with a single channel. Anser uses four channels at maximum capacity with a sampling rate of 100kHz per channel.

.. image:: _images/daqphoto.png
  :scale: 40%
  :align: center

The NI-USB 6216, along with many other NI devices, is directly compatable with Matlab through the use of the NI-DAQmx driver and the Matlab Data Acquisition Toolbox [1]_ . This toolbox makes interfacing the DAQ a simple task.

The 'Session' interface of the DAQ Toolbox is utilised to create a global structure for storing the sample data. The USB-DAQ automatically uses direct memory access (DMA) to refresh the structure with new sample data at each sampling interval. Implementation details can be found in the Matlab code for the Anser system.



..  [1] https://uk.mathworks.com/products/daq/
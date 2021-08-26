Waveform generator
==================

The AD9833 synthesises the reference sine waves for each emitter coil. The integrated circuit is programmed over the serial peripheral interface (SPI) using a microcontroller. The datasheet for this IC is available [1]_.
    
Programming the AD9833
----------------------
On powering up the IC needs to be configured to output the required frequency. The AD9833 contains a set of registers which can be written over the SPI interface. 

The desired frequency register value (denoted 'FREQREG' in the datasheet) can be found using the following formula:
:math:`\text{FREQREG} =\frac{f_{OUT}\times 2^{28}}{f_{MCLK}}` where :math:`f_{OUT}` is the desired output frequency of the AD9833 and :math:`f_{MCLK}` is the frequency of the master clock signal input provided by a clock driver.

For example, to program an output frequency of 20.5kHz using a 6MHz master clock signal:

.. math::

  \text{FREQREG} = \frac{20500 \times 2^{28}}{6\times 10^6} = 11011111111010100010_2

The full programming sequence is detailed in the datasheet and [application note] [2]_. Typically a microcontroller platform (for example Arduino [3]_ or MSP430 [4]_ is used to program each waveform generator when the system powered-on.



Variable gain stage
-------------------

The variable gain stage amplifies the output of the waveform generator in preparation for further processing and amplification. This stage is necessary as the output amplitude of the AD9833 is low (0-0.6 Volts). The gain stage consists of a TL081 operational amplifier in a non-inverting amplifier configuration shown below

.. image:: _images/noninverting.png
   :scale: 40 %
   :alt: alternate text
   :align: center

R1 and R2 form the feedback resistor network which controls the gain of the amplifier. The voltage gain is calculated using the following formula

.. math::
  A = 1 + \frac{R_2}{R_1}

R2 is potentiometer and can be varied to meet the gain requirements of the system. Detailed information regarding the circuit design and layout can be found in the schematics. 



Passive bandpass filter
-----------------------

The amplified signal from the variable gain stage contains noise and synthesis artifacts. A passive low-pass and high-pass filtering stage togther create a band-pass filter shown below:

.. image:: _images/bandpass.png
   :scale: 40 %
   :alt: alternate text
   :align: center


The cutoff frequency for each filter is given by the following equations:

.. math::
  f_{low} = \frac{1}{2 \pi R_L C_L}
  f_{high} = \frac{1}{2 \pi R_H C_H}

where bandwidth :math:`= f_{high} - f_{low}`. 

Choosing the component values for each filter depends on the frequencies of interest. Anser EMT transmits frequencies between 20.5kHz and 27.5kHz. One can therefore approximate a filter bandwidth of 10kHz with  20kHz and 30kHz being the lower and upper cutoff frequencies respectively. 

Further details of the filter implementation can be found in the schematic.


.. [1] http://www.analog.com/en/products/rf-microwave/direct-digital-synthesis/ad9833.html#product-overview
.. [2] http://www.analog.com/media/en/technical-documentation/application-notes/AN-1070.pdf
.. [3] https://www.arduino.cc/
.. [4] http://energia.nu/
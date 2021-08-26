Current summer
==============

A current summer amplifier is required to efficiently sample the current in each of the emitter coil PCBs. The composite signal is demodulated in an identical manner to the sensor signal. Data regarding the phases of the signals are extracted to provide information regarding the orientation of the sensor. This is used by the position and orientation algorithm (P&O). Without this, the sign of the :math:`n_A` vector cannot be determined. (i.e. Two solutions exist for the orientation angle, :math:`\theta` and :math:`\theta +\pi` The phase information decides which orientation is valid). The circuit schematic of the summer circuit is shown below

.. image:: _images/currentsummer.png
  :scale: 40%
  :align: center

:math:`V_1` to :math:`V_8` represent the current-sense voltage signals from each emitter coil. These voltage signals are generated from the high-speed amplifier shown in section 2a. Capacitors :math:`C_{DC}` block any DC bias from being amplified. Resistors :math:`R_{in}` set the gain of the amplifier in conjunction with :math:`R_f`. Both :math:`R_f` and :math:`C_f` also form a low-pass filter to block any high frequency noise from entering amplifier. A single TL082 operational amplifier (datasheet [1]_ ) is used in the Anser system, although this particular model is not required. The resulting output voltage :math:`V_{sum}` is given by:

.. math::

  V_{sum} = -\frac{R_f}{R_{in}}\left( V_1 +V_2+...V_8\right)

The precision of this circuit not vital for accurate system operation. The purpose of :math:`V_{sum}` is to provide the phase information of the coil current. i.e. magnitudes are not important. The amplifier gain should be chosen such that it can be accurately sampled by the data acquisition system (DAQ).


.. [1] http://www.ti.com/product/TL082
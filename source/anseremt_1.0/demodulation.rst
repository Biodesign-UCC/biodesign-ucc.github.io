Demodulation
============

Two modulation schemes are discussed in this section, synchronous and asynchronous methods are discussed. Asynchronous demodulation is the chosen scheme as it provides more information regarding the orientation of the sensor.

In order to calculate the amplitude of the AC magnetic field experienced by the sensor many techniques are available. Generally, the signals of interest are small in amplitude with relatively large noise levels as well as interference from the other transmitting channels. The most common method to extract the signals of this type is synchronous demodulation, also known as synchronous detection or lock-in amplification

Synchronous demodulation
------------------------
Synchronous demodulation is a method for extracting information from an AC carrier signal. Although asynchronous demodulation is used in Anser, synchronous demodulation illustrates basic concepts that are used in the asynchronous design.

The amplitude and phase of an AC signal can be calculated through multiplication by a reference signal that is locked in frequency with the original signal. The multiplication by the reference signal, shifts the signal down to a lower frequency, typically DC, which is then easier to accurately measure. The "locking" of frequencies can be implemented in many ways although the simplest is to use the source of the signal as a reference.

Consider an input signal:

.. math:: 
	v(t)=V\sin(\omega t + \varphi)

where :math:`V` is the modulating signal we wish to extract. The amplitude and phase of this signal can be determined by multiplying by two reference signals at the same frequency:

.. math:: 
	Y(t) = \sin(\omega t)
	X(t) = \cos(\omega t)

This multiplication result in two quadrature signals:

.. math:: 
	v_y(t) = v(t)Y(t) = \frac{V}{2}[\cos(\varphi)-\cos(2\omega t + \varphi)]
	v_x(t) = v(t)X(t) = \frac{V}{2}[\sin(\varphi)-\sin(2\omega t + \varphi)]

The DC component of the signal is extracted by using an appropriate low-pass filter. The resulting DC values are:

.. math::
	v'_y(t) = \frac{v}{2}\cos(\varphi)
	v'_x(t) = \frac{v}{2}\sin(\varphi)

The amplitude of the modulating signal :math:`V` can be found using:

.. math::

	V = 2\sqrt{(v'_x(t)^2 + v'_y(t)^2)}

The phase of the signal can be found using:

.. math::
	\varphi = \arctan\left(\frac{v'_y(t)}{v'_x(t)}\right)

Demodulating using this technique requires :math:`Y(t)` and :math:`X(t)` be generated from the reference source. This requires each of the eight coil voltages (20.5kHz, 21.5kHz...) to be individually sampled for processing, requiring an analogue to digital converter with a very high aggragate sampling frequency. Instead, simulated reference signals may be used to generate :math:`Y(t)` and :math:`X(t)` which results in asynchronous demodulation.

Asynchronous demodulation
-------------------------
Asynchronous demodulation uses simulated reference signals to generate the quadrature signals for demodulation. These simulated signals are **not** locked in phase with the signal to be demodulated and can experience frequency mismatch. This results in an increase in the number calculations required when determining the phase and magnitude of the signal of interest, but reduces the number of signals required for sampling.

Consider a tracking system consisting of N emitting coils, each coil carrying a current component of the following form:

.. math::

	i_i(t) = I_i\sin(\omega_i t + \varphi_{I_i})

where :math:`I_i` is the amplitude of the :math:`i_{th}` emitting coil waveform, :math:`\omega_i` is the excitation frequency and :math:`\varphi_i` is the current phase relative to an arbitrary reference. Summing all N current waveforms results in:

.. math::

	i(t) = \sum^N_{i=1} I_i\sin(\omega_i t + \varphi_{I_{i}})

The induced voltage on the sensor is a sum of the voltages induced by the coil currents:

.. math::

	v(t) = \sum^N_{i=1} V_i\sin(\omega_i t + \varphi_{V_{i}})

where :math:`V_i` is the amplitude of the induced voltage component and :math:`\varphi_{V_i}` is the associated phase. Each frequency component of the voltage signal is extracted using two reference signals:

.. math::

	Y_i = \sin(\omega_{ri} t)
	X_i = \cos(\omega_{ri} t)

where :math:`\omega_{ri}` is the frequency of the simulated reference signal. This demodulation results in the amplitudes and phases of all the frequency components relative to the simulated reference signal as follows:

.. math::
  \mathbf{V} = [V_1,V_2...V_n]
  \mathbf{I} = [I_1,I_2...I_n]
  \mathbf{\varphi_V} = [\varphi_{V_1},\varphi_{V_2}...\varphi_{V_n}]
  \mathbf{\varphi_I} = [\varphi_{I_1},\varphi_{I_2}...\varphi_{I_n}]

By subtracting the individual phases from each other the relative phase angle between the sensor voltage and coil current waveforms can be found:

.. math::

	\Delta\mathbf{\varphi} = \mathbf{\varphi_V} - \mathbf{\varphi_I}

The sign of this phase information indicates the axial orientation of the electromagnetic sensor with respect to the magnetic field.

With a simulated reference signal it can be difficult to lock the frequency to the signal source without the use of phase locking techniques. In our system this often results in a small mismatch in frequency since the simulated reference signal for a particular coil :math:`\omega_{ri}` is slightly different from the frequency to be demodulated :math:`\omega_i` since they are not locked. This results in a :math:`\Delta\omega=\omega_{ri} - \omega_r` causing a low frequency oscillation in the demodulated signal, which would not be present in synchronous demodulation.

To demonstrate this, consider a single frequency where the coil current and sensor voltage waveforms are given by:

.. math::

	i(t) = I\sin(\omega t + \varphi_I)
	v(t) = V\sin(\omega t + \varphi_V)

The simulated reference signals used for demodulation are given by:

.. math::

	Y(t) = \sin(\omega_r t)
	X(t) = \cos(\omega_r t)

Starting with the sensor voltage :math:`v(t)`, we multiply by the reference signals just as in the synchronous case to produce:

.. math::
	v(t)Y(t) = \frac{V}{2}[\cos((\omega-\omega_r) + \varphi_V) - \cos((\omega+\omega_r) + \varphi_V)]
	v(t)X(t) = \frac{V}{2}[\sin((\omega-\omega_r) + \varphi_V) - \sin((\omega+\omega_r) + \varphi_V)]

Extracting the low frequency components using a low-pass filter yields two quadrature voltage signals:

.. math::
	v_x=\frac{V}{2}\sin(\Delta\omega t + \varphi_V)
	v_y=\frac{V}{2}\cos(\Delta\omega t + \varphi_V)

where the difference in frequency is given by:

.. math::

	\Delta\omega = \omega-\omega_r

These signals are close to DC since they oscillate at a frequency of :math:`\Delta\omega` The amplitude :math:`V` can be determined as in the synchronous case using:

.. math::
	V = 2\sqrt{(v_x^2 + v_y^2)}

The phase can be determined using:

.. math::
	\gamma_V(t) = \arctan\frac{v_x}{v_y} = \Delta\omega +\varphi_V

Its clear that the phase has a time dependency. This is due to the frequency mismatch of the carrier and reference signals. In order to remove this dependency, the same demodulation procedure above is performed to the coil current waveform :math:`i(t)` to produce :math:`I` and :math:`\gamma_I`.  Subtracting the phase component :math:`\gamma_V` from :math:`\gamma_I` gives the constant relative phase angle between the two waveforms:

.. math::
	\gamma_V -  \gamma_I = \varphi_V-\varphi_I

This 'double demodulation' allows both the accurate retrieval of the amplitude and phase of each of the induced sensor voltages. Implementation details of how this demodulation is achieved  are described in the next section.


Demodulation implementation
---------------------------

The asynchronous demodulation process takes place in Matlab using an efficient matrix calculation technique. This method involves recording a number of samples of each signal of interest. This has the advantage of reduced solving time since all samples are available at the time of calculation. This is in contrast to real-time processing where samples are gathered and processed one-by-one in turn.

The signals of interest we wish to sample are:

 1. The induced voltage on the 5-DOF sensor coil(s)
 2. The composite coil current signal

Initially we consider the induced voltage on a single sensor that has been discretised through sampling:

.. math::
	x[n] = \sum_{i=1}^N V_i\sin\left(\frac{2 \pi f_i n}{f_s}+\varphi_i\right)

where N is the number of frequency of interest (N = 8, one frequency per emitter coil), :math:`f_i` is the frequency of interest in hertz, :math:`f_s` is the sampling frequency of the DAQ, :math:`V_i` is the amplitude and :math:`\varphi_i` is an associated phase shift. Collecting and string :math:`p` points results in a vector :math:`\mathbf{X}` containing :math:`p` samples:

.. math::

	\mathbf{X}=\left[x[0],x[1] ... x[p-1]\right]

In the previous section asynchronous demodulation was discussed. The first step of the demodulation involves multiplying the sampled signal by two sinusoids :math:`Y(n)=\sin(2\pi f_{ri} n)` and :math:`X(n)=\cos(2\pi f_{ri} n)`, where :math:`f_{ri}` is the simulated reference signal close in frequency to :math:`f_i` Using Euler's relation we combine :math:`X(n)` and :math:`Y(n)` into a single discrete complex sinusoid:

.. math::
	\cos(2\pi f_{ri}n) + j\sin(2\pi f_{ri} n) = e^{\frac{2 \pi f_{ri} j n }{f_s}}

where :math:`j = \sqrt{-1}` This complex exponential encapsulates the two quadrature signal components required for demodulation. Given the :math:`N` emitter coil frequencies, :math:`N` complex exponentials are required for the demodulation of each frequency. A :math:`p \times N`  matrix of complex exponentials is created  such that when pre-multiplied by :math:`\mathbf{X}` results in a vector of voltage magnitude:

.. math::
	\mathbf{E} = \begin{bmatrix}
                \epsilon_i[0]  & \dots & \epsilon_N[0] \newline
                \vdots& \ddots & \vdots \newline
                \epsilon_i[p-1] & \dots & \epsilon_N[p-1]
	\end{bmatrix}

where

.. math::
	\epsilon_i[n]=e^{\frac{2 \pi f_{ri} j n }{f_s}}

The row vector of demodulated voltages is given by premultiplying :math:`\mathbf{E}` by the row vector of :math:`p` samples:

.. math::
	\mathbf{Y} = [\widetilde{V}_1 ... \widetilde{V}_N] = 2\mathbf{X}\mathbf{E}

:math:`\mathbf{Y}` is a complex valued row-vector due to the presence of :math:`j` in the complex exponential calculation. The absolute value of each entry in :math:`\mathbf{Y}` is the amplitude received frequency of interest, :math:`V_i`. 

Finite impulse response (FIR filter)
------------------------------------

A finite impulse response filter is implemented as part of the demodulation step. This low pass FIR filter eliminates unwanted frequency components from the input sample stream :math:`\mathbf{X}` Consider an FIR filter denoted by :math:`f_i` with :math:`p` coefficients (\textit{i.e.} equal to the number of input samples). The output of such a filter can be represented as:

.. math::
	p[n] = \sum_{i=0}^{p-1}f_ix[n-i]

where :math:`p[n]` is the filtered sample vector and :math:`f_i` is a single filter tap coefficient. Each filter coefficient can be represented by a single matrix :math:`F` as shown below:

.. math::
	F = [f_0, f_1, f_2 \dots f_{p-1}]

The FIR filter can be applied to the demodulator by scaling each input sample of :math:`X` with the corresponding FIR coefficient given by :math:`F` This is achieved using an element by element multiplication:

.. math::
	\mathbf{Y} = 2(\mathbf{X}\circ \mathbf{F})\mathbf{E}

where :math:`\circ` represents the element-wise multiplication operator.

The amplitude of each frequency component can be determined by calculating the absolute value of :math:`\mathbf{Y}`, which is a complex quantity. The phase of :math:`\mathbf{Y}` can be found using the complex argument of :math:`Y`

.. math::
	[V_1 V_2 \dots V_N] = |\mathbf{Y}|
	[\varphi_1, \varphi_2 \dots \varphi_N] = \arg(\mathbf{Y})

The implementation of this calculation can be found in the Matlab code provided in the OSF file repository.




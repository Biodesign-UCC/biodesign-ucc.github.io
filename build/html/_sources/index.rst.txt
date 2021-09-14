

Biodesign UCC
=============

**Date**: |today| **Version**: |version|

**Download documentation**: `RST Files <https://github.com/Biodesign-UCC/biodesign-ucc.github.io/tree/master/source>`_


Quicklinks
----------

.. panels::
    :card: + intro-card text-center
    :column: col-lg-6 col-md-6 col-sm-6 col-xs-12 d-flex

    ---
    .. image:: _static/anser_goose.svg
      :width: 40%


    **Anser EMT**
    ^^^^^^^^^^^^^

    Documentation related to the electronic hardware design of Anser EMT magnetic tracking system

    +++

    .. link-button:: anseremt
            :type: ref
            :text: To the docs
            :classes: btn-block btn-secondary stretched-link

    ---
    .. image:: _static/github.svg
      :width: 40%

    **Group GitHub**
    ^^^^^^^^^^^^^^^^

    The main GitHub page for the group and contains all the repositories for hardware and software.

    +++

    .. link-button:: https://github.com/biodesign-ucc
            :text: To the GitHub page
            :classes: btn-block btn-secondary stretched-link

.. panels::
    :card: + intro-card text-center
    :column: col-lg-6 col-md-6 col-sm-6 col-xs-12 d-flex

    ---
    .. image:: _static/git-icon.svg
      :width: 33%

    **Git Access**
    ^^^^^^^^^^^^^^

    Follow this steps to use Git and gain access to the groups software and hardware repositories.

    +++

    .. link-button:: gitaccess
            :type: ref
            :text: To git guide
            :classes: btn-block btn-secondary stretched-link

    ---
    .. image:: _static/read-book.svg
      :width: 40%

    **Tutorials**
    ^^^^^^^^^^^^^

    Tutorials for getting started with various hardware and software devices in the lab

    +++

    .. link-button:: tutorials
            :type: ref
            :text: To the tutorials
            :classes: btn-block btn-secondary stretched-link


.. toctree::
   :hidden:

   about
   news
   people
   publications
   videos



Useful Tools
------------
Here is a list of some useful software tools used by the group.

* `Git <https://git-scm.com/download/win>`_ is the version control tool used in the group. This link is for the windows version.
* `3D Slicer <https://www.slicer.org/>`_ - is a visualisation tool for processing and viewing medical imaging and live optical and EM tracking data through OpenIGTLink.
* `OpenIGTLink <http://openigtlink.org/>`_ - is a network protocol for transferring image and position tracking data. It is used extensively in Anser EMT for ineterfacing with other software. The language of the core library is C++.
* `PyIGTLink <https://github.com/Danielhiversen/pyIGTLink>`_ is an implementation of the OpenIGTLink protocol written in Python.
* `OpenIGTLink MatlabUtils <https://github.com/PlusToolkit/PlusMatlabUtils/tree/master/MatlabOpenIGTLinkInterface>`_ is an implementation of the OpenIGTLink protocol written in Matlab.
* `PLUS toolkit <https://plustoolkit.github.io/>`_ is a software package for communicating with many commercial optical and magnetic tracking systems. e.g. the NDI Polaris and Aurora systems.
* `Absolute Orientation  <https://www.mathworks.com/matlabcentral/fileexchange/26186-absolute-orientation-horn-s-method>`_ is a implementation of Horns Method for performing rigid registration between two sets of corresponding points in different reference frames. A useful function when evaluting the accuracy of tracking systems.
* `distance2curve <https://uk.mathworks.com/matlabcentral/fileexchange/34869-distance2curve>`_  is a matlab function that finds the closest point on a curve from some given point in space. The function is capable of interpolation.
* `Inkscape <https://inkscape.org/>`_ is an open source tool for producing high quality vector graphics and digrams for papers.
* `Finite Element Method Magnetics <https://www.femm.info/wiki/HomePage>`_ (FEMM) is an open source field solver and is capable of solving 2D planar and axisymmetric magnetiostation and electrostatic problems. It is also capable of performing heatflow simulations.



..
   Indices and tables
   ==================


   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`

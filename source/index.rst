

Biodesign UCC
=============

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   anseremt_1.0/index

Software repositories:
----------------------

* `Anser EMT Python repository <https://github.com/Biodesign-UCC/AnserEMT_PyAnser>`_
* `Anser EMT Matlab repository <https://github.com/Biodesign-UCC/AnserEMT_Matlab>`_
* `Anser EMT C++ repository <https://github.com/Biodesign-UCC/AnserEMT_Cpp>`_


Hardware repositories:
----------------------

* `Anser EMT Hardware repository <https://github.com/Biodesign-UCC/AnserEMT_Hardware>`_
* `Anser EMT Firmware repository <https://github.com/Biodesign-UCC/AnserEMT_Firmware>`_


Get Access
----------
GitHub is used as the primary resource for storing design files and code used within the research group. In order to access the group's private repositories:

1. Create a GitHub account on `GitHub <https://github.com>`_.
2. Email `Alex <herman.alex.jaeger@gmail.com>`_ and provide your account username.
3. You will then be added to the lab organisation within GitHub and have read access to the repositories.

Making Changes
--------------
Additions, changes and updates to the existing repositories are encouraged. In order to submit a change to a repository you should:

1. Fork the repository using through GitHub. This will create a copy of the repository under your own GitHub account.
2. Clone the forked repository to your local PC.
3. Make the changes to the repository (source code edits, design file changes etc.). Ensure that any modificationw contain sufficient comments particularly in the case of source code changes.
4. Commit the changes to the repository adding a summary of your changes to the Git commit message. 
5. Submit a pull request through GitHub. This will alert the repository administrator that a change is being proposed and highlights the changes being made.
6. The administrator will review the pull request and will merge your changes into the original base repository. Everyone in the group will then be able to access your changes.

Updates to software and hardware designs can be easily accessed by the group. 


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

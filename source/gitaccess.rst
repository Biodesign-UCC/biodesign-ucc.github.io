Git Access
==========
GitHub is used as the primary resource for storing design files and code used within the research group. In order to access the group's private repositories:

1. Create a GitHub account on `GitHub <https://github.com>`_.
2. Email the `administrator <herman.alex.jaeger@gmail.com>`_ and provide your account username.
3. You will then be added to the lab organisation within GitHub and have read access to the repositories.



Downloading repositories
------------------------

1. Make sure Git is installed on your local machine
2. Create a local copy of the repository using the command :code:`git clone <url-to-repository>` on the command line. 
3. (Optional) Alternatively you can use a GUI client such as `GitHub Desktop`_.


Making changes
--------------
Additions, changes and updates to the existing repositories are encouraged. In order to submit a change to a repository you should:

1. Fork the repository using through GitHub. This will create a copy of the repository under your own GitHub account.
2. Clone the forked repository to your local PC. ``git clone <url-to-repository>``.
3. Make the changes to the repository (source code edits, design file changes etc.). Ensure that any modifications contain sufficient comments particularly in the case of source code changes.
4. Commit the changes to the repository adding a summary of your changes to the Git commit message using ``git commit -m 'my-message'``.
5. Submit a pull request through GitHub. This will alert the repository administrator that a change is being proposed and highlights the changes being made.
6. The administrator will review the pull request and will merge your changes into the original base repository. Everyone in the group will then be able to access your changes.

Updates to software and hardware designs can be easily accessed by the group. 

.. _GitHub Desktop: https://desktop.github.com/
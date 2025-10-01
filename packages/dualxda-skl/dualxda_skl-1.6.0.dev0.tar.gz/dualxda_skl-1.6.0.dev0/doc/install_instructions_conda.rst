Install conda using the `Anaconda or miniconda installers
<https://docs.conda.io/projects/conda/en/latest/user-guide/install/>`__ or the
`miniforge installers <https://github.com/conda-forge/miniforge#miniforge>`__ (no
administrator permission required for any of those). Then run:

.. prompt:: bash

  conda create -n sklearn_dual-env -c conda-forge scikit-learn
  conda activate sklearn_dual-env

In order to check your installation, you can use:

.. prompt:: bash

  conda list scikit-learn  # show scikit-learn version and location
  conda list               # show all installed packages in the environment
  python -c "import sklearn_dual; sklearn_dual.show_versions()"

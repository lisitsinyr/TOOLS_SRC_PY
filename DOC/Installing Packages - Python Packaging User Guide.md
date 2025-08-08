# Installing Packages
This section covers the basics of how to install Python packages.

It’s important to note that the term “package” in this context is being used to describe a bundle of software to be installed (i.e. as a synonym for a distribution). It does not refer to the kind of package that you import in your Python source code (i.e. a container of modules). It is common in the Python community to refer to a distribution using the term “package”. Using the term “distribution” is often not preferred, because it can easily be confused with a Linux distribution, or another larger software distribution like Python itself.

# Requirements for Installing Packages
This section describes the steps to follow before installing other Python packages.

## Ensure you can run Python from the command line
Before you go any further, make sure you have Python and that the expected version is available from your command line. You can check this by running:

py --version

You should get some output like Python 3.6.3. If you do not have Python, please install the latest 3.x version from python.org or refer to the Installing Python section of the Hitchhiker’s Guide to Python.

## Ensure you can run pip from the command line
Additionally, you’ll need to make sure you have pip available. You can check this by running:

py -m pip --version

If you installed Python from source, with an installer from python.org, or via Homebrew you should already have pip. If you’re on Linux and installed using your OS package manager, you may have to install pip separately, see Installing pip/setuptools/wheel with Linux Package Managers.

If pip isn’t already installed, then first try to bootstrap it from the standard library:

py -m ensurepip --default-pip

If that still doesn’t allow you to run python -m pip:

Securely Download get-pip.py [1]

Run python get-pip.py. [2] This will install or upgrade pip. Additionally, it will install Setuptools and wheel if they’re not installed already.

## Ensure pip, setuptools, and wheel are up to date
While pip alone is sufficient to install from pre-built binary archives, up to date copies of the setuptools and wheel projects are useful to ensure you can also install from source archives:

py -m pip install --upgrade pip setuptools wheel

## Optionally, create a virtual environment
See section below for details, but here’s the basic venv [3] command to use on a typical Linux system:

py -m venv tutorial_env

tutorial_env\Scripts\activate
This will create a new virtual environment in the tutorial_env subdirectory, and configure the current shell to use it as the default python environment.

# Creating Virtual Environments
Python “Virtual Environments” allow Python packages to be installed in an isolated location for a particular application, rather than being installed globally. If you are looking to safely install global command line tools, see Installing stand alone command line tools.

Imagine you have an application that needs version 1 of LibFoo, but another application requires version 2. How can you use both these applications? If you install everything into /usr/lib/python3.6/site-packages (or whatever your platform’s standard location is), it’s easy to end up in a situation where you unintentionally upgrade an application that shouldn’t be upgraded.

Or more generally, what if you want to install an application and leave it be? If an application works, any change in its libraries or the versions of those libraries can break the application.

Also, what if you can’t install packages into the global site-packages directory? For instance, on a shared host.

In all these cases, virtual environments can help you. They have their own installation directories and they don’t share libraries with other virtual environments.

Currently, there are two common tools for creating Python virtual environments:

venv is available by default in Python 3.3 and later, and installs pip into created virtual environments in Python 3.4 and later (Python versions prior to 3.12 also installed Setuptools).

virtualenv needs to be installed separately, but supports Python 2.7+ and Python 3.3+, and pip, Setuptools and wheel are installed into created virtual environments by default. Note that setuptools is no longer included by default starting with Python 3.12 (and virtualenv follows this behavior).

The basic usage is like so:

Using venv:

py -m venv DIR
DIR\Scripts\activate

Using virtualenv:

virtualenv DIR
DIR\Scripts\activate

For more information, see the venv docs or the virtualenv docs.

The use of source under Unix shells ensures that the virtual environment’s variables are set within the current shell, and not in a subprocess (which then disappears, having no useful effect).

In both of the above cases, Windows users should not use the source command, but should rather run the activate script directly from the command shell like so:

DIR\Scripts\activate
Managing multiple virtual environments directly can become tedious, so the dependency management tutorial introduces a higher level tool, Pipenv, that automatically manages a separate virtual environment for each project and application that you work on.

# Use pip for Installing
pip is the recommended installer. Below, we’ll cover the most common usage scenarios. For more detail, see the pip docs, which includes a complete Reference Guide.

# Installing from PyPI
The most common usage of pip is to install from the Python Package Index using a requirement specifier. Generally speaking, a requirement specifier is composed of a project name followed by an optional version specifier. A full description of the supported specifiers can be found in the Version specifier specification. Below are some examples.

To install the latest version of “SomeProject”:

py -m pip install "SomeProject"

To install a specific version:

py -m pip install "SomeProject==1.4"

To install greater than or equal to one version and less than another:

py -m pip install "SomeProject>=1,<2"

To install a version that’s compatible with a certain version: [4]

py -m pip install "SomeProject~=1.4.2"

In this case, this means to install any version “==1.4.*” version that’s also “>=1.4.2”.

# Source Distributions vs Wheels
pip can install from either Source Distributions (sdist) or Wheels, but if both are present on PyPI, pip will prefer a compatible wheel. You can override pip`s default behavior by e.g. using its –no-binary option.

Wheels are a pre-built distribution format that provides faster installation compared to Source Distributions (sdist), especially when a project contains compiled extensions.

If pip does not find a wheel to install, it will locally build a wheel and cache it for future installs, instead of rebuilding the source distribution in the future.

# Upgrading packages
Upgrade an already installed SomeProject to the latest from PyPI.

py -m pip install --upgrade SomeProject

# Installing to the User Site
To install packages that are isolated to the current user, use the --user flag:

py -m pip install --user SomeProject

For more information see the User Installs section from the pip docs.

Note that the --user flag has no effect when inside a virtual environment - all installation commands will affect the virtual environment.

If SomeProject defines any command-line scripts or console entry points, --user will cause them to be installed inside the user base’s binary directory, which may or may not already be present in your shell’s PATH. (Starting in version 10, pip displays a warning when installing any scripts to a directory outside PATH.) If the scripts are not available in your shell after installation, you’ll need to add the directory to your PATH:

On Linux and macOS you can find the user base binary directory by running python -m site --user-base and adding bin to the end. For example, this will typically print ~/.local (with ~ expanded to the absolute path to your home directory) so you’ll need to add ~/.local/bin to your PATH. You can set your PATH permanently by modifying ~/.profile.

On Windows you can find the user base binary directory by running py -m site --user-site and replacing site-packages with Scripts. For example, this could return C:\Users\Username\AppData\Roaming\Python36\site-packages so you would need to set your PATH to include C:\Users\Username\AppData\Roaming\Python36\Scripts. You can set your user PATH permanently in the Control Panel. You may need to log out for the PATH changes to take effect.

# Requirements files
Install a list of requirements specified in a Requirements File.

py -m pip install -r requirements.txt

# Installing from VCS
Install a project from VCS in “editable” mode. For a full breakdown of the syntax, see pip’s section on VCS Support.

py -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git          # from git
py -m pip install -e SomeProject @ hg+https://hg.repo/some_pkg                # from mercurial
py -m pip install -e SomeProject @ svn+svn://svn.repo/some_pkg/trunk/         # from svn
py -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git@feature  # from a branch

# Installing from other Indexes
Install from an alternate index

py -m pip install --index-url http://my.package.repo/simple/ SomeProject

Search an additional index during install, in addition to PyPI

py -m pip install --extra-index-url http://my.package.repo/simple SomeProject

# Installing from a local src tree
Installing from local src in Development Mode, i.e. in such a way that the project appears to be installed, but yet is still editable from the src tree.

py -m pip install -e <path>

You can also install normally from src

py -m pip install <path>

# Installing from local archives
Install a particular source archive file.

py -m pip install ./downloads/SomeProject-1.0.4.tar.gz

Install from a local directory containing archives (and don’t check PyPI)

py -m pip install --no-index --find-links=file:///local/dir/ SomeProject
py -m pip install --no-index --find-links=/local/dir/ SomeProject
py -m pip install --no-index --find-links=relative/dir/ SomeProject

# Installing from other sources
To install from other data sources (for example Amazon S3 storage) you can create a helper application that presents the data in a format compliant with the simple repository API:, and use the --extra-index-url flag to direct pip to use that index.

./s3helper --port=7777
python -m pip install --extra-index-url http://localhost:7777 SomeProject

# Installing Prereleases
Find pre-release and development versions, in addition to stable versions. By default, pip only finds stable versions.

py -m pip install --pre SomeProject

# Installing “Extras”
Extras are optional “variants” of a package, which may include additional dependencies, and thereby enable additional functionality from the package. If you wish to install an extra for a package which you know publishes one, you can include it in the pip installation command:

py -m pip install "SomePackage[PDF]"
py -m pip install "SomePackage[PDF]==3.0"
py -m pip install -e ".[PDF]"  # editable project in current directory

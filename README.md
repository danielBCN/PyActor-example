# PyActor Project Example

This is a simple project example on github using the
[PyActor](https://github.com/pedrotgn/pyactor) library.

[![Build Status](https://travis-ci.org/danielBCN/PyActor-example.svg?branch=master)](https://travis-ci.org/danielBCN/PyActor-example)
[![codecov](https://codecov.io/gh/danielBCN/PyActor-example/branch/master/graph/badge.svg)](https://codecov.io/gh/danielBCN/PyActor-example)
[![Code Health](https://landscape.io/github/danielBCN/PyActor-example/master/landscape.svg?style=flat)](https://landscape.io/github/danielBCN/PyActor-example/master)
[![Documentation Status](https://readthedocs.org/projects/pyactor-example/badge/?version=latest)](http://pyactor-example.readthedocs.io/en/latest/?badge=latest)



## Installing PyActor

Packages required:

    python, python-dev, python-pip

Install with:

    sudo pip install pyactor

If pip installs pyactor but gives an error with gevent, check that 'python-dev'
is installed and try again with:

    sudo pip install gevent

Or download the source by cloning [PyActor](https://github.com/pedrotgn/pyactor)'s
repository and installing with:

    sudo python setup.py install

If you clone the repository, you will also have access to the tests and a folder
full of examples. Just check the github page and the documentation for a detailed
tutorial.

## Tests

Just put your unit tests in the folder of the project in a way they can import
the modules. If you want your tests to have their own folder, then you need to
add your project to the PYTHONPATH in order to import the modules from outside.

You have a little example of a test in this project, but you should find
everything you need on the python docs:

[Testing with Python.](https://docs.python.org/2/library/unittest.html)


## Checking style

PEP8 checks the correctness of your code style based on a group of convention
guidelines (Such as indentation, line length, space usage). Install the package
with:

    sudo apt-get install pep8
    or
    sudo pip install pep8

Then, go to your project directory and execute:

    pep8 .      (or specify the path you want to check)

If the call prints no response: Congratulations!, your code is approved by the
style guide. Otherwise, you should take some seconds improving the readability
of your code.


## Setting up Travis

Projects can be linked to [Travis-CI](https://travis-ci.org), so they are build
and tested automatically at every commit. This ensures that the code on your
project's repository actually works and is always on date by continuous
integration. Putting a badge on your github page will
allow everyone to know the actual state of your project.

With Travis linked to the project, you can specify what do you want it to test.
Give it the tests, or tell it to check for PEP8 code style, in a way that warns
you if a commit does not accomplish everything you want to.

To configure this to work, you have to link your github account with the Travis
one by logging in on [travis-ci.org](https://travis-ci.org) with your github
account and select the repository you want to link. Then, you have to make a
commit adding a ``.travis.yml`` file on the root of your project.

This configuration file has a setup part and a script part. See the example on
this project.

First, you must specify the language the project is using. With python, you put
also the version.

Next comes the ``'install:'`` tag. Here goes all the code that Travis will execute
on its virtual machine before the actual test. That's the installation and setup
of all the requirements of your project, in this case, pyactor and PEP8, as we
are checking PEP8 to pass the build. As you could see, the pip requirements are
in a text file, so it is easier to change when needed.

On the ``'script:'`` goes the code that is actually the test: the commands that
must complete without errors for the build to end as a success. Here we are
putting the PEP8 checking command and the executions of the tests we have done.

Finally, you can add a piece of code that will execute only after the build
results in a success at the ``'after_success:'`` tag. We are using this to submit
our results to another page that counts the coverage of our code. That is, the
percentage of lines of the project that were executed (tested) during the tests.
We are configuring that in a sec.

The Travis configuration file has much more possibilities to offer. Feel free to
learn more about it by reading the
[docs](https://docs.travis-ci.com/user/customizing-the-build) and try them.

When Travis is working, it will generate a badge that you can put on the readme
of your project, so it will appear on the github page.

[![Build Status](https://travis-ci.org/danielBCN/PyActor-example.svg?branch=master)](https://travis-ci.org/danielBCN/PyActor-example)

## Code Coverage

The code coverage of a project is the percentage of lines that are tested on
the tests.

This information can be collected during the build at Travis and sent to
[codecov.io](https://codecov.io/) or another similar page, where anyone can see
the test coverage of the project and disaggregated information of all the
project's files, to the point of marking which lines have been tested and which
ones are missing.

First of all, you are going to need generating coverage info with your tests.
For that, add ``coverage`` to your pip requirements so the package is installed
on Travis. After that, change your script in the Travis file so that the
test-running command is:

    coverage run project/test.py

Changing it with the path of your tests.

That generates the data we need. The web configuration is pretty simple. Just log
in on [codecov.io](https://codecov.io/) with your github account and select your
repository to set it up. Then, add the next line to your Travis configuration
file, on the ``after_success`` section:

    bash <(curl -s https://codecov.io/bash)

This will upload the coverage data generated during the tests to codecov.io,
that will show it on its website.

Use this to enhance your tests and raise your coverage level.

Then, on the setting of your project, at codecov, you will find the badge to put
on your readme.

[![codecov](https://codecov.io/gh/danielBCN/PyActor-example/branch/master/graph/badge.svg)](https://codecov.io/gh/danielBCN/PyActor-example)


## Code Health

There is also another page that checks directly the health of your code. This
means that the service analyzes the code searching for inconsistences with the
PEP8 style guide, common bad smells and errors.

This results in health rate that gives the code a score. Try to keep that score
high, as your code gets mor readable and consistent.

Also, the health is represented in a badge that you can put on your readme for
everyone to know.

[![Code Health](https://landscape.io/github/danielBCN/PyActor-example/master/landscape.svg?style=flat)](https://landscape.io/github/danielBCN/PyActor-example/master)

## Documentation

Is very important to always document your code, as you may know.

To set up your docs at readthedocs.org, follow the guide to build a new
documentation project in rst using sphinx:
https://docs.readthedocs.io/en/latest/getting_started.html

Then, add a .rst file on the docs directory with the text you want.
Reference that file in the index.rst file, so it appears on the docs' content
tree.

If you want to generate documentations from the source files, you will need to
add the extension 'autodoc' during the sphinx setup. Then, add the corresponding
lines on a .rst file. For this to work, the project must be installed in the
python path, by creating a setup.py file and configuring it on readthedocs.

On the sphinx docs you have a quik guide on the rst format:
http://www.sphinx-doc.org/en/stable/rest.html

And maybe you find useful this online editor, so you can see how the text will
look like immediatly without having to build the whole documentation:
http://rst.ninjs.org/

[![Documentation Status](https://readthedocs.org/projects/pyactor-example/badge/?version=latest)](http://pyactor-example.readthedocs.io/en/latest/?badge=latest)

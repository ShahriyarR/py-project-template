# Python Project Template

Python project structure based on best practices, focused on security, automation and coding style.

## Prerequisites

Python 3.8+

First install [copier](https://pypi.org/project/copier/) and [copier_templates_extensions](https://pypi.org/project/copier-templates-extensions/)

`pip3 install copier`
`pip3 install copier-templates-extensions`

Then of course you need to have [GNU make](https://www.gnu.org/software/make/) installed on your machine.

## How to use?

* Go to the root folder where you are going to create the Python project. For eg, for me it is called `~/REPOS/others/`
`cd ~/REPOS/others/`

* Run copier as:

`copier copy --trust git@github.com:ShahriyarR/py-project-template.git py-remove-me`

or

`python3 -m copier copy --trust git@github.com:ShahriyarR/py-project-template.git py-remove-me`

* Answer the questions.
* You will have ready-to-go project structure


# TODO:

* Add GitHub workflows/CI runs.
* Update Makefile for adding separate test runs. test-slow, test-integration etc.
* Respectively add pytest marks.
* Issue and PR templates
# Team 6 Assignment 1

## Environment

Language: Python 3.6

Test Framework: unittest.

Code coverage: coverage.py

OS: Windows 10 or Debian 8 or 9. Other operating systems will likely work, but only these have been tested when writing this readme.

## Continuous Integration

This repository uses Project Pokémon's Team City server for continuous integrations. Contact Evan Dixon to request an account.

Build definitions:
* [Compile](https://teamcity.projectpokemon.org/viewType.html?buildTypeId=EvandixonPrivate_Team6Assignment1_Compile) - Compiles all python files to ensure valid syntax.
* [Test](https://teamcity.projectpokemon.org/viewType.html?buildTypeId=EvandixonPrivate_Team6Assignment1_Test) - Runs unit tests and generates an HTML code coverage report, zipped as a build artifact.

Use `pip install teamcity-messages` to enable Team City service messages when running tests, for use with Running Tests below.

## Contributing

1. Checkout the source
2. Create a branch
3. Make changes
4. Commit the changes
5. Push those changes
6. Open a Pull Request and wait for approval
7. Merge the Pull Request
8. Repeat

## Creating tests

Refer to [Python documentation](https://docs.python.org/3.6/library/unittest.html) for details, but keep the following in mind:
* Test files should be placed in /project/tests
* Test files do not need any footer

## Setup

### Windows

1. Install [Python 3.6](https://www.python.org/downloads/). Ensure python is in PATH.
2. Optional: To enable code coverage, run the following command: `pip install coverage`
3. Optional: For Team City build agents, run the following command: `pip install teamcity-messages`

### Debian

1. Run the following command: `sudo apt-get install python3`
2. Optional: To enable code coverage, run the following command: `pip3 install coverage`
3. Optional: For Team City build agents, run the following command: `pip3 install teamcity-messages`

## Running the API

### Windows

Run `python main.py host` in /project

### Debian

Run `python3 main.py host` in /project

## Running the console

### Windows

Run `python main.py console` in /project

### Debian

Run `python3 main.py console` in /project

## Running Tests

Code coverage reporting is optional, as Team City is configured to generate a report for every push.

### Without code coverage

For Windows:

1. Set the working directory to / or /project/tests, relative to the repository directory
2. Run `python -m unittest`.
    * For Team City build agents, run `python -m teamcity.unittestpy`.

For Debian:

1. Set the working directory to / or /project/tests, relative to the repository directory
2. Run `python3 -m unittest`.
    * For Team City build agents, run `python3 -m teamcity.unittestpy`.

### With code coverage

1. Set the working directory to / or /project/tests, relative to the repository directory
2. Run `coverage run -m unittest`.
    * For Team City build agents, run `coverage run -m teamcity.unittestpy`.
3. Run `coverage html`

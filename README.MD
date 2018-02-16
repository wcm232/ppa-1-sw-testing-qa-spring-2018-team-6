# Team 6 Assignment 1
(Words about the project)

## Environment
Language: Python 3

Test Framework: Python's default unittest.

Code coverage: coverage.py (`pip install coverage`)

## Continuous Integration
This repository uses Project Pok�mon's Team City server for continuous integrations. Contact Evan Dixon to request an account.

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

## Running Tests
With the working directory set to /project/tests:
* For local machines, run `python -m unittest`.
* For Team City, run `python -m teamcity.unittestpy`.
* For local machines with code coverage, run `coverage run -m unittest`.
* For Team City with code coverage, run `coverage run -m teamcity.unittestpy`.

To generate a code coverage report, run one of the above commands with code coverage, then run `coverage html`

## Creating tests
Refer to [Python documentation](https://docs.python.org/3.6/library/unittest.html) for details, but keep the following in mind:
* Test files should be placed in /project/tests
* Test files do not need any footer
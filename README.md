# Python Selenium BDD Demo
This project showcases basic capabilities of Selenium with Behave (BDD) framework, using the [Restful Booker Platform](https://automationintesting.online/) as its target. It also implements BehaveX for HTML reports and parallel test execution, along with API requests for creating test data.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features

### Page Object Pattern
This project utilizes the Page Object Pattern as its primary approach to code management. Each page of the application is represented as a corresponding class, which contains selectors for elements and methods covering specific actions across that page, available after initialization of the page object. All technical aspects of the Selenium framework, such as selector operations, explicit waits, or general actions across the entire application, are stored in one common parent class called BasePage. This pattern provides a clear separation between low-level "background" actions and high-level code used for creating tests.

An object-oriented approach has also been employed to store test data, such as accounts, bookings, messages, etc. Having templates for these common building blocks has resulted in better code readability and easier management of the data. API requests have also been designed as methods of one central class for clarity. Lastly, an object called context, implemented by the Behave framework itself, is used to transport all other objects and variables between BDD steps without the need for explicitly passing them as arguments.

### Scenarios and Scenarios Outlines
The tests utilize both approaches of the Gherkin language - Scenarios for non-parameterized test cases and Scenario Outlines for parameterized test cases. Outlines provide a clear way to build tests from flexible, more general steps, which are then customized by sets of values stored directly under scenarios. This also creates an opportunity to reuse the same sets of steps as separate scenarios by using different arguments and clear, readable titles for each scenario. A whole tested feature, containing many variants of data, might be covered by a small amount of code underneath.

However, there is a small drawback to that approach. During parallel test execution, sets of data across one scenario will NOT be paralleled and will be run one after another. Be aware of that fact when launching features containing Scenario Outlines with many examples. Sometimes it is sensible to break down these scenarios, dividing the amount of examples between now duplicated cases.

### Common steps
A single common step structure was implemented in the test suite to showcase the ability to reuse already defined steps in larger "chunks," allowing for better readability in longer scenarios. The provided example is simple (and could also be a single method within the Admin object), but the true strength of common steps lies in complex, lengthy scenarios. It allows for the gathering of a series of more general steps with parameters, then storing arguments to these parameters inside the common step definition, and finally naming the whole "chunks" with precise wording. For example, a step named "User buys a red convertible with V6 engine" could include several more general steps about paint color, chassis type, and engine type. Arguments such as "red," "convertible," and "V6" are hidden from the main scenario, which may be focusing on another feature and its parameters.

### Parallel test execution
BehaveX allows the test suite to be run as a set of parallel scenarios instead of queuing them one after another. This leads to significantly reduced test execution time, albeit potentially at the cost of slightly worse performance and stability of individual tests (although this varies depending on the architecture used for running tests, the application itself, etc.). This demo project runs tests locally, which is not a problem for the small number of scenarios, but in default parallel testing should be run on a Selenium Grid and launched via scripts in CI/CD pipelines. Combining this with a scaled container system allows end-to-end tests to run quickly, with high intensity and tolerable stability.

### Reporting
BehaveX, in addition to parallel test execution, also provides elegant, "business-friendly" HTML reports containing various metrics such as test execution rate, pass rate, scenario and test suite duration, captured errors, etc. Furthermore, this project leverages the ability to capture snapshots of the browser during failed scenarios and link them directly to BehaveX reports. The HTML file is stored inside the project directory as 'output/report.html', and screenshots are available within the report, accessible in the "Evidence" tab under the "Additional Evidence" button, specifically for failed scenarios. It's important to note that 'output/report.html' will be replaced each time you run the test suite, so ensure to archive reports in a different directory for later access.

### API requests
API requests, provided by the popular Python "requests" library, were utilized to generate test data and further validate some of the application's behavior. Creating test data, such as user accounts, orders, and products, via API, could shorten test execution time and allow scenarios to focus on the tested feature itself without redundant steps. Using API requests also adheres to the principle of test isolation, where each test operates on separate products of the application (e.g., accounts, orders). Additionally, in some cases where the environment might become quickly cluttered during the test suite itself, API requests can be part of a "cleanup" procedure, deleting unused test assets after the test has ended. This would come at the cost of losing some data useful for debugging the application and test cases themselves, but with excessive logging mechanisms and screenshot capture, that issue could be mitigated.

### Base for further development 
While serving as a comprehensive solution for simple, local tests, this demo could serve as a template for a larger project. It includes stubs for features such as multilingual tests (loading files with language strings and testing the same app with different language versions), multiple browser support (Chrome, Firefox, Edge), Selenium Grid (launching tests in a dockerized grid, via a local machine, or as part of CI/CD pipelines), and more. If you come across this project, feel free to experiment on your own and enhance it as you see fit.

## Installation

1. Download or clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the following command to install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Ensure that your Chrome browser is installed and up to date.

## Usage
### Running tests on a local machine
Run `behavex --parallel-processes 2 --parallel-scheme scenario` to launch the full test suite. It will run tests in 2 parallel processes, in headless mode. An HTML report with detailed test metrics will be stored as `output/report.html` in the project directory. 

#### Using tags
`-t <tag names>` - Adding `-t @customer` or `-t @admin` will only launch test scenarios specific to customer or admin. See Behave documentation for further tag usage.

#### Optional parameters
`-D retries=<integer>` - default `0`. Auto-retry feature for failed tests. It will re-run each failed scenario a specified number of times (total attempts = initial attempt + retried attempts).

`-D headless=<bool>` - default `True`. It allows browser processes to work in headless, invisible mode. It saves up resources with parallel testing but should be set to `False` while creating and debugging tests.

`-D debug=<bool>` - default `False`. Setting it to `True` will partially abort test cleanup, leaving the browser process opened. Good for debugging singular test cases, with custom tag and `-D headless=False` also set up.

#### Unused parameters
`-D language=<string>` - default `english`. Selects a file with language strings, for various assertions and checks. Strings for all code are stored in a single file, allowing running the same tests on different language versions of the tested application.

`-D browser=<string>` - default `chrome`. Selects a browser to run tests on. Selenium supports Firefox (geckodriver) and Edge (msedgedriver), both could be implemented as a choice in `driver.py` file. For this project I have used Chrome as a default choice, due to the convenience.

`-D runner_mode=<string>` - default `local`. This project could also run in CI/CD or directly on the Selenium Grid in the future. For this moment I have not created a whole infrastructure for these yet.

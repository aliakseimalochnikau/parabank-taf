# Parasoft ParaBank: Test Automation Framework
## ParaBank web application:

ParaBank is a demo web application used for demonstration of Parasoft software solutions.
It is used solely for simulating a realistic online banking website.

For more information about Parasoft solutions please visit www.parasoft.com 


## Test Automation Framework:

This a Python-based test automation framework utilizing Pytest and Selenium libraries.
It was created according to POM pattern to test [ParaBank web application.](https://parabank.parasoft.com/parabank/index.htm)

### Web app specifics

Due to web-server instability, sometimes the app may demonstrate inconsistent behavior, block test execution by Cloudflare or be completely unavailable.
To mitigate those impediments, supporting functions and additional validations were implemented.

### .env file

This framework was built to run tests in a container via GitHub actions. Thus, environment variables were placed in .env file, which was not meant to be pushed to repository.
Instead, GitHub variables and secrets were supposed to be used. But **.env** is required to run tests locally, so it is there.

If you want to follow the same approach, add **.env** to **.gitignore** and remove it from your repo in GitHub.
Also add variables stored in **.env** to GitHub variables and secrets.

### Pytest settings

To adjust Pytest settings used when running your tests, use **pytest.ini** config file.
By default, tests are run with the following parameters:
```
[pytest]
addopts =
    -sv
    --tb=short
    --showlocals
    --reruns 3
    --alluredir=allure-results
    -r a
markers =
    smoke
```

## Running tests:

To run tests, follow the steps below:

**1. Clone this repository to your machine:**
```
git clone https://github.com/aliakseimalochnikau/taf-pet-project.git
```

**2. Create a virtual environment:**
```
python -m venv venv
```

**3. Install project dependencies:**
```
pip install -r requirements.txt
```

**4. Run tests:**
```
pytest
```

## Allure report generation:

Once test run is complete, you can generate Allure report using the following command:
```
allure serve results
```
It will consolidate test results into a visual report which will be hosted locally until terminated.

To be able to use Allure report generation, make sure to install Allure and all its dependencies.
For more information follow [Allure Report installation](https://allurereport.org/docs/gettingstarted-installation/). 

## Running tests via docker-compose:

Instead of running tests locally, containerization approach can be utilized. Running tests in a container contributes to significant decrease in test execution time.
However, tests can be run only in headless mode (without UI).

To run tests in a container, the framework uses **Dockerfile** along with **docker-compose.yml**.

How to run tests:

1. **Install Docker:**

    Follow installation instructions for your OS at [Docker installation guide](https://docs.docker.com/desktop/install/windows-install/)


2. **Run the following commands:**
```
docker-compose build
```
```
docker-compose up
```

## Running tests via GitHub Actions:

To run tests in GitHub, follow the steps below:

1. **Create a GitHub repository**:

    You need to create a GitHub repository and set it as a remote for your project.


2. **Create and add a CI token**:
   
    - Navigate to *GitHub -> Settings -> Developer settings -> Personal access tokens* and create a new personal access token with permissions.
    - Navigate to *GitHub -> Repository -> Settings -> Secrets and variables -> Actions* and add a new repository secret **CI_TOKEN** with value from previous step.


3. **Add variables from *.env* file**:

    Variables stored in **.env** file should be added to GitHub secrets the same way as **CI_TOKEN** secret was added.


4. **Create *gh-pages* branch in your repository**


5. **Push changes to your repository**

   Make sure you push to **main**, not **gh-pages**.


6. **Run tests**

    In GitHub, navigate to *Actions -> ui-tests* and click on **Run workflow**.

Once test run is complete, Allure report will be generated and hosted on **gh-pages**.
It can be accessed via **pages-build-development** workflow next to **ui-tests**.

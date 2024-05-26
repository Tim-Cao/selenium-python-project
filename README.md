# How to set up a selenium project with python?

## Prerequisite

- Install [Python 3.9 or above](https://mirrors.huaweicloud.com/python/)

- Install [Pycharm Community Edition](https://www.jetbrains.com/pycharm/download/#section=linux)

## Add a python project

- File > New > Project > New Project

        Name: YourProjectName

        Location: Your project location

        Environment: Generate new

        Type: Virtualenv

        Base Python: Your python location

## Set up the domestic python image address

- `pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple/`

- `pip3 config set install.trusted-host mirrors.aliyun.com`

## Add required dependencies

- `pip3 install pdm`

- `pdm init`

  - Select the venv you just created

  - Press the Enter for others

- `pdm add pytest`

- `pdm add selenium`

- `pdm add webdriver_manager`

## Add driver classes to encapsulate selenium APIs

- Add classes under ***/src/package***

- The ***ChromeDriverManager*** will download chromedriver automatically in runtime

      webdriver.Chrome(service=Service(ChromeDriverManager().install()))

## Add page object classes to wrap specific tasks

- Add classes under ***/tests/package***

## Add tests

- Add classes under ***/tests/package***

If you would like to use example codes from this repo, follow these steps:

- Copy the [src](src) directory to yourProject

## Run single test in the class

### Pycharm

- Right-click on the method name in the code editor and select:

  - Run ***testCannotLoginAsTest()***

- Click on the method name in the code editor and press the key combination:

  - ***ctrl + shift + F10***

### Command Line

- Run  `pytest tests/test_login.py::testCannotLoginAsTest`
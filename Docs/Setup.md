# Project Setup and Requirements

This document outlines the steps and requirements necessary to set up and run the project. The setup process includes installing necessary tools and dependencies, ensuring your environment is correctly configured for mobile testing.

## Prerequisites

Before you begin, ensure that you have the following prerequisites installed on your system:

- **Java Development Kit (JDK)**: Java 11 or newer.
  - Check if Java is installed by running `java -version` in your terminal.
  - If not installed, download and install from [Oracle JDK](https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html) or adopt an OpenJDK version compatible with your system.

- **Node.js** and **npm**:
  - Required for running Appium. Download and install from [Node.js official website](https://nodejs.org/).

- **Python 3**:
   - Ensure Python 3.6 or newer is installed on your system. You can download it from [Python's official website](https://www.python.org/).
   - Verify the installation by running `python --version` in your terminal.

- **Appium** (Version 2 or newer) and UiAutomator2:
  - Install Appium by running `npm install -g appium@latest` in your terminal.
  - Install UiAutomator2 by running `appium driver install uiautomator2` in your terminal.

- **Android SDK**:
  - For testing Android applications, ensure Android Studio is installed and configured, along with the necessary SDK packages.

## Device Configuration

- Update `config.development.json` and `config.production.json` in the `configs` directory with the correct capabilities for your Android device or emulator.
- For testing on a real device, modify the `deviceName` key in the capabilities to match your device identifier.
- Ensure that your device has Developer Options and USB Debugging activated.


## Setting Up the Environment

1. **Environment Variables**:
   - Ensure `JAVA_HOME` is set to the JDK installation directory.
   - For Android testing, set `ANDROID_HOME` to your Android SDK location.

2. **Verify Appium Installation**:
   - Run `appium -v` in your terminal to check the Appium version and ensure it's correctly installed.

3. **Start the Appium Server**:
   - You can start the Appium server by running `appium` in your terminal. This will be necessary before executing any tests.

4. **Clone the Project Repository** (if not already done):
   - Use `git clone https://github.com/Sami-sfz/Score_Project.git` to clone the project to your local machine.

## Running the Tests

- Navigate to the project directory.
- Set up a Python virtual environment:

    - `python3 -m venv venv`

    - `source venv/bin/activate`
- Install required Python packages:

    - `pip install -r requirements.txt`
- To set your environment for the test run, use the command:
  - `export TEST_ENVIRONMENT=development`
  - The default value is set to `production` within the project configurations.
- Execute the test suite by running `pytest` in the root of project in terminal.

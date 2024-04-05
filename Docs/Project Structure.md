# Project Structure

## Overview
This document provides an overview of the project structure for the mobile app automation framework, focusing on a data-driven testing approach that allows for flexible testing of various app entities like players, teams, and leagues.

## Configuration
- **configs/**
  - `config_loader.py`: Loads environment-specific settings.
  - `config.development.json`: Contains development settings.
  - `config.production.json`: Contains production settings.

## Test Data
- **data/**
  - `data.py`: Defines the datasets for the parametrized tests, allowing flexibility across different entities.

## Page Objects
Page Objects pattern is used to interact with the app UI in a modular and reusable way.
- **pages/**
  - `launch_page.py`: Actions for initializing the app.
  - `league_page.py`: Interactions for the league-related features.
  - `main_page.py`: Interactions for the main page features.
  - `player_page.py`: Interactions for player-specific features.
  - `team_page.py`: Interactions for team-specific features.

## Test Base Class
- **test/**
  - `test_base.py`: Contains the setup and teardown methods for the WebDriver, shared across all tests.

## Test Cases
- **test/**
  - `test_entity.py`: This is the core test class that uses a data-driven approach to test different entities in the app.

## Test Implementation Approach
The `test_entity()` method in the `TestEntity` class is designed to handle multiple types of entities by:
  - Accepting data inputs for player, team, and league names.
  - Utilizing a search functionality to navigate to the appropriate page based on the entity type.
  - Verifying that the entity page opens correctly and that the page is as expected.
  - Navigating to a sub-tab (if applicable) and verifying its content.
  - Ensuring the back navigation works as expected.

## Utilities
- **utils/**
  - `webdriver_utils.py`: Utility functions for common WebDriver actions, such as element waiting and scrolling.

## Dependencies
- `requirements.txt`: Lists all necessary packages required for the project setup.

## README
- `README.md`: Provides setup and usage instructions for the test framework.

## Setup Instructions
Outlined steps to get the project up and running, including cloning the repository and installing dependencies.


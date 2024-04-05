# Test Specification

## Introduction
This specification details the automated tests for the mobile app. Tests are designed to validate the functionality of league, team, and player pages.

## Scenario: Open Entity Page
- **Objective**: Validate the ability to navigate and correctly display the selected entity page.
- **Steps**:
  1. Launch the app.
  2. Search or find the entity (League, Team, Player). The approach for Team and Player is searching but for League it's changed to finding the League's name in the League section.
  3. Confirm the entity page opens and the content is correct.

## Scenario: Sub-tab Navigation
- **Objective**: Validate the sub-tab functionality within the entity pages.
- **Steps**:
  1. Within an entity page, select a sub-tab (e.g., Standings).
  2. Verify the correct tab opens and relevant content displays.

## Scenario: Back Navigation
- **Objective**: Ensure back navigation returns the user to the previous page correctly.
- **Steps**:
  1. From a sub-tab, initiate back navigation.
  2. Confirm return to the previous page.

## Test Data
Utilize data-driven testing methods defined in `data.py` to test various entities and sub-tabs.

## Execution
Run tests using Pytest framework, iterating over parameters defined in `data.py`.

## Notes
- Each test must assert the presence of key content specific to the entity.
- Navigation between pages and tabs should be smooth and error-free.


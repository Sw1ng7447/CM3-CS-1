# CM3-CS-1
# Currency Converter

## Video Demo
https://youtu.be/BToC4oPX_FA

## Description
The **Currency Converter** is a Python-based console application that allows users to convert amounts between three different currencies: USD, EUR, and KZT. It uses predefined exchange rates to perform the conversions. The tool provides a simple way to convert currencies without relying on an internet connection, making it a reliable choice for basic conversions.

## Features
- Converts between USD, EUR, and KZT.
- Provides predefined exchange rates for offline use.
- Validates user input to ensure valid currency selections.
- Simple and user-friendly console interface.
- Includes unit tests to verify correct functionality.

## Installation
### Prerequisites
Ensure you have Python installed on your system. You can check by running:
```bash
python --version
```
If Python is not installed, download it from [python.org](https://www.python.org/).

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Sw1ng7447/CM3-CS-1
   ```
2. Navigate into the project folder:
   ```bash
   cd project
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the program using:
```bash
python project.py
```
Follow the prompts to input the amount, select the source currency, and the target currency. The system will display the converted amount or an error message if the input is invalid.

## Testing
Run the test cases with:
```bash
pytest test_project.py
```
These tests ensure that:
- The exchange rates return correct values.
- The currency conversion calculations are accurate.
- Invalid currency inputs are handled correctly.

## File Structure
- `project.py` - Main script containing the currency conversion logic.
- `test_project.py` - Unit tests for the converter functions.
- `requirements.txt` - Lists required dependencies.
- `README.md` - Documentation for the project.

## Exchange Rates Used
```
USD to EUR: 0.91
EUR to USD: 1.1
USD to KZT: 450
KZT to USD: 0.0022
EUR to KZT: 490
KZT to EUR: 0.0020
```
These exchange rates are static and can be updated in `project.py`.

## Design Choices
- **Hardcoded Exchange Rates**: To eliminate reliance on external APIs, exchange rates are predefined.
- **Simple Console UI**: Keeps the tool lightweight and easy to use.
- **Modular Functions**: Each function is designed to handle a specific task for better maintainability.
- **Testing with `pytest`**: Ensures robustness and prevents regressions.

## Challenges & Learnings
### Challenges Faced
- Handling incorrect currency inputs gracefully.
- Choosing exchange rates that remain somewhat realistic.
- Writing meaningful test cases to cover all edge cases.

### Lessons Learned
- Unit testing helps catch issues early.
- Modular design makes code easier to maintain and expand.
- Input validation improves the user experience significantly.

## Future Enhancements
- **Live Exchange Rate Updates**: Integrate an API to fetch real-time exchange rates.
- **GUI Version**: Create a graphical user interface using Tkinter or PyQt.
- **Multi-Currency Support**: Expand the tool to support more currencies.
- **Error Logging**: Implement logs for debugging invalid inputs.

## Author
- Gali Dauletkaliyev
- Sw1ng7447
- Robert Mardanov
- Robert_Mardanov

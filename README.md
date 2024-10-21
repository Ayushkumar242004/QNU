
# QRNG Number Randomness Detector

This project is a web application built with React and Django to detect the randomness of a given number. It utilizes a frontend developed in React and a backend powered by Django.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
  - [Frontend](#frontend)
  - [Backend](#backend)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

The Randomness Detector is an application designed to analyze numbers and determine their randomness. It serves as a useful tool for statistical analysis and educational purposes.

## Table of Contents

- Detects and analyzes the randomness of input numbers.
- NIST Statistical Tests: Consists of 17 tests to evaluate the - randomness of binary data.
- Dieharder Tests: Comprises 20 tests that provide further analysis of randomness.
- API Link Section: Allows users to enter the server link to fetch results for all 37 tests based on numbers generated from the QRNG server link.
- Generates detailed reports of test results through the report generation button.
- Visualizes results with graphs corresponding to the NIST tests via the graph generation button.
- Handles binary numbers up to 60,000 digits; upon tokenization, it can manage data up to 5,000,000 digits.
- Simple user interface with continuous improvement potential for handling large inputs and enhancing usability.
- Provides error handling; if a test result is -1, it indicates either the test input is not applicable or an exception occurred (e.g., division by zero).

## Features

- Detects and analyzes the randomness of input numbers.
- Interactive and user-friendly interface.
- Real-time results and feedback.

## Installation

### Frontend

1. Clone the repository:
   ```bash
   git clone https://github.com/Ayushkumar242004/QNU.git ./
   cd my-react-app

  
2. Install dependencies:
   npm install

3. Start the React development server:
   npm start

### backend
1. cd backend
2. Start the Django development server: python manage.py runserver

 ## Usage
- Ensure both the React and Django servers are running.
- Open your web browser and go to http://localhost:3000 to access the application.
- Input a number or click on select the binary data file button to see the randomness result.

## Technologies Used
- Frontend: React, Bootstrap, JavaScript
- Backend: Django, Python
- Other: npm, pip

## Contributions
  Contributions are welcome! Please follow these steps:
- Fork the repository.
- Create a new branch: 
   ```bash
   git checkout -b feature/YourFeature

- Commit your changes:
   ```bash
  git commit -m 'Add some feature'

- Push to the branch: 
   ```bash
   git push origin feature/YourFeature

- Open a Pull Request.

## Contact
- Author: Ayush Kumar
- Email: ayukumar242004@gmail.com
- GitHub: Ayushkumar242004


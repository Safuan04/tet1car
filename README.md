# Tet1Car

### Drive Your Dreams, Rent Your Journey

<img src="https://github.com/Safuan04/tet1car/blob/master/carrent/static/web_images/landing_page.PNG?raw=true">

## Table of Contents
- [Introduction](#introduction)
- [Setup](#setup)
- [Features](#features)
- [Usage](#usage)
- [Files](#files)
- [Models](#models)
- [Forms](#forms)
- [Contributing](#contributing)
- [License](#license)

## Introduction

CarRent is a car rental platform built using Flask, providing users with the ability to sign up, log in, rent cars, and manage their accounts. 

## Setup

To run this project locally, follow these steps:

1. Clone this repository.
2. Install the necessary dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up the database by configuring the `SQLALCHEMY_DATABASE_URI` in `__init__.py`.
4. Run the Flask application:
    ```bash
    python run.py
    ```
5. Access the application in your web browser at `http://localhost:5000`.

## Features

- User authentication (sign-up, login, logout)
- Car rental functionality
- Account management (update profile, view reservations)
- Owner management (add new owners, view owner details)
- Reservation system

## Usage

Upon launching the application, users can:

- Sign up for an account or log in if they already have one.
- Explore available cars on the landing page.
- View car details and make reservations.
- Update their account details and profile picture.
- Owners (specifically 'Safuan') can post new cars and manage existing listings.

## Files

### `run.py`

This file contains the Flask application setup and runs the server.

### `routes.py`

This file contains all the routes and view functions of the application.

### `forms.py`

Contains classes defining various forms used in the application.

### `models/`

Folder containing database models:

- `car.py`
- `owner.py`
- `reservation.py`
- `user.py`

## Models

The models represent database tables:

- `Car`: Represents car details and availability.
- `Owner`: Stores details of car owners.
- `Reservation`: Holds reservation details.
- `User`: Represents user information.

## Forms

Forms used for user interactions:

- `SignUpForm`
- `LoginForm`
- `UpdateAccountForm`
- `PostOwnerForm`
- `PostCarForm`
- `ReservationForm`

## Contributing

Contributions to improve this project are welcome. Feel free to fork the repository, make changes, and create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

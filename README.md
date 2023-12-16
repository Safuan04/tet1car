# Tet1Car

### Drive Your Dreams, Rent Your Journey

<img src="https://github.com/Safuan04/tet1car/blob/master/carrent/static/web_images/landing_page.PNG?raw=true">

## Table of Contents
- [Introduction](#introduction)
- [Setup](#setup)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Usage](#usage)
- [Files](#files)
  - [Routes](#routes)
  - [Forms](#forms)
- [Contributing](#contributing)

## Introduction

[Tet1car](https://www.safuan04.tech/) is a car rental website and it is an easy-to-use platform for renting cars. You can sign up, log in, and browse through a variety of cars available for rent.

This project  aims to simplify the process of renting vehicles in Tetouan, Morocco. This place is favored by a lot of moroccans and non moroccans specially in summer for its known beaches that need transportation to get to it... That's where this project comes handy where it provides an accessible platform for users to browse, book, and rent cars for their transportation needs.

## Setup

To run this project locally, follow these steps:

1. Clone this repository. https://github.com/Safuan04/tet1car
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

## Tech Stack

- **Flask**: Python-based web framework used for backend development.
- **SQLAlchemy**: Python SQL toolkit and Object-Relational Mapping (ORM) used for database operations.
- **Flask-Login**: Flask extension for managing user sessions and authentication.
- **MySQL**: Database management system used to store application data.
- **HTML/CSS**: Frontend technologies for structuring and styling web pages.
- **Jinja2**: Templating engine used with Flask for dynamic content.

## Usage

Upon launching the application, users can:

- Sign up for an account or log in if they already have one.
- Explore available cars on the landing page.
- View car details and make reservations.
- Update their account details and profile picture.
- The owner of the website can post new cars and manage existing listings.

## Files

### `run.py`

This file contains the Flask application setup and runs the server.

### `routes.py`

This file contains all the routes and view functions of the application.

#### Routes

The routes file (`routes.py`) contains all the routes and view functions of the application. Here are some of the main routes:

- `/sign-up`: Handles user sign-up functionality.
- `/login`: Manages user login and authentication.
- `/`: Landing page displaying available cars.
- `/home`: User homepage displaying cars and owners.
- `/logout`: Logs out the current user.
- `/account`: Manages user account details and profile picture.
- `/car/new`: Allows posting new cars (restricted to specific users).
- `/car/<int:car_id>/update`: Enables updating existing car details.
- `/reservation/<int:car_id>`: Manages car reservation functionality.
- `/owner/<int:owner_id>`: Displays owner details.
- `/owner/new`: Allows adding new owners (restricted to specific users).
- `/about`: Displays information about the application.
- `/owners`: Lists all owners.

### `forms.py`

Contains classes defining various forms used in the application.

## Forms

Forms used for user interactions:

- `SignUpForm`
- `LoginForm`
- `UpdateAccountForm`
- `PostOwnerForm`
- `PostCarForm`
- `ReservationForm`

### `models/`

Folder containing database models:

- `car.py`
- `owner.py`
- `reservation.py`
- `user.py`

## Contributing

Contributions to improve this project are welcome. Feel free to fork the repository, make changes, and create a pull request.

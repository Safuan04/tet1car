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
- [Acknowledgment](#acknowledgment)
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
- `/`: Displaying the Landing page.
- `/home`: User homepage displaying cars and owners.
- `/logout`: Logs out the current user.
- `/account`: Manages user account details and profile picture.
- `/car/new`: Allows posting new cars (restricted to specific users).
- `/car/<int:car_id>/update`: Enables updating existing car details (restricted to specific users).
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

## Acknowledgment

I would like to express my gratitude to the following individuals and resources for their contributions, inspiration, and support throughout the development of Tet1Car:

### Individuals
- [Adil](https://github.com/Elbadil): My cousin who worked on his own project alongside mine. We shared knowledge and supported each other through challenges. Adil's unwavering dedication and hard work have been a constant source of inspiration.

### Resources

- **[Flask Tutorial Youtube Playlist by: Corey Schafer](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&ab_channel=CoreySchafer)**
- **[DigitalOcean: How To Serve Flask Applications with Gunicorn and Nginx](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04)**
- **[ChatGPT](https://chat.openai.com/)**

I extend my thanks to everyone who has contributed in any way to the development and success of this project.


## Contributing

Contributions to improve this project are welcome. Feel free to fork the repository, make changes, and create a pull request.

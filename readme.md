# HTMX Interactive App Showcase

This project aims to demonstrate how to use [HTMX](https://htmx.org/) for building interactive web applications without relying on heavy front-end frameworks. It shows how HTMX can be integrated with Django to create a simple yet effective To-Do list application. The motivation for starting this demo project was to explore the HTMX craze that has been gaining traction on social media platforms and especially on YouTube.

## Features

- Lightweight
- Server-side logic
- Fast UI updates

## How to Run

First, the repository using the following command:

```bash
git clone https://github.com/randomicon00/todohtmx.git
```

Then, start a virtual environment using the command:

```bash
python3 -m venv <env-name>
```

Activate the virtual environment:

- On Windows: 
```cmd
<env-name>\Scripts\activate
```

- On Unix Or MacOs:
```bash 
source <env-name>/bin/activate
```

Then install the dependencies using:

```bash
pip install -r requirements.txt
```

To test the demo:
There are two components to the application.

1. The API Server
Navigate to the `todohtmx` directory and then run the server:

```bash
cd todohtmx
python manage.py runserver
```

2. The front-end HTML:
Serve the front-end using the following command (in a different terminal):

```bash
python -m http.server 8001
```

Make sure to replace `https://github.com/randomicon00/todohtmx.git` and `<env-name>` with your repository URL and preferred virtual environment name, respectively. And ensure you have a `requirements.txt` file with all the necessary dependencies listed.

## Dependencies

- Django
- HTMX

## Question

Do you think using HTMX for interactive UI is a better approach than using traditional heavy front-end frameworks? Why or why not?


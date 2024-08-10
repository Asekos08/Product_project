# Cities Project

This Django project provides an API to retrieve products and their photos based on a city ID. It allows filtering products by city and returns photos that are specific to the city or general photos if no city-specific photos exist.

## Features

- Retrieve products with city-specific photos
- Fallback to general photos if no city-specific photos exist
- RESTful API with Swagger documentation

## Installation

### Clone the repository:
   ```
   git clone https://github.com/yourusername/cities_project.git
   cd cities_project
   ```

### Create a Virtual Environment

Set up a virtual environment to isolate your Python dependencies and activate it:

```
python3 -m venv venv
source venv/bin/activate
```

###  Install Dependencies

Install the required Python packages using pip:

```
pip install -r requirements.txt
```


### Run Migrations

Apply the database migrations to set up your database schema:

```
python manage.py makemigrations
python manage.py migrate
```

## Running the Project

### Populate the Database

To fill the database with sample data (cities, products, and photos), run the script:
```
python manage.py seed_data   
```

### Start the Development Server

Run the Django development server:

```
python manage.py runserver
```

### Access the Swagger Documentation

```
http://127.0.0.1:8000/swagger/
```

### Running Tests

```
python manage.py test
```





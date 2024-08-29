# Django Ecommerce Project
## Installation
### Prerequisites

#### 1. Install Python
Install ```Python 3.12.4```.

#### 2. Install MySQL
Install ```mysql-8.0.37.0```.

#### 3. Setup virtual environment
```bash
# Create virtual environment by typing this command:
py -m venv env

# Activate virtual environment by typing this command:
env\Scripts\activate.bat
```

#### 4. Clone git repository
```bash
git clone "https://github.com/mayilraj07/ecommerce.git"
```

#### 5. Install requirements
```bash
cd ecommerce/
pip install -r requirements.txt
```

#### 6. Edit project settings
```bash
# open settings file
ekart/settings.py

# Edit Database configurations with your MySQL configurations.
# Search for DATABASES section.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<mysql-name>',
        'USER': '<mysql-user>',
        'PASSWORD': '<mysql-password>',
        'HOST': '<mysql-host>',
        'PORT': '<mysql-port>',
    }
}

# save the file
```
#### 7. Run the server
```bash
# Make migrations
py manage.py makemigrations
py manage.py migrate

# Run the server
py manage.py runserver

# your server is up on port 8000
```
Try opening [http://localhost:8000](http://localhost:8000) in the browser.
Now you are good to go home page.


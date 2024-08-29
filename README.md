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
#### Home Page:
![home_page](https://github.com/user-attachments/assets/baf8880a-2c66-444f-a107-a2b105f20cb2)
#### Signup Page:
![register_page](https://github.com/user-attachments/assets/6acc9f4b-7a4a-41f7-90d1-8689023de833)
#### Login Page:
![login_page](https://github.com/user-attachments/assets/6baab2b1-a132-4c6a-afc9-60e7c159ad5a)
#### Category Page:
![category_page](https://github.com/user-attachments/assets/fc1e6b63-a9fa-4e4a-af78-257569bfde06)
#### Product Page:
![products_view_page](https://github.com/user-attachments/assets/1b0996c5-52f4-4dab-a6c1-627113d78a45)
#### Product Detail Page:
![product_page](https://github.com/user-attachments/assets/c1af549d-bad6-4492-9066-efa199f733ae)
#### Profile Page:
![profile_page](https://github.com/user-attachments/assets/2ae309a0-6b32-4173-9928-6f1570a1d1de)
#### Cart Page:
![cart_page](https://github.com/user-attachments/assets/35f87e8e-eab1-4612-9240-86d68c48a311)
#### Address Page:
![delivery_address_page](https://github.com/user-attachments/assets/8c6c9372-5466-4998-b23a-90f50b12be77)
#### Order Page:
![order_page](https://github.com/user-attachments/assets/c4321255-228d-4cec-a957-eff9bf27a898)
#### Payment Page:
![payment_page](https://github.com/user-attachments/assets/16ac0f9a-f988-4a8b-bc77-ac93f9109bd0)
#### Logout Page:
![logout_page](https://github.com/user-attachments/assets/65f48a5d-c15e-446e-91c9-a74e522956b7)

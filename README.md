
# Food Truck Application Setup

## Prerequisites

Before you begin, make sure your environment is prepared with the following:

- **Python**: Version 3.8 or higher is recommended.
- **pip**: The Python package installer.

---

## Step 1: Setting Up a Virtual Environment

Using a virtual environment is recommended to manage your project dependencies efficiently.

### 1.1 Create a Virtual Environment

- **Windows**:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **macOS/Linux**:
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

Once activated, your terminal will display the virtual environment name, `venv`, at the beginning of each prompt.

---

## Step 2: Installing Project Dependencies

With your virtual environment activated, install the project dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## Step 3: Database Setup

Run the Django migrations to set up the database structure:

```bash
python manage.py migrate
```

---

## Step 4: Create a Superuser

To access the Django admin panel, you'll need a superuser. Create one by running:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the username, email, and password.

---

## Step 5: Run the Development Server

Finally, start the Django development server:

```bash
python manage.py runserver
```

By default, the server will be running at:

- http://127.0.0.1:8000/

---

## Step 6: Access the Django Admin Panel

Navigate to the admin panel and log in with the superuser credentials you created earlier:

- http://127.0.0.1:8000/admin/

---
### 7.2 Apply Migrations

apply the migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## IMPORT CSV

### 1. Click on import

![alt text](/Screenshot%20(2).png)

### 2. Select the CSV file

![alt text](/Screenshot%20(3).png)


### 3. Confirm Import

![alt text](/Screenshot%20(5).png)

### 3. Done

![alt text](/Screenshot%20(6).png)


### 4. Give the latitude and longitude in the url to get all Five Food Trucks of that location
```
127.0.0.1:8000/api/?latitude=37.764745350719494&longitude=-122.41656213947006
```
![alt text](/Screenshot%20(7).png)


---
# VIP-s-Django_Tutorials

1. **Task 1 - Login/Register Page with Authentication**
   - Utilizes Django framework for web development.
   - Implements user authentication with the help of SQLite for data storage.

2. **Task 2 - Multi-Step User Information Entry App**
   - Utilizes Django framework along with PostgreSQL for advanced data management.
   - Implements a multi-step registration process with the following steps:
     - User details entry form
     - Address details entry form
     - Educational qualifications entry form
     - Hobbies/Interests entry form
     - Display of entered details with a "Start Again" button to repeat the process.
   - Seperate tables are created in postgresql
   - When certain users log in, they will be automatically redirected to specific pages. For instance, when 'user1' logs in, they will be directed to 'page1,' and when 'user2' logs in, they will be directed to 'page2.

## Project Setup
### Step 0: Change directory to the working django folder

### Step 1: Set up PostgreSQL Database
- Download and install PostgreSQL.
- Create a database in PostgreSQL.
- Update your settings.py file with the database details.

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt

### Step 3: Make Migrations
```bash
python manage.py makemigrations

### Step 4: Migrate it
```bash
python manage.py migrate

### Step 5: Run the server
```bash
python manage.py runserver

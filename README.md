# DRF Library

A Django REST Framework project for managing books, users, and borrowings, with notifications via Telegram and scheduled tasks for overdue borrowings.

---

## Features

- **Books Service**
  - CRUD operations for books
  - Only admin users can create/update/delete
  - All users can list books
  - JWT authentication integration

- **Users Service**
  - User registration and management
  - JWT token support

- **Borrowings**
  - List, detail, create borrowings
  - Validate book inventory
  - Attach current user to borrowing
  - Return functionality (cannot return twice)
  - Filtering by active borrowings and user
  - Telegram notifications on borrowing creation
  - Daily overdue borrowings check

- **Notifications**
  - Telegram bot integration
  - Messages about new and overdue borrowings
  - Private info stays secure in `.env` files

- **Scheduled Tasks**
  - Daily task using Django-Q
  - Notifies about overdue borrowings or "No borrowings overdue today!"

- **Docker**
  - PostgreSQL database setup
  - Easy local development

---

## Getting Started

### Prerequisites

- Python 3.11+
- pip
- Docker & docker-compose 
- PostgreSQL

### Installation

1. Clone the repo:

```bash
git clone <your-repo-url>
cd drf_library
```

2. Create virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Setup environment variables:

```bash
cp .env.sample .env
# Fill in your DB credentials and Telegram bot token
```

5. Apply migrations:

```bash
python manage.py migrate
```

6. Create Superuser:
```bash
python manage.py createsuperuser
```
or use # DRF Library

A Django REST Framework project for managing books, users, and borrowings, with notifications via Telegram and scheduled tasks for overdue borrowings.

---

## Features

- **Books Service**
  - CRUD operations for books
  - Only admin users can create/update/delete
  - All users can list books
  - JWT authentication integration

- **Users Service**
  - User registration and management
  - JWT token support

- **Borrowings**
  - List, detail, create borrowings
  - Validate book inventory
  - Attach current user to borrowing
  - Return functionality (cannot return twice)
  - Filtering by active borrowings and user
  - Telegram notifications on borrowing creation
  - Daily overdue borrowings check

- **Notifications**
  - Telegram bot integration
  - Messages about new and overdue borrowings
  - Private info stays secure in `.env` files

- **Scheduled Tasks**
  - Daily task using Django-Q
  - Notifies about overdue borrowings or "No borrowings overdue today!"

- **Docker**
  - PostgreSQL database setup
  - Easy local development

---

## Getting Started

### Prerequisites

- Python 3.11+
- pip
- Docker & docker-compose 
- PostgreSQL

### Installation

1. Clone the repo:

```bash
git clone <your-repo-url>
cd drf_library
```

2. Create virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Setup environment variables:

```bash
cp .env.sample .env
# Fill in your DB credentials and Telegram bot token
```

5. Apply migrations:

```bash
python manage.py migrate
```

6. Create Superuser:
```bash
python manage.py createsuperuser
```
For quick testing, you can use the demo superuser:

- **Email:** admin@admin.com  
- **Password:** superuser  

7. Run server:

```bash
python manage.py runserver
```

### Docker Setup

```bash
docker-compose up --build
```

•	PostgreSQL will be ready inside the container  
•	Run migrations and create superuser inside the container:  

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

#### Usage  
##### Books Endpoints  
	• GET /books/ – list all books  
	• POST /books/ – create book (admin only)  
	• PUT /books/<id>/ – update book (admin only)  
	• DELETE /books/<id>/ – delete book (admin only)  
##### Users Endpoints  
	• POST /users/register/ – register user  
	• POST /users/token/ – get JWT token  
##### Borrowings Endpoints  
	• GET /borrowings/ – list borrowings (user sees only own borrowings)  
	• POST /borrowings/ – create borrowing  
	• POST /borrowings/<id>/return/ – return book  
##### Telegram Notifications  
	• Bot sends messages for new borrowings and overdue books  



#### Scheduled Tasks
•	Implemented with Django-Q  
•	Example schedule creation (add to apps.py or management command):

```bash
from django.utils import timezone
from django_q.models import Schedule

Schedule.objects.get_or_create(
    func='borrowings.tasks.check_overdue_borrowings',
    schedule_type=Schedule.DAILY,
    next_run=timezone.now(),
)
```

•	Daily overdue check will run automatically while the Django-Q cluster is running
```bash
email: admin@admin.com
password: superuser
```

7. Run server:

```bash
python manage.py runserver
```

### Docker Setup

```bash
docker-compose up --build
```

•	PostgreSQL will be ready inside the container  
•	Run migrations and create superuser inside the container:  

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

#### Usage  
##### Books Endpoints  
	• GET /books/ – list all books  
	• POST /books/ – create book (admin only)  
	• PUT /books/<id>/ – update book (admin only)  
	• DELETE /books/<id>/ – delete book (admin only)  
##### Users Endpoints  
	• POST /users/register/ – register user  
	• POST /users/token/ – get JWT token  
##### Borrowings Endpoints  
	• GET /borrowings/ – list borrowings (user sees only own borrowings)  
	• POST /borrowings/ – create borrowing  
	• POST /borrowings/<id>/return/ – return book  
##### Telegram Notifications  
	• Bot sends messages for new borrowings and overdue books  



#### Scheduled Tasks
•	Implemented with Django-Q  
•	Example schedule creation (add to apps.py or management command):

```bash
from django.utils import timezone
from django_q.models import Schedule

Schedule.objects.get_or_create(
    func='borrowings.tasks.check_overdue_borrowings',
    schedule_type=Schedule.DAILY,
    next_run=timezone.now(),
)
```

•	Daily overdue check will run automatically while the Django-Q cluster is running
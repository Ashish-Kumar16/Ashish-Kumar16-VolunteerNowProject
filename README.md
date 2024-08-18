# VolunteerNow

**VolunteerNow** is a platform designed to connect volunteers with opportunities and facilitate donations to organizations. It features functionalities for managing user accounts, applying for volunteer opportunities, and making donations.

## Features

- **User Management**:
  - User registration and login with JWT authentication.
  - Password reset functionality using OTP.

- **Volunteer Opportunities**:
  - Create, list, and filter volunteer opportunities.
  - Support for remote and in-person opportunities.

- **Applications**:
  - Apply for volunteer opportunities.

- **Donations**:
  - Make donations to organizations.

- **API Documentation**:
  - Swagger UI and Redoc for interactive API documentation.

## Project Structure

```
volunteernow/
├── volunteernow/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── docs/
│   ├── build/
│   ├── source/
│   ├── make.bat
│   ├── Makefile
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── signals.py
│   ├── templates/
│       ├── account/
│           ├── login.html
│           ├── password_reset_confirm.html
│           ├── password_reset.html
│           ├── signup.html
├── opportunities/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── filters.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── manage.py
```

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/volunteernow.git
   cd volunteernow
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at `http://127.0.0.1:8000/`.

## Usage

### User Management

- **Register**: `POST /auth/register/`
- **Login**: `POST /auth/login/`
- **Password Reset**: `POST /auth/password-reset/`
- **Password Reset Confirm**: `POST /auth/password-reset-confirm/`

### Volunteer Opportunities

- **List Opportunities**: `GET /api/opportunities/`
- **Create Opportunity**: `POST /api/opportunities/`
- **Filter Opportunities**: Use query parameters to filter by `location`.

### Applications

- **Apply for an Opportunity**: `POST /api/applications/`

### Donations

- **Make a Donation**: `POST /api/donations/`

### API Documentation

- **Swagger UI**: `http://127.0.0.1:8000/swagger/`
- **Redoc**: `http://127.0.0.1:8000/redoc/`

## Testing with Postman

To test the API endpoints with Postman:

1. **Import Postman Collection**

   - Download the Postman collection file from the [Postman Collection](link-to-collection-file) if available, or create your own.

2. **Set Up Environment**

   - Create a new environment in Postman with variables for `base_url` (e.g., `http://127.0.0.1:8000`) and any authentication tokens.

3. **Run Requests**

   - Use Postman to send requests to the endpoints. Here's a brief on how to test each feature:
   
     - **Register User**: Send a `POST` request to `/auth/register/` with required fields (`username`, `email`, `password`).
     - **Login**: Send a `POST` request to `/auth/login/` with `username` and `password`.
     - **Password Reset**: Send a `POST` request to `/auth/password-reset/` with `email`.
     - **Password Reset Confirm**: Send a `POST` request to `/auth/password-reset-confirm/` with `email`, `otp`, and `new_password`.
     - **List Opportunities**: Send a `GET` request to `/api/opportunities/`.
     - **Create Opportunity**: Send a `POST` request to `/api/opportunities/` with required fields (`title`, `organization`, etc.).
     - **Apply for Opportunity**: Send a `POST` request to `/api/applications/` with `opportunity`, `applicant_name`, and `applicant_email`.
     - **Make a Donation**: Send a `POST` request to `/api/donations/` with `organization`, `amount`, `donor_name`, and `donor_email`.

## Configuration

- **Database**: SQLite is used by default. Update `DATABASES` in `settings.py` for other databases.
- **Email Backend**: SMTP configuration is set for Gmail in `settings.py`. Update `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` with your credentials.



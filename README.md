# Job Platform Backend

## Project Setup
This is the backend for the Job Platform. It is built using Django and Django REST Framework.

### Prerequisites
- Python 3.13
- Git
- Virtual Environment (recommended)

### Installation
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/realAbhi-web/Backend-Gurugram.git
   cd Backend-Gurugram
   ```

2. **Create a Virtual Environment and Activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Start the Server:**
   ```sh
   python manage.py runserver
   ```

The backend will be running at `http://127.0.0.1:8000/`

---

## API Endpoints

### Jobs API
- **GET /jobs/api/jobs/** - Get all jobs
- **POST /jobs/api/jobs/** - Create a new job
  - **Request Body:**
    ```json
    {
        "title": "Example Job",
        "description": "This is an example job.",
        "price": "500.00",
        "is_completed": false
    }
    ```
  - **Response:**
    ```json
    {
        "id": 1,
        "title": "Example Job",
        "description": "This is an example job.",
        "price": "500.00",
        "created_at": "2025-02-28T12:38:06.925270Z",
        "is_completed": false
    }
    ```

### Workers API
- **GET /jobs/api/workers/** - Get all workers
- **POST /jobs/api/workers/** - Create a new worker
  - **Request Body:**
    ```json
    {
        "bio": "I am a skilled developer.",
        "skills": "Python, Django",
        "hourly_rate": "50.00",
        "location": "Remote",
        "profile_picture": null
    }
    ```
  - **Response:**
    ```json
    {
        "id": 1,
        "bio": "I am a skilled developer.",
        "skills": "Python, Django",
        "hourly_rate": "50.00",
        "location": "Remote",
        "profile_picture": null
    }
    ```

### 1. **User & Contractor Registration**
#### **Endpoint:**
```
POST /jobs/api/register/
```
#### **Description:**
This endpoint allows the creation of a new **User** or **Contractor** by providing the necessary details.

#### **Request Body:**
Send a JSON payload containing the required fields:

```json
{
    "username": "Ritu",
    "password": "The biggest heavyweight tits champion",
    "role": "contractor",
    "skills": "Always higher",
    "hourly_rate": "50.00",
    "location": "New York"
}
```

- `username` (string, required): Unique username for the user.
- `password` (string, required): Secure password for authentication
- `role` (string, required): Can either be 'user' or 'contractor'.

#### **Response:**
On success, returns a JSON object with the created user details.

```json
{
    "message": "User Ritu343 registered as contractor."
}
```

On error (e.g., missing fields or duplicate username), a relevant error message is returned.
```json
{
   "error": "Username, password, and role are required.
}
```


---

### 2. **Retrieve All Users**
#### **Endpoint:**
```
GET /jobs/api/users/
```
#### **Description:**
This endpoint retrieves a list of all registered users in the system.

#### **Response:**
Returns a JSON array of user objects.

```json
[
  {
    "id": 1,
    "username": "example_user",
    "email": "user@example.com"
  },
  {
    "id": 2,
    "username": "another_user",
    "email": "another@example.com"
  }
]
```

---

### 3. **Retrieve All Contractors**
#### **Endpoint:**
```
GET /jobs/api/contractors/
```
#### **Description:**
Fetches a list of all registered **contractors** in the system.

#### **Response:**
Returns a JSON array of contractor profiles.

```json
[
  {
    "id": 1,
    "username": "contractor_1",
    "email": "contractor1@example.com"
  },
  {
    "id": 2,
    "username": "contractor_2",
    "email": "contractor2@example.com"
  }
]
```

---

### Authentication
No authentication or tokens are required for accessing these APIs.

---

## Contribution
Feel free to fork and contribute to this project!

---

## License
This project is licensed under the MIT License.


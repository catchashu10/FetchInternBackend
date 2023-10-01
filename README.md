# Points Management API

This API is a Flask-based application for managing points and point transactions for users. It allows you to add, spend, and check the balance of points.

## Features

- **Add Points:** Add points for a user from different payers with a timestamp.
- **Spend Points:** Spend points with considerations to predefined rules.
- **Fetch Balance:** Check the current point balance from each payer.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

- Python 3.6 or later

## Installing and Running

#### Step 1: **Clone the repository:**
   ```sh
   git clone https://github.com/catchashu10/FetchInternBackend.git
   ```
   
#### Step 2: **Set Up a Virtual Environment** (This might take sometime)
Create a virtual environment in the project directory.
```sh
python3 -m venv FetchBackend
```

Activate the virtual environment.

##### Windows:
```sh
.\FetchBackend\Scripts\activate
```

##### macOS/Linux:
```sh
source FetchBackend/bin/activate
```

#### Step 3: **Install Dependencies**
Install the project dependencies listed in the requirements.txt file.

```sh
pip install -r requirements.txt
```

#### Step 4: **Run the Application**
Start the Flask application on port 8000.
```sh
flask run --port 8000
```

The API will be accessible at http://127.0.0.1:8000.

## **Testing the API**
You can call the apis using Postman or use curl from a new terminal. The server response will be visible in new terminal where the curl command is sent from.

#### 1. Add Points
```sh
curl -X POST http://127.0.0.1:8000/add -H "Content-Type: application/json" -d '{"payer": "DANNON", "points": 300, "timestamp": "2022-10-31T10:00:00Z"}'
curl -X POST http://127.0.0.1:8000/add -H "Content-Type: application/json" -d '{"payer": "UNILEVER", "points": 200, "timestamp": "2022-10-31T11:00:00Z"}'
curl -X POST http://127.0.0.1:8000/add -H "Content-Type: application/json" -d '{"payer": "DANNON", "points": -200, "timestamp": "2022-10-31T15:00:00Z"}'
curl -X POST http://127.0.0.1:8000/add -H "Content-Type: application/json" -d '{"payer": "MILLER COORS", "points": 10000, "timestamp": "2022-11-01T14:00:00Z"}'
curl -X POST http://127.0.0.1:8000/add -H "Content-Type: application/json" -d '{"payer": "DANNON", "points": 1000, "timestamp": "2022-11-02T14:00:00Z"}'
```

#### 2. Spend Ponits
```sh
curl -X POST http://127.0.0.1:8000/spend -H "Content-Type: application/json" -d '{"points": 5000}'
```

#### 3. Fetch Points Balance
```sh
curl http://127.0.0.1:8000/balance
```

Output for 3 will look like this:
```JSON
{
  "DANNON": 1000,
  "UNILEVER": 0,
  "MILLER COORS": 5300
}
```

## **Deactivating the Virtual Environment**
Once you have finished, you can deactivate the virtual environment by running:
```sh
deactivate
```

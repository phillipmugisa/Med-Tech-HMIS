# Med-Tech-HMIS
HMIS Web Application
This is a Health Management Information System built to run in the cloud.
The project will adapt a modular way of implementation; where each feature is implemented as a component.

## Modules
- Patients
- Visits
- Self Requests
- Tringe
- Doctor
- Lab
- Radiology
- Dental
- Pharmacy
- Theater 
- Inventory
- Finances 
- Cashier
- Invoices
- SMS

## Languages Used

| FrontEnd   | BackEnd    |
| ---------- | ---------- |
| HTML       |   Django   |
| CSS        |   Nodejs   |
| JAVASCRIPT |  Postgres  |


## setting up django and postgres
-----------------------------------------
### postgres
```
sudo -u postgres psql
CREATE USER medsafe WITH PASSWORD 'medsafe';
ALTER ROLE medsafe SET client_encoding TO 'utf8';
ALTER ROLE medsafe SET default_transaction_isolation TO 'read committed';
ALTER ROLE medsafe SET timezone TO 'UTC';
CREATE DATABASE medsafe OWNER medsafe;
GRANT ALL PRIVILEGES ON DATABASE medsafe TO medsafe;
```

-----------------------------
### django
```
sudo apt install python3:10
python3 -m venv venv
source ./venv/bin/activate
python3 -m pip install -r requirements.txt
python ./functional_tests/main.py
`
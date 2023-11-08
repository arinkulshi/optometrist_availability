## Running unit tests
All the tests can be run via ```pytest``` inside of the src/tests directory 
python -m pytest tests

## Running the full Project locally
python3 src/app.py


Implement a model to represent an appointment with one of two doctors (Strange, Who). Appointments can be arbitrary length i.e. 20 mins, 45 mins, 60 mins

Implement a model to represent the working hours of each doctor (9 AM to 5 PM, M-F for Strange, 8 AM to 4 PM M-F for Who). You can assume working hours are the same every week. i.e. The schedule is the same each week.

Implement an API to create an appointment, rejecting it if there's a conflict.

Implement an API to get all appointments within a time window for a specified doctor.

Implement an API to get the first available appointment after a specified time. i.e. I'm a patient and I'm looking for the first available appointment


Deploying the Project to GCP

#Make sure to have a valid project_id before deploying and a Cloud SQL instance set up 
gcloud builds submit --tag gcr.io/PROJECT-ID/opp_appointment
gcloud run deploy --image gcr.io/PROJECT-ID/helloworld --platform managed
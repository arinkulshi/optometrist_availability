from src.extensions import db
from flask import jsonify
from datetime import datetime


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    doctor_name = db.Column(db.String, nullable=False)
    patient_name = db.Column(db.String, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, nullable=False) 

    def json(self) -> str:
        return jsonify({
            'id': self.id,
            'doctor_name': self.doctor_name,
            'patient_name': self.patient_name,
            'start_time': self.start_time.strftime('%Y-%m-%d %H:%M:%S'),
            'duration': self.duration
        })



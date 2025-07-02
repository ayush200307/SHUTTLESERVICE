from app import db
from datetime import datetime, time
from sqlalchemy import Enum
import enum

class VehicleStatus(enum.Enum):
    ACTIVE = "active"
    MAINTENANCE = "maintenance"
    OUT_OF_SERVICE = "out_of_service"

class BookingStatus(enum.Enum):
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"

class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_location = db.Column(db.String(200), nullable=False)
    end_location = db.Column(db.String(200), nullable=False)
    distance_km = db.Column(db.Float, nullable=False)
    estimated_duration_minutes = db.Column(db.Integer, nullable=False)
    stops = db.Column(db.Text)  # JSON string of stops
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    schedules = db.relationship('Schedule', backref='route', lazy=True, cascade='all, delete-orphan')

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(20), unique=True, nullable=False)
    model = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    status = db.Column(Enum(VehicleStatus), default=VehicleStatus.ACTIVE)
    last_maintenance = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    schedules = db.relationship('Schedule', backref='vehicle', lazy=True)

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    license_number = db.Column(db.String(50), unique=True, nullable=False)
    license_expiry = db.Column(db.Date, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    schedules = db.relationship('Schedule', backref='driver', lazy=True)

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)
    departure_time = db.Column(db.Time, nullable=False)
    arrival_time = db.Column(db.Time, nullable=False)
    days_of_week = db.Column(db.String(20), nullable=False)  # e.g., "1,2,3,4,5" for weekdays
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    bookings = db.relationship('Booking', backref='schedule', lazy=True, cascade='all, delete-orphan')

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.id'), nullable=False)
    passenger_name = db.Column(db.String(100), nullable=False)
    passenger_phone = db.Column(db.String(20), nullable=False)
    passenger_email = db.Column(db.String(120), nullable=False)
    pickup_stop = db.Column(db.String(200), nullable=False)
    dropoff_stop = db.Column(db.String(200), nullable=False)
    booking_date = db.Column(db.Date, nullable=False)
    status = db.Column(Enum(BookingStatus), default=BookingStatus.CONFIRMED)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

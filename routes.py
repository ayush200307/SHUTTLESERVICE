from flask import render_template, request, jsonify, redirect, url_for, flash
from app import app, db
from models import Route, Vehicle, Driver, Schedule, Booking, VehicleStatus, BookingStatus
from datetime import datetime, date
import json

@app.route('/')
def dashboard():
    # Get dashboard statistics
    total_routes = Route.query.filter_by(is_active=True).count()
    total_vehicles = Vehicle.query.filter_by(status=VehicleStatus.ACTIVE).count()
    total_drivers = Driver.query.filter_by(is_active=True).count()
    total_bookings = Booking.query.filter_by(status=BookingStatus.CONFIRMED).count()
    
    # Recent bookings
    recent_bookings = Booking.query.order_by(Booking.created_at.desc()).limit(5).all()
    
    return render_template('dashboard.html', 
                         total_routes=total_routes,
                         total_vehicles=total_vehicles,
                         total_drivers=total_drivers,
                         total_bookings=total_bookings,
                         recent_bookings=recent_bookings)

@app.route('/routes')
def routes():
    routes_list = Route.query.all()
    return render_template('routes.html', routes=routes_list)

@app.route('/routes/add', methods=['POST'])
def add_route():
    try:
        name = request.form['name']
        start_location = request.form['start_location']
        end_location = request.form['end_location']
        distance_km = float(request.form['distance_km'])
        estimated_duration = int(request.form['estimated_duration'])
        stops = request.form.get('stops', '')
        
        route = Route(
            name=name,
            start_location=start_location,
            end_location=end_location,
            distance_km=distance_km,
            estimated_duration_minutes=estimated_duration,
            stops=stops
        )
        
        db.session.add(route)
        db.session.commit()
        flash('Route added successfully!', 'success')
    except Exception as e:
        flash(f'Error adding route: {str(e)}', 'error')
        db.session.rollback()
    
    return redirect(url_for('routes'))

@app.route('/routes/edit/<int:route_id>', methods=['POST'])
def edit_route(route_id):
    try:
        route = Route.query.get_or_404(route_id)
        route.name = request.form['name']
        route.start_location = request.form['start_location']
        route.end_location = request.form['end_location']
        route.distance_km = float(request.form['distance_km'])
        route.estimated_duration_minutes = int(request.form['estimated_duration'])
        route.stops = request.form.get('stops', '')
        
        db.session.commit()
        flash('Route updated successfully!', 'success')
    except Exception as e:
        flash(f'Error updating route: {str(e)}', 'error')
        db.session.rollback()
    
    return redirect(url_for('routes'))

@app.route('/routes/delete/<int:route_id>', methods=['POST'])
def delete_route(route_id):
    try:
        route = Route.query.get_or_404(route_id)
        route.is_active = False
        db.session.commit()
        flash('Route deactivated successfully!', 'success')
    except Exception as e:
        flash(f'Error deactivating route: {str(e)}', 'error')
        db.session.rollback()
    
    return redirect(url_for('routes'))

@app.route('/vehicles')
def vehicles():
    vehicles_list = Vehicle.query.all()
    return render_template('vehicles.html', vehicles=vehicles_list)

@app.route('/vehicles/add', methods=['POST'])
def add_vehicle():
    try:
        license_plate = request.form['license_plate']
        model = request.form['model']
        capacity = int(request.form['capacity'])
        year = int(request.form['year'])
        
        vehicle = Vehicle(
            license_plate=license_plate,
            model=model,
            capacity=capacity,
            year=year
        )
        
        db.session.add(vehicle)
        db.session.commit()
        flash('Vehicle added successfully!', 'success')
    except Exception as e:
        flash(f'Error adding vehicle: {str(e)}', 'error')
        db.session.rollback()
    
    return redirect(url_for('vehicles'))

@app.route('/vehicles/edit/<int:vehicle_id>', methods=['POST'])
def edit_vehicle(vehicle_id):
    try:
        vehicle = Vehicle.query.get_or_404(vehicle_id)
        vehicle.license_plate = request.form['license_plate']
        vehicle.model = request.form['model']
        vehicle.capacity = int(request.form['capacity'])
        vehicle.year = int(request.form['year'])
        vehicle.status = VehicleStatus(request.form['status'])
        
        db.session.commit()
        flash('Vehicle updated successfully!', 'success')
    except Exception as e:
        flash(f'Error updating vehicle: {str(e)}', 'error')
        db.session.rollback()
    
    return redirect(url_for('vehicles'))

@app.route('/drivers')
def drivers():
    drivers_list = Driver.query.all()
    return render_template('drivers.html', drivers=drivers_list)

@app.route('/drivers/add', methods=['POST'])
def add_driver():
    try:
        driver = Driver(
            employee_id=request.form['employee_id'],
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            phone=request.form['phone'],
            email=request.form['email'],
            license_number=request.form['license_number'],
            license_expiry=datetime.strptime(request.form['license_expiry'], '%Y-%m-%d').date()
        )
        
        db.session.add(driver)
        db.session.commit()
        flash('Driver added successfully!', 'success')
    except Exception as e:
        flash(f'Error adding driver: {str(e)}', 'error')
        db.session.rollback()
    
    return redirect(url_for('drivers'))

@app.route('/drivers/edit/<int:driver_id>', methods=['POST'])
def edit_driver(driver_id):
    try:
        driver = Driver.query.get_or_404(driver_id)
        driver.employee_id = request.form['employee_id']
        driver.first_name = request.form['first_name']
        driver.last_name = request.form['last_name']
        driver.phone = request.form['phone']
        driver.email = request.form['email']
        driver.license_number = request.form['license_number']
        driver.license_expiry = datetime.strptime(request.form['license_expiry'], '%Y-%m-%d').date()
        
        db.session.commit()
        flash('Driver updated successfully!', 'success')
    except Exception as e:
        flash(f'Error updating driver: {str(e)}', 'error')
        db.session.rollback()
    
    return redirect(url_for('drivers'))

@app.route('/schedules')
def schedules():
    schedules_list = Schedule.query.join(Route).join(Vehicle).join(Driver).all()
    routes_list = Route.query.filter_by(is_active=True).all()
    vehicles_list = Vehicle.query.filter_by(status=VehicleStatus.ACTIVE).all()
    drivers_list = Driver.query.filter_by(is_active=True).all()
    
    return render_template('schedules.html', 
                         schedules=schedules_list,
                         routes=routes_list,
                         vehicles=vehicles_list,
                         drivers=drivers_list)

@app.route('/schedules/add', methods=['POST'])
def add_schedule():
    try:
        schedule = Schedule(
            route_id=int(request.form['route_id']),
            vehicle_id=int(request.form['vehicle_id']),
            driver_id=int(request.form['driver_id']),
            departure_time=datetime.strptime(request.form['departure_time'], '%H:%M').time(),
            arrival_time=datetime.strptime(request.form['arrival_time'], '%H:%M').time(),
            days_of_week=request.form['days_of_week']
        )
        
        db.session.add(schedule)
        db.session.commit()
        flash('Schedule added successfully!', 'success')
    except Exception as e:
        flash(f'Error adding schedule: {str(e)}', 'error')
        db.session.rollback()
    
    return redirect(url_for('schedules'))

@app.route('/bookings')
def bookings():
    bookings_list = Booking.query.join(Schedule).join(Route).all()
    schedules_list = Schedule.query.filter_by(is_active=True).all()
    
    return render_template('bookings.html', 
                         bookings=bookings_list,
                         schedules=schedules_list)

@app.route('/bookings/add', methods=['POST'])
def add_booking():
    try:
        booking = Booking(
            schedule_id=int(request.form['schedule_id']),
            passenger_name=request.form['passenger_name'],
            passenger_phone=request.form['passenger_phone'],
            passenger_email=request.form['passenger_email'],
            pickup_stop=request.form['pickup_stop'],
            dropoff_stop=request.form['dropoff_stop'],
            booking_date=datetime.strptime(request.form['booking_date'], '%Y-%m-%d').date()
        )
        
        db.session.add(booking)
        db.session.commit()
        flash('Booking added successfully!', 'success')
    except Exception as e:
        flash(f'Error adding booking: {str(e)}', 'error')
        db.session.rollback()
    
    return redirect(url_for('bookings'))

@app.route('/bookings/cancel/<int:booking_id>', methods=['POST'])
def cancel_booking(booking_id):
    try:
        booking = Booking.query.get_or_404(booking_id)
        booking.status = BookingStatus.CANCELLED
        db.session.commit()
        flash('Booking cancelled successfully!', 'success')
    except Exception as e:
        flash(f'Error cancelling booking: {str(e)}', 'error')
        db.session.rollback()
    
    return redirect(url_for('bookings'))

# API endpoints for AJAX calls
@app.route('/api/stats')
def api_stats():
    stats = {
        'total_routes': Route.query.filter_by(is_active=True).count(),
        'total_vehicles': Vehicle.query.filter_by(status=VehicleStatus.ACTIVE).count(),
        'total_drivers': Driver.query.filter_by(is_active=True).count(),
        'total_bookings': Booking.query.filter_by(status=BookingStatus.CONFIRMED).count()
    }
    return jsonify(stats)

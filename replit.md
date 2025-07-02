# Shuttle Management System

## Overview

This is a Flask-based web application for managing shuttle operations, including routes, vehicles, drivers, schedules, and passenger bookings. The system provides a comprehensive dashboard and CRUD operations for all major components of a shuttle service.

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Database ORM**: SQLAlchemy with Flask-SQLAlchemy extension
- **Database**: SQLite (default) with PostgreSQL support via environment configuration
- **Session Management**: Flask sessions with configurable secret key
- **Middleware**: ProxyFix middleware for proper header handling behind proxies

### Frontend Architecture
- **Template Engine**: Jinja2 (Flask's default)
- **CSS Framework**: Bootstrap 5 with dark theme
- **Icons**: Font Awesome 6.4.0
- **JavaScript**: jQuery with Bootstrap components
- **Responsive Design**: Mobile-first approach using Bootstrap grid system

### Database Schema
The application uses SQLAlchemy ORM with the following main entities:
- **Route**: Manages shuttle routes with start/end locations, distance, and stops
- **Vehicle**: Vehicle fleet management with status tracking
- **Driver**: Driver information with license and contact details
- **Schedule**: Links routes, vehicles, and drivers with timing information
- **Booking**: Passenger bookings with status tracking

## Key Components

### Models (models.py)
- Enum-based status management for vehicles and bookings
- Relationship mapping between entities
- Timestamp tracking for record creation
- Cascade deletion for related records

### Routes (routes.py)
- Dashboard with statistics and recent activity
- CRUD operations for routes, vehicles, drivers, schedules, and bookings
- RESTful API endpoints with JSON responses
- Form validation and error handling

### Templates
- Base template with consistent navigation and styling
- Specialized pages for each entity type
- Modal forms for adding new records
- Responsive table layouts with action buttons

### Static Assets
- Custom CSS for enhanced styling and dark theme support
- JavaScript for form validation, tooltips, and user interactions
- Bootstrap and Font Awesome integration

## Data Flow

1. **Request Processing**: Flask routes handle HTTP requests and form submissions
2. **Database Operations**: SQLAlchemy ORM manages database interactions
3. **Template Rendering**: Jinja2 renders HTML templates with context data
4. **Response Delivery**: Flask returns rendered HTML or JSON responses
5. **Client Interaction**: JavaScript enhances user experience with validation and dynamic updates

## External Dependencies

### Python Packages
- Flask: Web framework
- Flask-SQLAlchemy: Database ORM
- Werkzeug: WSGI utilities and middleware

### Frontend Libraries
- Bootstrap 5: UI framework with dark theme
- Font Awesome: Icon library
- jQuery: JavaScript utilities

### Database
- SQLite: Default development database
- PostgreSQL: Production database (configurable via DATABASE_URL)

## Deployment Strategy

### Environment Configuration
- Database URL configurable via `DATABASE_URL` environment variable
- Session secret configurable via `SESSION_SECRET` environment variable
- Development defaults provided for local testing

### Database Management
- Automatic table creation on application startup
- Connection pooling with automatic reconnection
- Support for both SQLite and PostgreSQL

### Production Considerations
- ProxyFix middleware for deployment behind reverse proxies
- Configurable host and port binding
- Debug mode controllable via application entry point

## Changelog

```
Changelog:
- July 02, 2025. Initial setup
```

## User Preferences

```
Preferred communication style: Simple, everyday language.
```
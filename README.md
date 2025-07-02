# Shuttle Management System

A comprehensive web application for managing shuttle operations, built with Flask, Bootstrap, and jQuery.

## Features

- **Dashboard**: Overview with statistics and recent activity
- **Route Management**: Add, edit, and manage shuttle routes
- **Vehicle Management**: Track vehicles, capacity, and maintenance status
- **Driver Management**: Manage driver information and license tracking
- **Schedule Management**: Create and manage shuttle schedules
- **Booking System**: Handle passenger bookings and reservations

## Technology Stack

- **Backend**: Flask (Python), SQLAlchemy ORM
- **Frontend**: Bootstrap 5 (Dark Theme), jQuery, Font Awesome
- **Database**: SQLite (default) or PostgreSQL
- **Deployment**: Gunicorn WSGI server

## Local Setup Instructions

### Prerequisites

Make sure you have Python 3.8 or higher installed on your computer:
```bash
python --version
# or
python3 --version
```

### Step 1: Download the Project

Download all the project files to a folder on your computer. The folder structure should look like this:

```
shuttle-management/
├── app.py
├── main.py
├── models.py
├── routes.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── routes.html
│   ├── vehicles.html
│   ├── drivers.html
│   ├── schedules.html
│   └── bookings.html
└── static/
    ├── css/
    │   └── custom.css
    └── js/
        └── main.js
```

### Step 2: Create a Virtual Environment (Recommended)

Open a terminal/command prompt and navigate to your project folder:

```bash
# Navigate to your project folder
cd path/to/your/shuttle-management

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r local_requirements.txt
```

### Step 4: Set Environment Variables (Optional)

Create a `.env` file in your project folder for custom settings:

```bash
# .env file (optional)
SESSION_SECRET=your-secret-key-here
DATABASE_URL=sqlite:///shuttle_management.db
```

If you don't create this file, the app will use default settings.

### Step 5: Run the Application

```bash
# Start the application
python main.py
```

The application will start and you'll see output like:
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

### Step 6: Access the Application

Open your web browser and go to:
```
http://localhost:5000
```

You should see the Shuttle Management System dashboard.

## Using the Application

### Getting Started

1. **Add Routes**: Go to Routes page and add your first shuttle route
2. **Add Vehicles**: Go to Vehicles page and add your fleet
3. **Add Drivers**: Go to Drivers page and add driver information
4. **Create Schedules**: Go to Schedules page to assign routes, vehicles, and drivers
5. **Manage Bookings**: Go to Bookings page to handle passenger reservations

### Sample Data

When you first run the app, all tables will be empty. You can add sample data:

**Sample Route:**
- Name: Downtown Express
- Start: Central Station
- End: Business District
- Distance: 15.5 km
- Duration: 45 minutes

**Sample Vehicle:**
- License Plate: ABC-123
- Model: Mercedes Sprinter
- Capacity: 20
- Year: 2022

**Sample Driver:**
- Employee ID: DRV001
- Name: John Smith
- Phone: +1-555-0123
- Email: john.smith@example.com
- License: DL123456789
- License Expiry: 2025-12-31

## Database

The application uses SQLite by default, which creates a local database file. No additional database setup is required.

For production use with PostgreSQL:
1. Install PostgreSQL
2. Create a database
3. Set the DATABASE_URL environment variable:
   ```
   DATABASE_URL=postgresql://username:password@localhost/shuttle_db
   ```

## Troubleshooting

### Common Issues

**Port Already in Use:**
```bash
# Kill process using port 5000
# On Windows:
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F

# On macOS/Linux:
lsof -ti:5000 | xargs kill -9
```

**Permission Errors:**
- Make sure you have write permissions in the project folder
- Try running as administrator/sudo if needed

**Module Not Found:**
- Make sure your virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

**Database Errors:**
- Delete the database file `shuttle_management.db` to reset
- Restart the application to recreate tables

### Development Mode

For development with auto-reload:
```bash
export FLASK_ENV=development  # On Windows: set FLASK_ENV=development
python main.py
```

## Production Deployment

For production deployment:
1. Set `DEBUG=False` in `main.py`
2. Use a production WSGI server like Gunicorn
3. Set up a reverse proxy (nginx)
4. Use PostgreSQL database
5. Set secure environment variables

## Support

If you encounter any issues:
1. Check the console output for error messages
2. Verify all dependencies are installed
3. Make sure the database file has proper permissions
4. Restart the application

The application includes comprehensive error handling and logging to help identify issues.
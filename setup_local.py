#!/usr/bin/env python3
"""
Local Setup Script for Shuttle Management System
This script helps set up the application on your local computer.
"""

import os
import sys
import subprocess
import platform

def print_step(step_num, description):
    """Print a formatted step description."""
    print(f"\n{'='*60}")
    print(f"STEP {step_num}: {description}")
    print(f"{'='*60}")

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"Current version: {platform.python_version()}")
        return False
    else:
        print(f"✅ Python {platform.python_version()} detected")
        return True

def create_virtual_environment():
    """Create a virtual environment."""
    if os.path.exists('venv'):
        print("✅ Virtual environment already exists")
        return True
    
    try:
        print("Creating virtual environment...")
        subprocess.run([sys.executable, '-m', 'venv', 'venv'], check=True)
        print("✅ Virtual environment created successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to create virtual environment")
        return False

def get_activation_command():
    """Get the command to activate virtual environment based on OS."""
    if platform.system() == "Windows":
        return "venv\\Scripts\\activate"
    else:
        return "source venv/bin/activate"

def install_dependencies():
    """Install required dependencies."""
    try:
        if platform.system() == "Windows":
            pip_path = os.path.join('venv', 'Scripts', 'pip')
        else:
            pip_path = os.path.join('venv', 'bin', 'pip')
        
        print("Installing dependencies...")
        subprocess.run([pip_path, 'install', '-r', 'local_requirements.txt'], check=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def create_env_file():
    """Create a sample .env file."""
    if os.path.exists('.env'):
        print("✅ .env file already exists")
        return
    
    env_content = """# Shuttle Management System Environment Variables
# You can customize these values

# Session secret key (change this for production)
SESSION_SECRET=shuttle-management-secret-key-2025

# Database URL (SQLite by default)
DATABASE_URL=sqlite:///shuttle_management.db

# Debug mode (set to False for production)
DEBUG=True
"""
    
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ Created .env file with default settings")
    except Exception as e:
        print(f"⚠️  Could not create .env file: {e}")

def print_next_steps():
    """Print the next steps to run the application."""
    activation_cmd = get_activation_command()
    
    print(f"\n{'='*60}")
    print("🎉 SETUP COMPLETE!")
    print(f"{'='*60}")
    print("\nTo run the Shuttle Management System:")
    print(f"\n1. Activate the virtual environment:")
    print(f"   {activation_cmd}")
    print(f"\n2. Start the application:")
    print(f"   python main.py")
    print(f"\n3. Open your browser and go to:")
    print(f"   http://localhost:5000")
    print(f"\n{'='*60}")
    print("Enjoy using the Shuttle Management System! 🚌")
    print(f"{'='*60}")

def main():
    """Main setup function."""
    print("🚌 Shuttle Management System - Local Setup")
    print("This script will help you set up the application on your computer.")
    
    # Step 1: Check Python version
    print_step(1, "Checking Python Version")
    if not check_python_version():
        return
    
    # Step 2: Create virtual environment
    print_step(2, "Creating Virtual Environment")
    if not create_virtual_environment():
        return
    
    # Step 3: Install dependencies
    print_step(3, "Installing Dependencies")
    if not install_dependencies():
        return
    
    # Step 4: Create environment file
    print_step(4, "Creating Environment Configuration")
    create_env_file()
    
    # Step 5: Print next steps
    print_next_steps()

if __name__ == "__main__":
    main()
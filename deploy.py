#!/usr/bin/env python
"""
Deployment helper script for backpro
This script helps prepare the Django app for Render deployment
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}:")
        print(f"Command: {command}")
        print(f"Error: {e.stderr}")
        return None

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'requirements.txt',
        'build.sh',
        'render.yaml',
        'manage.py',
        'backendcm/settings.py'
    ]
    
    print("🔍 Checking required files...")
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
        else:
            print(f"✅ {file} found")
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files found")
    return True

def main():
    print("🚀 Django Render Deployment Helper")
    print("==================================")
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Check requirements
    if not check_requirements():
        print("\n❌ Please ensure all required files are present before deployment")
        sys.exit(1)
    
    # Test Django setup
    print("\n🧪 Testing Django configuration...")
    
    # Check if virtual environment is active
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Warning: Virtual environment not detected. Consider using one for local development.")
    
    # Test Django commands
    run_command("python manage.py check", "Django configuration check")
    run_command("python manage.py check --deploy", "Django deployment check")
    
    print("\n🎉 Pre-deployment checks completed!")
    print("\nNext steps:")
    print("1. Push your code to GitHub")
    print("2. Create a new Web Service on Render")
    print("3. Connect your GitHub repository")
    print("4. Deploy with the provided render.yaml configuration")
    print("\nYour backend will be available at: https://backpro.onrender.com")

if __name__ == "__main__":
    main()

#!/bin/bash

# Ensure pip is installed
python -m ensurepip --default-pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate --noinput

# Deployment finished successfully
echo "Deployment completed successfully!"
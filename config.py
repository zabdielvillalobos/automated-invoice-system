import os
from dotenv import load_dotenv

# Load environment variables from .env file if needed (you can skip this if you don't use .env)
load_dotenv()

class Config:
    SECRET_KEY = '0a7780ad23f2c5d09cb3bcfd049ed5b4f803b41af248d949080fc45206b936bd'  # Your secret key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///invoices.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', 'your_stripe_public_key')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', 'your_stripe_secret_key')



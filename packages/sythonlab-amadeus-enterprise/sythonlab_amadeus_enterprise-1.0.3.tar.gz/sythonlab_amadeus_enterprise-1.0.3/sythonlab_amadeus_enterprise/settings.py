import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(os.path.join(BASE_DIR, '.env'))

AMADEUS_CONFIG = {
    'OFFICE_ID': os.getenv('AMADEUS_OFFICE_ID'),
    'USERNAME': os.getenv('AMADEUS_USERNAME'),
    'PASSWORD': os.getenv('AMADEUS_PASSWORD'),
    'ENDPOINT': os.getenv('AMADEUS_FLIGHT_ENDPOINT'),
}

"""Centralized constants for VicAlerts with environment variable overrides."""

import os

# Feed configuration
FEED_URL = os.environ.get(
    "VICALERTS_FEED_URL",
    "https://emergency.vic.gov.au/public/events-geojson.json"
)

# Database configuration
DEFAULT_DB_PATH = os.environ.get(
    "VICALERTS_DB_PATH",
    "vicalerts.sqlite"
)

# Polling configuration
DEFAULT_INTERVAL = int(os.environ.get(
    "VICALERTS_INTERVAL",
    "60"
))  # seconds

MIN_INTERVAL = int(os.environ.get(
    "VICALERTS_MIN_INTERVAL",
    "10"
))  # seconds

# HTTP client configuration
DEFAULT_TIMEOUT = float(os.environ.get(
    "VICALERTS_TIMEOUT",
    "30.0"
))  # seconds

# Retry configuration
MAX_RETRIES = int(os.environ.get(
    "VICALERTS_MAX_RETRIES",
    "3"
))

RETRY_DELAYS = [1, 2, 4]  # seconds between retries
#!/usr/bin/env python3
import sqlite3
import sys
from datetime import datetime, timedelta

try:
    # Connect to database
    conn = sqlite3.connect('/data/vicalerts.db')
    cur = conn.cursor()

    # Check if database is accessible
    cur.execute('SELECT COUNT(*) FROM feeds_raw')
    count = cur.fetchone()[0]
    if count == 0:
        print("ERROR: Database is empty")
        sys.exit(1)

    # Check for recent activity (within last 5 minutes)
    cur.execute('''
        SELECT MAX(fetched_at) FROM feeds_raw
    ''')
    last_fetch = cur.fetchone()[0]

    if last_fetch:
        # Parse ISO format timestamp with timezone
        from dateutil import parser
        last_fetch_dt = parser.isoparse(last_fetch)
        from datetime import timezone
        now = datetime.now(timezone.utc)
        time_diff = now - last_fetch_dt

        if time_diff > timedelta(minutes=5):
            print(f"ERROR: No new data in {time_diff.total_seconds()/60:.1f} minutes")
            sys.exit(1)
        else:
            print(f"OK: Last update {time_diff.total_seconds()/60:.1f} minutes ago")
            sys.exit(0)
    else:
        print("ERROR: Cannot determine last update time")
        sys.exit(1)

except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)
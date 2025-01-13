from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz

# Define timezone
tz = pytz.timezone("Asia/Dhaka")  # Adjust for your timezone

# Create a calendar
cal = Calendar()
cal.add('prodid', '-//AI Learning Schedule//mxm.dk//')
cal.add('version', '2.0')

# Define start date
start_date = datetime(2025, 1, 14, tzinfo=tz)

# Define daily schedule
daily_schedule = [
    ("Exercise & Breakfast", timedelta(hours=7), timedelta(hours=1)),
    ("Morning Learning: Topic 1", timedelta(hours=8), timedelta(hours=1.5)),
    ("Break", timedelta(hours=9.5), timedelta(minutes=30)),
    ("Coding Practice", timedelta(hours=10), timedelta(hours=2)),
    ("Lunch & Relax", timedelta(hours=12), timedelta(hours=1)),
    ("Project Work", timedelta(hours=13), timedelta(hours=1.5)),
    ("Community Engagement", timedelta(hours=14.5), timedelta(minutes=30)),
    ("Advanced Learning", timedelta(hours=15), timedelta(hours=1.5)),
    ("Break", timedelta(hours=16.5), timedelta(minutes=30)),
    ("Revision and Notes", timedelta(hours=17), timedelta(hours=1)),
    ("Dinner & Relax", timedelta(hours=18), timedelta(hours=1)),
    ("Project Sharing on GitHub", timedelta(hours=19), timedelta(hours=1)),
    ("Free Exploration", timedelta(hours=20), timedelta(hours=1)),
    ("Relax and Prepare for Bed", timedelta(hours=21), timedelta(hours=1))
]

# Generate events for 7 days (1 week of routine)
for day in range(7):
    day_date = start_date + timedelta(days=day)
    for event_name, start_time, duration in daily_schedule:
        event = Event()
        event_start = day_date + start_time
        event_end = event_start + duration
        event.add('summary', event_name)
        event.add('dtstart', event_start)
        event.add('dtend', event_end)
        event.add('dtstamp', datetime.now(tz))
        event.add('description', f"Scheduled activity: {event_name}")
        cal.add_component(event)

# Save the calendar as an ICS file
ics_file_path = "AI_ML_Learning_Schedule.ics"
with open(ics_file_path, 'wb') as f:
    f.write(cal.to_ical())

print(f"ICS file created at: {ics_file_path}")

import datetime
import pytz

def get_local_time(country):
    tz = pytz.timezone(country)
    local_time = datetime.datetime.now(tz)
    return local_time.strftime('%Y-%m-%d %H:%M:%S')

countries = {
    'India': 'Asia/Kolkata',
    'USA': 'America/New_York',
    'Saudi Arabia': 'Asia/Riyadh'
}

while True:
    print("Current Time:")
    for country, timezone in countries.items():
        current_time = get_local_time(timezone)
        print(f"{country}: {current_time}")
    print("---------------------------")

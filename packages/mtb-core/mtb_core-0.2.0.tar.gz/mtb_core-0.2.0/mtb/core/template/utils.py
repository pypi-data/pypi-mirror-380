import datetime

import requests


def get_current_datetime_string():
    """Get the current time and date in the format "DAY DDth MONTH YYYY HH:MM"."""
    now = datetime.datetime.now()
    day_name = now.strftime("%A")
    day = now.day
    day_suffix = "th"
    if 4 <= day <= 20 or day > 20 and day % 10 == 0:
        day_suffix = "th"
    elif day % 10 == 1 and day != 11:
        day_suffix = "st"
    elif day % 10 == 2 and day != 12:
        day_suffix = "nd"
    elif day % 10 == 3 and day != 13:
        day_suffix = "rd"
    month_name = now.strftime("%B")
    year = now.year
    hour = now.hour
    minute = now.minute
    return f"{day_name} {day}{day_suffix} {month_name} {year} {hour:02}:{minute:02}"


def get_geolocation_string(timeout=10):
    """
    Get the geolocation as a human string (city, country) using ipinfo.io.

    Requires no API key for basic usage.
    """
    try:
        response = requests.get("https://ipinfo.io", timeout=timeout)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        city = data.get("city", "Unknown City")
        country = data.get("country", "Unknown Country")
        timezone = data.get("timezone", "Unknown Timezone")
        region = data.get("region", "Unknown Region")

        return {"city": city, "country": country, "timezone": timezone, "region": region}

    except requests.exceptions.RequestException as e:
        return f"Error getting geolocation: {e}"


if __name__ == "__main__":
    print(get_current_datetime_string())
    print(get_geolocation_string())

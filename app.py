import streamlit as st
from datetime import datetime
import pytz
import time

# List of cities and their time zones
cities = [
    {'name': 'New York', 'timezone': 'America/New_York'},
    {'name': 'London', 'timezone': 'Europe/London'},
    {'name': 'Tokyo', 'timezone': 'Asia/Tokyo'},
    {'name': 'Sydney', 'timezone': 'Australia/Sydney'}
]

# Main page: World Clock App
def world_clock_page():
    st.title('World Clock App')
    st.write('Select the cities to display their current time:')

    # Function to get current time for a given city
    def get_current_time(city):
        tz = pytz.timezone(city['timezone'])
        current_time = datetime.now(tz)
        return current_time.strftime('%Y-%m-%d %H:%M:%S')
    
    # Function to get current UNIX timestamp
    def get_unix_timestamp():
        return int(datetime.now().timestamp())

    # Multi-select widget to choose cities
    selected_cities = st.multiselect('Select cities:', [city['name'] for city in cities], default=['New York'])

    # Create placeholders for displaying time
    time_placeholders = {city['name']: st.empty() for city in cities}
    timestamp_placeholders = {city['name']: st.empty() for city in cities}

    # Display current time for selected cities
    while True:
        for city in cities:
            if city['name'] in selected_cities:
                current_time = get_current_time(city)
                time_placeholders[city['name']].text(f"{city['name']}: {current_time}")
                # Display UNIX timestamp
                timestamp_placeholders[city['name']].text(f"UNIX Timestamp ({city['name']}): {get_unix_timestamp()}")
        time.sleep(1)  # Update every second

# Convert UNIX timestamp to human-readable time page
def unix_to_human_page():
    # Function to convert UNIX timestamp to human-readable time
    def unix_to_human(unix_timestamp):
        try:
            unix_timestamp = int(unix_timestamp)
            human_time = datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')
            return human_time
        except ValueError:
            return "Invalid UNIX timestamp"
        
    st.title('Convert UNIX Timestamp to Human Time')
    unix_timestamp = st.text_input('Enter UNIX timestamp:')
    human_time = unix_to_human(unix_timestamp)
    st.write('Human Time:', human_time)

# Navigation
pages = {
    "World Clock": world_clock_page,
    "UNIX to Human Time": unix_to_human_page
}

# Sidebar with page selection
selected_page = st.sidebar.radio("Select Page", list(pages.keys()))

# Display selected page
pages[selected_page]()
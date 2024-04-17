import os
import requests
import re

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
CHANNEL_ID = 'UCjf4X2qXcTHa7KoN3m7VKCg'
API_URL = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={YOUTUBE_API_KEY}"

def fetch_stats():
    response = requests.get(API_URL).json()
    stats = response['items'][0]['statistics']
    return {
        'subscriberCount': stats['subscriberCount'],
        'viewCount': stats['viewCount'],
        'videoCount': stats['videoCount']
    }

def update_readme(stats):
    with open('README.md', 'r') as file:
        readme_contents = file.read()

    def replace_count(match):
        label = match.group(1)
        # Constructing key correctly based on actual stat names in the dictionary
        key_map = {'Subscribers': 'subscriberCount', 'Views': 'viewCount', 'Videos': 'videoCount'}
        key = key_map[label]  # This will now correctly map the label to the dictionary key
        new_count = stats[key]  # Safely fetch the count using the correct key
        return f"{label}-{new_count}"

    # Use regex to dynamically find and replace subscriber, view, and video counts in the README
    new_contents = re.sub(r"(Subscribers|Views|Videos)-\d+", replace_count, readme_contents)

    with open('README.md', 'w') as file:
        file.write(new_contents)

if __name__ == "__main__":
    stats = fetch_stats()
    update_readme(stats)

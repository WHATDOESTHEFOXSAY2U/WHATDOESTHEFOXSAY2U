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

    # Regex to find existing counts and replace them
    def replace_count(match):
        label = match.group(1)  # Get the label part ('Subscribers', 'Views', 'Videos')
        new_count = stats[f'{label.lower()}Count']  # Match label to stat key and get new count
        return f"{label}-{new_count}"

    # Use regular expression to replace all occurrences of subscriber, view, and video counts
    new_contents = re.sub(r"(Subscribers|Views|Videos)-\d+", replace_count, readme_contents)

    with open('README.md', 'w') as file:
        file.write(new_contents)

if __name__ == "__main__":
    stats = fetch_stats()
    update_readme(stats)

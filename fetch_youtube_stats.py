import os
import requests
import re

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
CHANNEL_ID = 'UCjf4X2qXcTHa7KoN3m7VKCg'
API_URL = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={YOUTUBE_API_KEY}"

def fetch_stats():
    response = requests.get(API_URL).json()
    stats = response['items'][0]['statistics']
    print("Fetched Stats:", stats)  # Print to verify correct fetching of stats
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
        key = f"{label.lower()}Count"
        print("Label and Key being used:", label, key)  # Debugging to verify the correct key is formed
        if key in stats:
            new_count = stats[key]
            return f"{label}-{new_count}"
        else:
            print(f"KeyError: '{key}' not found in stats")  # Print error if key not found
            return match.group(0)  # Return the original match if key is not found

    new_contents = re.sub(r"(Subscribers|Views|Videos)-\d+", replace_count, readme_contents)
    print("Updated README Content:", new_contents)  # Print the updated contents for verification

    with open('README.md', 'w') as file:
        file.write(new_contents)

if __name__ == "__main__":
    stats = fetch_stats()
    update_readme(stats)

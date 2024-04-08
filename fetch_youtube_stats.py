
import os
import requests

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
CHANNEL_ID = 'UCjf4X2qXcTHa7KoN3m7VKCg'
API_URL = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={YOUTUBE_API_KEY}"

def fetch_stats():
    response = requests.get(API_URL).json()
    print("API Response:", response)  # Add this line to log the API response
    stats = response['items'][0]['statistics']
    return {
        'subscriberCount': stats['subscriberCount'],
        'viewCount': stats['viewCount'],
        'videoCount': stats['videoCount']
    }

def update_readme(stats):
    with open('README.md', 'r') as file:
        readme_contents = file.read()

    # Replace 'Number' with actual stats in the badge URLs
    new_contents = readme_contents.replace("Subscribers-Number", f"Subscribers-{stats['subscriberCount']}")
    new_contents = new_contents.replace("Views-Number", f"Views-{stats['viewCount']}")
    new_contents = new_contents.replace("Videos-Number", f"Videos-{stats['videoCount']}")

    with open('README.md', 'w') as file:
        file.write(new_contents)


if __name__ == "__main__":
    stats = fetch_stats()
    update_readme(stats)

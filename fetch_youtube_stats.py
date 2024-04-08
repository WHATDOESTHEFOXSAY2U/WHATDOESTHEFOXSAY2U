
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

    # Define new badge URLs with Markdown image syntax
    new_subscribers_badge = "![Subscribers](https://img.shields.io/badge/dynamic/json?color=blue&label=Subscribers&query=$.subscriberCount&url=https%3A%2F%2Fyoutube-channel-stats.vercel.app%2Fapi%2Fsubscribers%3FchannelID%3D" + CHANNEL_ID + "&style=for-the-badge&logo=YouTube)"
    new_views_badge = "![Views](https://img.shields.io/badge/dynamic/json?color=important&label=Views&query=$.viewCount&url=https%3A%2F%2Fyoutube-channel-stats.vercel.app%2Fapi%2Fviews%3FchannelID%3D" + CHANNEL_ID + "&style=for-the-badge&logo=YouTube)"
    new_videos_badge = "![Videos](https://img.shields.io/badge/dynamic/json?color=red&label=Videos&query=$.videoCount&url=https%3A%2F%2Fyoutube-channel-stats.vercel.app%2Fapi%2Fvideos%3FchannelID%3D" + CHANNEL_ID + "&style=for-the-badge&logo=YouTube)"

    # Direct string replacement based on the placeholders or existing URLs
    # Ensure these placeholders or parts of the existing URLs are unique and identifiable
    readme_contents = readme_contents.replace("EXISTING_SUBSCRIBERS_BADGE_URL", new_subscribers_badge)
    readme_contents = readme_contents.replace("EXISTING_VIEWS_BADGE_URL", new_views_badge)
    readme_contents = readme_contents.replace("EXISTING_VIDEOS_BADGE_URL", new_videos_badge)

    with open('README.md', 'w') as file:
        file.write(readme_contents)


if __name__ == "__main__":
    stats = fetch_stats()
    update_readme(stats)

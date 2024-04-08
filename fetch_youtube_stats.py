
import os
import requests

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
CHANNEL_ID = 'UCjf4X2qXcTHa7KoN3m7VKCg'
print(YOUTUBE_API_KEY, CHANNEL_ID)
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
    new_subscribers_badge = f"![Subscribers](https://img.shields.io/badge/dynamic/json?color=blue&label=Subscribers&query=$.subscriberCount&url=https%3A%2F%2Fyoutube-channel-stats.vercel.app%2Fapi%2Fsubscribers%3FchannelID%3D{CHANNEL_ID}&style=for-the-badge&logo=YouTube)"
    new_views_badge = f"![Views](https://img.shields.io/badge/dynamic/json?color=important&label=Views&query=$.viewCount&url=https%3A%2F%2Fyoutube-channel-stats.vercel.app%2Fapi%2Fviews%3FchannelID%3D{CHANNEL_ID}&style=for-the-badge&logo=YouTube)"
    new_videos_badge = f"![Videos](https://img.shields.io/badge/dynamic/json?color=red&label=Videos&query=$.videoCount&url=https%3A%2F%2Fyoutube-channel-stats.vercel.app%2Fapi%2Fvideos%3FchannelID%3D{CHANNEL_ID}&style=for-the-badge&logo=YouTube)"

    # Pattern to find within the README to replace
    subscriber_pattern = "![Subscribers]("  # Adjust these patterns to match the start of your existing badge URLs
    view_pattern = "![Views]("
    videos_pattern = "![Videos]("

    # Replacing the old badge URLs with new ones
    readme_contents = readme_contents.replace(subscriber_pattern, new_subscribers_badge, 1)  # Use count=1 to replace only the first occurrence
    readme_contents = readme_contents.replace(view_pattern, new_views_badge, 1)
    readme_contents = readme_contents.replace(videos_pattern, new_videos_badge, 1)

    with open('README.md', 'w') as file:
        file.write(readme_contents)

if __name__ == "__main__":
    stats = fetch_stats()
    update_readme(stats)

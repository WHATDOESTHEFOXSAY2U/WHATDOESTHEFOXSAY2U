
import os
import requests

API_KEY = os.getenv('API_KEY')
CHANNEL_ID = 'UCjf4X2qXcTHa7KoN3m7VKCg'
API_URL = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={API_KEY}"

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

    # Construct the new URLs for badges
    subs_badge_url = f"https://img.shields.io/badge/dynamic/json?color=blue&label=Subscribers&query=subscriberCount&url=https%3A%2F%2Fyoutube-channel-stats.vercel.app%2Fapi%2Fsubscribers%3FchannelID%3D{CHANNEL_ID}"
    views_badge_url = f"https://img.shields.io/badge/dynamic/json?color=green&label=Views&query=viewCount&url=https%3A%2F%2Fyoutube-channel-stats.vercel.app%2Fapi%2Fviews%3FchannelID%3D{CHANNEL_ID}"
    videos_badge_url = f"https://img.shields.io/badge/dynamic/json?color=red&label=Videos&query=videoCount&url=https%3A%2F%2Fyoutube-channel-stats.vercel.app%2Fapi%2Fvideos%3FchannelID%3D{CHANNEL_ID}"

    # Replace placeholders in the README contents
    readme_contents = readme_contents.replace('placeholder_url_subscribers', subs_badge_url)
    readme_contents = readme_contents.replace('placeholder_url_views', views_badge_url)
    readme_contents = readme_contents.replace('placeholder_url_videos', videos_badge_url)

    with open('README.md', 'w') as file:
        file.write(readme_contents)

if __name__ == "__main__":
    stats = fetch_stats()
    update_readme(stats)

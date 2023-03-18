import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
import datetime
from datetime import timedelta
from googleapiclient.http import MediaFileUpload
import time
import random
import pytz
from art import *

art_1 = text2art('YT BOT BY ARGUE')
print(art_1)


# Set up OAuth2 credentials
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('api/token.json')
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('api/youtube.json', scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
        creds = flow.run_local_server(port=0)
        
    # Save the credentials for the next run
    with open('token.json', 'w') as token_file:
        token_file.write(creds.to_json())
    with open('token.json', 'w') as token_file:
        token_file.write(creds.to_json())

# Set up YouTube API client
youtube = build('youtube', 'v3', credentials=creds)

print('Youtube Api Logged In')

with open('title.txt', 'r') as f:
    title = f.read().strip()
    
# Set your timezone
local_tz = pytz.timezone('Asia/Kolkata')

# Set the initial scheduled upload time to the current time plus 15 minutes
scheduled_time = datetime.datetime.now(local_tz) + timedelta(minutes=15)


print(f'Current time : {scheduled_time}')

videoFolder = 'videos'
titleNum = 1

for video_file in os.listdir(videoFolder):
    if video_file.endswith('.mp4'):
        # Create a new video object and set its attributes
        video_path = os.path.join(videoFolder, video_file)
        video = {
            'snippet': {
                'title': f'{title} - # {titleNum}',
                'description': '',
                'categoryId': '22',
                'tags': ['#argue', '#argue', '#argue'],
                'defaultLanguage': 'en'
            },
            'status': {
                'privacyStatus': 'unlisted',
                'selfDeclaredMadeForKids': False,
            }
        }

        # Upload the video to YouTube
        try:
            response = youtube.videos().insert(
                part='snippet,status',
                body=video,
                media_body=MediaFileUpload(video_path)
            ).execute()

            video_id = response['id']
            print(f'The video was uploaded with ID: {video_id}')

            # Schedule the video to be published
            publish_time = scheduled_time
            update = {'id': video_id, 'status': {'publishAt': publish_time.strftime('%Y-%m-%dT%H:%M:%SZ'), 'privacyStatus': 'private'}}
            youtube.videos().update(part='status', body=update).execute()

            print(f'Video "{video_file}" scheduled for {scheduled_time.strftime("%Y-%m-%d %H:%M:%S")} IST')

        except HttpError as error:
            print(f'An HTTP error {error.resp.status} occurred: {error.content}')

        # Increment the scheduled upload time by 15 minutes for the next video
        scheduled_time += timedelta(minutes=40)
        titleNum += 1
        randInt = random.randint(4,10)
        time.sleep(randInt)




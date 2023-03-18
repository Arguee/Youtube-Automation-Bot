# Youtube Upload and Schedule Bot

This is a youtube bot which uploads youtube video present in Videos folder one by one and schedule each video on 30 minutes interval





## Authors

- [@Argue](https://github.com/Arguee/)


## Requirements
+ ``` pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pytz art```


## Steps
+ Go to the Google Cloud Console [Cloud Console](https://console.cloud.google.com/) and create a new project.
+ Once you have created the project, click on the hamburger menu on the top-left corner, and navigate to APIs & Services > Dashboard.
+ Click on "+ ENABLE APIS AND SERVICES" button, and search for "YouTube Data API v3". Select it and enable the API.
+ Navigate to APIs & Services > Credentials, and click on "+ CREATE CREDENTIALS". Select "OAuth client ID".
+ Configure the OAuth consent screen with your bot's name and email address. Choose "External" as the user type
+ Select "Desktop app" as the application type, give it a name, and create the client ID.
+ Download the client secret JSON file by clicking the download icon next to the client ID.
+ And Save it as `youtube.json` in `api folder`.


## Uploader

You can configure more in `bot.py`.
## Feedback

If you have any feedback, please reach out tome at 
`!Argue#6693` on Discord


## Work

Seeking work for my Porfolio contact me via Discord.

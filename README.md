# <div align = "center"> Youtube Automation Bot </div> </a>

![Youtube x Python Image](https://res.cloudinary.com/practicaldev/image/fetch/s--UJMX0wcf--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kr8qigb94o7vbyjfap9k.jpg)


<p align=center>This is a semi-automated youtube bot which allows users to upload multiple videos in bulk, eliminating the need for manual uploading one video at a time. This saves significant time and effort, especially for channels with frequent content releases. The bot offers a scheduling feature that enables users to specify the interval between each video upload. Users have the flexibility to set specific intervals between video uploads according to their channel's requirements.</p>



## Programmed By

- [@Argue](https://github.com/Arguee/)


## Requirements
+ ``` pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pytz art```

## Note
+ You can upload max 6 videos with this bot daily, but I recommend uploading 5 videos. This is because of the youtube api's daily quota limit.

## Steps
+ Go to the Google Cloud Console [Cloud Console](https://console.cloud.google.com/) and create a new project.
+ Once you have created the project, click on the hamburger menu on the top-left corner, and navigate to APIs & Services > Dashboard.
+ Click on "+ ENABLE APIS AND SERVICES" button, and search for "YouTube Data API v3". Select it and enable the API.
+ Navigate to APIs & Services > Credentials, and click on "+ CREATE CREDENTIALS". Select "OAuth client ID".
+ Configure the OAuth consent screen with your bot's name and email address. Choose "External" as the user type
+ Select "Desktop app" as the application type, give it a name, and create the client ID.
+ Download the client secret JSON file by clicking the download icon next to the client ID.
+ And Save it as `youtube2.json` in `api folder`.


## Uploader

+ You can configure more in `bot.py`.
+ Change text from `title.txt` to your videos title.
## Feedback

If you have any feedback, please reach out to me at 
`!Argue#6693` on Discord


## Work

Seeking work for my Porfolio contact me via Discord.

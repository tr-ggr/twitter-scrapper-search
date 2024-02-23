from tweety import Twitter
import http.client, urllib
from datetime import datetime, timedelta
import pytz
import keyboard
import time
import pickle

utc=pytz.UTC
username = "@BobetSchol7943"
password = "IamStupid12"

app = Twitter("session")
app.sign_in(username, password)
print(app.user)

dbfile = open('dbfile.pkl', 'rb')    
db = pickle.load(dbfile)

tweetSet = db

dbfile.close()

while(not keyboard.is_pressed('q')):
  print("Starting scrape!")
  time.sleep(5)
  tweets = app.search('lf commissioner')
  for tweet in tweets:
      if tweet.id in tweetSet:
        continue

      else:
        datetime_start = tweet.created_on.replace(tzinfo=utc) 
        datetime_end = (datetime.now() - timedelta(days=1)).replace(tzinfo=utc)

        if(datetime_start > datetime_end):
            print(tweet.created_on)
            conn = http.client.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
              urllib.parse.urlencode({
                "title": "COMMISSION ALERT!",
                "token": "a1hwwg2fsyaa3y2jpc34fm23wywjvm",
                "user": "ufd51y9n28co3dkaqrifiad9ko9xdp",
                "message": "https://twitter.com/cheese4139/status/" + tweet.id,
              }), { "Content-type": "application/x-www-form-urlencoded" })
            conn.getresponse()

        tweetSet.add(tweet.id)


dbfile = open('dbfile.pkl' , 'ab')
pickle.dump(tweetSet, dbfile);
dbfile.close()


      

    

from tweety import Twitter
import http.client, urllib
from datetime import datetime, timedelta
import pytz
import keyboard
import time
import pickle

def appSearch(filter):
  tweets = app.search(filter)
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

utc=pytz.UTC
username = "@"
password = ""

app = Twitter("session")
app.sign_in(username, password)
print(app.user)

dbfile = open('dbfile.pkl', 'rb')


try:
  tweetSet = pickle.load(dbfile)
except EOFError:
   tweetSet = set()



dbfile.close()

while(not keyboard.is_pressed('q')):
  print("Starting scrape!")
  time.sleep(1800)
  appSearch("lf commissioner")
  appSearch("lf programmer")
  appSearch("lf java")
  appSearch("lf program")
  




dbfile = open('dbfile.pkl' , 'ab')
pickle.dump(tweetSet, dbfile);
dbfile.close()



import tweepy, time, sys
from secret.keytokens import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

argfile = str(sys.argv[1])

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

for line in f:
    post = line + ' ~Jack\'s Twitter Robot'
    api.update_status(post) #updates twitter status
    print('Posted the following: %s' % post)
    time.sleep(120) #sleeps 120 seconds

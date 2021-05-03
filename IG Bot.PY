from instabot import Bot
from PIL import Image
im = Image.open("") #PASTE IMAGE PATH HERE".
newsize = (1080, 1080) #THIS WILL RESIZE THE IMAGE SO IT WILL FIT IG'S PARAMETERS.
im1 = im.resize(newsize)
im1.save('') #SAVE YOUR NEWLY RESIZED IMAGE.

bot = Bot()
bot.login(username = "", password = "") #INSERT IG CREDENTIALS
bot.upload_photo("", caption ="This post was uploaded using Python automation")

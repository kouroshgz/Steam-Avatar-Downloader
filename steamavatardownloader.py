from urllib import request as req
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# get profile id
print("https://steamcommunity.com/id/[THIS PART IS WHAT YOU ENTER]")
print('Check for spelling / case mistakes!')
print('Avatar will be downloaded to folder directory containing steamavatardownloader.py')
profileID = input("Enter steam profile id: ")
# variable holding desired URL
myUrl = "https://steamcommunity.com/id/" + profileID
# Open Connection + Grab page
uClient = uReq(myUrl)
# Variable stores raw html
pageHtml = uClient.read()
# Close Connection
uClient.close()
# Parse html
pageSoup = soup(pageHtml, "html.parser")
# locate profile avatar url
if pageSoup.find('meta', property="og:image"):
    avatarUrl = pageSoup.find('meta', property="og:image")['content']
    # create substring containing avatar file name
    file = avatarUrl.split("/avatars/")
    avatar = file[1][3:]
    # download profile avatar
    req.urlretrieve(avatarUrl, avatar)
    print("Avatar successfully downloaded")
else: # messages if profile/avatar cant be located
    print("Could not find steam profile/avatar")
    print("Check your spelling and run the script again")







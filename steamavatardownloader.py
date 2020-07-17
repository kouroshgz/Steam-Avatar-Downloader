from urllib import request as req
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# get profile id and privacy settings
print("https://steamcommunity.com/id/[THIS PART IS WHAT YOU ENTER]")
print('Check for spelling / case mistakes!')
print('Avatar will be downloaded to folder directory containing steamavatardownloader.py')
repeat = True

def dict(repeat):
    return {
            "y": True,
            "Y": True,
            "n": False,
            "N": False,
        }.get(repeat, False)

while repeat == True:
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
	if pageSoup.find('div', {"class":"playerAvatarAutoSizeInner"}):
		avatarUrl = pageSoup.find('div', {"class":"playerAvatarAutoSizeInner"}).find('img', recursive = False)['src']
		# create substring containing avatar file name
		print(avatarUrl)
		file = avatarUrl.split("/avatars/")
		avatar = file[1][3:]
		# download profile avatar
		req.urlretrieve(avatarUrl, avatar)
	else: # messages if profile/avatar cant be located
		print("Could not find steam profile/avatar or you mistyped Y/N response")
		print("Check your spelling and run the script again")
	# Prompt another profile search
	repeat = input("Search for another profile? (Y/N):" )
	repeat = dict(repeat)










# Steam-Avatar-Downloader
Simple python script that downloads a specified profile's steam avatar.
Python 3.8.3 

# Usage
The script will prompt the user to enter the steam profile ID of the profile with the desired avatar in the following format:
https://steamcommunity.com/id/ [THIS PART IS WHAT YOU ENTER]

ex: https://steamcommunity.com/id/exampleprofilepleasedontexist

Will output message "Avatar succesfully downloaded" if avatar acquisition is successfull. 
Will output message "Could not find steam profile/avatar
                     Check your spelling and run the script again"
if the inputted profile id does not match with an existing steam user profile.
Wil return an index error if the supplied user profile id belongs to a private profile. 

Note: input must be spelled exactly as it appears on the users steam profile URL and the script doesnt currently work with profiles set to private, 
although this will be fixed soon.


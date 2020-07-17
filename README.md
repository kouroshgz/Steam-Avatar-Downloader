# Steam-Avatar-Downloader
Simple python script that downloads a specified profile's steam avatar.

Python 3.8.3, Beautiful Soup 4

# Usage
The script will prompt the user to enter the steam profile ID of the profile with the desired avatar in the following format:
https://steamcommunity.com/id/ [THIS PART IS WHAT YOU ENTER]

ex: https://steamcommunity.com/id/kouroshgz

Following successful avatar acquisition, there will be a (Y/N) prompt asking the user if they wish to search for another profile.

# Recent Changes (as of 7/16/20)
- No longer need to specify if a profile is private or public

- Fixed bug that prevented avatar acquisition if profile was using an avatar frame

- Reduced code redundancy  

- Support for multiple profile acquisition added

- Support for private profile avatar acquisition added

See commit history for complete details



#Created by Jared-Base for the "Beginners Guide to (almost) Everything SpaceX" website
#Generates a .txt file that uploads to GitHub and is then displaied on the site using HTML Code
#Uses the Launch Library website to get info

import requests #Used to get info from sites
from github import Github #Used to upload file to GitHub
import json #May not actually need but whatever 
from datetime import datetime #Used to get current date and time

#GitHub Login or Token
g = Github("username", "password")

#Get Basic Launch Info
launch = requests.get("https://launchlibrary.net/1.4/launch?next=1&location=17&location=16" ).json()['launches'][0]

#Prints Launch Info to Console
print(launch['name'])
print("No Earlier Than: ")
print(launch['net'])
print("Launch Window")
print(launch['windowstart'])
print(launch['windowend'])

#Determine if Instantaneous Launch Window
#if launch ['windowstart'] == launch['windowend']:
 #   print("Instantaneous Launch Window")
    
#Assign Variables    
mission = launch['name']
winstart = launch['windowstart']
winend = launch['windowend']
launchid = launch['id']

#Get More Launch Info using the Launch ID
morelaunchinfo = requests.get("http://launchlibrary.net/1.4/launch/" + str(launchid)).json()['launches'][0]['location']['pads'][0]

#Prints More Launch Info to Console
print('Launch Pad:')
print(morelaunchinfo['name'])

#Get Current Date and Time
t = datetime.now()
#d = datetime.date.now()
print("Current Date: " + str(t.month) + "/" + str(t.day) + "/"+ str(t.year))
print("Current Time: " + str(t.hour) + ":" + str(t.minute))
print("Timezone: Eastern Standard Time (UTC-5)")
#dt = t

#Create Commit Message for GitHub (info about the upload)
last_update = str("Last updated: " + str(t.month) + "/" + str(t.day) + "/"+ str(t.year) + " at " + str(t.hour) + ":" + str(t.minute) + " UTC")

#Assign Variables for Date and Time (c = Current)
cm = t.month
cd = t.day
cy = t.year
cth = t.hour
ctm = t.minute

#Create File for Site
file_output = '''%s

No Earlier Than:
%s

Window Start:
%s UTC

Window End:
%s UTC

Launch Pad:
%s

Last Updated: %s/%s/%s (MM/DD/YYYY)  %s:%s (UTC) 
'''
#Only UTC-5 on PC, normal UTC on RPi

#Optional Local File Writing
#f= open("next_mission.txt","w")
#f.write(file_output % (launch['name'], launch['net'], launch['windowstart'], launch['windowend'], morelaunchinfo['name'], cm, cd, cy, cth, ctm))
#f.close()

#Find Repository
repo = g.get_user().get_repo('repo')
#Not quite sure what this does; saw it in a tutorial so i included it
file = repo.get_file_contents("file to replace")

#Commit Updated File to GitHub
repo.update_file("file to replace", last_update, file_output % (launch['name'], launch['net'], launch['windowstart'], launch['windowend'], morelaunchinfo['name'], cm, cd, cy, cth, ctm), file.sha)
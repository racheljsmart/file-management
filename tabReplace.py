#!/usr/bin/env python3


pidsFile = '/home/rs15r/pids.txt' #path to the list of pids
newPidsFile = '/home/rs15r/new_pids.txt' #path to the new file to be written to
new_pid = open(newPidsFile, 'w') #opens the new file to be written to
pidf = open(pidsFile, 'r') #reading pids.txt and assigning the contents of the file as a vairable pidf


for line in pidf: #for every line in the file...
	pid = line.replace('\t','').replace('\r\n','') #check every line in the file for tabs and line breaks, replace them with no characters
	#print(pid) #view the output
	new_pid.write(pid + '\r\n') #write changed pid to new file

#FFQBs2
#FFQBs.py
import os
from bs4 import BeautifulSoup
import urllib2

# CONSTANT VARIABLES
output_file_path = os.path.join(os.getcwd(), "OutFFQBs2.txt")
error_file_path = os.path.join(os.getcwd(), "ErrorfileFFQBs2.txt")

f = open(output_file_path,'w')
errorFile = open(error_file_path,'w')
url = [	
	"http://games.espn.com/ffl/leaders?&sortMap=AAAAARgAAAADAQ" \
	"AIY2F0ZWdvcnkDAAAAAwEABmNvbHVtbgMAAAABAQAJZGlyZWN0aW9uAwAAAAE%3" \
	"D&scoringPeriodId=",
	"&seasonId=2017&slotCategoryId=0&startIndex=0"
]


# Open page. Copy QBS - make a tuple out of that. I don't think I can do that 
#	with a findall
x=0
y=1
weeks = 17
nameQB=	[]
lists = [[] for i in xrange(weeks)]	
# Why do the bye week players get skipped and what does the '$0' thing mean 
#	in the inspected element
# I need to loop the projects beecause otherwsie column 23 will keep overwriting
#	itself
while (x<=weeks):   
	#Because we want the first 140 players. It's doing something weird where
	# it reloads the page and just grabs the top one in the row 
	#and change the start ponit in the table cause you can change the URL to
	# do that. NVM it's grabbing all then doing +40. Duh,cause that's the counter.
		soup = BeautifulSoup(urllib2.urlopen("{}{}{}".format(url[0]+ str(x) + url[1])).read(), 'html.parser')

		# This basically locates the table and grabs all of its infor
		tableStats = soup.find("table", {"class": "playerTableTable tableBody"}) 
		
		# This is what loops through the data. The [2:]: is somethign that 
		# says we want to start at number 2 and go throgugh the end
		for row in tableStats.findAll('tr')[2:]: 
				col = row.findAll('td')

				try:
					#.a = it's a link... we're asking for the text of the link. 
					# In this case were grabbig the player name				
					proj = col[23].string.strip() 
					float(proj)
					#print(name)
					#nameQB.append(name)
					#nameQB.encode("ascii")
					lists[x].append(proj)
					print(lists)	
				except Exception as e:
					errorFile.write (str(x)+ '*********' + str(e)+ '*********' + str(col) +'\n')

					#see the error, and move on don't get hung up 
					pass 
				
		x=x+1
#At this point I now have a list of all the qbs name





f.close
errorFile.close

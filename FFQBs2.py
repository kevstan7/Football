#FFQBs2
#FFQBs.py
from bs4 import BeautifulSoup
import urllib2

f = open('/Users/kevinstanley/documents/PythonProjects/OutFFQBs2.txt','w')
errorFile = open('/Users/kevinstanley/documents/PythonProjects/ErrorfileFFQBs2.txt','w')


#Open page. Copy QBS - make a tuple out of that. I don't think I can do that with a findall
x=0
y=1
weeks = 17
nameQB=	[]
lists = [[] for i in xrange(weeks)]	
#Why do the bye week players get skipped and what does the '$0' thing mean in the inspected element
#I need to loop the projects beecause otherwsie column 23 will keep overwriting itself
while (x<=weeks):   #Because we want the first 140 players. It's doing something weird where it reloads the page and just grabs the top one in the row 
	#and change the start ponit in the table cause you can change the URL to do that. NVM it's grabbing all then doing +40. Duh,cause that's the counter.
		soup = BeautifulSoup(urllib2.urlopen('http://games.espn.com/ffl/leaders?&sortMap=AAAAARgAAAADAQAIY2F0ZWdvcnkDAAAAAwEABmNvbHVtbgMAAAABAQAJZGlyZWN0aW9uAwAAAAE%3D&scoringPeriodId='+ str(x) + '&seasonId=2017&slotCategoryId=0&startIndex=0' ).read(), 'html.parser')

		tableStats = soup.find("table", {"class": "playerTableTable tableBody"}) #This basically locates the table and grabs all of its infor
		
		for row in tableStats.findAll('tr')[2:]: #This is what loops through the data. The [2:]: is somethign that says we want to start at number 2 and go throgugh the end
#			while(y<18):    #FACKKKKK
#				soup2 = BeautifulSoup(urllib2.urlopen('http://games.espn.com/ffl/leaders?&sortMap=AAAAARgAAAADAQAIY2F0ZWdvcnkDAAAAAwEABmNvbHVtbgMAAAABAQAJZGlyZWN0aW9uAwAAAAE%3D&scoringPeriodId=' +str(y) +'&seasonId=2017&slotCategoryId=0&startIndex=0.read(), 'html.parser')		

				col = row.findAll('td')

				try:
					proj = col[23].string.strip() #.a = it's a link... we're asking for the text of the link. In this case were grabbig the player name				
					float(proj)
					#print(name)
					#nameQB.append(name)
					#nameQB.encode("ascii")
					lists[x].append(proj)
					print(lists)	
				except Exception as e:
					errorFile.write (str(x)+ '*********' + str(e)+ '*********' + str(col) +'\n')

					pass #see the error, and move on don't get hung up 
				
		x=x+1
#At this point I now have a list of all the qbs name





f.close
errorFile.close

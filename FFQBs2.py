#FFQBs2
#FFQBs.py
import os
from bs4 import BeautifulSoup
import urllib2

# CONSTANT VARIABLES
output_file_path = os.path.join(os.getcwd(), "OutFFQBs2.txt") 
error_file_path = os.path.join(os.getcwd(), "ErrorfileFFQBs2.txt") #os.path.join does some magic shit where it finds 
#the path you're using and copies it in and saves the file there so that you can run this program on any computer

f = open(output_file_path,'w')
errorFile = open(error_file_path,'w')
url = [	
	"http://games.espn.com/ffl/leaders?&sortMap=AAAAARgAAAADAQ" \
	"AIY2F0ZWdvcnkDAAAAAwEABmNvbHVtbgMAAAABAQAJZGlyZWN0aW9uAwAAAAE%3" \
	"D&scoringPeriodId=",
	"&seasonId=2017&slotCategoryId=0&startIndex=0"
]
#http://games.espn.com/ffl/leaders?&sortMap=AAAAARgAAAADAQAIY2F0ZWdvcnkDAAAAAwEABmNvbHVtbgMAAAABAQAJZGlyZWN0aW9uAwAAAAE%3D&scoringPeriodId=1&seasonId=2017&slotCategoryId=0&startIndex=0

# Open page. Copy QBS - make a tuple out of that. I don't think I can do that 
#	with a findall
x=0
y=1
weeks = 17
listnameQB = ["List of QBs"]
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
		soup = BeautifulSoup(urllib2.urlopen("{}{}{}".format(url[0], x, url[1])).read(), 'html.parser')

		# This basically locates the table and grabs all of its infor
		tableStats = soup.find("table", {"class": "playerTableTable tableBody"}) 
		
		# This is what loops through the data. The [2:]: is somethign that 
		# says we want to start at number 2 and go throgugh the end
		j=x-1	
		weeknumb = "Week: " + str(x)
		lists[j].insert(0, weeknumb)	
		for row in tableStats.findAll('tr')[2:]: 
				col = row.findAll('td')

				try:
					#.a = it's a link... we're asking for the text of the link. 
					# In this case were grabbig the player name				
					proj = col[23].string.strip() 
					proj = float(proj)
					#name = col[1].a.string.strip()
					#name = str(name)
					#listnameQB.append(name)
					
					#Do something where I insert "week x in the front of each list"
					
						
					lists[j].append(proj)
					if x == 1:
						name = col[0].a.string.strip()
						listnameQB.append(name)
				#write an except line that says if Column 2 equals "bye" then pull the string that says "--" in column 23 and then replace it with a 0	
				except Exception as e:
					errorFile.write (str(x)+ '*********' + str(e)+ '*********' + str(col) +'\n')

					#see the error, and move on don't get hung up 
					pass 
				
		x=x+1
#At this point I now have a list of all the qbs name



print(listnameQB)
print(lists)
print(len(lists))
#Which QB do you want to see
query = input("What QB do you want to see? ")#Type in the number of the element which the desired QB is. 
	#e.g. Blake bortles is 6th so type in number 6 to see his projecs
##numbers = [item[query] for item in lists] #what exactly is this line doing? 
##output = []
##output.append(listnameQB[query])
##output.append(numbers) #bye weeks are skipped in the projection list which screws this up. This is a beautiful soup thing?
# I need to get the html of '--' to read as '0'
##print(output)
count =0
#output.append()
individuallist = []
#Call a player and find his correllatig 
if query in listnameQB:	#I think this is redundant to teh lines that create 'numbers' and 'output' but I think this is a
#better way to do it because you can type in the player name
	position = listnameQB.index(query)
	while count < len(lists):
		individuallist.append(lists[count][position])
		count=count+1
	individualdict = {query:individuallist}
	print (individualdict)

else: 
	print("I don't see the name of that player")



errorFile.close

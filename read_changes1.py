# option 2, spaces around pipes'
changes_file = 'changes_python.log'
data = [line.strip() for line in open(changes_file, 'r')]

print(len(data))

sep = 72*'-'

# parse each of the commits and put them into a list of commits
commits = []
index = 0
author = {}

while index < len(data):
	try:
		# parse each of the commits and put them into a list of commits
		#the author with space at the end removed
 
		#details = data[index + 1].split('|') no strip if there are spaces on each side of the pipe.
		details = data[index + 1].split(' | ') 
		#print details
		commit =({'revision':details[0], 'author':details[1], 'date':details[2]})
		index=data.index(sep, index + 1)
		commits.append(commit)
		index=data.index(sep, index + 1)	
	except IndexError:
		break

# print(len(commits))

output_file = 'changes1.csv'
my_file = open(output_file, 'w')
my_file.write('Revision, Author,Date\n')
for details in commits:
	my_file.write(commit['revision'] + ',' + commit['author'] + ',"' + commit['date'] + '"\n')
my_file.close()

# for details in commit:
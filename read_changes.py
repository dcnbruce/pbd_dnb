
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
 
		details = data[index + 1].split('|')
	   #details = data[index + 1].split(' | ') no strip if there are spaces on each side of the pipe.
		print details
		commits.append(details)
		index=data.index(sep, index + 1)
		
	except IndexError:
		break

print(len(commits))

output_file = 'changes.csv'
my_file = open(output_file, 'w')
my_file.write('Revision, Author,Date')
for details in commits:
	my_file.write(details[0].strip() + ',' + details[1].strip() + ',"' + details[2].strip() + '\n"')
my_file.close()

# for details in commit:
Input Format

The first line contains N and X separated by a space.
The next X lines contains the space separated marks obtained by students in a particular subject.


Output Format

Print the averages of all students on separate lines.

The averages must be correct up to 1 decimal place.

n, x = map(int, input().split()) 

sheet = []
for _ in range(x):
    sheet.append( map(float, input().split()) ) 

for i in zip(*sheet): 
    print( sum(i)/len(i) )


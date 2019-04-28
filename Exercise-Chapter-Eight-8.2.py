# fhand = open('mbox.txt')
# count = 0
# words = []
# for line in fhand:
#     words = line.split()
# # print 'Debug:', words
#     if len(words) == 0 : continue
#     if words[0] != 'From' : continue
#     print(words[2])
    #if the starts with 'From' and the white space
    #if the line starts with 'From' and something else is written
    #not including the day we want to be printed
def week_day() :
    week = ['Sat','Sun','Mon','Tue','Wed','Thu','Fri']

fhand = open('mbox.txt')
count = 0
words = []
week = ['Sat','Sun','Mon','Tue','Wed','Thu','Fri']
for line in fhand:
    words = line.split()
# print 'Debug:', words
    if len(words) == 0 or len(words) < 3 : continue
    if words[2] not in week : continue

    if words[0] != 'From' : continue
    print(words[2])

import fileinput
import sys
# str(line[4:line.find('(')])


GoodToGo = False
Line1 = 'open(\'Callstack\',\'a\')'
store = ''
FirstTimeDone = False
with open('test.txt', 'r') as f:
    first_line = f.readline()
    print first_line
    if first_line.startswith('# Callstack Creator Ready!'):
        sys.exit()
for line in fileinput.input('test.txt', inplace=1, backup='.Backup'):
    if fileinput.isfirstline():
        if line.startswith('# Callstack Creator Ready!'):
            FirstTimeDone = True
        else:
            print '# Callstack Creator Ready'
    if line.startswith('def'):
        store = line[4:line.find('(')]
        GoodToGo = True
    print line
    if GoodToGo & FirstTimeDone == False:
        print '    ' + store
        GoodToGo = False
    store = ''

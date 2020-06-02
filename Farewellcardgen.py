#Farewell Card Generator (For CMS) 3 lines
#add support for people going to the same school as you later
#License stuffs
import sys
License = '''Farewell Card Generator for the AP students of Chesapeake Montessori School
Distributed under the Modzilla Public License V.2.0
(c) 2020, Created By Justin McCubbin
Dedicated to Hamza Nasher, because you can dedicate code to people now, too (I guess)?'''
print (License,'\n'*2)
MyName = input('What is your name? ')
TheirName = input('Who are you writing to? ')
MyGrade = input('What is your grade? (7, 8) ')
TheirGrade = input('What is {}\'s grade? '.format(TheirName))
Knowledge = input('Did you know them before? (y, n) ')
Line2 = input('Sentence about you and {}\'s time together. (eg: I enjoyed building a town with you.) '.format(TheirName))
#if you are new or dont know anybody, it says you get to know them, otherwise, you are 'reconnecting' with them
if TheirGrade == '7' and Knowledge == 'n':
    Line1 = 'It was great getting to know you this year!'
elif TheirGrade == '7' and MyGrade == '8' and Knowledge == 'y':
    Line1 = 'It was great reconnecting with you this year!'
elif TheirGrade == '7' and MyGrade == '7' and Knowledge == 'y':
    Line1 = 'It was great reconnecting with you this year!' 
elif TheirGrade == '8' and Knowledge == 'n':
    Line1 = 'It was great getting to know you this year!'
elif TheirGrade == '8' and Knowledge == 'y':
    Line1 = 'It was great reconnecting with you this year!'
    
if TheirGrade == '7':
    Line3 = 'See you next year.'
else:
    Line3 = 'Hope you do well in High School.'
#saves output (Data) to a txt file (TheirName.txt)
Data = (f'Hi {TheirName},\n{Line1}  {Line2}  {Line3}  \nAll the best, {MyName}')
Datafile = open(f'{TheirName}data.txt', 'w')
Datafile.write(Data)
Datafile.close()
print (Data)
sys.exit()
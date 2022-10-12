from time import sleep
import pyfiglet

with open('readme.txt','rt') as f:
    classes = f.read().rstrip('\n').split('\n')
    for person in classes:
        if person == 'person':
            print(pyfiglet.figlet_format('person found'))
            sleep(1)
        else :
            print('We have seen only',person)
            sleep(1)
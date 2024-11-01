import os
os.system('cls')
def action():
   global question
   question=input('you or dealer? ')
   if 'me' in question.lower():
      print('Brave')
   elif 'dealer' in question.lower():
      print('Coward')
while True:
   action()
   if 'me' in question.lower() or 'dealer' in question.lower():
      break

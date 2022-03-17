def validate_int(question, min, max):
  x = int(input(question))
  while ((x < min) or (x > max)):
    x = int(input(question))
  return x

def fileExist(archiveName):
  try:
    a = open(archiveName, 'rt')
    a.close()
  except FileNotFoundError:
    return False
  else:
    return True

def fileCreate(fileName):
  try:
    a = open(fileName, 'wt+')
    a.close()
  except:
    print('Error in the file creation')
  else:
    print('File {} was been created successfully\n'.format(fileName))

def registerGame(fileName, gameName, consoleName):
  try:
    a = open(fileName, 'at')
  except:
    print('Error while trying to open the file.')
  else:
    a.write('{};{}\n'.format(gameName,consoleName))
  finally:
    a.close()

def listFile(fileName):
  try:
    a = open(fileName, 'rt')
  except:
    print('Error while trying to read the list.')
  else:
    print(a.read())
  finally:
    a.close()

file = 'games.txt'
if fileExist(file):
  print('Archive located in the computer.')
else:
  print('Nonexistent File.')
  fileCreate(file)
while True:
  print('Menu')
  print('1 - Register new item')
  print('2 - List registers')
  print('3 - Quit')

  op = validate_int('Choose the wanted option: ',1 ,3)
  if op == 1:
    print("You've choosen the option to register new items...\n")
    gameName = input('Insert the game name: ')
    consoleName = input('Insert the console name: ')
    registerGame(file, gameName, consoleName)

  elif op == 2:
    print('Option to list the registered items...\n')
    listFile(file)
  elif op == 3:
    print('Finishing the program...')
    break
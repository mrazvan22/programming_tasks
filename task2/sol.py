import numpy as np


def loadFile(filePath):

  persDetails = {}

  # print(adsa)
  with open(filePath, 'r') as f:
    f.readline()
    # print(adas)
    for line in f.readlines():
      print(line)
      words = line[:-1].split(' ')
      name = words[0]
      # print(words)
      age = int(words[1])
      address = words[2]
      job = words[3]
      persDetails[name] = (age,address,job)


  return persDetails

def getAge(persDetails, name):
  return persDetails[name][0]

def getAddress(persDetails, name):
  return persDetails[name][1]

def getNamesFromAge(persDetails, age):
  '''
  Returns the names of all persons with the corresponding age
  :param persDetails:
  :param age:
  :return:
  '''
  return [k for k,v in zip(persDetails.keys(), persDetails.values()) if v[0] == age]

def getNamesFromJob(persDetails, job):
  '''
  Returns the names of all persons with the corresponding age
  :param persDetails:
  :param job:
  :return:
  '''
  return [k for k,v in zip(persDetails.keys(), persDetails.values()) if v[2] == job]


def addToDict(persDetails, name, age, address, job):
  persDetails[name] = (age, address, job)

  return persDetails

def removeFromDict(persDetails, name):
  newDict = {}
  for k in persDetails.keys():
    if k != name:
      newDict[k] = persDetails[k]

  return newDict

def writeToFile(persDetails, filePath):
  with open(filePath, 'w') as f:
    for k in persDetails.keys():
      f.write('%s %d %s %s\n' % (k, persDetails[k][0], persDetails[k][1], persDetails[k][2]))

persDetails = loadFile('addresses.txt')
print(persDetails)

ageIonel = getAge(persDetails, 'Ionel')
print('ageIonel ', ageIonel)
addressIonel = getAddress(persDetails, 'Ionel')
print('addressIonel ', addressIonel)

names24 = getNamesFromAge(persDetails, 24)
print('names24', names24)
persDetails = addToDict(persDetails, 'Adriana', 25, 'Str_Maniu_nr_3', 'medic')
# should show entry with Adriana
print(persDetails)

persDetails = removeFromDict(persDetails, 'Enescu')
# Show not show Enescu entry
print(persDetails)

writeToFile(persDetails, 'new_addresses.txt')


m1 = np.array([[1,3,6,9], [3,4,7,1]])
m3 = np.array([[1,3], [0,4], [-2,0], [9,1]])

def matrixMultiply(m,n):
  rowsP,colsM = m.shape
  colsP = n.shape[1]
  p = np.zeros((rowsP,colsP), float)
  for i in range(rowsP):
    for j in range(colsP):
      for k in range(colsM):
        p[i,j] += m[i,k]*n[k,j]

  return p

print(m1, m3)

print(matrixMultiply(m1,m3))
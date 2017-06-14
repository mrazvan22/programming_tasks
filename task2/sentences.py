def write_to_file(file, sentences):
  # for s in sentences:
  #   file.write(s + '\n')

  file.write(sentences)

fileHandle = open('sentences.txt', 'w')
s = ['propozitia1', 'ana are mere', 'sentence2']
write_to_file(fileHandle, s)
fileHandle.close()
import naivebayes as nb

naive_bayes = nb.NaiveBayes()

Input = []
Output = []
txt = ''
read = open('Elon Musk.txt', 'r')
for line in read:
    result = line.strip()
    txt += result + '\n'
read.close()
txt += '#'
txt = txt.replace('\n#', '')
lineList = txt.split('\n')
for x in lineList:
    tokenList = x.split(' ')
    Input.append(tokenList)
    Output.append(['Elon Musk'])
txt = ''
read = open('Jeff Bezos.txt', 'r')
for line in read:
    result = line.strip()
    txt += result + '\n'
read.close()
txt += '#'
txt = txt.replace('\n#', '')
lineList = txt.split('\n')
for x in lineList:
    tokenList = x.split(' ')
    Input.append(tokenList)
    Output.append(['Jeff Bezos'])

naive_bayes.fit(Input, Output)

classe1 = 'Motor Trend awards Tesla Model S best Car of the Year ever in their 70 year history!!'.split(' ')
result1 = naive_bayes.predict(classe1)
classe2 = 'Flawless BE-3 restart and perfect booster landing. CC chutes deployed. @BlueOrigin'.split(' ')
result2 = naive_bayes.predict(classe2)

print(f'classe1 = {classe1}: \n result1 = {result1}\n\nclasse2 = {classe2}:\n result2 = {result2}')

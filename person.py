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

class2 = 'Motor Trend awards Tesla Model S best Car of the Year ever in their 70 year history!!'.split(' ')
result2 = naive_bayes.predict(class2)
class1 = 'Flawless BE-3 restart and perfect booster landing. CC chutes deployed. @BlueOrigin'.split(' ')
result1 = naive_bayes.predict(class1)

# print(f'class1 = {class1}: \n result1 = {result1}\n\nclass2 = {class2}:\n result2 = {result2}')

class3 = input('Write text from Jeff or Elon:\n').split(' ')
result3 = naive_bayes.predict(class3)
print(f'author = {result3}')

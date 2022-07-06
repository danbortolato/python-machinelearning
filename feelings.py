import naivebayes as nb

naive_bayes = nb.NaiveBayes()

Input = []
Output = []

txt = ''
read = open('Happy.txt', 'r')
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
    Output.append(['Happy'])


txt = ''
read = open('Sad.txt', 'r')
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
    Output.append(['Sad'])

naive_bayes.fit(Input, Output)

class1 = 'I am so happy to see you today'.split(' ')
result1 = naive_bayes.predict(class1)
class2 = 'I am not good today.'.split(' ')
result2 = naive_bayes.predict(class2)

#print(f'class1 (Happy): {result1}\n\nclass2 (Sad): {result2}')

class3 = input('Tell me something about your day:\n').split(' ')
result3 = naive_bayes.predict(class3) 
print(f'Feeling = {result3}')

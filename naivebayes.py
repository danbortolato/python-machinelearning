class NaiveBayes():
    def fit(self, Input=[], Output=[]):
        _input = []
        _output = []
        i = 0
        while i < len(Input):
            j = 0
            while j < len(Input[i]):
                _input.append(Input[i][j])
                _output.append(Output[i][0])
                j += 1
            i += 1
        self.Input = _input
        self.Output = _output

    def getClass(self):
        Output = self.Output
        Output = sorted(Output)
        result = []
        value = ''
        for x in Output:
            if x != value:
                value = x
                result.append(x)
        return result

    def qtdInputClass(self, inputName='', className=''):
        Input = self.Input
        Output = self.Output
        n = 0
        i = 0
        while i < len(Input):
            if inputName == Input[i] and className == Output[i]:
                n += 1
            i += 1
        return n

    def qtdInput(self, inputName=''):
        Input = self.Input
        return Input.count(inputName)

    def totalClass(self):
        return len(self.Output)

    def qtdClass(self, className=''):
        Output = self.Output
        return Output.count(className)

    def weightClass(self, className=''):
        return self.qtdClass(className) / self.totalClass()

    def predict(self, Enter=[]):
        result = dict()
        allClass = self.getClass()
        for _input in Enter:
            for _output in allClass:
                _qtdInputClass = self.qtdInputClass(_input, _output)
                _qtdClass = self.qtdClass(_output)
                _qtdInput = self.qtdInput(_input)
                _totalClass = self.totalClass()
                try:
                    total = (_qtdInputClass / _qtdClass) * (_qtdClass / _totalClass) / (_qtdInput / _totalClass) * 100
                except:
                    total = 0
                if _output in result:
                    result[_output] += round(total / len(Enter), 2)
                    if result[_output] >= 99.99:
                        result[_output] = 100.00
                    elif result[_output] <= 0.01:
                        result[_output] = 0.00
                else:
                    result[_output] = round(total / len(Enter), 2)
                    if result[_output] >= 99.99:
                        result[_output] = 100.00
                    elif result[_output] <= 0.01:
                        result[_output] = 0.00

        _max = 0
        _class = ''
        for _output in allClass:
            if result[_output] >= _max:
                _max = result[_output]
                _class = _output
        if _max == 50 or _max == 0:
            result = self.Output[-1]
        else:
            result = _class
        return result

    def classify(self, Enter=[]):
        return self.predict(Enter)

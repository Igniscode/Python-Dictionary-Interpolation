import csv

class InterpolationDictionary:
    dest = {}
    str = ""
    def __init__(self, decimalpoint, dictionary):
        self.source = dictionary
        self.decimalpoint = decimalpoint
    
    def allRound(self):
        lastdiff = 0
        self.minindex = 99999999
        self.maxindex = 0
        for key in self.source.keys():
            index = round(key, self.decimalpoint)
            if self.minindex>index: self.minindex = index
            if self.maxindex<index: self.maxindex = index
            value = self.source[key]
            if index in self.dest:
                if abs(index - key) < lastdiff:
                    self.dest[index] = value
                    lastdiff = abs(index - key)
            else:
                self.dest[index] = value
                lastdiff = abs(index - key)

    def interpolation(self):
        positionswitch = 10 ** self.decimalpoint
        for i in range( int(self.minindex * positionswitch),int(self.maxindex * positionswitch)):
            index = round(i/positionswitch,self.decimalpoint)
            self.dest[index] = self.value(index, index)
            print(str(index) + " " +str(self.dest[index]))
            self.str += str(index) + "," +str(self.dest[index]) + "\n"

    def value(self, start, index):
        positionswitch = 10 ** self.decimalpoint
        fp_index = round(index, self.decimalpoint)
        if fp_index in self.dest:
            return self.dest[fp_index]
        else:
            return (self.dest[round(start-1/positionswitch, self.decimalpoint)]+self.value(start, fp_index+1/positionswitch))/2

d = {}
with open('data.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        k, v = row
        d[float(k)] = float(v)

interpol = InterpolationDictionary(1, d)
interpol.allRound()
interpol.interpolation()

with open('mycsvfile.csv', 'w') as f:  # You will need 'wb' mode in Python 2.x
    dump = interpol.str
    f.write(dump)

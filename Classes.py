def refreshMissingVals(missCell,missContainer):
    """
        Remove values in missCell, not in missContainer
    """
    for i in missCell.missingValues:
        if i not in missContainer:
            missCell.deleteMissingValue(i)
            
def removeValues(inputList,vals):
    """
        Remove given values from the given list
        args:
            inputList(list),vals(list)
        returns:
            None.
    """
    l=len(vals)
    for i in range (l):
        try:
             inputList.remove(vals[i])
        except ValueError:
            pass
        except TypeError:
            pass

def most_common(inputList):
    """
        Return the most common element in a list
        args:
           inputList(list) 
    """
    try:
        return max(set(inputList), key=inputList.count)
    except ValueError:
        pass
  
def pickMostCommonTwo(vals,indices):
    """
        Return the indices of 2 most common elements in the list and the common value.
        Returns -1,-1 if not found.
    """
    outIndeces=[]
    mostCommon=most_common(vals)
    for i in range (len(vals)):
        if vals[i]==mostCommon:
            outIndeces.append(indices[i])
    if len(outIndeces)==2:
        return (outIndeces,mostCommon)
    else:
        return -1,-1
      
class Cell(object):
    def __init__(self,val=0):
        self.value=val
        self.missingValues=[]
        self.randomVal=0
    
    def addMissingValues(self,vals):
        if self.value==0:
            self.missingValues=vals
        
    def deleteMissingValue(self,value):
        self.missingValues.remove(value)
    
    def setValue(self,value):
        self.value=value
        self.missingValues=[]
    
    def setRandomVal(self,value):
        self.randomVal=value
    
    def clearRandomVal(self):
        self.randomVal=0
    
    def __str__(self):
        if self.value==0:
            if self.randomVal!=0:
                return str(int(self.randomVal))
            return ' '
        return str(int(self.value))

class CellContainer(object):
    def __init__(self):
        self.elements=[ [] for i in range (9)  ]
        self.missingValues=[i for i in range (1,10)]
    
    def __str__(self):
        outStr="Container: "
        for i in range (9):
            outStr=outStr+'-'+str(self.elements[i])
        return outStr
    
    def setElement(self,index,cell):
        self.elements[index]=cell
        if cell.value !=0:
            try:
                self.missingValues.remove(cell.value)
            except ValueError:
                pass
        
    def refresh(self):
        for i in range (9):
            try:
                self.missingValues.remove(self.elements[i].value)
            except ValueError:
                pass
        "Set a value if element is the only one with that value"
        for i in range (9):
            refreshMissingVals(self.elements[i],self.missingValues)
            
        for val in self.missingValues:
            index=0
            count=0
            for i in range (9):
                if val in self.elements[i].missingValues:
                    index=i
                    count+=1
            if count==1:
                self.elements[index].setValue(val)
        
        "Algorithms for missingValues"
        for i in range (9):
            d=self.elements[i].missingValues
            if len(d)==1:
                "If d containes only one missingValue, set it and delete others"                
                self.algorithmOne(d,i)
            elif len(d)==2:
                """If d has two values, there are two possiblities
                1-d=[1,2],other=[1,2],delete {1,2} from other missing values
                2-d=[1,2],other1=[1,3],other2=[2,3] delete {1,2,3} from other missing values
                """
                self.algorithmTwo(d,i)
                self.algorithmThree(d[:],i)
    
    
    def algorithmOne(self,value,selfi):
        for i in range (9):
            if i!=selfi:
                "Delete value from other elements missingValues"
                try:
                    self.elements[i].deleteMissingValue(value[0])
                except ValueError:
                    pass
            else:
                "Set the value"
                self.elements[i].setValue(value[0])

    def algorithmTwo(self,value,selfi):
        for i in range (9):
            if i!=selfi:
                if self.elements[i].missingValues==value:
                    "Remove two elements from the other elements missing values"
                    self.removeTwo(value,i,selfi)
    
    def algorithmThree(self,value,selfi):
        vals=[]
        indices=[]
        for i in range (9):
            if (i!=selfi)and ((value[0] in self.elements[i].missingValues) or (value[1] in self.elements[i].missingValues)):
                old=self.elements[i].missingValues[:]
                removeValues(old,value)
                if len(old)==1:
                    vals.append(old[0])
                    indices.append(i)
        otherIndeces,commonVal=pickMostCommonTwo(vals,indices)
        if otherIndeces!=-1:
            value.append(commonVal)
            self.removeThree(value,selfi,otherIndeces[0],otherIndeces[1])

    def removeTwo(self,vals,selfi1,selfi2):
        for i in range (9):
            if (i!=selfi1) and (i!=selfi2):
                removeValues(self.elements[i].missingValues,vals)
                
    
    def removeThree(self,vals,selfi1,selfi2,selfi3):
        for i in range (9):
            if (i!=selfi1) and (i!=selfi2) and (i!=selfi3) :
                removeValues(self.elements[i].missingValues,vals)
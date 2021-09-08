def printStr(params):
    return {"upperSection" : "mov si, {dataChunk}\ncall "+ str(params[1].s) +"\ncall printString", "lowerSectionUnmodified" : ": db '"+ str(params[0].s) +"',10,13,0"}

class FunctionDefinitionChecker():
    def __init__(self):
        print("Initialized FunctionChecker.")

        #####################################
        self.Functions = {"print" : printStr}
        #####################################

    def check(self, funcName, funcParams):
        return self.Functions[funcName](funcParams)


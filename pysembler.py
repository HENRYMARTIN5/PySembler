import ast, sys, json, util
from functiondefinitions import *

configF = open("config.json", "r")
config = json.load(configF)
fName = config["Filename"]
outputfName = config["OutputFilename"]
debugEnabled = util.str2bool(config["DebugEnabled"])


outputfData = ["; Hi there!","; This code was generated by PySembler, made by Henrysjm#1827."]
outputfDataData = []



with open(fName, "r") as f:
    fData = f.read()
    data = ast.parse(fData)
    treeDump = ast.dump(data)
    tree = data
    f.close()
if debugEnabled and treeDump: print("Module data found: " + treeDump)

root = tree.body

print("Fetching data from /templateData...")
with open("templateData\\start.asm", "r") as f:
    for line in f:
        outputfData.append(line.replace("\n", ""))
print("Got data!")
currentDataChunk = ["a"]
dataChunkPrefix = "DataChunk"
if root:
    functionDefinitionChecker = FunctionDefinitionChecker()
    for item in root:
        if type(item) is ast.FunctionDef:
            if item.name == "Main":
                for item2 in item.body:
                    if type(item2) is ast.Expr:
                        if type(item2.value) is ast.Call:
                            funcName = item2.value.func.id
                            funcParams = item2.value.args
                            funcOutput = functionDefinitionChecker.check(funcName, funcParams)
                            dataToAppend = ""
                            for char in currentDataChunk:
                                dataToAppend = char.upper() + dataToAppend
                            outputfData.append(funcOutput["upperSection"].replace("{dataChunk}", dataChunkPrefix+dataToAppend))
                            dataToAppend = funcOutput["lowerSectionUnmodified"]
                            for char in currentDataChunk:
                                dataToAppend = char.upper() + dataToAppend
                            dataToAppend = dataChunkPrefix + dataToAppend
                            outputfDataData.append(dataToAppend)
                            currentDataChunk[-1] = chr(ord(currentDataChunk[-1]) + 1)
                            if currentDataChunk[-1] == "{":
                                currentDataChunk[-1] = "z"
                                currentDataChunk.append("a")

outputfData.append("JMP $")
outputfData.append("")
print("Parsed data, getting functions and ending...")
with open("templateData\\funcs.asm", "r") as f:
    for line in f:
        outputfData.append(line.replace("\n", ""))
for item in outputfDataData:
    outputfData.append(item)
with open("templateData\\end.asm", "r") as f:
    for line in f:
        outputfData.append(line.replace("\n", ""))
with open(outputfName, "w") as f:
    f.close()
with open(outputfName, "a") as f:
    for line in outputfData:
        f.write(line + "\n")
print("Done!")
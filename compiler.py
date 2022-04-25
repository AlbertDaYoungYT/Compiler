import json

global config
with open("./config.json") as f:config = json.load(f)

def WriteCompiledLine(line):
    WriteLine = ""
    for x in line:
        WriteLine = ''.join(x)
    WriteLine = WriteLine[:-1]
    open(out, "a", encoding="utf-8").write(WriteLine + "\n")

def ParseLine(line):
    line.split(config["Splitter"])
    for x in line:
        for y in range(len(config["DataTypesFrom"])):
            x.replace(config["DataTypesFrom"][y], config["DataTypesTo"][y])
        for y in range(len(config["OperatorsFrom"])):
            x.replace(config["OperatorsFrom"][y], config["OperatorsTo"][y])
        
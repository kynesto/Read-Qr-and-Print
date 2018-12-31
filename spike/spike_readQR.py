# typedString = input()

# print(typedString)

typedStringTest = "$FA0134253$5154482061$AB080331&3$ST016373 & Schweiyer ESO$49186$$M1100037G$3$3$330$4,3$$SCHWEGLER BURSA$49186$"

typedString = typedStringTest
ToolInfo = typedString.split("$")

print(ToolInfo[12])
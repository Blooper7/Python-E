#DON"T LOOK AT ME I"M HIDEOUS

import sys
import os

keywords={
	" ":" ",
	"e":"print",
	"ee":"return",
	"eee":"def",
	
	#conditionals
	"eeee":"if",
	"eeeee":"elif",
	"eeeeee":"else",
	"eeeeeee":"and",
	"eeeeeeee":"or",
	"eeeeeeeee":"is",
	"eeeeeeeeee":"not",
	"eeeeeeeeeee":"in",
	"eeeeeeeeeeee":"True",
	"eeeeeeeeeeeee":"False",	
	
	#loops
	"eeeeeeeeeeeeee":"for",
	"eeeeeeeeeeeeeee":"range",
	"eeeeeeeeeeeeeeee":"while",
	
	#other
	"eeeeeeeeeeeeeeeee":"import",
	
	#Parenthesis, brackets, quotes, logic, and terminator
	"E":"(",
	"EE":")",
	"EEE":"[",
	"EEEE":"]",
	"EEEEE":"{",
	"EEEEEE":"}",
	"EEEEEEE":";",
	"EEEEEEEE":"\"",
	"EEEEEEEEE":"\'",
	"EEEEEEEEEE":"="
}

def checkE(string):
	E=True
	for i in range(len(string)):
		if not string[i].lower()=="e":
			E=False
			break
	return E

def translate(string):
	if checkE(string):
		if string not in keywords:
			raise Exception(f"Keyword {string} doesn't exist. Remember, each keyword must be separated by a space, including parenthesis")
		else:
			return keywords[string]
	else:
		return string
		
def tokenize(string): #turn funny strings with \n and \t into strings that actually work
	splString=[*string]
	splString.append(";")
	
	tmpString=""
	stringRoot=0
	end=0
	for i in range(len(splString)):
		#print(i)
		#print(stringRoot)
		if not splString[i].isspace() and not splString[i]==";":
			if splString[i-1].isspace():
				stringRoot=i
			tmpString+=splString[i]
			
		elif splString[i].isspace or splString[i]==";":
			if len(tmpString)>0:
				splString[stringRoot]=tmpString
				#print(splString)
				
			for ii in range(stringRoot+1, i-1):
				splString[ii]=None
				
			tmpString=""
			
		#print(tmpString)
			
	splString.pop()
	
	if splString[len(splString)-1].lower()!="e":
		splString[len(splString)-1]=None
	
	final=[item for item in splString if item is not None]
	
	#print(splString)
	#print(final)
	for i in range(len(final)):
		final[i]=translate(final[i])
	#print(final)
	return final

def scanForSpaces(string):
	for i in string:
		if i.isspace():
			return True
	return False

def compileToPython(filename):
	original=open(filename, "r")
	data=original.read()
	original.close()
	#print(filename)
	
	filename=filename.split('.')[0]
	compiled=open(f".{filename}.py", "a")
	data=data.split(" ")
	#print(data)
	
	for i in range(len(data)):
		if not i==0:
			compiled.write(" ")
		
		if "." in data[i]:
			#print("found a .")
			splData=data[i].split(".")
			for ii in range(len(splData)):
				if not ii==0:
					compiled.append(".")
				compiled.write(translate(splData[ii]))
		elif scanForSpaces(data[i]):
			tkData=tokenize(data[i])
			for i in tkData:
				compiled.write(i)
		else:
			#print(f"{translate(data[i])}")
			compiled.write(translate(data[i]))
	#print(f"compiled {filename}.e to .{filename}.py")

inputFile=sys.argv[1]

inputFile=open(inputFile, "r")
#print(inputFile.read())

compileToPython(sys.argv[1])
inputFile.close()
#print("-----------------")
os.system(f"python .{sys.argv[1].split('.')[0]}.py")
os.system(f"rm .{sys.argv[1].split('.')[0]}.py")

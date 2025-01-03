import re
print("Enter C code (press 'Enter' on an empty line to finish):")
lines = []
while True:
    line = input()
    if line == "": 
        break
    lines.append(line)
text = "\n".join(lines)
symbols = ['!', '@', '#', '$', '%', '&', '^', '*']
operators = ['+', '-', '*', '/', '=', '+=', '-=', '==', '<', '>', '<=', '>=']
keywords = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 
            'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 
            'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 
            'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
special_characters = [' ', '	', '.', ',', '\n', ';', '(', ')', '<', '>', '{', '}', '[', ']']
in_keywords = []
in_spl_symbols = []
in_operators = []
in_special_characters = []
in_identifiers = []
in_constants = []

tokens = []
isStr = False
isWord = False
isCmt = 0
token = ''
for i in text:
    if i == '/':
        isCmt = isCmt + 1

    elif isCmt == 2:
        if i == '\n':
            token = ''
            isCmt = 0
    
    elif i == '"' or i == "'":
        if isStr:
            tokens.append(token)
            token = ''
        isStr = not isStr 

    elif isStr:
        token = token + i
    
    elif i in symbols:
        tokens.append(i)
    
    elif i.isalnum() and not isWord:
        isWord = True
        token = i
    
    elif (i in special_characters) or (i in operators):
        if token:
            tokens.append(token)
            token = ''
        
        if not (i == ' ' or i == '\n' or i == '	'):
            tokens.append(i)

    elif isWord:
        token = token + i
for token in tokens:
    if token in symbols:
        in_spl_symbols.append(token)
    elif token in operators:
        in_operators.append(token)
    elif token in keywords:
        in_keywords.append(token)
    elif re.search("^[_a-zA-Z][_a-zA-Z0-9]*$", token):
        in_identifiers.append(token)
    elif token in special_characters:
        in_special_characters.append(token)
    else:
        in_constants.append(token)
    
print("No of tokens = ", len(tokens))   
print("\n keywords = ", in_keywords)
print("\n special symbols = ", in_spl_symbols)
print("\n operators = ", in_operators)
print("\n identifiers = ", in_identifiers)
print("\n constants = ", in_constants)
print("\n special characters = ", in_special_characters)

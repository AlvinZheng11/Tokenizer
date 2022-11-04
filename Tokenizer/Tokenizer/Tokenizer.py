#Alvin Zheng
#C:\Users\azhen\source\repos\Tokenizer\Main.jack
#https://www.youtube.com/watch?v=O4Bt_CyZWbI

symbols = ['[',']','{','}',',',';','=','.','+','-','*','/','|','~','(',')']
symbols2 = {'[':'[',']':']','{':'{','}':'}',',':',',';':';','=':'=','.':'.','+':'+','-':'-','*':'*','/':'/','|':'|','~':'~','(':'(',')':')'}
keywords = ['class''constructor','method', 'function', 'int', 'boolean', 'char', 'void', 'var', 'static', 'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true', 'false', 'null', 'this']
keywords2 = {'class':'class', 'constructor':'constructor','method':'method', 'function':'function', 'int':'int', 'boolean':'boolean', 'char':'char', 'void':'void', 'var':'var', 'static':'static', 'field':'field', 'let':'let', 'do':'do', 'if':'if', 'else':'else', 'while':'while', 'return':'return', 'true':'true', 'false':'false', 'null':'null', 'this':'this'}
ignore = {'/':'/'}
conversion = {'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot'}
identifier = ['Array', 'length','Main','main','sum','Keyboard', 'readInt','new','printInt']
identifier2 = {'Array':'Array', 'length':'length','Main':'Main','main':'main','sum':'sum','Keyboard':'Keyboard', 'readInt':'readInt','new':'new','printInt':'printInt'}
#xml = ["<tokens>"]

file_path = input("Enter path to .jack file to read: ").strip('.jack') + '.jack'
xml_path = input("Enter name of .xml file to write results to: ").strip('.xml') + '.xml'
with open(file_path) as f:
    jackFile = f.read()

symbols_key = symbols2.keys()
ignore_key = ignore.keys()
conversion_key = conversion.keys()
count = 0
swap = ""
stringConst = 0
xml_swap = ""
xml=[]

fileSections =  jackFile.split("\n")

for char in fileSections:

    for token in char:
        if token in ignore_key:
            break
        else:
            if token.isalpha() or token == '_' and token != ' ' and token.next() != token.isalpha():
                swap = swap + token
            if token in [' ', '\n', '\t','"']:
                if swap == "" or swap == '\t':
                    swap = ""
                else:
                    xml.append("<identifier> " + swap + " </identifier>")
                    swap = ""
            if token in symbols:
                xml.append("<symbol> " + token + " </symbol>") 
            if swap in keywords:
                 for c in keywords2:
                    xml_swap = xml_swap.replace(c, keywords2[c])
                 xml.append("<keywords> " + xml_swap + " </keywords>")
                 swap = ""
            if swap in identifier:
                for c in identifier2:
                    xml_swap = xml_swap.replace(c, identifier2[c])
                xml.append("<identifier> " + xml_swap + " </identifier>")
                swap = ""
            if token in conversion_key:
                for c in conversion:
                    xml_swap = xml_swap.replace(c, conversion[c])
                xml.append("<symbol> " + xml_swap + " </symbol>")
            
xml_write = '<tokens>'
for t in xml:
    xml_write = xml_write + t + '\n'
xml_write = xml_write + '\n</tokens>\n'

with open(xml_path, 'w') as f:
    f.write(xml_write)

print("Output written to " + xml_path)
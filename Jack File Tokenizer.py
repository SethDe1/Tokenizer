# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 18:11:52 2022

@author: Seth DeWalt

"""
Symbols = ['(',')','[', ']', '{','}',',',';','=','.','+','-','*','/','&','|','~','<','>']
Keywords = ['constructor','method','function','int','boolean','char','void','var','static','field','let','do','if', 'else','while','return','true','false','null','this', 'class']
Constants = ['0','1','2','3','4','5','6','7','8','9']
Spacing = ['',' ','\n','\t','\t\n']

"File to read"
print("Which file do you have to load?\n1: Main.jack \n2: SquareGame.jack")
choice=int(input())
if choice==1:
    readPath = 'D:\\UCA Spring 2022\\Principles of Programming\\Main.jack'
    writepath ='D:\\UCA Spring 2022\\Principles of Programming\\Main.txt'
elif choice==2:
    readPath = 'D:\\UCA Spring 2022\\Principles of Programming\\SquareGame.jack'
    writepath ='D:\\UCA Spring 2022\\Principles of Programming\\SquareGame.txt'

with open(readPath, 'r') as rFile:
    char= [""]
    sizeText = len(open(readPath).readlines())
    
    wFile= open(writepath, "w")
    
    wFile.write("<tokens>\n")
    
    for i in range(0, sizeText):
        
        char = open(readPath).readlines()[i]
        sizeLine= len(open(readPath).readlines()[i])
        
        if char.startswith("//") or char.startswith("/*") or char.startswith(" *") or char.__contains__("//"):
            i+=1
            
        else:
            
            word=[]
            for j in range (0, sizeLine):
                if char[j].isalpha() and char[j] not in Symbols and char[j] not in Spacing:
                    word+=char[j]
                    word = ''.join(map(str, word))
                    if word in Keywords:
                        wFile.write("<keyword> "+word+" </keyword>\n")
                        word=''
                    elif char[j+1] is Spacing or (char[j+1] in Symbols or char[j+1].isspace()) and not(char[j].isspace()):
                        wFile.write("<identifier> "+ word +" </identifier>\n")
                        word=''
                if char[j] in Symbols:
                    wFile.write("<symbol> "+char[j]+" </symbol>\n")
                if char[j] in Constants:
                    wFile.write("<integerConstant> "+char[j]+" </integerConstant>\n")
    wFile.write("</tokens>")
    
print("Program has finished.")
    
    
    
    
    
    
    
    
    
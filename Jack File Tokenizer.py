# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 18:11:52 2022

@author: Seth DeWalt
This file is taking Jack files and fitting them into XML format
"""
#Lists to select terms
Symbols = ['(',')','[', ']', '{','}',',',';','=','.','+','-','*','/','&','|','~','<','>']
Keywords = ['constructor','method','function','int','boolean','char','void','var','static','field','let','do','if', 'else','while','return','true','false','null','this', 'class']
Constants = ['0','1','2','3','4','5','6','7','8','9']
Spacing = ['',' ','\n','\t','\t\n']

"File to read"
#File Choices
print("Which file do you have to load?\n1: Main.jack \n2: SquareGame.jack")
choice=int(input())
#Read and Write file selection
if choice==1:
    readPath = 'D:\\UCA Spring 2022\\Principles of Programming\\Main.jack'
    writepath ='D:\\UCA Spring 2022\\Principles of Programming\\Main.txt'
elif choice==2:
    readPath = 'D:\\UCA Spring 2022\\Principles of Programming\\SquareGame.jack'
    writepath ='D:\\UCA Spring 2022\\Principles of Programming\\SquareGame.txt'

#opening file
with open(readPath, 'r') as rFile:
    char= [""]
    sizeText = len(open(readPath).readlines())
    
    wFile= open(writepath, "w")
    #opening write file
    wFile.write("<tokens>\n")
    
    for i in range(0, sizeText):
        #getting entire line
        char = open(readPath).readlines()[i]
        #getting line size
        sizeLine= len(open(readPath).readlines()[i])
        #Skipping comment lines
        if char.startswith("//") or char.startswith("/*") or char.startswith(" *") or char.__contains__("//"):
            i+=1
            
        else:
            
            word=[]
            for j in range (0, sizeLine):
                #if the character is a word
                if char[j].isalpha() and char[j] not in Symbols and char[j] not in Spacing:
                    #creating words from he characters
                    word+=char[j]
                    word = ''.join(map(str, word))
                    #if the word is in keywords, write to file as keyword token
                    if word in Keywords:
                        wFile.write("<keyword> "+word+" </keyword>\n")
                        word=''
                    #if the word is anything else write as identifier token
                    elif char[j+1] is Spacing or (char[j+1] in Symbols or char[j+1].isspace()) and not(char[j].isspace()):
                        wFile.write("<identifier> "+ word +" </identifier>\n")
                        word=''
                #if the character is a symbol write as a symbol token
                if char[j] in Symbols:
                    wFile.write("<symbol> "+char[j]+" </symbol>\n")
                #if the character is a number write as a integer constant
                if char[j] in Constants:
                    wFile.write("<integerConstant> "+char[j]+" </integerConstant>\n")
    wFile.write("</tokens>")
#prompt for the end
print("Program has finished.")
    
    
    
    
    
    
    
    
    
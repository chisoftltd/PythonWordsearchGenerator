#Python Wordsearch Generator - www.101computing.net/python-wordsearch-generator/
import random
from replit import clear
#A subroutine to replace all "-" (empty characters) with a random letter
def randomFill(wordsearch):
	LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for row in range(0,14):
		for col in range(0,14):
			if wordsearch[row][col]=="-":
				randomLetter = random.choice(LETTERS)
				wordsearch[row][col]=randomLetter
	return wordsearch
#A subroutine to output the wordsearch on screen    
def displayWordsearch(wordsearch):
	#print("|____________________________|")
	#print("|                         |")
	for row in range(0,14):
		line=""
		for col in range(0,14):
			#if col < 13:
			line = line + wordsearch[row][col] + " "
			#else:
			#line = line + wordsearch[row][col] + ""
			line = line #+ "|"
		print(line)
  	#print("|____________________________|")  
    
#A subroutine to add a word to the wordsearch at a random position
def addWord(word,wordsearch):
  row=random.randint(0,13)
  col=0
  for i in range(0,len(word)):
    wordsearch[row][col+i]=word[i]
  #CHANGE THIS CODE TO
  # ----Randomly decide where the word will start
  # ----Decide if the word will be added horizontally, vertically or diagonally
  # ----Check that the word will fit in (within the 12 by 12 grid)
  # ----Check that the word will not overlap with existing letters/words in the wordsearch
  

#Create an empty 12 by 12 wordsearch (list of lists)
wordsearch = []
for row in range(0,14):
  wordsearch.append([])
  for col in range(0,14):
    wordsearch[row].append("-")


def exist(board, word):
	n =len(board)
	m = len(board[0])
	for i in range(n):
		for j in range(m):
			if word[0] == board[i][j]:
				if find(board,word,i,j):
					return True
	return False
def find(board,word,row,col,i=0):
	if i== len(word):
		return True
	if row>= len(board) or row <0 or col >=len(board[0]) or col<0 or word[i]!=board[row][col]:
		return False
	board[row][col] = '*'
	res = find(board,word,row+1,col,i+1) or find(board,word,row-1,col,i+1) or find(board,word,row,col+1,i+1) or find(board,word,row,col-1,i+1)
	board[row][col] = word[i]
	return res

#Adding words to our wordsearch
more_search = True
while more_search:
	addWord("PYTHON",wordsearch)    
	addWord("ALGORITHM",wordsearch)    
	addWord("CODING",wordsearch)    
	addWord("PROGRAM",wordsearch)  
	addWord("JAVA",wordsearch)    
	addWord("DATA",wordsearch)    
	addWord("BIGDATA",wordsearch)    
	addWord("POWERBI",wordsearch)  
	print("PYTHON\n""ALGORITHM\n""CODING\n""PROGRAM\n""JAVA\n""DATA\n""BIGDATA\n""POWERBI\n")
	word1 = input("Enter word to search: ").upper()
	print()
	#All unused spaces in the wordsearch will be replaced with a random letter
	board = []
	board1 = randomFill(wordsearch)

	#Display the fully competed wordseach on screen
	displayWordsearch(wordsearch)
	print()
	print(exist(board1, word1))
	print()
	reply = input("Search for more word? Type 'y' or 'n': ").lower()
	if reply == "n":
		print()
		print("Thank you for using our software.\nFor your feedback and review, email chinwej.obiageri@gmail.com")
		more_search = False
	else:
		clear()
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# declare a list with 9 blocks of empty space
# print the board on screen
# take input from user a or user b with specific position
# check if the pos is empty then only take it as a valid input,else ask again
# after the input is placed ,check if some player has won,its a draw
# ask if the user wants to play again
# enter the score for all the matches


# In[4]:


def empty_list_XO():
    tmp_list = []
    for i in range(9):
        tmp_list.append(" ")
    return tmp_list
XO_list = empty_list_XO()
def printboard(xolist):
  print(xolist[0],  "|",xolist[1],   "|" ,xolist[2])
  print("----------")
  print(xolist[3],  "|",xolist[4],   "|", xolist[5])
  print("----------")
  print(xolist[6],  "|",xolist[7],   "|", xolist[8])
printboard(empty_list_XO())
import random
def whowilgofirst():
  player = random.randint(0,1)
  if player == 0:
    print('player a will go first')
  else:
    print("player b will go first")
  return player
whowilgofirst()
def takeinput(player,xolist):
  print("hey player, ",player)
  flag = 0
  while flag ==0:
    pos = int(input("please enter the position for your next move[ 0 to 8] - "))
    if pos >= 0 and pos <= 8:
      if xolist[pos] == ' ':
        print("valid input")
        if player == 0:
            xolist[pos] = "X"
        else:
            xolist[pos] = 'O'        
        return xolist
        flag = 1
      else:
        print("please enter again,its occupied valid input again")
      flag = 0
    else:
      print("please give valid input again")
      flag = 0
XO_list = takeinput(1,empty_list_XO())
#if return is 0 then player a is winner
#if return is 1 then player b is winner
#if return is 2 the its a draw
def checkwin(xolist):
    flag = 0
    print(xolist)
    for i in range(9):
        if xolist[i] ==' ':
            flag = 1
    if (xolist[0] == 'O' and xolist[1] == 'O' and xolist[2] == 'O') or (xolist[3] == 'O' and xolist[4] == 'O' and xolist[5] == 'O')  or (xolist[6] == 'O' and xolist[7] == 'O' and xolist[8] == 'O') or (xolist[0] == 'O' and xolist[3] == 'O' and xolist[6] == 'O') or (xolist[1] == 'O' and xolist[4] == 'O' and xolist[7] == 'O') or (xolist[2] == 'O' and xolist[5] == 'O' and xolist[8] == 'O') or (xolist[0] == 'O' and xolist[4] == 'O' and xolist[8] == 'O') or (xolist[6] == 'O' and xolist[4] == 'O' and xolist[2] == 'O'):
        print("player A is winner")
        return 0
    elif (xolist[0] == 'X' and xolist[1] == 'X' and xolist[2] == 'X') or (xolist[3] == 'X' and xolist[4] == 'X' and xolist[5] == 'X')  or (xolist[6] == 'X' and xolist[7] == 'X' and xolist[8] == 'X') or (xolist[0] == 'X' and xolist[3] == 'X' and xolist[6] == 'X') or (xolist[1] == 'X' and xolist[4] == 'X' and xolist[7] == 'X') or (xolist[2] == 'X' and xolist[5] == 'X' and xolist[8] == 'X') or (xolist[0] == 'X' and xolist[4] == 'X' and xolist[8] == 'X') or (xolist[6] == 'X' and xolist[4] == 'X' and xolist[2] == 'X'):
        print("player B is winner")
        return 1
    
    elif flag == 1:
        return -1
    else:
        return 2
XO_list = empty_list_XO()
printboard(XO_list)
play = whowilgofirst()
scoreA = 0
scoreB = 0
gamestatus = 0
chance = 0
while gamestatus == 0:
    if play == 0:
        XO_list = takeinput(0,XO_list)
        printboard(XO_list)
        winstat =checkwin(XO_list)
        play = 1
    else:
        XO_list = takeinput(1,XO_list)
        printboard(XO_list)
        winstat =checkwin(XO_list)
        play = 0
    if winstat == 0 or winstat == 1 or winstat == 2:
        gamestatus = 1
        print("win-" , winstat)
    else:
        gamestatus = 0


# In[8]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[5]:


def boardprint():
    print(board[9]+" |"+board[8]+" |"+board[7])
    print('__|__|__')
    print(board[6]+" |"+board[5]+" |"+board[4])
    print('__|__|__')
    print(board[3]+" |"+board[2]+" |"+board[1])
    print('  |  |  ')


# In[6]:


def gameplay(position,turn):
    print(turn+" Turn")    
    board[position]=turn       
    boardprint()
    return turn


# In[7]:


def stargame():

    count=0
    for i in range(1,10):
        
        try:
            
            position=int(input("Enter your position"))
            
        except:
            print("Please Enter a numeric value from 1 to 9")
            position=int(input("Enter your position"))
            
        if i%2==0:
            turn=gameplay(position,"O")
            count=count+1
        else:
            turn=gameplay(position,"X")
            count=count+1
        if count>=5:
            if board[9]==turn and board[8]==turn and board[7]==turn:
                print(turn +" Won")
                break
            elif board[6]==turn and board[5]==turn and board[4]==turn:
                print(turn +" Won")
                break
            elif board[3]==turn and board[2]==turn and board[1]==turn:
                print(turn +" Won")
                break
            elif board[9]==turn and board[6]==turn and board[3]==turn:
                print(turn +" Won")
                break
            elif board[8]==turn and board[5]==turn and board[2]==turn:
                print(turn +" Won")
                break
            elif board[7]==turn and board[4]==turn and board[1]==turn:
                print(turn +" Won")
                break
            elif board[7]==turn and board[5]==turn and board[3]==turn:
                print(turn +" Won")
                break
            
            elif board[9]==turn and board[5]==turn and board[1]==turn:
                print(turn +" Won")
                break
            else:
                print("Match Draw Try again")


# In[8]:


board={9:' ',8:' ',7:' ',6:' ',5:' ',4:' ',3:' ',2:' ',1:' '}
stargame()






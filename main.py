import random

def homepage():
  print("")
  print("")
  print("--"*20)
  print("        WELCOME TO MASTERMIND!!!")
  print("--"*20)
  print("")

  print("1. Start game:")
  print("2. Instructions:")
  print("3. Close:")

  #interactive commands for the program
  while True:
    command=input("\nEnter '1','2','3' to go to the desired page> ")
    if command=='1':
      start()
      break
    elif command=='2':
      instructions()()
      break
    elif command=='3':
      exit()
    else:
      print("Error please try again")
      continue 
  
  
def instructions():
  #instructions
  print("\n-------------GAME EXPLANATION-------------")  
  print("This game contains 5 different shapes such as ")
  print("[circle, rectangle, triangle, square, pentagon]")

  
  print("\n-------------HOW TO PLAY?-------------")
  print("1.This game will randomly generate 4 shapes from the 5 shapes available.")
  print("2.You are to guess and input the shape and it's position accordingly.")
  print("3.The game will determine how many shapes you have entered correctly. ")
  print("4.The game will end when you successfully enter the correct shape and it's position accordingly.")
  
  print("\n-------------Rules to follow-------------")
  print("1.User is to enter the initial alphabet of the shape such as-")
  print("c=Circle, r=Rectangle, t=Triangle, s=Square, p=Pentagon")

  print("\n1. Start game:")
  print("2. homepage:")
  
  #interactive commands for the program
  while True:
    command=input("\nEnter '1','2' to go to the desired page> ")
    print("--"*30)
    if command=='1':
      start()
      break
    elif command=='2':
      homepage()
      break
    else:
      print("Error please try again")
      continue 
    

def replay():
    print("")
    print("|"*35)
    print("Do you wanna play again? ")
    print("-"*35)
    print("\n1. Start game:")
    print("2. homepage:")
    print("3. Exit:")

    #interactive commands for the program
    while True:
      command=input("\nEnter '1','2','3' to go to the desired page> ")
      print("--"*30)
      if command=='1':
        start()
        break
      elif command=='2':
        homepage()
        break
      elif command=='3':
        exit()
      else:
        print("Error please try again")
        continue


#start the game
def start():
  shapes=['C','R','T','S','P']
  attempt=1
  print("")
  print("The shapes available are as follows:\n","c--Circle\n","r--Rectangle\n","t--Triangle\n","s--Square\n","p--Pentagon\n")
  print("enter ** if u wish to exit the game. \n")
  #generate random shapelist
  random_shapelist=random.sample(shapes,4)
  #print(random_shapelist)# use for demo of code.
  the_game(random_shapelist,shapes,attempt)

  
# continue 'the game' so loop will be available
def the_game(random_shapelist,shapes,attempt): 
  
  correct=0 
  shape_guessed=[]
  temporary_guess=[]
  temporary_shapelist=[]
  shapesonly_guess=0

  #prompt user to guess the shapes
  for guess in range(len(random_shapelist)):
    print("")
    user_input=input("Please guess the shape> ").upper()
  
    while True:
    
      #error handling when user enters invalid shape
      if user_input=="**":
        print("exit")
        exit()
      
      elif user_input != 'C' and user_input != 'R' and user_input != 'T' and user_input != 'S' and user_input != 'P':
        print("Shape not found! ")
        print("")
        user_input=input('Please guess the shape again> ').upper()
        
      else:
        shape_guessed.append(user_input)
        break
        
    print("user guessed: ",shape_guessed)      
            
  #guessed correctly 
  for i in range (4):
    if shape_guessed[i]==random_shapelist[i]:
      correct = correct + 1

  
  #correct but wrong placement
  for i in range (4):
    if shape_guessed[i] in shapes and shape_guessed[i] != random_shapelist[i]:
  
      temporary_guess.append(shape_guessed[i])
      temporary_shapelist.append(shapes[i])
  
  for i in range (len(temporary_guess)):
    if temporary_guess[i] in temporary_shapelist and shape_guessed[i] != temporary_shapelist[i]:
      shapesonly_guess = shapesonly_guess + 1
      

  #the mastermind(win)
  if correct==4:
    print("")
    print("*"*40)
    print(f"CONGRATS U ARE THE MASTERMIND. YOU ONLY TOOK {attempt} ATTEMPTS")
    print("*"*40)
    print("")
    print("correct shape guessed:",correct)
    print("correct shape guessed but wrong position:",shapesonly_guess)
    
    replay()

  #prints the number of correct shape and position, allows user to continue until correct
  else:
    print("correct shape guessed:",correct)
    print("correct shape guessed but wrong position:",shapesonly_guess)
    print("Please try again ")
    attempt+=1
    the_game(random_shapelist,shapes,attempt)
  
  



homepage()

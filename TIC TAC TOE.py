import random # imports a library to be able to randomly pick from a list 

player1_victory = False # initializes the bool flags that will become True when a victory/draw is detected
player2_victory = False
draw = False
game_ended = False 

player1_points = 0 # initializes a point counter to be display after each match 
player2_points = 0

player1_turn = random.choice([True, False]) # starts at random, player 1 plays first, when False, it's player2 or IA's turn to play 

empty = "_" # for visualisation in the terminal 
board = [empty] * 9 # we initialize a board, that is a 3x3 square so 9 values of index 0-8

########################################### IS THE CASE PLAYABLE FUNCTION #################################################

def is_playable(board) : 
    """ Returns a list of the indexes of the cases that are empty and allowed to be played on """
    
    possible_plays = []

    for index in range(9) : # for all board cases
        if board[index] == empty : # if the case is playable on 
            possible_plays.append(index) # add that playable case in a list

    return possible_plays # returns the list for the IA to pick a default play from, or check if a human's player input is valid 

########################################### IA PLAY FUNCTION #####################################################

def IA (board, sign) : 
    """ Function that when called, returns the index of board it wants to play in 
        Returns False in case of an error """ # we will use that returned value to modify the board 
    
    for player in ["O", "X"] : # Check if there's a horizontal win this turn, then a horizontal loss next turn and plays accordingly
        for case in [0, 3, 6] : 
            if board[case] == board[case+1] == player and board[case+2] == empty :
                return case + 2
            elif board[case] == board[case+2] == player and board[case+1] == empty :
                return case + 1 
            elif board[case+1] == board[case+2] == player and board[case] == empty :
                return case     

    for player in ["O", "X"] : # Check if there's a vertical win this turn, then a vertical loss next turn and plays accordingly
        for case in [0, 1, 2] : 
            if board[case] == board[case+3] == player and board[case+6] == empty : 
                return case + 6 
            if board[case] == board[case+6] == player and board[case+3] == empty :  
                return case + 3 
            if board[case+6] == board[case+3] == player and board[case] == empty : 
                return case     
    
    for player in ["O", "X"] : # check one diagonal for a win this turn, then a loss next turn and plays accordingly
        if board[0] == board[4] == player and board[8] == empty : 
            return 8
        if board[0] == board[8] == player and board[4] == empty :  
            return 4
        if board[4] == board[8] == player and board[0] == empty : 
            return 0

    for player in ["O", "X"] : # check the other diagonal for a win this turn, then a loss next turn and plays accordingly
        if board[2] == board[4] == player and board[6] == empty : 
            return 6
        if board[2] == board[6] == player and board[4] == empty :  
            return 4
        if board[4] == board[6] == player and board[2] == empty : 
            return 2

    if board == [empty] * 9 : # if the IA is first to play, always pick a corner
        return random.choice([0,2,6,8]) 

    return random.choice(is_playable(board)) # randomly picks a spot to play on among the empty ones

########################################### DISPLAY BOARD FUNCTION ##############################################

def display_board(board):
    """ called to display the current state of the board
    returns None """

    print(f"{board[0]}  {board[1]}  {board[2]}")
    print(f"{board[3]}  {board[4]}  {board[5]}")
    print(f"{board[6]}  {board[7]}  {board[8]}")

########################################### VICTORY CONDITIONS FUNCTION ##############################################""

def end_of_game(board) : 
    """ called to check if any condition of end of game are met : a player victory or a draw 
    if so, globally changes the value of game_ended to True and updates the score
    Returns None """
    global game_ended # the game_ended flag modifications has to be global so the gameplay loop can catch on it 
    global player1_points
    global player2_points

    player1_victory = False # initializes the bool flags that will become True when an end of game condition is met 
    player2_victory = False
    board_full = False

    if board[0] == board[1] == board[2] == "X" or board[3] == board[4] == board[5] == "X" or board[6] == board[7] == board[8] == "X" : 
        player1_victory = True # HORIZONTAL VICTORY FOR P1
    elif board[0] == board[3] == board[6] == "X" or board[1] == board[4] == board[7] == "X" or board[2] == board[5] == board[8] == "X" : 
        player1_victory = True # VERTICAL VICTORY FOR P1
    elif board[0] == board[4] == board[8] == "X" or board[2] == board[4] == board[6] == "X" : 
        player1_victory = True # DIAGONAL VICTORY FOR P1
    
    if player1_victory : 
        print("Player 1 wins!")
        game_ended = True
        player1_points += 1 
        
    if board[0] == board[1] == board[2] == "O" or board[3] == board[4] == board[5] == "O" or board[6] == board[7] == board[8] == "O" : 
        player2_victory = True # HORIZONTAL VICTORY FOR P2
    elif board[0] == board[3] == board[6] == "O" or board[1] == board[4] == board[7] == "O" or board[2] == board[5] == board[8] == "O" : 
        player2_victory = True # VERTICAL VICTORY FOR P2 
    elif board[0] == board[4] == board[8] == "O" or board[2] == board[4] == board[6] == "O" : 
        player2_victory = True # DIAGONAL VICTORY FOR P2 
      
    if player2_victory : 
        print("Player 2 wins!")
        game_ended = True
        player2_points += 1 

    played_case_counter = 0 # counts how many cases are played on 
    for element in board : 
        if element != empty : 
            played_case_counter +=1 
    if played_case_counter == 9 : # if the count reaches 9 and a victory didn't trigger earlier
        board_full = True # FLAGS draw AS True

    if board_full and not player1_victory and not player2_victory : 
        print("It's a draw!")
        game_ended = True
    
######################################## MODE PICK ###################################################

while True : 
    mode = int(input("How many players? Pick '1' (vs. IA) or '2' : "))
    if mode == 1 or mode == 2 : 
        break
    print("Please pick a valid number")
    
######################################## 2 PLAYER MODE ###############################################

while mode == 2 : # game loop that only stops if user inputs something other than yes on the replay? input

    while game_ended == False : # game_ended will be set to True by the end_of_game function after each player turn, breaking this loop
                                # and triggering the "replay?" option
        
        print("Player versus player game started!")
        display_board(board) # initial display of the empty board

        if player1_turn : 
            print("PLAYER 1'S TURN! The board cases have matching numbers from 1 to 9 in reading order") # instructions for the player
            
            while True :
                play = int(input("What case does Player 1 places X on? ")) # player inputs the case he plays on
                if play-1 in is_playable(board) : # if it's not an empty case, repeat the input request until it is 
                    break
                print(f'{play} is not an empty case')

            board[play-1] = "X" # board updates
            display_board(board) # board shows its current state
            end_of_game(board) # check if any end of game condition is met and updates game_ended Bool flag 
            if game_ended : # if so
                break # doesn't trigger player 2 turn, trigger replay? option
            player1_turn = False
        
        if not player1_turn :
            print("PLAYER 2'S TURN! The board cases have matching numbers from 1 to 9 in reading order")

            while True :
                play = int(input("What case does Player 2 places O on? ")) # player inputs the case he plays on
                if play-1 in is_playable(board) : # if it's not an empty case, repeat the input request until it is 
                    break
                print(f'{play} is not an empty case')

            board[play-1] = "O" 
            display_board(board)
            end_of_game(board)
            player1_turn = True

    if game_ended:     # a win / a draw is detected 
        print(f"SCORE : PLAYER ONE {player1_points} : {player2_points} PLAYER TWO")
        replay = input("Play again? Type yes or no ").lower()  # ask the user if they wanna replay
        if replay == "yes" or replay == "y ":   
            board = [empty] * 9    # clears board
            game_ended = False     # removes the game_ended flag
            player1_turn = random.choice([True, False])  # back to player 1 or 2 at random
        else : 
            print("Thanks for playing!") # bah casse toi alors ma foi???
            break

################################################ 1 PLAYER VS IA MODE ###################################################################

while mode == 1 : # game loop that only stops if user inputs something other than yes on the replay? input

    print("Player vs IA game started!")
    display_board(board) # initial display of the empty board

    while game_ended == False : # game_ended will be set to True by the end_of_game function after each player turn, breaking this loop
                                # and triggering the "replay?" option

        if player1_turn : 
            print("PLAYER 1'S TURN! The board cases have matching numbers from 1 to 9 in reading order") # instructions for the player

            while True :
                play = int(input("What case does Player 1 places X on? ")) # player inputs the case he plays on
                if play-1 in is_playable(board) : # if it's not an empty case, repeat the input request until it is 
                    break
                print(f'{play} is not an empty case')

            board[play-1] = "X" # board updates
            display_board(board) # board shows its current state
            end_of_game(board) # check if any end of game condition is met and updates game_ended Bool flag 
            if game_ended : # if so
                break # doesn't trigger player 2 turn, trigger replay? option
            player1_turn = False # IA's turn now
        
        if not player1_turn : # if its IA's turn
            board[IA(board, "O")] = "O" # IA puts its circle at a random place through the function IA()
            print("Player2 IA's play :") # little print for a cute mise en page 
            display_board(board) # displays current board state
            end_of_game(board) # checks for a victory or a draw 
            player1_turn = True # Player's turn now

    if game_ended:     # a win / a draw is detected 
        print(f"SCORE : PLAYER ONE {player1_points} : {player2_points} IA")
        replay = input("Play again? Type yes or no ").lower()  # ask the user if they wanna replay
        if replay == "yes" or replay == "y ":   
            board = [empty] * 9    # clears board
            game_ended = False     # removes the game_ended flag
            player1_turn = random.choice([True, False])  # back to player 1 or IA at random
        else : 
            print("Thanks for playing!") # bah casse toi alors ma foi???
            break

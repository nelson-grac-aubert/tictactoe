import random # imports a library to be able to randomly pick from a list

game_ended = False # initializes Bool flag that will be True when victory or draw is detected

player1_points = 0 # initializes a point counter to be displayed after each match
player2_points = 0

who_plays_first = random.choice([1,2]) # player who gets to act first is random
player1_turn = who_plays_first == 1    

empty = "_" # for visualisation in the terminal 
board = [empty] * 9 # we initialize a board, that is a 3x3 square so 9 values of index 0-8

def display_board(board):
    """ Called to display the current state of the board
    Returns None """

    print(f"{board[0]}  {board[1]}  {board[2]}")
    print(f"{board[3]}  {board[4]}  {board[5]}")
    print(f"{board[6]}  {board[7]}  {board[8]}")

def alternate() : 
    """ When called, alternates who gets to play first this match
        Updates the player1_turn Bool accordingly
        Returns None"""
    global who_plays_first, player1_turn # global to access and change variables on the global scope, aka the whole code 
                                         # we don't want to create a new local variable that'll disappear when the function call has returned 
    if who_plays_first == 1 :
         who_plays_first = 2
    else : 
        who_plays_first = 1

    if who_plays_first == 1 : 
        player1_turn = True
    else : 
        player1_turn = False

def is_playable(board) : 
    """ Returns a list of the indexes of the cells that are empty and allowed to be played on """
    
    possible_plays = [i for i in range(9) if board[i] == empty] 

    return possible_plays # returns the list for the IA to pick a play from, or check if a human's player input is valid 

def check_if_game_ended(board) : 
    """ Called to check for a player victory or a draw
    If so, globally changes the value of game_ended to True and updates the score
    Returns None """
    global game_ended, player1_points, player2_points 

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
        if mode == 2 : 
            print("Player 2 wins!")
        elif mode == 1 : 
            print("The AI wins!")
        game_ended = True
        player2_points += 1 

    played_cell_counter = 0 # if all 9 cells are played on, flags board_full as True
    for element in board : 
        if element != empty : 
            played_cell_counter +=1 
    if played_cell_counter == 9 : 
        board_full = True 

    if board_full and not player1_victory and not player2_victory : 
        print("It's a draw!")
        game_ended = True

def IA (board,diff) : 
    """ board is the current state of the game, diff is the difficulty
        Returns the index of board the AI will chose """ 
    
    if difficulty == 'hard' : 
        for player_sign in ["O", "X"] : # AI always plays circle, so first check all conditions with circle for an instant win this turn
                                        # then, check all conditions with cross to block a potential enemy win next turn
            
            # check if there's a horizontal win this turn, then a horizontal loss next turn and plays accordingly
            for cell in [0, 3, 6] : 
                if board[cell] == board[cell+1] == player_sign and board[cell+2] == empty :
                    return cell + 2
                elif board[cell] == board[cell+2] == player_sign and board[cell+1] == empty :
                    return cell + 1 
                elif board[cell+1] == board[cell+2] == player_sign and board[cell] == empty :
                    return cell     
            
            # check if there's a vertical win this turn, then a vertical loss next turn and plays accordingly
            for cell in [0, 1, 2] : 
                if board[cell] == board[cell+3] == player_sign and board[cell+6] == empty : 
                    return cell + 6 
                if board[cell] == board[cell+6] == player_sign and board[cell+3] == empty :  
                    return cell + 3 
                if board[cell+6] == board[cell+3] == player_sign and board[cell] == empty : 
                    return cell     
        
            # check the descending diagonal for a win this turn, then a loss next turn and plays accordingly
            if board[0] == board[4] == player_sign and board[8] == empty : 
                return 8
            if board[0] == board[8] == player_sign and board[4] == empty :  
                return 4
            if board[4] == board[8] == player_sign and board[0] == empty : 
                return 0

            # check the other diagonal for a win this turn, then a loss next turn and plays accordingly
            if board[2] == board[4] == player_sign and board[6] == empty : 
                return 6
            if board[2] == board[6] == player_sign and board[4] == empty :  
                return 4
            if board[4] == board[6] == player_sign and board[2] == empty : 
                return 2
    
    # if previous conditions fails and a corner is available, will pick one at random
    playable_corner = [i for i in [0, 2, 6, 8] if i in is_playable(board)]
    if playable_corner != [] and difficulty == 'hard': 
        return random.choice(playable_corner)
    else : # if all else fails, or if difficulty is easy, randomly picks a spot to play on among the empty ones
        return random.choice(is_playable(board)) 

def perform_player_turn(player_number, symbol):
    """ When called, takes the player input for his turn
        Updates the board accordingly, displays it, then check for end of game conditions
        Returns none"""
    global player1_turn

    print(f"PLAYER {player_number}'S TURN! The board cells have matching numbers from 1 to 9 in reading order")

    while True:
        try:
            cell_choice = int(input(f"What cell does Player {player_number} place {symbol} on? "))
            if cell_choice - 1 in is_playable(board): # -1 be cause list index are 0-8, but to be user friendly the cells are 1-9
                break
            print(f'{cell_choice} is not an empty cell')
        except ValueError: # handles user input errors, typos 
            print('Enter a number matching an empty cell (1-9)')

    board[cell_choice - 1] = symbol
    display_board(board)
    check_if_game_ended(board) 

    player1_turn = player_number != 1 

def perform_game_ending() : 
    """ When called, display current score, ask for continue or stop playing input
        If yes, clears board, calls alternate function, restart gameplay loop
        If no, display winner, final score, exit message
        Returns None """
    global game_ended, board, mode

    if mode == 2 :
        print(f"SCORE : PLAYER ONE {player1_points} : {player2_points} PLAYER TWO")
    else : 
        print(f"SCORE : PLAYER ONE {player1_points} : {player2_points} AI")
    
    while True : 
        replay = input("Play again? Type yes or no ").lower() # ask the user if they wanna replay
        if replay == "yes":   
            board = [empty] * 9  
            game_ended = False     
            alternate()
            break
        elif replay == "no" : 
            mode = 0 # breaks out of the gameplay loop 
            if player1_points > player2_points : 
                print(f"Player 1 wins {player1_points} to {player2_points}!")
            elif player1_points < player2_points and mode == 2 : 
                print(f"Player 2 wins {player2_points} to {player1_points}!")
            elif player1_points < player2_points and mode == 1 : 
                print(f"The AI wins {player2_points} to {player1_points}!")
            elif player1_points == player2_points : 
                print(f"It's a tie! {player1_points} point each")
            print("Thanks for playing!")
            break
        else : 
            print("Please type 'yes' or 'no' ").lower()
            continue

while True : # 2 player or 1 player vs. IA choice
    try : 
        mode = int(input("How many players? Pick '1' (vs. IA) or '2' : "))
        if mode == 1 or mode == 2 : 
            break
        print("Please pick a valid number (1 or 2)")
    except ValueError :
        print("Please enter a number (1 or 2)")

while mode == 1 : # IA difficulty choice
    difficulty = input("What difficulty? 'easy' or 'hard' : ")
    if difficulty == 'easy' or difficulty == 'hard' : 
        break
    print("Invalid input, please try again")

while mode == 2 : # 2 players gameplay loop

    print("Player versus player game started!")
    display_board(board) 

    while game_ended == False : 
        if player1_turn : 
            perform_player_turn(1, "X") 
            if game_ended :
                break # doesn't trigger player 2 turn, triggers replay? input
        if not player1_turn :
            perform_player_turn(2, "O") 
            
    perform_game_ending()

while mode == 1 : # 1 player gameplay loop 

    print("Player vs IA game started!")
    display_board(board)

    while game_ended == False : 

        if player1_turn : 
            perform_player_turn(1, "X")  
            if game_ended : 
                break # doesn't trigger AI turn, triggers replay? input
        
        if not player1_turn :
            board[IA(board,difficulty)] = "O" 
            print("IA's play :")
            display_board(board)
            check_if_game_ended(board)
            player1_turn = True
 
    perform_game_ending()
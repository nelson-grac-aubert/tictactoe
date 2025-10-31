# import a library to randomly pick from a list
import random 
# import a library to add artificial delay on AI decisions
import time 

# initialize Bool flag that will be True when victory or draw is detected
game_ended = False 
# initialize a point counter to be displayed after each match
player1_points = 0 
player2_points = 0
# initialize a board, that is a 3x3 square so 9 list values of index 0-8
empty = "_"  
board = [empty] * 9 

# player who gets to act first is random
who_plays_first = random.choice([1,2]) 
player1_turn = who_plays_first == 1  

def display_board(board) :
    """ When called, displays the current state of the board
    Returns None """

    print(f"{board[0]}  {board[1]}  {board[2]}")
    print(f"{board[3]}  {board[4]}  {board[5]}")
    print(f"{board[6]}  {board[7]}  {board[8]}")

def alternate() : 
    """ When called, alternates who gets to play first this match
        Updates the player1_turn Bool accordingly
        Returns None """
    
    # global to access and change variables on the global scope, aka the whole code 
    global who_plays_first, player1_turn 
                                          
    if who_plays_first == 1 : who_plays_first = 2
    else : who_plays_first = 1

    if who_plays_first == 1 : player1_turn = True
    else : player1_turn = False

def is_playable(board) : 
    """ Returns a list of the indexes of the cells that are allowed to be played on 
        Used for the IA's algorithm and to check if player's inputs are valid """
    
    possible_plays = [i for i in range(9) if board[i] == empty] 
    return possible_plays  

def check_if_game_ended(board) : 
    """ When called, checks for a player victory or a draw
    If so, globally changes the value of game_ended to True and updates the score
    Returns None """
    global game_ended, player1_points, player2_points 

    # initialize Bool flags that will become True when win/draw condition is met 
    player1_victory = False 
    player2_victory = False
    board_full = False

    # horizontal, then vertical, then diagonal win conditions
    if board[0] == board[1] == board[2] == "X" or board[3] == board[4] == board[5] == "X" \
    or board[6] == board[7] == board[8] == "X" : 
        player1_victory = True 
    elif board[0] == board[3] == board[6] == "X" or board[1] == board[4] == board[7] == "X" \
    or board[2] == board[5] == board[8] == "X" : 
        player1_victory = True
    elif board[0] == board[4] == board[8] == "X" or board[2] == board[4] == board[6] == "X" : 
        player1_victory = True
    
    if player1_victory : 
        print("Player 1 wins!")
        game_ended = True
        player1_points += 1 
        
    if board[0] == board[1] == board[2] == "O" or board[3] == board[4] == board[5] == "O" \
    or board[6] == board[7] == board[8] == "O" : 
        player2_victory = True 
    elif board[0] == board[3] == board[6] == "O" or board[1] == board[4] == board[7] == "O" \
    or board[2] == board[5] == board[8] == "O" : 
        player2_victory = True 
    elif board[0] == board[4] == board[8] == "O" or board[2] == board[4] == board[6] == "O" : 
        player2_victory = True 
      
    if player2_victory : 
        if mode == 2 : 
            print("Player 2 wins!")
        elif mode == 1 : 
            print("The AI wins!")
        game_ended = True
        player2_points += 1 

    # draw conditions 
    played_cell_counter = 0 
    for element in board : 
        if element != empty : 
            played_cell_counter +=1 
    if played_cell_counter == 9 : 
        board_full = True 

    if board_full and not player1_victory and not player2_victory : 
        print("It's a draw!")
        game_ended = True

def IA(board,sign) : 
    """ board is the current state of the game, sign is always "O" 
        Returns the index of board the AI will chose """ 
    
    print("Let me think...")
    time.sleep(1)

    # check for an immediate win, then for a potential loss next turn
    # and return a play that wins now / prevent loss next turn
    if difficulty == 'hard' : 
        for player_sign in [sign, "X"] :                     
            # horizontal check
            for cell in [0, 3, 6] : 
                if board[cell] == board[cell+1] == player_sign and board[cell+2] == empty :
                    return cell + 2
                elif board[cell] == board[cell+2] == player_sign and board[cell+1] == empty :
                    return cell + 1 
                elif board[cell+1] == board[cell+2] == player_sign and board[cell] == empty :
                    return cell     
            # vertical check
            for cell in [0, 1, 2] : 
                if board[cell] == board[cell+3] == player_sign and board[cell+6] == empty : 
                    return cell + 6 
                if board[cell] == board[cell+6] == player_sign and board[cell+3] == empty :  
                    return cell + 3 
                if board[cell+6] == board[cell+3] == player_sign and board[cell] == empty : 
                    return cell     
            # descending diagonal check
            if board[0] == board[4] == player_sign and board[8] == empty : 
                return 8
            if board[0] == board[8] == player_sign and board[4] == empty :  
                return 4
            if board[4] == board[8] == player_sign and board[0] == empty : 
                return 0
            # ascending diagonal check
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
    # if all else fails, or if difficulty is easy, randomly picks a spot to play on among the empty ones
    else : 
        return random.choice(is_playable(board)) 

def perform_player_turn(player_number, symbol):
    """ When called, takes the player input for his turn
        Updates the board accordingly, displays it, then check for end of game conditions
        Gives next move to the opponent, Returns None"""
    global player1_turn

    print(f"PLAYER {player_number}'S TURN! The board cells have matching numbers from 1 to 9 in reading order")

    while True:
        try:
            cell_choice = int(input(f"What cell does Player {player_number} place {symbol} on? "))
            # -1 because list index are 0-8, but to be user friendly the cells are 1-9
            if cell_choice - 1 in is_playable(board): 
                break
            print(f'{cell_choice} is not an empty cell')

        # handles user input errors, typos 
        except ValueError: 
            print('Enter a number matching an empty cell (1-9)')

    board[cell_choice - 1] = symbol
    display_board(board)
    check_if_game_ended(board) 

    # right part is a Bool, True if currently player 2 turn  
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
        replay = input("Play again? Type yes or no ").lower() 
        if replay == "yes":   
            board = [empty] * 9  
            game_ended = False     
            alternate()
            break
        elif replay == "no" : 
            # breaks out of the gameplay loop 
            mode = 0 
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
            # handles user input errors
            print("Please type 'yes' or 'no' ")

def gameplay() :
    """ Game mode selection, IA difficulty selection if relevant
    Gameplay loop """

    global game_ended, player1_points, player2_points, player1_turn, \
    board, who_plays_first, difficulty, mode

    # 2 players or 1 player vs. IA choice
    while True : 
        try : 
            mode = int(input("How many players? Pick '1' (vs. IA) or '2' : "))
            if mode == 1 or mode == 2 : 
                break
            print("Please pick a valid number (1 or 2)")
        except ValueError :
            print("Please enter a number (1 or 2)")

    # IA difficulty choice
    while mode == 1 : 
        difficulty = input("What difficulty? 'easy' or 'hard' : ")
        if difficulty == 'easy' or difficulty == 'hard' : 
            break
        print("Invalid input, please try again")

    # 2 players gameplay loop
    while mode == 2 : 

        print("Player versus player game started!")
        display_board(board) 

        while game_ended == False : 
            if player1_turn : 
                perform_player_turn(1, "X") 
                if game_ended :
                    # doesn't trigger player 2 turn, triggers replay? input
                    break 
            if not player1_turn :
                perform_player_turn(2, "O") 
                
        perform_game_ending()

    # 1 player gameplay loop 
    while mode == 1 : 

        print("Player vs IA game started!")
        display_board(board)

        while game_ended == False : 

            if player1_turn : 
                perform_player_turn(1, "X")  
                if game_ended : 
                    # doesn't trigger AI turn, triggers replay? input
                    break 
            
            if not player1_turn :
                board[IA(board,"O")] = "O" 
                print("IA's play :")
                display_board(board)
                check_if_game_ended(board)
                player1_turn = True
    
        perform_game_ending()

gameplay()
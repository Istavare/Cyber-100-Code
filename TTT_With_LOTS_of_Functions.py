import random
import copy

def play_game() -> None:
  """
  Initializes and runs the main game loop
  """
  saveList = []
  
  for q in range(3):
    saveListPart = ["-" for i in range(3)]
    saveList.append(saveListPart)
  
  def printBoard(board: list[list[str]]) -> None:
    """
    Prints the current board to the console with proper formatting

    Inputs:
      board (list[list[str]]): 3x3 list of strings representing a grid
    """
    for q in range(len(board)):
      for w in range(len(board[q])):
        if w != 2:
          print(" " + board[q][w]  + " |",end="")
        else:
          print(" " + board[q][w]  + " ",end="")
      print()
      if q != 2:
        print("---+---+---")
      else:
        print()
  
  def win(board: list[list[str]], player: str) -> bool:
    """
    Checks if the player has a winning configuration

    Inputs:
      board (list[list[str]]): Current game board
      player (str): Symbol to check ('X' or 'O')

    Returns:
      bool: True if the player won, and False otherwise
    """
    if board[0][0] == player and board[0][1] == player and board[0][2] == player: #row 1
      return(True)
    if board[1][0] == player and board[1][1] == player and board[1][2] == player: #row 2
      return(True)
    if board[2][0] == player and board[2][1] == player and board[2][2] == player: #row 3
      return(True)
    if board[0][0] == player and board[1][0] == player and board[2][0] == player: #column 1
      return(True)
    if board[0][1] == player and board[1][1] == player and board[2][1] == player: #column 2
      return(True)
    if board[0][2] == player and board[1][2] == player and board[2][2] == player: #column 3
      return(True)
    if board[0][0] == player and board[1][1] == player and board[2][2] == player: #left to right diagonal
      return(True)
    if board[0][2] == player and board[1][1] == player and board[2][0] == player: #right to left diagonal
      return(True)
  
  def tie(board: list[list[str]]) -> bool:
    """
    Checks if the board is full with no wins

    Inputs:
      board (list[list[str]]): Current game board

    Returns:
      bool: True if there is a tie, and False otherwise
    """
    for q in board:
      for w in q:
        if w == "-":
          return(False)
    return(True)
  
  def winningMove(board: list[list[str]], role: str) -> tuple[int, int]:
    """
    Simulates the board to see if 'role' has a move that wins

    Inputs:
      board (list[list[str]]): Current game board
      role (str): Symbol ('X' or 'O')

    Returns:
      tuple[int, int]: The (row, column) coordinates of the winning move, or (-1, -1) if none exists
    """
    boardCopy = board.copy()
    for q in range(len(boardCopy)):
      for w in range(len(boardCopy[q])):
        if boardCopy[q][w] == "-":
          boardCopy[q][w] = role
          if win(boardCopy, role):
            return(q, w)
          else:
            boardCopy[q][w] = "-"
    return(-1, -1)
  
  def forks(board: list[list[str]], role_f: str, role_p: str) -> tuple[int, int]:
    """
    Checks for a 'fork' opportunity (a move that creates two winning lines)

    Inputs:
      board (list[list[str]]): Current game board
      role_f (str): Role creating the fork
      role_p (str): Opponent

    Returns:
      tuple[int, int]: The (row, column) of the fork move or (-1, -1)
    """
    boardCopy = copy.deepcopy(board)
    for q in range(len(boardCopy)):
      for w in range(len(boardCopy[q])):
        if boardCopy[q][w] == "-":
          boardCopy[q][w] = role_f
          (w1, w2) = winningMove(boardCopy, role_f)
          if (w1, w2) != (-1,-1):
            boardCopy[w1][w2] = role_p
            if winningMove(boardCopy, role_f) != (-1,-1):
              boardCopy[w1][w2] = "-"
              boardCopy[q][w] = "-"
              return(q,w)
            boardCopy[w1][w2] = "-"
          boardCopy[q][w] = "-"
    return(-1,-1)
  
  def ai(board: list[list[str]], bot_role: str, player_role: str) -> tuple[int, int]:
    """
    AI logic controller that determines the best move based off of priority

    Inputs:
      board (list[list[str]]): Current game board
      bot_role (str): AI's letter
      player_role (str): Player's letter

    Returns:
      tuple[int, int]: The (row, col) of the chosen move
    """
    #Check for winning move
    winOutBot = winningMove(board, bot_role)
    if winOutBot[0] != -1:
      return(winOutBot)
    #Block opponent from their winning move
    winOutPlayer = winningMove(board, player_role)
    if winOutPlayer[0] != -1:
      return(winOutPlayer)
    #Play Forks
    (f1, f2) = forks(board, bot_role, player_role)
    if (f1, f2) != (-1,-1):
      return(f1, f2)
    #Prevent forks
    (f3, f4) = forks(board, player_role, bot_role)
    if (f3, f4) != (-1,-1):
      return(f3, f4)
    #Checks Center
    if board[1][1] == "-":
      return(1, 1)
    #Checks Corners
    cornerList = [(0,0), (2,0), (0,2), (2,2)]
    while len(cornerList) > 0:
      randListIndex = random.randint(0,len(cornerList)-1)
      if board[cornerList[randListIndex][0]][cornerList[randListIndex][1]] == "-":
        return(cornerList[randListIndex])
      else:
        cornerList.pop(randListIndex)
    #Checks Sides
    sideList = [(0,1), (1,0), (1,2), (2,1)]
    while True:
      randXVal = random.randint(0,2)
      randYVal = random.randint(0,2)
      if (randXVal, randYVal) in sideList and board[randXVal][randYVal] == "-":
        return(randXVal, randYVal)
  #Randomize Roles
  playerRole = "-"
  botRole = "-"
  xo = random.randint(1,2)
  if xo == 1:
    playerRole = "X"
    botRole = "O"
  else:
    playerRole = "O"
    botRole = "X"
  
  turn = random.randint(1, 2)
  while True:
    print("\033c")
    print("You're " + playerRole + ", and the bot is " + botRole + ". \n")
    printBoard(saveList)
    if tie(saveList):
      print("Tie!")
      break
    if turn == 1:
      while True:
        inputRow = input("Which row? ")
        inputColumn = input("Which column? ")
        if(inputRow.isdigit() and inputColumn.isdigit()):
          inputRow = int(inputRow)-1
          inputColumn = int(inputColumn)-1
          if inputRow >= 0 and inputRow <= 2 and inputColumn >= 0 and inputColumn <= 2 and saveList[inputRow][inputColumn] == "-":
            break
          print("\nBad input: \n- Entered number must be greater than or equal to 1.\n- Entered number must be less than or equal to 3.\n- Space can not be taken.\nPlease try again.\n")
        else:
          print("\nYou must enter valid integers!\nPlease try again.\n")
      saveList[inputRow][inputColumn] = playerRole
      if win(saveList, playerRole):
        print("\nPlayer has won!\n")
        printBoard(saveList)
        break
      turn = 2
    else:
      (r,c) = ai(saveList, botRole, playerRole)
      saveList[r][c] = botRole
      if win(saveList, botRole):
        print("Bot has won!\n")
        printBoard(saveList)
        break
      turn = 1
while True:
    play_game()
    user_input = input("\nPress Enter to exit, or type anything and press Enter to restart: ").strip()
    if not user_input:

        break

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Vérification des lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]  # Retourne le symbole du gagnant

    # Vérification des colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]  # Retourne le symbole du gagnant

    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]  # Retourne le symbole du gagnant

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]  # Retourne le symbole du gagnant

    return None  # Aucun gagnant

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0  # Compteur de mouvements

    while moves < 9:  # Maximum de 9 mouvements
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input! Please enter numbers between 0 and 2.")
                continue
            
            if board[row][col] == " ":
                board[row][col] = player
                moves += 1  # Incrémente le compteur de mouvements
                
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    print("Player " + winner + " wins!")
                    return  # Fin du jeu
                
                # Changer de joueur
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    print_board(board)
    print("It's a draw!")  # Message de match nul

tic_tac_toe()
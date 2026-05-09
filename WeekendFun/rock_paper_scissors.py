#Rock-Paper-Scissors (One Round): Ask Player 1 and
#Player 2 to enter: "rock", "paper", or "scissors" Print:
#"Player 1 wins"
#"Player 2 wins"
#"Tie" Use nested if-else.
#Hint: 1. Rock beats Scissors looses to Paper
#2. Paper beats Rock but looses to Scissors
#3. Scissors beats Paper but looses to Rock


def get_winner(player1, player2):
    if player1.lower() == "rock" and player2.lower() == "scissors":
        result = "Player1 wins"       
    elif player2.lower() == "paper" and player1.lower()  == "scissors":
        result = "Player1 wins"
    elif player2.lower() == "rock" and player1.lower() == "paper":
        result = "Player1 wins"
    elif player2.lower() == "rock" and player1.lower() == "scissors":
        result = "Player2 wins"
    elif player1.lower() == "paper" and player2.lower() == "scissors":
        result = "Player2 wins"
    elif player1.lower() == "rock" and player2.lower() == "paper":
        result = "Player2 wins"
    elif player1 == player2:
        result =  "Tie"
    else:
        result = "wrong entry"
    return result


player1 = input('Player1: Enter "rock", "paper", or "scissors": ')
player2 = input('Player2: Enter "rock", "paper", or "scissors": ')
print(get_winner(player1, player2))

        

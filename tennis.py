# Run this program by using the following terminal command: "python tennis.py"

# Import sys to allow program termination by user
import sys


def print_scoreline():
    # Request user input for the current scoreline in the specified format
    scoreline_numeric = input(
        'Scoreline in no. of points (score_player1 - score_player2): '
    )

    # Process the request to terminate the program
    if scoreline_numeric.lower() == "exit":
        print("Exiting program.")
        sys.exit()

    try:
        # If possible, extract the numerical scores from the user input
        score_player1, score_player2 = [
            int(s) for s in scoreline_numeric.replace(' ', '').split('-')
        ]

        # Dictionary of score names based on the numerical value
        score_names = {0: 'Love', 1: 'Fifteen', 2: 'Thirty',  3: 'Forty'}

        # Check if the scoreline results in a Deuce
        if score_player1 == score_player2 and score_player1 >= 3:
            scoreline = 'Deuce'

        # Check if the scoreline results in a named score based on score_names
        elif (score_player1 <= 3) and (score_player2 <= 3):

            # Check if the scores are equal ("x-all")
            if score_player1 == score_player2:
                scoreline = f'{score_names[score_player1]}-all'

            # Otherwise, obtain the full scoreline
            else:
                scoreline = f'{score_names[score_player1]}-{score_names[score_player2]}'

        # Check for the remaining cases
        else:

            # Calculate the absolute score difference
            score_diff = abs(score_player1 - score_player2)

            # Determine the number of the player (1 or 2) that is ahead
            player_ahead = (score_player2 > score_player1) + 1

            # Check for an advantage condition of the player ahead
            if score_diff == 1:
                scoreline = f'Advantage for player{player_ahead}'

            # Check for a win condition of the player ahead
            elif max(score_player1, score_player2) == 4 or score_diff == 2:
                scoreline = f'Win for player{player_ahead}'

            # Otherwise, the scoreline is invalid
            else:
                scoreline = 'Invalid scoreline!'

        # Print the scoreline
        print(scoreline)

    except ValueError:
        # Restart the program if the user input is invalid
        print('Please only insert non-negative integers in the correct format.')


if __name__ == '__main__':
    print('Type "exit" to terminate the program.')
    print()

    # Run the program until the user terminates
    while True:
        print_scoreline()
        print()

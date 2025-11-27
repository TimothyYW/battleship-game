def get_username():
    """
    function getting username for welcome message
    """
    while True:
        user_name = input("Enter your name:")
        if user_name:
            print(f"Welcome to the battleship game {user_name}!")
            return user_name
        else:
            print("Please enter your name.")
            
def guide_rule():
    """
    function to display rule for the game
    """
    print("rule of game: ")
    print("there are 5 ships for player and computer")
    print("give them coordinate for row and column from 0 to 10")
    print("once 5 ships has been sunk,the game will be over")
    print("have fun!")
    
def create_battlefield(map_size):
    """
    function to create a map based on size
    """
    return [["_"] * map_size for _ in range(map_size)]
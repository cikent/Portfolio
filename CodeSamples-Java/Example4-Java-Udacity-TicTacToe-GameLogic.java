    /**
     * Checks if the game has ended either because a player has won, or if the game has ended as a tie.
     * If game hasn't ended the return string has to be "None",
     * If the game ends as tie, the return string has to be "Tie",
     * If the game ends because there's a winner, it should return "X wins" or "O wins" accordingly
     * @param grid 2D array of characters representing the game board
     * @return String indicating the outcome of the game: "X wins" or "O wins" or "Tie" or "None"
     */
    
    public String checkGameWinner(char [][]grid){
        String result = "None";
                // no one can even win unless there are at least 4 or less Free Spots remaining
        if (freeSpots <= 4){
            // Check's if X has Won
            // check if [1][0] has an X
            if (grid[1][0] == 'x') {
                // check if vertical or horizontal positions match
                if (grid[0][0] == 'x' && grid[2][0] == 'x' || grid[1][1] == 'x' && grid[1][2] == 'x') {
                    result = "X Wins";
                }
            }
            // check if [0][1] has an X
            if (grid[0][1] == 'x') {
                    // check if vertical or horizontal positions match
                    if (grid[1][1] == 'x' && grid[2][1] == 'x' || grid[0][0] == 'x' && grid[0][2] == 'x') {
                        result = "X Wins";
                    }
            }
            // check if [2][1] has an X
            if (grid[2][1] == 'x') {
                    // check if vertical or horizontal positions match
                    if (grid[0][1] == 'x' && grid[1][1] == 'x' || grid[2][0] == 'x' && grid[2][2] == 'x') {
                        result = "X Wins";
                }
            }
            // check if [1][2] has an X
            if (grid[1][2] == 'x') {
                // check if vertical or horizontal positions match
                if (grid[0][2] == 'x' && grid[2][2] == 'x' || grid[1][0] == 'x' && grid[1][1] == 'x') {
                    result = "X Wins";
                }
            }
            // check if [1][1] has an X
            if (grid[1][1] == 'x') {
                // check if diagonal positions match
                if (grid[0][0] == 'x' && grid[2][2] == 'x' || grid[0][2] == 'x' && grid[2][0] == 'x') {
                    result = "X Wins";
                }
            }
            // Check's if O has Won
            // check if [1][0] has an O
            if (grid[1][0] == 'o') {
                // check if vertical or horizontal positions match
                if (grid[0][0] == 'o' && grid[2][0] == 'o' || grid[1][1] == 'o' && grid[1][2] == 'o') {
                    result = "O Wins";
                }
            }
            // check if [0][1] has an O
            if (grid[0][1] == 'o') {
                // check if vertical or horizontal positions match
                if (grid[1][1] == 'o' && grid[2][1] == 'o' || grid[0][0] == 'o' && grid[0][2] == 'o') {
                    result = "O Wins";
                }
            }
            // check if [2][1] has an O
            if (grid[2][1] == 'o') {
                // check if vertical or horizontal positions match
                if (grid[0][1] == 'o' && grid[1][1] == 'o' || grid[2][0] == 'o' && grid[2][2] == 'o') {
                    result = "O Wins";
                }
            }
            // check if [1][2] has an O
            if (grid[1][2] == 'o') {
                // check if vertical or horizontal positions match
                if (grid[0][2] == 'o' && grid[2][2] == 'o' || grid[1][0] == 'o' && grid[1][1] == 'o') {
                    result = "O Wins";
                }
            }
            // check if [1][1] has an O
            if (grid[1][1] == 'o') {
                // check if diagonal positions match
                if (grid[0][0] == 'o' && grid[2][2] == 'o' || grid[0][2] == 'o' && grid[2][0] == 'o') {
                    result = "O Wins";
                }
            }
        }
        // evaluate if no win-conditions are active for X or O and if Free Spots is still 0 then its a Tie
        if (freeSpots == 0 && result == "None"){
            result = "Tie";
        }
        return result;
    }
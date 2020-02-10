#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

/*
Compile: 
- gcc high_score.c -o high_score
*/
// 16 bytes
struct player {
    char name[12]; 
    int score; 
}; 


// Scores of previous players
int scores[20] = {17,25,26,39,54,67,92,101};
int total_size = 8; 

struct player *player; 

int is_high_score(score){

    // Not high score 
    if(score < scores[total_size -1]){
        return 0;
    }

    // High score!
    scores[total_size] = score; 
    score++; 
    return 1; 
}

// Get the random score for the user. 
int add_score(){
    
    // My Score!
    // 16 bytes
    int size = 4; 
    int *p_array = (int *)malloc(sizeof(int)*size);
    int r; 
    int total; 

    // Can get this to be allocated in the spot that is free, with a few tries
    // Seems to like the 4th element!
    // Which makes sense, compared to the struct. 
    for(int i = 0; i < size; i++){
        p_array[i] = i+100;  
    }

    // Gets the total score...
    // Add these numbers to randomly generated values...
    for(int i =0; i < size; i++){
        r = rand() % 16; 
        total = total + r + (p_array[i] - 90);
    }

    free(p_array);
    return total; 
}

void setup(){
    srand(time(NULL)); 
}

int main()
{
    char line[128];
    int has_user_been_created;  // Has the player been created
    int new_score; 
    puts("This is a game about who can get the highest score! The highest score seen in 100; can you break the high score?");
    setup();

    // Loop to play the game :)
    while(1){

        puts("Please select from the following options:\n 1. create\n 2. reset\n 3. new\n 4. won");
        // Gets the input
        if(fgets(line, sizeof(line), stdin) == NULL) break;


        // The game! \\
        // Create the user
        if(strncmp(line, "create", 5) == 0) {
            player = malloc(sizeof(player));
            memset(player,0,sizeof(player));

            // Initialize the player
            puts("Please enter a name: ");
            if(fgets(player->name, 12, stdin) == NULL) break;
            player->score=0;
            printf("Player name is set to %s\n", player->name);
            has_user_been_created = 1; 
            
        }

        // Deletes the current player
        if(strncmp(line, "reset", 5) == 0 && has_user_been_created == 1){
            free(player);
            puts("Player has been removed!");
        }
        
        // Plays the game!
        if(strncmp(line, "new", 3) == 0 && player != NULL) {
            new_score = add_score();
            printf("Your new score is %d\n", new_score);
        }

        // Sets the new score for the user. 
        if(strncmp(line, "set", 3) == 0 && player != NULL) {
            player->score = new_score; 
            printf("The score is set!\n");
        }

        // Checks to see if the user has the high score!
        if(strncmp(line, "won", 3) == 0){
            // Set a score to 101, which seems to be impossible with the RNG that we can add. 
            printf("\nPlayer->name: %s... \nPlayer->score %d\n", player->name, player->score);
            // checks to see if the user has the high score!
            int high_score = is_high_score(player->score);
            if(high_score){
		FILE *fp; 
		int c; 
		fp = fopen("flag.txt","r");
		if(fp){
			while((c = getc(fp)) != EOF)
				putchar(c); 
        		fclose(fp);
			return 0; 
		}
            }
        }
    }



    return 0;
}


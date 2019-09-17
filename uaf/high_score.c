#include <stdio.h>
#include <time.h>
#include <stdlib.h>

struct player {
    char name[12]; 
    int score; 
}; 

int scores[20];
struct player *player; 

void add_first_scores(){
    // Add a score that is MUCH larger than 400.
}

// Get the random score for the user. 
int add_score(){
    
    // My Score!
    int *p_array = (int *)malloc(sizeof(int)*15);
    int r; 
    for(int i = 0; i < 15; i++){
        p_array[i] = i; 
    }

    // Gets the total score...
    for(int i =0; i < 15; i++){
        r = r + p_array[i];
    }
    return r; 
}

void setup(){
    srand(time(NULL)); 
}

int main()
{
    char line[128];
    int has_user_been_created; 
    int new_score; 

    setup();

    while(1){

        puts("Please select from the following options: ");
        // Gets the input
        if(fgets(line, sizeof(line), stdin) == NULL) break;

        // OPTIONS
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
        
        if(strncmp(line, "best", 4) == 0 && player != NULL) {
            new_score = add_score();
            printf("Your new score is %d\n", new_score);
        }

        if(strncmp(line, "set", 3) == 0 && player != NULL) {
            player->score = new_score; 
            printf("The score is set!");
        }

        // Deletes the current player
        if(strncmp(line, "reset", 5) == 0){
            free(player);
        }

        // checks to see if the user has the high score!
        if(strncmp(line, "won", 3) == 0){
            printf("\nPlayer->name: %s... \nPlayer->score %d", player->name, player->score);
            // checks to see if the user has the high score!
        }

        // Delete the player (check if a player HAS existed)
        // Create new player 
        // Play the new game

    }



    return 0;
}


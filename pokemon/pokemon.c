/*
Can you get your pokemon above level 100? 

Compile: gcc pokemon.c -lm -o pokemon
Run: ./pokemon 
Need: stat.csv also.

*/

#include <strings.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <complex.h>
#include<time.h> 

#define true 1 
#define false 0

#define ROWS 18
#define COLUMNS 10 
#define STRING_LENGTH 40

// Definition of a move
struct Move {
	char name[50];
	unsigned int power; 
	unsigned int accuracy; 
};
// Definiton of a pokemon 
struct Pokemon {
	int id; 
	char name[50]; 
	unsigned int level; 
	unsigned int experience;
	unsigned int HP;
	unsigned int growth_rate;
	struct Move move1;
	struct Move move2; 
	struct Move move3; 
	struct Move move4;

};
struct Pokemon myself; 
struct Pokemon enemy; 

/*
Structure of csv file: 
0: Pokemon Name 
1: Level -> NA
2: Exp -> NA
3: HP multiplier
4: growth_rate (0-3), going from slow to fast
5: Move1 name 
6: Move1 power 
7: Move1 accuracy
8: Move2 name 
9: Move2 power 
10: Move2 accuracy
11: Move3 name 
12: Move3 power 
13: Move3 accuracy
14: Move4 name 
15: Move4 power 
16: Move4 accuracy
17: ID of pokemon 
*/
char import_matrix[ROWS][COLUMNS][STRING_LENGTH];
int import_matrix_size; 


// Function declarations 
void import(); 
void transfer(int , int, int, int); 
unsigned fast(int);
unsigned int fast_medium(int);
unsigned int slow_medium(int);
unsigned int slow(int);
int choose_pokemon(); 
void does_level_up(); 
void stats_screen();
void after_battle(); 
int did_hit(int ); 
int select_move(int); 
void intro(); 
void show_statline(int); 
int battle(); 
int init(); 

// Imports the pokemon csv file in the import_matrix array for use in other functions. 
void import(){
	size_t len = 0; // Current spot in the file. 
	char * line; // Location of the buffer 
	size_t read; // Size of the data just read. 
	FILE * text_file; // Pointer to the file. 
	int row = 0; 
	// https://stackoverflow.com/questions/3501338/c-read-file-line-by-line

	text_file = fopen("stats.csv","r");
    while ((read = getline(&line, &len, text_file)) != -1) {
		
		// Iterates over a given row. 
		char *token; 

		int col = 0; 
		while ((token = strsep(&line, ","))){
			//printf("%s\n", token);
			strncpy(import_matrix[col][row],token, STRING_LENGTH);
			//printf("%s\n",import_matrix[col][row]);
			col++;
		}
		
		row += 1; 
    }
	
	import_matrix_size = row;
}

// Transfers a pokemon into one of the player modules. 
/*
player: integer that is 0 for myself and 1 for enemy 
poke_index: The pokemon to load in, indexed from the import_matrix
level: The level of the pokemon to import 
exp: The amount of exp to give the pokemon initially. 
*/
void transfer(int player, int poke_index, int level, int exp){
	
	// Which pokemon to import into
	struct Pokemon* poke_struct; 
	if(player == 0){
		poke_struct = &myself; 
	}
	else{
		poke_struct = &enemy; 
	}
	
	// Name, level, exp and HP set for pokemon. 
	strncpy(poke_struct->name, import_matrix[0][poke_index], 50);
	printf("Poke_struct Name: %s\n", poke_struct->name);
	printf("Myself Name: %s\n", myself.name);
	
	poke_struct->level = level; 
	printf("Level: %d\n", poke_struct->level);
	poke_struct->experience = exp; 
	printf("Exp: %d\n", poke_struct->experience);
	poke_struct->HP = level * atoi(import_matrix[3][poke_index]) * 3;
	printf("HP: %d\n", poke_struct->HP);
	poke_struct->growth_rate = atoi(import_matrix[4][poke_index]);
	
	// Moves 
	strncpy(poke_struct->move1.name, import_matrix[5][poke_index], 50);
	printf("Move1 Name: %s\n", poke_struct->move1.name);
	poke_struct->move1.power = atoi(import_matrix[6][poke_index]);
	printf("Move1 Power: %d\n", poke_struct->move1.power);
	poke_struct->move1.accuracy = atoi(import_matrix[7][poke_index]);
	printf("Move1 Accuracy: %d\n", poke_struct->move1.accuracy);
	
	strncpy(poke_struct->move2.name, import_matrix[8][poke_index], 50);
	printf("Move2 Name: %s\n", poke_struct->move2.name);
	poke_struct->move2.power = atoi(import_matrix[9][poke_index]);
	printf("Move2 Power: %d\n", poke_struct->move2.power);
	poke_struct->move2.accuracy = atoi(import_matrix[10][poke_index]);
	printf("Move2 Accuracy: %d\n", poke_struct->move2.accuracy);
	
	strncpy(poke_struct->move3.name, import_matrix[11][poke_index], 50);
	printf("Move3 Name: %s\n", poke_struct->move3.name);
	poke_struct->move3.power = atoi(import_matrix[12][poke_index]);
	printf("Move3 Power: %d\n", poke_struct->move3.power);
	poke_struct->move3.accuracy = atoi(import_matrix[13][poke_index]);
	printf("Move3 Accuracy: %d\n", poke_struct->move3.accuracy);
	
	strncpy(poke_struct->move4.name, import_matrix[14][poke_index], 50);
	printf("Move4 Name: %s\n", poke_struct->move4.name);
	poke_struct->move4.power = atoi(import_matrix[15][poke_index]);
	printf("Move4 Power: %d\n", poke_struct->move4.power);
	poke_struct->move4.accuracy = atoi(import_matrix[16][poke_index]);
	printf("Move4 Accuracy: %d\n", poke_struct->move4.accuracy);
	
	poke_struct->id = atoi(import_matrix[17][poke_index]);

}

int choose_pokemon(){

	import(); // Import all pokemon into the import_matrix
	
	// Get the users preferred Pokemon 
	puts("Choose a pokemon to battle with:");
	for (int index=0; index < import_matrix_size; index++){
		printf("%d. %s\n", index+1, import_matrix[0][index]);
	}
	printf("\n>");
	int option_select;
	scanf ("%d",&option_select);
	if(option_select > import_matrix_size || option_select <= 0){
		option_select = 1;
	}
	show_statline(option_select-1);
	
	// Get input from user to set level 
	puts("Choose a level for that Pokemon that is lower than 50: ");
	printf("\n>");
	int level_select;
	scanf ("%d",&level_select);
	if( level_select> 50 || level_select <= 0){
		level_select = 5;
	}	
	int base_exp = 40 * pow(level_select-1,2); // calculate base exp 
	printf("Base EXP: %d\n",base_exp);
	transfer(0,option_select-1, level_select, base_exp); // 0 references the myself player. Getting the pokemon and the stats. 
	
	// Get the Enemies preferred Pokemon 
	puts("Choose a pokemon to battle AGAINST:");
	for (int index=0; index < import_matrix_size; index++){
		printf("%d. %s\n", index+1, import_matrix[0][index]);
	}
	printf("\n>");
	scanf ("%d",&option_select);
	if(option_select > import_matrix_size){
		option_select = 1;
	}
	show_statline(option_select-1);
	
	// Get input from user to set level 
	puts("Choose a level for the enemy Pokemon that is lower than 50: ");
	printf("\n>");
	scanf ("%d",&level_select);
	if( level_select > 50 || level_select <= 0){
		level_select = 5;
	}	
	base_exp = 40 * pow(level_select-1,2); // calculate base exp 
	transfer(1,option_select-1, level_select, base_exp); // 1 references the enemy player. Getting the pokemon and the stats. 
	
	printf("Enemy: %d, %d, %d\n", level_select, enemy.HP,enemy.level);
	return true; 
}

/*
After a battle has occured, level things happen to the pokemon. 
- Get experience points 
- Check for level up 
*/
void after_battle(){
	int level_up = atoi(import_matrix[3][enemy.id-1]) * 10;  // enemy HP rating 

	int exp_to_level;
	if(myself.growth_rate == 0) exp_to_level = slow(myself.level);
	else if(myself.growth_rate == 1) exp_to_level = slow_medium(myself.level);
	else if(myself.growth_rate == 2) exp_to_level = fast_medium(myself.level);
	else exp_to_level = fast(myself.level);
	
	// Calculate experience points and if the pokemon should go to a new level
	int difficulty_points = level_up * enemy.level; 
	int final_exp = exp_to_level  + difficulty_points + myself.experience;
	myself.experience = final_exp;
	
	// Check to see if the pokemon should level up.
	does_level_up();
}

// Determines if a player got hit by an attack or not. 
// accuracy: Accuracy of the move 
int did_hit(int accuracy){
	srand(time(0)); 
	int random_value = rand(); 
	if(random_value % 256 < (float) 255 * ((float)accuracy * 0.01)){
		return true; 
	}
	
	return false; 
}

// 0 for myself, 1 for CPU 
int select_move(int player){
	
	int move = 0; 
	if(player == 0){
		
		puts("\nChoose a move: "); 
		
		// Show interactive panel to choose move.
		printf("\nNO \t Name: \t\t\t Power \t Accuracy\n");
		printf("1. \t%s : \t %d \t %d\n", myself.move1.name, myself.move1.power, myself.move1.accuracy); 
		printf("2. \t %s : \t\t %d \t %d\n", myself.move2.name, myself.move2.power, myself.move2.accuracy); 
		printf("3. \t %s : \t\t %d \t %d\n", myself.move3.name, myself.move3.power, myself.move3.accuracy); 
		printf("4. \t %s : \t\t %d \t %d\n", myself.move4.name, myself.move4.power, myself.move4.accuracy); 		
		printf(">");
		scanf ("%d",&move);
		if(move >= 4 || move < 0){
			move = 0;
		}			
		move = move -1;
	}
	else{
		srand(time(0)); 
		int random_value = rand() % 4; 
		move = random_value; 
	}
	
	return move;
}

/*
Have enemy randomly pick a move. 
Check if one has died? 
If not, keep playing. 
*/
int battle(){
	int turn = 0; // CPU goes first.
	struct Pokemon* attacker; 
	struct Pokemon* defender; 
	
	stats_screen();
	while(myself.HP != 0 && enemy.HP != 0) {

		// Makes the code easier to follow whose attacking who. 
		if(turn % 2 == 0){
			 attacker = &myself; 
			 defender = &enemy; 
		}
		else{
			attacker = &enemy; 
			defender = &myself; 
		}
		
		// Creating a pointer to the move to be used
		struct Move* move;
		int move_no = select_move(turn % 2);
		if(move_no == 0) move = &attacker->move1;
		else if(move_no == 1) move = &attacker->move2;
		else if(move_no == 2) move = &attacker->move3;
		else move = &attacker->move4;
		
		// The damage part of the calculation. 
		printf("%s attacks with %s ",attacker->name, move->name);
		if(did_hit(move->accuracy) == 1){
			int HP_left = (defender->HP - move->power);
			if(HP_left < 0){
				defender->HP = 0; 
			}else{
				defender->HP = HP_left;
			}
			printf("and hits %s for %d HP!\n\n",defender->name, move->power);
		}
		else{
			puts("and misses!");
		}
		
		// A single turn for both players 
		if(turn % 2 == 1){
			stats_screen();
		}
		turn += 1; // Change the turn
	}
	
	if(myself.HP == 0 ){
		puts("Game Over :( Tough Loss...");
		return 0;
	}
	else {
		printf("%s wins the battle! \n",attacker->name);
	}
	return 1; 
	
}

// Intro text
void intro(){
	// There goal is to get a pokemon to above level 100. Can you see how? 
	puts("Hi, Ash Ketchup has died in a terrible bike accident where he ran into a giant Oak tree. So, it is now your job to become the best pokemon trainer that ever lived!");
	puts("What was something that Ash or Red never did? Get a pokemon ABOVE level 100. Can you accomplish it?\n");
}

void stats_screen(){
	// Display both players HP... Maybe some ascii part even? 
	puts("Pokemon \t Health");
	puts("====================");
	printf("%s \t %d\n",myself.name, myself.HP);
	printf("%s \t %d\n\n",enemy.name, enemy.HP);
}

// Show the statline of a given pokemon 
void show_statline(int index){
	printf("Name : %s, ", import_matrix[0][index]);
	printf("Base HP : %s, ", import_matrix[3][index]);
	printf("Growth Rate: %s, ", import_matrix[4][index]);
	printf("Move 1 Name: %s, ", import_matrix[5][index]);
	printf("Move 1 Power: %s, ", import_matrix[6][index]);
	printf("Move 1 Accuracy: %s, ", import_matrix[7][index]);
	printf("Move 2 Name: %s, ", import_matrix[8][index]);
	printf("Move 2 Power: %s, ", import_matrix[9][index]);
	printf("Move 2 Accuracy: %s, ", import_matrix[10][index]);
	printf("Move 3 Name: %s, ", import_matrix[11][index]);
	printf("Move 3 Power: %s, ", import_matrix[12][index]);
	printf("Move 3 Accuracy: %s, ", import_matrix[13][index]);
	printf("Move 4 Name: %s, ", import_matrix[14][index]);
	printf("Move 4 Power: %s, ", import_matrix[15][index]);
	printf("Move 4 Accuracy: %s\n\n", import_matrix[16][index]);
}

/*
Is the pokemon over level 100. IF so, you win!
Need to read this from a file before the CTF starts.... // TODO - MAX
*/
int did_win(){
	if(myself.level > 100){
		FILE *fp; 
		int c; 
		fp = fopen("flag.txt","r");
		if(fp){
			while((c = getc(fp)) != EOF){
				putchar(c);
			}
			fclose(fp);
		}
		return true; 
	}
	return false; 
}

/*
Note: These are inverted from the original game series.
For example, the original slow_medium is not the fast_medium
*/
unsigned fast(int level){
	return (5/4) * pow(level,3);
}

unsigned int fast_medium(int level){
	return (6/5)* pow(level,3) - (15 * pow(level,2)) + (100 * level) - 140;
}

unsigned int slow_medium(int level){
	return pow(level, 3);
}

unsigned int slow(int level){
	return (4/5) * pow(level, 3);
}

// If the pokemon is not at the right level for its exp, then level it up! 
void does_level_up(){
	
	printf("EXP is at: %d\n", myself.experience);
	int level = (int)csqrt((myself.experience/40));
	if(level != myself.level){
		printf("Pokemon %s leveled up to %u!\n",myself.name, (unsigned int)level);
		myself.level = level; 
	}
	return;
}

int init(){
	intro();
	choose_pokemon();
	return 1; 
}

int main(){

	init(); // Import pokemon and choose pokemon 
	int win = battle(); // The single battle
	if(win == 1){
		after_battle(); // exp increase and level up. 
		did_win();		// Check to see if the challenge has been solved. 
	}

	return 0;

}

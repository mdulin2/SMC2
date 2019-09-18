# High ScORe

Use after free bug:
- The player is freed, but still has a pointer going to it. 
- This space can be picked up by the p_array heap allocation (within the add_score function), which will then set the memory within this area. 
    - In the tests ran, it tends to be 103 for the final score or the last item (which makes sense)
- Flow:
    - create player (create AAAA)
    - Add one score (new)
    - reset the player (reset)
    - Add 20 scores (new) * 20 in order to guarentee the setting of the value,
    - Check the score (won)
    - Should have corrupted the memory to something like 103 to win.
- Run `cat answer | ./a.out` to beat the challenge
- Should be tested on other architectures though!


## Drawn out: 

structs drawn out in 4 byte increments. c is character, i is integer. 
- char: 1 byte 
- int: 4 bytes  
player struct: 
    cccc <--player name
    cccc
    cccc
    i    <--player score 

parray allocation: 
    i
    i 
    i 
    i   <-- Ends up being player score; each is last 4 bytes.

Because the allocations are each 16 bytes long, when the player struct is freed, the parray allocation will take this spot. Because of this, the player->score has been corrupted.
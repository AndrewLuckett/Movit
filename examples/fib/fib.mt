Set 6 128 //Max Value
Rst 4 6 //if greater than 128

Set 7 23 //Jump out address
Rst 5 7 //Set jump out address
Set 5 12 //Set loop address

Set 8 0 //Zero
Rst 3 8 //Reset adder with zero
Set 9 0 //Last
Set 10 1 //Last last?

Mov 1 3 //Print current sum
Set 2 10 //Print newline

Mov 9 10 //Push last forward
Mov 10 3 //Move current into last
Mov 3 9 //Add to current

Mov 4 3 //Is current greater than 128
Mov 5 4 //Get jump address
Mov 0 5 //Jump to address

Done

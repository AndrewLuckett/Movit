//Sierpinski triangle

Set 4 32 //Image size
Rst 3 4 //Reset Y subtractor to image size
Set 8 0 //Zero

//Mainloop
Set 14 16
Rst 5 14 //SubMainloop if Y not 0
Set 5 113 //Done if Y is 0
Mov 5 3 //Check Y
Mov 0 5 //Make jump



//SubMainloop
Set 3 1 //Y -= 1
Rst 6 8 //I = 0

//Loop 1
Rst 7 6
Mov 7 3 // Y > I

Set 14 51
Rst 5 14 //Subloop 1 if Y > I
Set 5 29 //Else continue
Mov 5 7 //Check Y > I
Mov 0 5 //Make jump

Rst 2 8 //X = 0

//Loop 2
Rst 9 2
Mov 9 3 //X + Y

Rst 7 9
Mov 7 4 //Image size > X + Y

Set 14 58
Rst 5 14 //Subloop 2 if Image size > X + Y
Set 5 44 //Else continue
Mov 5 7 //Check Image size > X + Y
Mov 0 5 //Make jump

Set 1 10 //Print newline

Set 0 7 //Jump back to Mainloop



//Subloop 1
Set 1 32 //Print Space
Set 6 1 //I += 1
Set 0 20 //Jump to Loop 1



//Subloop 2
Rst 11 2 //A = X
Rst 12 3 //B = Y

//Loop 3
Set 0 71 //Subloop 3
//End Loop 3

Set 2 1 //X += 1
Set 0 32 //Jump to Loop 2



//Subloop 3
Set 14 77
Rst 5 14 //Continue if A not 0
Set 5 101 //Else jump to Cond 1
Mov 5 11 //Check A
Mov 0 5 //Make jump

Rst 10 11
Set 10 2 //A % 2
Rst 13 10 //T = A % 2

Rst 10 12
Set 10 2 //B % 2
Mov 13 10 //T += B % 2

Set 13 -2 //T += -2

Set 14 93
Rst 5 14 //Continue if T not 0
Set 5 108 //Else jump to Cond 2
Mov 5 13 //Check T
Mov 0 5 //Make jump

Set 11 2 //A //= 2
Set 12 2 //B //= 2

Set 0 68 //Force Loop



//Cond 1
Set 1 42
Set 1 32
Set 0 64 //Jump to end loop 3



//Cond 2
Set 1 32
Set 1 32
Set 0 64 //Jump to end loop 3


Done
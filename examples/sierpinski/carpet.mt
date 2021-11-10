//Sierpinski carpet

Set 4 27 //Image size
Rst 3 4 //Reset Y subtractor to image size
Set 8 0 //Zero

//Mainloop
Set 14 16
Rst 5 14 //SubMainloop if Y not 0
Set 5 97 //Done if Y is 0
Mov 5 3 //Check Y
Mov 0 5 //Make jump



//SubMainloop
Set 3 1 //Y -= 1
Rst 2 8 // X = 0

//Loop 1
Rst 7 4
Mov 7 2 // X > image size

Set 14 29
Rst 5 14 //Continue if X > image size
Set 5 32 //Else Subloop 1
Mov 5 7 //Check X > image size
Mov 0 5 //Make jump

Set 1 10
Set 0 7 //Jump to Mainloop


//Subloop 1
Rst 11 2 //A = X
Rst 12 3 //B = Y

//Loop 2
Set 0 47 //Jump to Subloop 2
//Endloop 2

Set 2 1 //X += 1
Set 0 20 //Jump to loop 1



//Subloop 2
Set 14 53
Rst 5 14 //Continue if A not 0
Set 5 74 //Else jump to Cond 1
Mov 5 11 //Check A
Mov 0 5 //Make jump

Rst 10 11
Set 10 3 //A % 3
Rst 13 10 //T = A % 3
Set 13 -1 //T += -1

Set 14 64
Rst 5 14 //Continue if T not 0
Set 5 80 //Else jump to Cond 2
Mov 5 13 //Check T
Mov 0 5 //Make jump

//Cond 2 return

Set 11 3 //A //= 3
Set 12 3 //B //= 3

Set 0 47 //Force loop



//Cond 1
Set 1 42
Set 0 40 //Jump to end loop 2



//Cond 2
Rst 10 12
Set 10 3 //B % 3
Rst 13 10 //T = B % 3
Set 13 -1 //T += -1

Set 14 65
Rst 5 14 //Jump to Cond 2 return if T not 0
Set 5 92 //Else jump to Cond 3
Mov 5 13 //Check T
Mov 0 5 //Make jump



//Cond 3
Set 1 32
Set 0 40 //Jump to end loop 2

Done
Set lder 31 //Load AsciiPrinter
Mov aprint lder
Set lder 30 //Load ValuePrinter
Mov vprint lder


Set lder 11 //Load Subtractor
Mov sub lder
Set lder 21 //Load Negative comparitor
Mov neg lder
Set lder 12 //Load multiplyer
Mov mult lder
Set lder 10 //Load Adder
Mov add lder

Set a 0
Set b 1
Set max 1000

Mov vprint a //Print current sum
Set aprint 10 //Print newline

Rst add
Mov add a
Mov add b //add = a + b
Mov a b //a = b
Mov b add //b = add

Rst sub
Mov sub a
Mov sub max //sub = a - max

Mov neg sub //is sub negative

Rst mult
Set mult -26
Mov mult neg //mult = neg * -26

Rst add
Set add 45
Mov add mult //add = 45 + mult

Mov pc add //Jump to add


Done
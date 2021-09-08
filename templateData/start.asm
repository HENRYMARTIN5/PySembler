[BITS 16]
[ORG 7c0h]

MOV AH, 0
MOV AL, 12H
INT 10H
mov si, reservedloaddata
call blue
call printString
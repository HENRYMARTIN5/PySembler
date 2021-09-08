printString:
printChar:
mov ah, 09h
mov bh, 0  
mov cx, 1
lodsb
cmp al, 0x00
je done     
int 10h   
mov bh, 0
mov ah, 03h
int 10h
mov ah, 02h
mov bh, 0
inc dl
int 10h
jmp printChar
done: 
mov ah, 02h
mov bh, 0
mov dl, 0
inc dh  
int 10h
ret        

blue:
mov bl, 0011b
ret 

red:
mov bl, 0x000C
ret

green:
mov bl, 0x000A
ret

grey:
mov bl, 0x0007
ret 
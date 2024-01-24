dosseg
.model small
.stack 100h
.data
.code

main proc

mov dl, 65
mov ah, 2
mov cl, 26

start:
	int 21h
	inc dl
loop start

mov ah, 4ch
int 21h

main endp
end main
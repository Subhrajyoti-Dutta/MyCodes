dosseg
.model small
.stack 100h
.data
.code

main proc

mov ah, 2
mov dl, 'H'
int 21h

mov dl, 'e'
int 21h

mov dl, 'l'
int 21h

mov dl, 'l'
int 21h

mov dl, 'o'
int 21h

mov ah, 4ch
int 21h

main endp
end main
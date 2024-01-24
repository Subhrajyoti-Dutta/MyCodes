dosseg
.model small
.stack 100h
.data
.code

main proc

mov ah, 1
int 21h
mov bl, al

mov ah, 2
mov dl, 13
int 21h
mov dl, 10
int 21h

mov ah, 1
int 21h
mov bh, al


mov dl, bl
and dl, bh
int 21h


mov dl, 13
int 21h
mov dl, 10
int 21h
mov dl, bl
or  dl, bh
int 21h


mov dl, 13
int 21h
mov dl, 10
int 21h
mov dl, bl
xor dl, bh
int 21h


mov dl, 13
int 21h
mov dl, 10
int 21h
mov dl, bl
not dl
int 21h

mov ah, 4ch
int 21h

main endp
end main
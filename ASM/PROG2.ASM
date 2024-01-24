dosseg
.model small
.stack 100h
.data
.code

main proc

mov ah, 1
int 21h
mov bl, al

int 21h
add bl, al

sub bl, 96

sub bl, 10
mov dl, 49

mov ah, 2
int 21h

add bl, 48
mov dl, bl

mov ah, 2
int 21h

mov ah, 4ch
int 21h

main endp
end main
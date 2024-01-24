dosseg
.model small
.stack 100h
.data
.code

main proc

mov ah, 2
mov dl, 65
int 21h
mov dl, 61
int 21h

mov ah, 1
int 21h
mov bl, al

mov ah, 2
mov dl, 13
int 21h
mov dl, 10
int 21h
mov dl, 66
int 21h
mov dl, 61
int 21h

mov ah, 1
int 21h
mov bh, al


mov ah, 2
mov dl, 13
int 21h
mov dl, 10
int 21h
mov dl, 65
int 21h
mov dl, 78
int 21h
mov dl, 68
int 21h
mov dl, 61
int 21h
mov dl, bl
and dl, bh
int 21h


mov dl, 13
int 21h
mov dl, 10
int 21h
mov dl, 79
int 21h
mov dl, 82
int 21h
mov dl, 61
int 21h
mov dl, bl
or  dl, bh
int 21h

mov dl, 13
int 21h
mov dl, 10
int 21h
mov dl, 88
int 21h
mov dl, 79
int 21h
mov dl, 82
int 21h
mov dl, 61
int 21h
mov dl, bl
xor dl, bh
int 21h


mov dl, 13
int 21h
mov dl, 10
int 21h
mov dl, 78
int 21h
mov dl, 79
int 21h
mov dl, 84
int 21h
mov dl, 32
int 21h
mov dl, 79
int 21h
mov dl, 70
int 21h
mov dl, 32
int 21h
mov dl, 65
int 21h
mov dl, 61
int 21h
mov dl, bl
not dl
int 21h

mov ah, 4ch
int 21h

main endp
end main
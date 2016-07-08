; libc
section	.text
global	main

extern	getchar_unlocked
extern	putchar_unlocked
extern	exit

readint:
	call	getchar_unlocked
	cmp	eax,	0xA
	je	readint
	cmp	eax,	0x20
	je	readint
	xor	esi,	esi
	xor	ebx,	ebx
	cmp	eax,	0x2D
	jne	_readint_positive
	inc	esi
_readint_loop:
	push	ebx
	call	getchar_unlocked
	pop	ebx
_readint_positive:
	cmp	eax,	48
	jl	_done_readint
	cmp	eax,	57
	jg	_done_readint
	sub	eax,	48
	imul	ebx,	10
	add	ebx,	eax
	jmp	_readint_loop
_done_readint:
	mov	eax,	ebx
	test	esi,	esi
	jz	_ret_readint
	neg	eax
_ret_readint:
	ret

writeint:
	mov	edi,	10
	xor	esi,	esi
	cmp	eax,	esi
	jge	_write_positive
	push	eax
	push	0x2D
	call	putchar_unlocked
	add	esp,	4
	pop	eax
	neg	eax
_write_positive:
	xor	edx,	edx
	div	edi
	add	edx,	48
	push	edx
	inc	esi
	test	eax,	eax
	jnz	_write_positive

_write_loop:
	call	putchar_unlocked
	add	esp,	4
	dec	esi
	test	esi,	esi
	jnz	_write_loop

	push	0xA
	call	putchar_unlocked
	add	esp,	4
	ret

main:
	call	readint
	mov	ecx,	eax
_aplusb_loop:
	push	ecx
	call	readint
	push	eax
	call	readint
	pop	ebx
	add	eax,	ebx
	call	writeint
	pop	ecx
	dec	ecx
	test	ecx,	ecx
	jnz	_aplusb_loop

	push	0
	call	exit

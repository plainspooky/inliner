'' kaleidoscope (MSX 16 colors)

' define WIDTH 255
' define HEIGHT 191
' define MAXCOLORS 16

COLOR 15,0,0
SCREEN 2
I%=RND(-TIME)

main_loop:
    FOR I%=0 TO @{WIDTH} STEP 2
        ' pick up a color
        K%=@{MAXCOLORS}*RND(1)
        ' left side
        LINE (0,0)-STEP(i%,@{HEIGHT}),K%
        LINE (0,@{HEIGHT})-STEP(I%,-@{HEIGHT}),K%
        ' right side
        LINE (@{WIDTH},0)-STEP(-I%,@{HEIGHT}),K%
        LINE (@{WIDTH},@{HEIGHT})-STEP(-I%,-@{HEIGHT}),K%

    NEXT I%
    GOTO @{main_loop}

' take a look in the MSX2 version too!

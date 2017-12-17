'' KALEIDOSCOPE, APPLE II VERSION
' define WIDTH 279
' define HEIGHT 191
' define MAXCOLORS 8
HGR2

main_loop:
    FOR I=0 TO {{WIDTH}} STEP 2
        ' pick up a color
        HCOLOR=INT({{MAXCOLORS}}*RND(1))
        
        ' left side
        HPLOT 0,0
            \ TO I,{{HEIGHT}}
        HPLOT 0,{{HEIGHT}} TO
            \ I,0

        ' right side
        HPLOT {{WIDTH}},0
            \ TO {{WIDTH}}-I,{{HEIGHT}}
        HPLOT {{WIDTH}},{{HEIGHT}}
            \ TO {{WIDTH}}-I,0

    NEXT I
GOTO {{main_loop}}

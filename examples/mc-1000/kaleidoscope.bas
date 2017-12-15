'' KALEIDOSCOPE (MC-1000 VERSION)
' define WIDTH 127
' define HEIGHT 63
' define MAXCOLORS 4

GR

main_loop:
    FOR I=0 TO @{WIDTH} STEP 2

        ' pick up a color
        COLOR=INT(@{MAXCOLORS}*RND(1))

        ' left side
        PLOT 0,0 TO I,@{HEIGHT}
        PLOT 0,@{HEIGHT} TO I,0

        ' right side
        PLOT @{WIDTH},0 TO @{WIDTH}-I,@{HEIGHT}
        PLOT @{WIDTH},@{HEIGHT} TO @{WIDTH}-I,0

    NEXT I

    GOTO @{main_loop}

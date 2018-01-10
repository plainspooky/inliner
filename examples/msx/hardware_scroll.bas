'' MSX2+ hardware scroll animation

' define PAL 5
' define NTSC 6

' define randint fn ri%

color 15,0,0
screen 5
i%=rnd(-time)
' only 192 lines
vdp(10)=vdp(10) and &h7f

def {{randint}}(i%)
    \=i%*rnd(1)

' initialize everything
gosub {{redefine_colors}}
gosub {{make_tile}}
gosub {{draw_background}}
gosub {{draw_tiles}}

main_loop:
    for i%=0 to 255
        ' reset system timer
        time=0
        ' shift screen i% pixel to the left
        set scroll i%,0,1

        ' it times is less than 1/10s...
        if time<{{NTSC}} then
           '... waits
            \ {{@}}
        \ else
           '... go to the next item
            \ next i%
            goto {{main_loop}}

redefine_colors:
    for i%=0 to 7
        ' (0-7) colors of the rock (a kind of orange/brow)
        color=(i%,i%,i%\2,i%\4)
        ' (8-15) colors of the sky (black -> blue)
        color=(8+i%,0,0,i%)
    next i%
    return


make_tile:
    ' draw the rock pattern
    for j%=0 to 15
        for i%=0 to 15
            ' pick a color and plot on the screen
            pset(i%,j%),{{randint}}(8)
    next i%,j%
    ' copy to another place of VRAM
    copy(0,0)-step(15,15) to (0,192)
    return


draw_background:
    for i%=0 to 7
        ' top
        line(0,12*i%)-step(255,11),8+i%,bf
        ' bottom (inverse)
        line(0,180-12*i%)-step(255,11),8+i%,bf
    next i%
    return


draw_tiles:
    for j%=0 to 191 step 16
        for i%=0 to 255 step 16
            ' pick a number and draw a rock
            if {{randint}}(16)>11 then
                \ copy (0,192)-step(15,15) to (i%,j%)

    next i%,j%
    return

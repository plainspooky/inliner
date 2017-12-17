'
' MSX2 OR-Colored Sprites
'
color 15,0,0
screen 4,3,0

gosub {{set_sprite}}
gosub {{set_colors}}

put sprite 0,(112,79),,1
put sprite 1,(112,79),,0

goto {{@}}

set_colors:
    color=( 6,6,2,1)
    color=( 9,7,6,6)
    color=(15,0,1,5)
    return

set_sprite:
    restore {{ship_pattern}}
    for j%=0 to 1

        k$=""
        for i%=0 to 31
            read k%
            k$=k$+chr$(k%)
        next i%
        sprite$(j%)=k$

        k$=""
        for i%=0 to 15
            read k%
            k$=k$+chr$(k%)
        next i%
        color sprite$(j%)=k$

    next j%
    return

ship_pattern:
    ' white
    data &h00,&h00,&h03,&h03,&h03,&h03,&h07,&h03,
        \&h4B,&h57,&h4C,&h7E,&h73,&h61,&h00,&h00,
        \&h00,&h00,&h80,&h80,&h80,&h80,&hC0,&h80,
        \&hA4,&hD4,&h64,&hFC,&h9C,&h0C,&h00,&h0

    data &h06,&h06,&h06,&h06,&h06,&h06,&h06,&h06,
        \&h06,&h06,&h06,&h06,&h06,&h06,&h06,&h06

    ' red/blue
    data &h01,&h01,&h02,&h02,&h02,&h00,&h45,&h45,
        \&h0D,&h18,&h33,&h21,&h0C,&h26,&h43,&h01,
        \&h00,&h00,&h80,&h80,&h80,&h00,&h44,&h44,
        \&h60,&h30,&h98,&h08,&h60,&hC8,&h84,&h00

    data &h49,&h49,&h49,&h49,&h49,&h49,&h49,&h49,
        \&h49,&h49,&h49,&h49,&h49,&h49,&h49,&h49

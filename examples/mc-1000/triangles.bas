'' TRIANGLES.BAS

' High resolution graphics
HGR

FOR A=1 TO 10
    B=B+10
    PLOT 30+B,60
        \ TO 30+B,180
        \ TO 90+B,128
        \ TO 30+B,60
NEXT A

FOR I=1 TO 500:NEXT

'
' IF ... THEN ... ELSE example
'
' define LEGAL 18
' define YES "Y"
' define NOT "N"

main_loop:
    INPUT "HOW OLD ARE YOU ?";A

    IF A>={{LEGAL}} THEN
        \ PRINT "WOULD YOU LIKE A BEER, BUD?"
    \ ELSE
        \ PRINT "HOW ABOUT A SODA, KID?"

    ask_loop:
        PRINT
        INPUT "AGAIN (Y/N) ?";K$

        IF K$={{NOT}} THEN
            \ END
        \ ELSE
            IF K$<>{{YES}} THEN
                \ {{ask_loop}}
            \ ELSE
                \ {{main_loop}}

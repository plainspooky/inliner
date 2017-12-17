'
' IF ... THEN example
'
' define LEGAL 18
' define YES "Y"
' define NOT "N"

main_loop:
    INPUT "HOW OLD ARE YOU ?";A

    IF A>={{LEGAL}} THEN
        \ PRINT "WOULD YOU LIKE A BEER, BUD?"
        GOTO {{ask_loop}}

    PRINT "HOW ABOUT A SODA, KID?"

    ask_loop:
        PRINT
        INPUT "AGAIN (Y/N) ?";K$

        IF K$={{NOT}} THEN
            \ END

        IF K$<>{{YES}} GOTO
            \ {{ask_loop}}

        GOTO {{main_loop}}

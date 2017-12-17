'' EXAMPLE.BAS
' define YES k$="Y" or k$="y"
' define NO k$="N" or k$="n"

main_loop:
    ' get user's name
    input "What is your name?";k$

    ' print name on screen
    print "Hello ";
          \ k$;",
          \ how do you doing?"

    ask_loop:
        input "Again (Y/N)?";k$
        if {{NO}} then
            \ end

        if {{YES}} then
            \ goto {{main_loop}}

        goto {{ask_loop}}

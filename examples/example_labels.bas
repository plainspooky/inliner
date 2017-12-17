'' EXAMPLE.BAS

main_loop:
    ' get user's name
    input "What is your name?";k$

    ' print name on screen
    print "Hello ";
          \ k$;",
          \ how do you doing?"

    ask_loop:
        input "Again (Y/N)?";k$
        if k$="N" then
            \ end

        if k$="Y" then
            \ goto {{main_loop}}

        goto {{ask_loop}}

let i%=0

main_loop:

    if i%<20 then gosub {{wrong_label}}
    
    i%=i%+1
    goto {{main_loop}}

    end

right_label:
    print "*";
    return

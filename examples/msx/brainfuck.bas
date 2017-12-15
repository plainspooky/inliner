'
' BRAINFUCK INTERPRETER FOR MSX-BASIC
' (C)2005-2017 - Giovanni Nunes <giovanni.nunes@gmail.com>
'
' I wrote this program years ago as a one-liner:
'
' 1 DIMA(255):FORI=0TO40*CSRLIN-41:J=VPEEK(I):B=A(K):A(K)=B+(J=45)
' -(J=43):K=K+(J=60)-(J=62):IFJ=46THENPRINTCHR$(A(K));:NEXTELSEIFJ
' =44THENA(K)=ASC(INPUT$(1)):NEXTELSEIFJ=91THENL=B:P=I:NEXTELSEIFJ
' =93THENL=L-1:I=-(L>0)*P-(L=0)*I:NEXTELSENEXT
'
' Using Inliner is now possible view it in a more readable format.
'
dima(255)
fori=0to40*csrlin-41
    j=vpeek(i)
    b=a(k)
    a(k)=b+(j=45)-(j=43)
    k=k+(j=60)-(j=62)
    ifj=46then
        \printchr$(a(k));
        next
    \else
        \ifj=44then
            \a(k)=asc(input$(1))
            next
        \else
            \ifj=91then
                \l=b
                p=i
                next
            \else
                \ifj=93then
                    \l=l-1
                    i=-(l>0)*p-(l=0)*i
                    next
                \else
            \next

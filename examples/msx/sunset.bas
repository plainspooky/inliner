'' SUNSET.BAS

main:
	color 15,0,0
	key off
	screen 2
	' stores colors
	dim c%(2)

	' draw shades on screen
	gosub {{shades}}
	' redefines tiles
	gosub {{pattern}}

	goto {{@}}

shades:
	for i%=0 to 7
		for j%=0 to 31
			for k%=0 to 767 step 256
				vpoke 6144+k%+i%*32+j%,i%
			next k%
		next j%
	next i%
	return

pattern:
	' read colors
	restore {{color_data}}
	for i%=0 to 2
		read k$
		c%(i%)=val("&H"+k$)
	next i%

	' read patterns
	restore {{pattern_data}}
	for j%=0 to 63
        ' read pattern as string
		read k$
        ' and convert to integer
		k%=val("&H"+k$)

		' do it in each part of screen
		for i%=0 to 6143 step 2048
			vpoke j%+i%,k%
			vpoke 8192+j%+i%,c%(i%\2048)
		next i%
	next j%
	return

	color_data:
		data
			' magenta over blue
		   \ d5,
			' light red over magenta
			\9d,
			' yellow over light red
			\a9

	pattern_data:
		data 00,00,00,00,00,00,00,00,00,22,00,88,00,22,00,88,
		    \00,aa,00,aa,00,aa,00,aa,11,aa,44,aa,11,aa,44,aa

		data 55,aa,55,aa,55,aa,55,aa,55,bb,55,ee,55,bb,55,ee,
		    \55,ff,55,ff,55,ff,55,ff,77,ff,dd,ff,77,ff,dd,ff

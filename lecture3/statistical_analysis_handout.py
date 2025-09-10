

import random


alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "ejqsyobzvcmltpidhrxvgaufkn"
text = """u’s cwxv lumy vi upvyrcyqv oir e titypv. azev kiw’ry ryoyrupb vi ex lupwf, ux up oeqv, bpw/lupwf, ir ex u’gy ryqypvlk vemyp vi qellupb uv, bpw dlwx lupwf. lupwf ux piv ep idyrevupb xkxvyt wpvi uvxylo, jwv revzyr epivzyr oryy qitdipypv io e owllk owpqvuipupb bpw xkxvyt tesy wxyowl jk vzy bpw qirylujx, xzyll wvuluvuyx eps guvel xkxvyt qitdipypvx qitdruxupb e owll ix ex syoupys jk dixuf.

tepk qitdwvyr wxyrx rwp e tisuouys gyrxuip io vzy bpw xkxvyt ygyrk sek, auvziwv ryeluhupb uv. vzriwbz e dyqwluer vwrp io ygypvx, vzy gyrxuip io bpw azuqz ux ausylk wxys visek ux iovyp qellys “lupwf”, eps tepk io uvx wxyrx ery piv eaery vzev uv ux jexuqellk vzy bpw xkxvyt, sygylidys jk vzy bpw dricyqv.

vzyry ryellk ux e lupwf, eps vzyxy dyidly ery wxupb uv, jwv uv ux cwxv e derv io vzy xkxvyt vzyk wxy. lupwf ux vzy myrpyl: vzy dribret up vzy xkxvyt vzev elliqevyx vzy teqzupy’x ryxiwrqyx vi vzy ivzyr dribretx vzev kiw rwp. vzy myrpyl ux ep yxxypvuel derv io ep idyrevupb xkxvyt, jwv wxylyxx jk uvxylo; uv qep iplk owpqvuip up vzy qipvyfv io e qitdlyvy idyrevupb xkxvyt. lupwf ux pirtellk wxys up qitjupevuip auvz vzy bpw idyrevupb xkxvyt: vzy azily xkxvyt ux jexuqellk bpw auvz lupwf essys, ir bpw/lupwf. ell vzy xi-qellys “lupwf” suxvrujwvuipx ery ryellk suxvrujwvuipx io bpw/lupwf
"""

result = ""
for letter in text:
    
    if letter.lower() in key:
        result += alphabet[key.find(letter.lower())]
    else:
        result += letter

print(result)
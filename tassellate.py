
import math
import random

# assegno la dimensione del lato delle piastrelle
l = 15.1

# assegno il numero di piastrelle lungo x e y

np = 100


# non cambiare nulla tra gli asterischi
# ****************************************************************************** 
with open('output.svg','w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
    f.write('<svg\n')
    f.write('   xmlns:dc="http://purl.org/dc/elements/1.1/"\n')
    f.write('   xmlns:cc="http://creativecommons.org/ns#"\n')
    f.write('   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n')
    f.write('   xmlns:svg="http://www.w3.org/2000/svg"\n')
    f.write('   xmlns="http://www.w3.org/2000/svg"\n')
    f.write('   id="svg8"\n')
    f.write('   version="1.1"\n')
    f.write('   viewBox="0 0 1000 1000"\n')
    f.write('   height="1000mm"\n')
    f.write('   width="1000mm">\n')
    f.write('  <defs id="defs2" />\n')
    f.write('  <metadata id="metadata5">\n')
    f.write('  <rdf:RDF>\n')
    f.write('  <cc:Work rdf:about="">\n')
    f.write('  <dc:format>image/svg+xml</dc:format>\n')
    f.write('  <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" />\n')
    f.write('  <dc:title></dc:title>\n')
    f.write('  </cc:Work>\n')
    f.write('  </rdf:RDF>\n')
    f.write('  </metadata>\n')
    f.write('  <g id="layer1">\n')
    
    #for i in range(10):
    #    for j in range(10):
    
    for i in range(np):
        for j in range(np):
            dx = l * math.cos(math.radians(30.0))
            dy = l * math.sin(math.radians(30.0))
            
            vx = i*2*dx+dx*(j%2)
            vy = 1.5*l*j
            
# ******************************************************************************


            # metto in una lista i codici dei colori delle piastrelle
            # i colori sono espressi in esadecimale che corrisponde ai tuoi colori
            # i colori sono in ordine 1 2 3 4 
            colors = ('#ccbfb6','#ab9887', '#7f6459', '#8c796b')
############
            # assegno le probabilità ai vari tipi di piastrella ( p compreso tra 0 e 1 e p1+p2+p3+p4 = 1) 
            p1 = 0.5 # 0.5 = 50%
            p2 = 0.2 # 0.2 = 20%
            p3 = 0.2
            p4 = 0.1
            
            # non cambiare nulla tra gli asterischi
            # **************************************** 
            # scelgo il colore in modo random
            n = random.random()
            
            if n < p1:
                col = colors[0]
            elif n < p1+p2:
                col = colors[1]
            elif n < p1+p2+p3:
                col = colors[2]
            else:
                col = colors[3]
            # **************************************** 
                
############
            # scegli il colore della fuga:
            # devi commentare il colore che NON vuoi
            # grigio perla
            cf = '#cdc5b8'    
            # asia
            #cf = '#b49882'    
############
            # definisci lo spessore della fuga in cm
            sf = 0.2
            
            # non cambiare nulla tra gli asterischi
            # **************************************** 
            f.write('  <path\n')
            f.write('    id="path69-'+str(i)+'"\n')
            f.write('    d="m '+str(vx)+','+str(vy)+' '+str(dx)+','+str(dy)+' '+str(0)+','+str(l)+' '+str(-dx)+','+str(dy)+' '+str(-dx)+','+str(-dy)+' '+str(0)+','+str(-l)+' z"\n')
            # ****************************************
            
############
            # decommentare la prossima riga per avere tutte le piastrelle con la stessa probabilita
            #f.write('    style="fill:'+str(random.choice(colors))+';fill-opacity:1;stroke:#ffffff;stroke-width:0.2;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"\n')
            # commentare la prossima riga per avere tutte le piastrelle con la stessa probabilita
            f.write('    style="fill:'+str(col)+';fill-opacity:1;stroke:'+str(cf)+';stroke-width:'+str(sf)+';stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"\n')
            
            
            # ****************************************
            f.write('    />\n')
    f.write('  </g>\n')
    f.write('</svg>\n')
    # ****************************************

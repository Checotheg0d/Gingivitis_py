def vof(r):
    if r == "si":
        return True
    elif r == "no":
        return False
def val(r):
    r = r.lower()
    while(r != "no" and r != "si"):
        r = r.lower()
    return r


p = 0

print("Gingivitis")

r = input("¿Presentas alguna molestia?\n")
if vof(val(r)):
    p+=1

r = input("¿El malestar sucede en la cabeza?\n")
if vof(val(r)):
    p+=1

r = input("¿El malestar se encuentra en la cavidad bucal?\n")
if vof(val(r)):
    p+=1

r = input("¿Las molestias son constantes u ocasionales?\n")
if vof(val(r)):
    p+=1

r = input("¿El malestar es en las piezas dentales?\n")
if vof(val(r)):
    p+=2

r = input("¿El malestar es en el tejido de las encías?\n")
if vof(val(r)):
    p+=3

r = input("¿Al estar en contacto le genera más molestia?\n")
if vof(val(r)):
    p+=2

r = input("¿El tejido de sus encías presenta irritación?\n")
if vof(val(r)):
    p+=3

r = input("¿Sus encías presentan un color rojo obscuro? \n")
if vof(val(r)):
    p+=3

r = input("¿Ha presentado sangrado en sus encías al momento del cepillado?\n")
if vof(val(r)):
    p+=3

r = input("¿Presenta mal olor bucal?\n")
if vof(val(r)):
    p+=2

r = input("¿Presenta inflamación en las encías?\n")
if vof(val(r)):
    p+=3

r = input("¿Presenta movilidad en alguna pieza dental?\n")
if vof(val(r)):
    p+=3

r = input("¿Ha acudido al dentista recientemente? (en los últimos 6 meses)\n")
if vof(val(r)):
    p+=3

r = input("¿Realiza el cepillado dental de manera regular? (1 a 3 veces al día)\n")
if vof(val(r)):
    p+=2

r = input("¿Utiliza hilo dental?\n")
if vof(val(r)):
    p+=2

r = input("¿Utiliza enjuague dental?\n")
if vof(val(r)):
    p+=2


if p<4: print("Usted no tiene gingivitis")
elif p<15: print("Se recomienda acudir al dentista por posible gingivitis")
else: print("Acuda al dentista a recibir tratamiento para gingivitis")



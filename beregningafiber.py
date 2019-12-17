
taller = 1
taller = int(input('tryk 1) 1310nm eller 2) 1550nm'))

tab1310nm= 0.35
tab1550nm=0.2
sikkerhedsmargin=3
reparationer=0.5

while taller == 1:
   km1= float(input('Indtast længde i kilometer'))
   splidsninger=int(input('Indstast antal splidsninger'))
   Konnektor=int(input('Indtast antal konnektorpar'))
   samlettab=splidsninger+Konnektor
   netto_overskud=samlettab-sikkerhedsmargin-reparationer
   samlet_tab1310=Konnektor+splidsninger+tab1310nm*km1
   print("Tab ved 1310nm",samlet_tab1310,"dB")
   ialt=samlet_tab1310-netto_overskud
   print('Netto overskud', ialt, 'dB')
   print('')
   taller = int(input('tryk 1) 1310nm eller 2) 1550nm'))

while taller == 2:
   km1= float(input('Indtast længde i kilometer'))
   splidsninger=int(input('Indstast antal splidsninger'))
   Konnektor=int(input('Indtast antal konnektorpar'))
   samlettab=splidsninger+Konnektor
   netto_overskud=samlettab-sikkerhedsmargin-reparationer
   samlet_1550=Konnektor+splidsninger+tab1310nm*km1
   print("Tab ved 1550nm",samlet_1550,"dB")
   i_alt=samlet_1550-netto_overskud
   print('Netto overskud', i_alt, 'dB')
   print('')
   taller = int(input('tryk 1) 1310nm eller 2) 1550nm'))


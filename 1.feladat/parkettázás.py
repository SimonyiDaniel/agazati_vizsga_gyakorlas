szelesseg = input("Kérem a szoba szélességét: ")
hosszusag = input("Kérem a szoba hosszúsaégét: ")
csomagok = input("Hány csomag parketta van: ")
szoba_terulet = input("Kérem a teruletet: (m^2)")
terulet = float(szelesseg) * float(hosszusag)
print(f"A szoba terulet: {str(terulet)} négyzetméter.")
if float(csomagok) * 2 >= float(terulet):
    print("Van elegendő parketta!")
else:
    print("Szükséges még parkettát vásárolni!")

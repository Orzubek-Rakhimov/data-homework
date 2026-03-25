menu = {"Osh": 25000, "Manti": 20000, "gomma":25000,"Shashlik": 15000, "Somsa": 8000}
narx=max(menu.values())
qimmat_ovqatlar={}
for ovqat in menu:
    if menu[ovqat]== narx:
        qimmat_ovqatlar.update({ovqat:narx})
print(f"eng qimmat ovqatlar:{qimmat_ovqatlar}")
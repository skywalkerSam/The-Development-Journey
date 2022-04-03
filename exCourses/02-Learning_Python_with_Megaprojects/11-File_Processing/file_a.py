
with open("tests/planets.txt", "a+") as afile:
    afile.write("\n Mercury \n Venus \n Earth \n Mars \n Jupiter \n Saturn \n Uranus \n Neptune \n ")
    afile.write("Nineth Planet")

    afile.seek(0)      # It just work like cursor, move cursor at the start...
    adata = afile.read()


# without including "a+", you won't be able to read the file...
print(adata)

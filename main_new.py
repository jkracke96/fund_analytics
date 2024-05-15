import tabula

df = tabula.read_pdf("data/Depotauszug.pdf", pages="all")

print(df)

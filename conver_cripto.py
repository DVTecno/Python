def conversion_criptomoneda(bitcoin, ethereum, litecoin):
    btcEUR = 6500.81
    ethEUR = 493.35
    ltcEUR = 104.50
    totalEUR = (bitcoin*btcEUR)+(ethereum*ethEUR)+(litecoin*ltcEUR)
    return totalEUR
bitcoin = float(input("Ingrese el Nombre de la Primera moneda:->>"))
ethereum = float(input("Ingrese el Nombre de la Segunda moneda:->>"))
litecoin = float(input("Ingrese el Nombre de la Tercera moneda:->>"))
print("El monto total resultante de la suma de los tres valores calculados en Euros:->>EUR",
    conversion_criptomoneda(bitcoin, ethereum, litecoin))
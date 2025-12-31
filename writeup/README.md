# Løsning

Bruk variablen `w` til å lese ut tallverdien av den originale meldingen (med flagg) delt på `N`. I krypteringen brukes `w` slik:

```py
N = 1234...
m = bytes_to_long(b"long message ...")

w = m // N
m = m % N
```

Dette gjør at man kan kryptere mye større meldinger med RSA, og er ikke begrenset til å ha meldinger mindre enn `N`. Bruken av `w` er en informasjonslekkasje, og gjør at man kan lese ut første del av store meldinger (alt som i tallverdien er over `N`).

Ved å gjøre forklaringen til JULENISSEN ganske lang, vil man kunne lese ut første del som inneholder flagg ved å gjøre:

```py
N = 1234...
w = 41235...

partial_m = w * N
print(long_to_bytes(partial_m))
```

[solve.py](./solve.py)

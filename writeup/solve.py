from Crypto.Util.number import long_to_bytes

print("Send som input:")
print("a" * 400)

print()

N = int(input("N = "))
w = int(input("w = "))

print()

print(long_to_bytes(w * N).decode("utf-8", errors="ignore"))

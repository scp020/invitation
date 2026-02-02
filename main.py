# === 填入你算出的 A, B, C, D ===
A = 300
B = 110
C = 750
D = 2

# 若计算无误，应满足：
# (A + B + C + D) % 1000 == 162

cipher_hex = "4a10f1e3306dfa7bc0a089d092df6552329eaf6a56866beee98d09bbf35c7bd38d8e09"
cipher = bytes.fromhex(cipher_hex)


def xs32(x: int) -> int:
    x &= 0xFFFFFFFF
    x ^= (x << 13) & 0xFFFFFFFF
    x ^= (x >> 17) & 0xFFFFFFFF
    x ^= (x << 5) & 0xFFFFFFFF
    return x & 0xFFFFFFFF


seed = (A << 20) | (B << 12) | (C << 2) | D

x = seed
out = bytearray()
for b in cipher:
    x = xs32(x)
    out.append(b ^ (x & 0xFF))

print(out.decode("ascii"))

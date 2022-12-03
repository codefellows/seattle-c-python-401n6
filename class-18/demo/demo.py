# IWT FJXRZ QGDLC UDM YJBETS DKTG IWT APOXAN HATTEXCV SDV
# THE                     E    E  THE            E
# Most used letters: EATONRISH

# 1 - 2 - 3
# shift by 1 -> 234
# shift by 11 -> 234
def encrypt(plain, key):
    shifted_number = ''
    str_plain = str(plain)
    for char in str_plain:
        temp = (int(char) + key) % 10
        shifted_number += str(temp)
    return shifted_number


def decrypt(encrypted, key):
    return encrypt(encrypted, -key)


if __name__ == '__main__':
    print(encrypt(123, 1))  # 234
    print(encrypt(123, 2))  # 345
    print(encrypt(3587, 13))  # 6810
    print(decrypt(234, 1))
    print(decrypt(345, 2))
    print(decrypt(6810, 13))

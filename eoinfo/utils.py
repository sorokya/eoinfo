MAX1 = 253
MAX2 = 64009
MAX3 = 16194277


def decode_number(bytes):
    data = [1, 1, 1, 1]
    for i in range(0, 4):
        if len(bytes) > i:
            data[i] = bytes[i]

        if data[i] == 254:
            data[i] = 1

        if data[i] == 0:
            data[i] = 128

        data[i] -= 1

    return data[3] * MAX3 + data[2] * MAX2 + data[1] * MAX1 + data[0]

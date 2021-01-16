def convert_to_pcm(data, length: int):

    res = bytearray(length*2)
    for ind, sample in enumerate(data):
        res[ind*2:ind*2+2] = int(sample).to_bytes(length=2,
                                                  byteorder='little', signed=True)

    return bytes(res)

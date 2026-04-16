from string import digits, ascii_lowercase

abc = (digits + ascii_lowercase).encode()
n = len(abc)          # 36
word_len = 6
prefix_len = 2
suffix_len = word_len - prefix_len
block_size = n ** suffix_len

def bruteforce_fastest():
    template = bytearray(b'-' * word_len + b'\n')
    
    # Wypełniamy suffix (raz na początku)
    for i in range(prefix_len, word_len):
        repeat = n ** (word_len - 1 - i)
        vals = (abc * repeat)[:block_size * (word_len + 1)]
        template[i::word_len + 1] = vals

    with open("all_6char.txt", "wb", buffering=1024*1024*16) as f:  # duży bufor
        for a in abc:
            template[0] = a
            for b in abc:
                template[1] = b
                f.write(template * block_size)


# bruteforce_fastest()   # ~36^6 = 2.176 mld linii → plik ~15–17 GB

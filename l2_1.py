My_list = [(-1 + 0j), 1, 2.2, True, None, 'string', [3, 4], (5, 6, 6.5), {7: 'seven', 8: 'eight'}, {9, 10}, range(11),
           bytearray(b'thirteen'), zip(*[(14, 15), (16, 17), ('a', 'b')]), TypeError]
for i, val in enumerate(My_list, 1):
    print(f"{i}) {val} - {type(val)}")

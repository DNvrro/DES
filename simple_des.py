from des_gui import DesKey

key0 = DesKey(b'10101100')
message = key0.encrypt(b'Yo what the fuck is up man!?', padding=True)

print(message)
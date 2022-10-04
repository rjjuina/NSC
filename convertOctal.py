import json
import sys

result = []

# calculate decimal number
decimal = int(sys.argv[1], 8)
# create associative array and create xml from it
decimalDic = dict(title=str(decimal), subtitle="Decimal", uid="decimal",
                  valid=True, arg=str(decimal), icon="icons/decimal.png")
result.append(decimalDic)

# calculate binary number
binary = bin(decimal)[2:].zfill(8)
# create associative array and create xml from it
binaryDic = dict(title=str(binary), subtitle="Binary", uid="binary", valid=True,
                 arg=str(binary), icon="icons/binary.png")
result.append(binaryDic)

# calculate hex number
hexadec = hex(decimal)[2:].upper()
# create associative array and create xml from it
hexDic = dict(title=str(hexadec), subtitle="Hexadecimal", uid="hex", valid=True,
              arg=str(hexadec), icon="icons/hex.png")
result.append(hexDic)

response = json.dumps({"items": result})

sys.stdout.write(response)

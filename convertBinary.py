import json
import sys

result = []

# calculate decimal number
decimal = int(sys.argv[1], 2)
# create associative array and create xml from it
decimalDic = dict(title=str(decimal), subtitle="Decimal", uid="decimal",
                  valid=True, arg=str(decimal), icon="icons/decimal.png")
result.append(decimalDic)

# calculate octal number
octal = oct(decimal)[1:]
# create associative array and create xml from it
octalDic = dict(title=str(octal), subtitle="Octal", uid="octal", valid=True,
                arg=str(octal), icon="icons/octal.png")
result.append(octalDic)

# calculate hex number
hexadec = hex(decimal)[2:].upper()
# create associative array and create xml from it
hexDic = dict(title=str(hexadec), subtitle="Hexadecimal", uid="hex", valid=True,
              arg=str(hexadec), icon="icons/hex.png")
result.append(hexDic)

response = json.dumps({"items": result})

sys.stdout.write(response)

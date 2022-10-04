""" Arguments
    sys.argv[0] = filename
    sys.argv[1] = number
    sys.argv[2] = source
    sys.argv[3] = destination
"""

import json
import string
import sys

ALPHA = string.digits + string.ascii_uppercase + string.ascii_lowercase + '+' + '/'
result = []


def base64_encode(num, base, alphabet=ALPHA):
    """Encode a number in Base X
  
    `num`: The number to encode
    `base`: Base of number
    `alphabet`: The alphabet to use for encoding
    """
    if num == 0:
        return alphabet[0]
    arr = []
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def base64_decode(str, base, alphabet=ALPHA):
    """Decode a Base X encoded string into the number
  
    Arguments:
    - `string`: The encoded string
    - `base`: base of number
    - `alphabet`: The alphabet to use for encoding
    """
    str_len = len(str)
    num = 0

    idx = 0
    for char in str:
        power = (str_len - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num


try:
    if len(sys.argv) == 4 and sys.argv[3] != "1":
        # calculate integer first
        if int(sys.argv[2]) <= 36:
            # use built in pythON conversion if possible
            decimal = int(sys.argv[1], int(sys.argv[2]))
        elif 36 < int(sys.argv[2]) <= 64:
            # otherwise, use base64_decode
            decimal = base64_decode(sys.argv[1], int(sys.argv[2]))
        else:
            # create dictionary to create xml from it
            errorDic = dict(title="Ohoh, your number couldn't be converted",
                            subtitle="make sure your base is between 2 and 64",
                            uid="error", valid=False)
            result.append(errorDic)
            sys.stdout.write(json.dumps({"item": result}))
            sys.exit()

        # create dictionary to create xml from it
        decimalDic = dict(title=str(decimal), subtitle="Decimal", uid="decimal",
                          valid=True, arg=str(decimal), icon="icons/decimal.png")
        result.append(decimalDic)

        # calculate new number
        if 2 <= int(sys.argv[3]) <= 64:
            conv = base64_encode(decimal, int(sys.argv[3]))
        else:
            # create dictionary to create xml from it
            errorDic = dict(title="Ohoh, your number couldn't be converted",
                            subtitle="make sure your base is between 2 and 64",
                            uid="error", valid=False)
            result.append(errorDic)
            sys.stdout.write(json.dumps({"item": result}))
            sys.exit()

        # create dictionary to create xml from it
        convertDic = dict(title=conv, subtitle=f"Number to base {str(sys.argv[3])}", uid="conv", valid=True, arg=conv)
        result.append(convertDic)

        if int(sys.argv[2]) >= 36 or int(sys.argv[3]) >= 36:
            # create dictionary to create xml from it
            infoDic = dict(title="Case-Sensitive", subtitle="Be aware, if base is >= 36 letters are case-sensitive",
                           uid="conv", valid=True, arg=conv)
            result.append(infoDic)

        sys.stdout.write(json.dumps({"items": result}))
    else:
        if len(sys.argv) != 4:
            errorDic = dict(title="Make sure to pass 3 numbers",
                            subtitle="convert 'number' 'base of original' 'base to convert to'",
                            uid="error", valid=False, arg="error")
            result.append(errorDic)
            sys.stdout.write(json.dumps({"items": result}))
        elif int(sys.argv[3]) == 1:
            errorDic = dict(title="Base 1 makes no sense", subtitle="", uid="error", valid=False, arg="error")
            result.append(errorDic)
            sys.stdout.write(json.dumps({"items": result}))
except:
    errorDic = dict(title="Error Happened", subtitle="Something wrong, please check", uid="error", valid=False,
                    arg="error")
    result.append(errorDic)
    sys.stdout.write(json.dumps({"items": result}))

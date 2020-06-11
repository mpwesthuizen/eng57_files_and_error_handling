# example of error handling with try and except

def int_convert(var):

    try:
        return int(var)

    except ValueError:
        print("ValueError: The value doesn't contain numbers")


# print(int_convert(13))
#
# print(int_convert("string"))
#
# print(int_convert(13.00))


def int_convert2(var):
    if type(var) == int:
        try:
            return type(var)

        except ValueError:
            return 'ValueError: ' + type(var) + ' is not an \'int\''

print(int_convert2(13))

print(int_convert2("string"))

print(int_convert2(13.00))

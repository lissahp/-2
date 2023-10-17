def hex_string_to_int(hex_string):
    return int(hex_string, 16)

def int_to_hex_string(integer):
    return hex(integer)[2:]

def perform_operation(operation, num1, num2):
    operations = {
        "ADD": num1 + num2,
        "SUB": num1 - num2,
        "MUL": num1 * num2
    }
    if operation in operations:
        return operations[operation]
    else:
        raise ValueError("Unsupported operation")

hex_string1 = "36f028580bb02cc8272a9a020f4200e346e276ae664e45ee80745574e2f5ab80"
operation1 = "ADD"
hex_string2 = "70983d692f648185febe6d6fa607630ae68649f7e6fc45b94680096c06e4fadb"

num1 = hex_string_to_int(hex_string1)
num2 = hex_string_to_int(hex_string2)

result = perform_operation(operation1, num1, num2)
result_hex = int_to_hex_string(result)

print(f"Результат операції {operation1}: {result_hex}")

hex_string3 = "33ced2c76b26cae94e162c4c0d2c0ff7c13094b0185a3c122e732d5ba77efebc"
operation2 = "SUB"
hex_string4 = "22e962951cb6cd2ce279ab0e2095825c141d48ef3ca9dabf253e38760b57fe03"

num3 = hex_string_to_int(hex_string3)
num4 = hex_string_to_int(hex_string4)

result2 = perform_operation(operation2, num3, num4)
result_hex2 = int_to_hex_string(result2)

print(f"Результат операції {operation2}: {result_hex2}")

hex_string5 = "7d7deab2affa38154326e96d350deee1"
operation3 = "MUL"
hex_string6 = "97f92a75b3faf8939e8e98b96476fd22"

num5 = hex_string_to_int(hex_string5)
num6 = hex_string_to_int(hex_string6)

result3 = perform_operation(operation3, num5, num6)
result_hex3 = int_to_hex_string(result3)

print(f"Результат операції {operation3}: {result_hex3}")

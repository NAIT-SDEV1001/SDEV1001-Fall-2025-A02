from dotenv import dotenv_values

config = dotenv_values(".env")

print("Our configuration")
for key, value in config.items():
    print(F"key {key}, value: {value}")
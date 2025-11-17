from dotenv import dotenv_values

config = dotenv_values(".env")
# documentation is here https://pypi.org/project/python-dotenv/

print("Our configuration")
for key, value in config.items():
    print(F"key {key}, value: {value}")

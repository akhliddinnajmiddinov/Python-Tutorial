from tasks import add


result = add.delay(2, 2)
# print(result.ready())

# print(result.get(timeout=10000))
# print("SALOM")


print(result.backend)
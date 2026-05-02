test_cases =["login", "logout", "add to cart", "checkout", "search"]

for test in test_cases:
    print("Running test: " +test)

test_cases.append("payment")
print("Total number of tests: " + str(len(test_cases)))

for i in range(1,4):
    print("Test run number: " + str(i))

attempts = 0
while attempts < 3:
    print("Attempt number: " + str(attempts + 1))
    attempts += 1


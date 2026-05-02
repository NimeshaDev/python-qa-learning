test_user= [
    {"username": "standard_user", "password": "secret_sauce", "expected": "pass"},
    {"username": "locked_out_user", "password": "secret_sauce", "expected": "fail"},
    {"username": "wrong_user", "password": "wrong_pass", "expected": "fail"}
]

def check_login(username, password):
    if username == "standard_user" and password == "secret_sauce":
        print("Login successful")
    else:
        print("Login failed")

def run_all_tests(users):
    passed = 0
    failed = 0
    for user in users:
        result = check_login(user["username"], user["password"])
        if result == user["expected"]:
            print("Test passed")
            passed += 1
        else:
            print("Test failed")
            failed += 1

    print("Total tests passed: " + str(passed))
    print("Total tests failed: " + str(failed))

run_all_tests(test_user)
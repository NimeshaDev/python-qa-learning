def check_login(username,password):
    if username == "standard_user" and password == "secret_sauce":
        return "login successful"
    else:
        return "login failed"

def validate_url(url, expected_url):
    if url == expected_url:
        return "URL check passed"
    else:
        return "URL check failed"

def run_test_suite(tests):
    print("starting running test suite")
    for test in tests:
        print("running test: " + test)
    print("All " +str(len(tests)) + " tests complete")

print( check_login("standard_user", "secret_sauce"))
print( check_login("wrong_user", "wrong_pw"))
print( validate_url("saucedemo.com/inventory", "inventory"))


my_tests= ["login test", "cart test", "checkout test"]
run_test_suite(my_tests)

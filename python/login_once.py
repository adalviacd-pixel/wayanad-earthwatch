import earthaccess

auth = earthaccess.login(strategy="interactive", persist=True)
print("Logged in:", auth.authenticated)
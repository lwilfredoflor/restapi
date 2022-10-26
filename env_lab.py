

ENVIRONMENT_IN_USE = "sandbox"

# Set the 'Environment Variables' based on the lab environment in use
if ENVIRONMENT_IN_USE == "sandbox":
    dnac = {
        "host": "sandboxdnac2.cisco.com",
        "port": 443,
        "username": "devnetuser",
        "password": "Cisco123!"
    }
import yaml
import requests
import json

# 1. Pull random data from the internet
# Using a public API to get a random 'To-Do' item
response = requests.get('https://jsonplaceholder.typicode.com')
data_from_web = response.json()

# 2. Generate the config.yaml file
with open('config.yaml', 'w') as f:
    # yaml.dump converts the Python dict to YAML format
    yaml.dump(data_from_web, f, default_flow_style=False)

print("Successfully generated config.yaml with data from internet.")

# 3. Read it back using the pre-5.1 yaml.load() API
with open('config.yaml', 'r') as f:
    # In PyYAML < 5.1, this call is simple but inherently UNSAFE
    # It defaults to the 'Loader' class which allows code execution
    config = yaml.load(f)

print("\nData loaded from config.yaml:")
print(config)

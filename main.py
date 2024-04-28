import json


def read_data_from_config() -> str:
    """Get website Url from config file"""
    with open('config.json', 'r') as config_file:
        config_file = json.load(config_file)
        website = config_file['website']
    return website


if __name__ == "__main__":
    website_url = read_data_from_config()

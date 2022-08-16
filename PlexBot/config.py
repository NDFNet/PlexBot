import json

with open("config.json") as conf:
    config = json.load(conf)
debug = config["debug"]
discord_token = config["discord"]["token"]
discord_prefix = config["discord"]["prefix"]
plex_token = config["plex"]["token"]
plex_url = config["plex"]["url"]
from plexapi.server import PlexServer
from PlexBot.config import plex_token, plex_url
from PlexBot.logging import log
plex: PlexServer = PlexServer(plex_url, plex_token)
log.info(f"Logged into {plex.friendlyName} as {plex.myPlexUsername}")

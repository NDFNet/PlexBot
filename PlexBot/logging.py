import coloredlogs, logging
log = logging.getLogger(__name__)
coloredlogs.install(level='INFO')
logging.getLogger("nextcord.gateway").setLevel(logging.WARNING)

class PlexBotException(Exception):
    """Exception class from which every exception in this project will derive.
    """
    pass

class UserNotInVC(PlexBotException):
    """User is not in a vc"""
    pass

class UserNotInSameVC(PlexBotException):
    """User is not in the same VC as the bot"""
    pass

class UserOnBlacklist(PlexBotException):
    """User is on the blacklist"""
    pass

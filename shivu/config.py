class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1962399469"
    sudo_users = "1962399469", "7378476666"
    GROUP_ID = -1002168488906
    TOKEN = 
    mongo_url = 
    PHOTO_URL = 
    SUPPORT_CHAT = "blade_x_support"
    UPDATE_CHAT = "blade_x_community"
    BOT_USERNAME = "Devine_wifu_bot"
    CHARA_CHANNEL_ID = "-1002168367599"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7885908019"
    sudo_users = "7885908019", "7640076990", "7756901810" 
    GROUP_ID =-1002640379822
    TOKEN = "7673948265:AAFfj9piGxd0e-0bdV-eePwnjd5hIRUyFXg" 
    mongo_url = "mongodb+srv://noloves:naruto1179@nolove.yojms.mongodb.net/?retryWrites=true&w=majority&appName=nolove" 
    PHOTO_URL = "https://files.catbox.moe/0nb1p7.jpg" 
    SUPPORT_CHAT = "https://t.me/Anime_Circle_Club"
    UPDATE_CHAT = "https://t.me/+D_z2g--T1UJjOWM1"
    BOT_USERNAME = "Madara_Husbando_grabber_Bot"
    CHARA_CHANNEL_ID = "-1002552013602"
    api_id = 28159105
    api_hash = "a0936ddf210a7e091e19947c7dc70c91"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

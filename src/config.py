import os
from dotenv import load_dotenv

# bot token
load_dotenv()
TOKEN = os.getenv("TOKEN")

# embed colors!
SUCCESS = 0x4bf288
WARNING = 0xf2d64b
ERROR = 0xf24b4b

# logging
LOGS_CHANNEL = 1121592213663662171

# custom emojis used in embeds etc
emojis = {
    "num_0": "<:bl_0:1122919509355937832>",
    "num_1": "<:bl_1:1122919560132169821>",
    "num_2": "<:bl_2:1122919598933692508>",
    "num_3": "<:bl_3:1122919637701636196>",
    "num_4": "<:bl_4:1122919690914771066>",
    "num_5": "<:bl_5:1122919715757633730>",
    "num_6": "<:bl_6:1122919783101386842>",
    "num_7": "<:bl_7:1122919825547726858>",
    "num_8": "<:bl_8:1122919865515266098>",
    "num_9": "<:bl_9:1122919905747030137>",
    "announcement": "<:bl_announcement:1122922138869973102>",
    "boost": "<:bl_boost:1122931883748118578>",
    "bot": "<:bl_bot:1122935291519442984>",
    "channel": "<:bl_channel:1122920833208299540>",
    "chat": "<:bl_chat:1122920700383080469>",
    "connection": "<:bl_connection:1122922204364025866>",
    "developer": "<:bl_dev:1122942676199805060>",
    "discover:": "<:bl_discover:1122921064087945286>",
    "dot": "<:bl_dot:1122942775588040704>",
    "gear": "<:bl_gear:1122942917573627947>",
    "gift": "<:bl_gift:1122922329828241480>",
    "github": "<:bl_github:1122922398753247263>",
    "heart": "<:bl_heart:1122921263246082228>",
    "image": "<:bl_image:1122922077129822208>",
    "leftarrow": "<:bl_left:1122921843293159544>",
    "link": "<:bl_link:1122920240335048746>",
    "member": "<:bl_member:1122920124450619434>",
    "moderation": "<:bl_moderation:1122942820878139542>",
    "nitro": "<:bl_nitro:1122946242020905124>",
    "no": "<:bl_no:1122920008415182849>",
    "notification": "<:bl_notification:1122921373149433968>",
    "owner": "<:bl_owner:1122935250813730896>",
    "partner": "<:bl_partner:1122920192037621890>",
    "plus": "<:bl_plus:1122942561833713734>",
    "bulletpoint": "<:bl_point:1122935332745261107>",
    "question": "<:bl_question:1122942615067836536>",
    "rightarrow": "<:bl_right:1122921774640799914>",
    "rocket": "<:bl_rocket:1122935378958102599>",
    "rules": "<:bl_rules:1122920639074930768>",
    "search": "<:bl_search:1122931826772672654>",
    "server": "<:bl_server:1122942730964828271>",
    "shield": "<:bl_shield:1122921132421562501>",
    "news": "<:bl_news:1122920916876275835>",
    "slashcmd": "<:bl_slashcmd:1122921187803144212>",
    "star": "<:bl_star:1122920868264284211>",
    "sticker": "<:bl_sticker:1122921443085275296>",
    "tag": "<:bl_tag:1122943273485475963>",
    "yes": "<:bl_yes:1122919972490981526>",
    "signs": "<:bl_signs:1122922455028219954>"   
}


########################################################################################################################
#The file includes methods to work with the bot
########################################################################################################################
import telegram



#Function: The function is used to get info of the bot with the specified token.
#Parameters: bot_token - token of the bot you want to get information of...
async def botGetInfo(bot_token):
    bot = telegram.Bot("5592920404:AAHv4_3IERHMW96fOchGBGUqjkPO-0TwMs4")
    async with bot:
        print("Bot information:")
        print(await bot.get_me())
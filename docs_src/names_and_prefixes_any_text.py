import re

import vkquick as vq

bot = vq.Bot.init_via_token("token")


@bot.add_command(any_text=True)
def foo():
    return "Hello!"


bot.run()

import sys
import traceback
import discord
from discord.ext import commands


initial_extensions = [
    'cogs.owner',
    'cogs.professions'
]

bot = commands.Bot(command_prefix=config['SETTINGS']['prefix'], 
                    activity=discord.Game(name='Harry Potter: Wizards Unite', type=1))
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')


if __name__ == '__main__':
    for extension in initial_extensions:
    
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()
            
    if config.getboolean('TOKEN', 'is-developing'):
        log.info("Running with Development token")
        TOKEN = config['TOKEN']['dev-token']
    else:
        log.info("Running with Production token")
        TOKEN = config['TOKEN']['prod-token']
            
    bot.run(TOKEN, bot=True, reconnect=True)

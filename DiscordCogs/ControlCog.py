from discord import Embed
from discord.ext.commands import Cog, command
from Config.Configs import VConfigs
from Config.Helper import Helper
from Config.Colors import VColors
from Music.VulkanBot import VulkanBot
from Config.Embeds import VEmbeds

helper = Helper()


class ControlCog(Cog):
    """Class to handle discord events"""

    def __init__(self, bot: VulkanBot):
        self.__bot = bot
        self.__config = VConfigs()
        self.__colors = VColors()
        self.__embeds = VEmbeds()
        self.__commands = {
            'MUSIC': ['resume', 'pause', 'loop', 'stop',
                      'skip', 'play', 'queue', 'clear',
                      'np', 'shuffle', 'move', 'remove',
                      'reset', 'prev', 'history'],
            'RANDOM': ['choose', 'cara', 'random']

        }

    @command(name="help", help=helper.HELP_HELP, description=helper.HELP_HELP_LONG, aliases=['h', 'ajuda'])
    async def help_msg(self, ctx, command_help=''):
        if command_help != '':
            for command in self.__bot.commands:
                if command.name == command_help:
                    txt = command.description if command.description else command.help

                    embedhelp = Embed(
                        title=f'**Описание команды {command_help}**',
                        description=txt,
                        colour=self.__colors.BLUE
                    )

                    await ctx.send(embed=embedhelp)
                    return

            embedhelp = Embed(
                title='Помощь',
                description=f'Команда {command_help} не существует, введите {self.__config.BOT_PREFIX}help, чтобы увидеть все команды',
                colour=self.__colors.BLACK
            )

            await ctx.send(embed=embedhelp)
        else:

            helptxt = ''
            help_music = '🎧 `МУЗЫКА`\n'
            help_random = '🎲 `СЛУЧАЙНЫЙ`\n'
            help_help = '👾 `HELP`\n'

            for command in self.__bot.commands:
                if command.name in self.__commands['МУЗЫКА']:
                    help_music += f'**{command}** - {command.help}\n'

                elif command.name in self.__commands['СЛУЧАЙНЫЙ']:
                    help_random += f'**{command}** - {command.help}\n'

                else:
                    help_help += f'**{command}** - {command.help}\n'

            helptxt = f'\n{help_music}\n{help_help}\n{help_random}'
            helptxt += f'\n\nВведите {self.__config.BOT_PREFIX}help "command" для получения дополнительной информации о выбранной команде.
            embedhelp = Embed(
                title=f'**Доступные команды {self.__bot.user.name}**',
                description=helptxt,
                colour=self.__colors.BLUE
            )

            embedhelp.set_thumbnail(url=self.__bot.user.avatar)
            await ctx.send(embed=embedhelp)

    @command(name='invite', help=helper.HELP_INVITE, description=helper.HELP_INVITE_LONG, aliases=['convite', 'inv', 'convidar'])
    async def invite_bot(self, ctx):
        invite_url = self.__config.INVITE_URL.format(self.__bot.user.id)
        txt = self.__config.INVITE_MESSAGE.format(invite_url, invite_url)

        embed = Embed(
            title="Пригласить Гефест",
            description=txt,
            colour=self.__colors.BLUE
        )

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ControlCog(bot))

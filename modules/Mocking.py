import uwuify
from discord.ext import commands

#colorama.init()

flags = uwuify.SMILEY | uwuify.YU | uwuify.STUTTER

class Mocking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def echo(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(text)
    @commands.command(pass_context=True)
    async def uwuify(self, ctx, *, text):
        await ctx.send(uwuify.uwu(text, flags=flags))

async def setup(bot):
    await bot.add_cog(Mocking(bot))
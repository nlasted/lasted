from discord.ext import commands

class Health(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def ping(self, ctx):
        await ctx.send(f':ping_pong: Pong!{round (self.bot.latency * 1000)}ms')

async def setup(bot):
    await bot.add_cog(Health(bot))
import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def Kick(self, ctx, *, username:discord.User):
        if ctx.message.author.guild_permissions.administrator:
            await self.bot.kick(username)
            await ctx.send(f"Kicked {username}")
        else:
            await ctx.send("You don't have administrator permission to kick.")
        
async def setup(bot):
    await bot.add_cog(Moderation(bot))
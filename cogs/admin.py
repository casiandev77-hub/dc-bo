import discord
from discord.ext import commands
from discord import app_commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount: int = 5):
        """Löscht Nachrichten"""
        if amount > 100:
            await ctx.send("❌ Maximal 100 Nachrichten können gelöscht werden!")
            return
        
        deleted = await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'✅ {len(deleted) - 1} Nachrichten gelöscht!', delete_after=5)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kickt einen User"""
        await member.kick(reason=reason)
        await ctx.send(f'✅ {member.display_name} wurde gekickt!')

async def setup(bot):
    await bot.add_cog(Admin(bot))
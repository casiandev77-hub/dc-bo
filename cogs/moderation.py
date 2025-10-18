import discord
from discord.ext import commands
import asyncio

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Bannt einen User"""
        if ctx.author.guild_permissions.ban_members:
            await member.ban(reason=reason)
            await ctx.send(f'✅ {member.display_name} wurde gebannt!')
        else:
            await ctx.send("❌ Du hast keine Berechtigung zum Bannen!")

    @commands.command()
    async def unban(self, ctx, *, member):
        """Entbannt einen User"""
        if ctx.author.guild_permissions.ban_members:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')
            
            for ban_entry in banned_users:
                user = ban_entry.user
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f'✅ {user.mention} wurde entbannt!')
                    return
            await ctx.send("❌ User nicht gefunden!")
        else:
            await ctx.send("❌ Du hast keine Berechtigung zum Entbannen!")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
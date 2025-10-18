import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Zeigt den Bot-Ping"""
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'🏓 Pong! {latency}ms')

    @commands.command()
    async def roll(self, ctx, dice: str = "1d6"):
        """Würfelt (Format: 1d6)"""
        try:
            amount, sides = map(int, dice.split('d'))
            if amount > 10 or sides > 100:
                await ctx.send("❌ Maximale Werte: 10 Würfe, 100 Seiten")
                return
            
            rolls = [random.randint(1, sides) for _ in range(amount)]
            total = sum(rolls)
            await ctx.send(f'🎲 Würfel: {rolls} | Summe: **{total}**')
        except:
            await ctx.send("❌ Ungültiges Format! Benutze: `!roll 2d6`")

    @commands.command()
    async def choose(self, ctx, *choices):
        """Wählt zwischen mehreren Optionen"""
        if len(choices) < 2:
            await ctx.send("❌ Bitte gib mindestens 2 Optionen an!")
            return
        
        choice = random.choice(choices)
        await ctx.send(f'🤔 Ich wähle: **{choice}**')

async def setup(bot):
    await bot.add_cog(Fun(bot))
import discord
import os
import sys
from discord.ext import commands
from dotenv import load_dotenv

# .env Datei laden
load_dotenv()

# Prüfe ob Token existiert
TOKEN = os.getenv('BOT_TOKEN')
if not TOKEN:
    print("❌ BOT_TOKEN nicht in .env gefunden!")
    print("ℹ️ Stelle sicher, dass die .env Datei existiert und BOT_TOKEN enthält")
    sys.exit(1)

print("🚀 Starte Discord Bot...")

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=os.getenv('BOT_PREFIX', '!'),
            intents=discord.Intents.all(),
            help_command=None
        )

    async def setup_hook(self):
        try:
            # Lade Application Cog
            await self.load_extension('cogs.application')
            print('✅ Application Cog geladen')
        except Exception as e:
            print(f'❌ Fehler beim Laden des Application Cogs: {e}')
            print(f'❌ Fehlerdetails: {type(e).__name__}: {e}')

    async def on_ready(self):
        print(f'✅ Bot ist online als {self.user}')
        print(f'📊 Aktiv auf {len(self.guilds)} Servern')
        
        # Setze Status
        activity = discord.Activity(type=discord.ActivityType.watching, name="Bewerbungen 📝")
        await self.change_presence(activity=activity)

# Bot starten
try:
    bot = Bot()
    bot.run(TOKEN)
except Exception as e:
    print(f"❌ Kritischer Fehler: {e}")
    sys.exit(1)
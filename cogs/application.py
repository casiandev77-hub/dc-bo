import discord
import os
from discord.ext import commands
from discord.ui import Button, View, Modal, TextInput

class ApplicationSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup_bewerbung(self, ctx):
        """Bewerbungssystem einrichten"""
        embed = discord.Embed(
            title="🎯 Bewerbungssystem",
            description="Wähle eine Bewerbungsart aus!",
            color=discord.Color.blue()
        )
        
        embed.add_field(
            name="📋 Positionen",
            value="• 🛡️ **Team** - Werde Teammitglied\n• 🎮 **Content Creator** - Erstelle Inhalte\n• 🔧 **Developer** - Bot-Development\n• ⚡ **Supporter** - Hilf Mitgliedern",
            inline=False
        )
        
        view = ApplicationMainView()
        await ctx.send(embed=embed, view=view)
        await ctx.send("✅ Bewerbungssystem aktiviert!", delete_after=5)

class ApplicationMainView(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="🛡️ Team", style=discord.ButtonStyle.primary, custom_id="app_team")
    async def team_app(self, interaction: discord.Interaction, button: Button):
        modal = TeamApplicationModal()
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="🎮 Creator", style=discord.ButtonStyle.success, custom_id="app_creator")
    async def creator_app(self, interaction: discord.Interaction, button: Button):
        modal = ContentCreatorModal()
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="🔧 Developer", style=discord.ButtonStyle.green, custom_id="app_dev")
    async def developer_app(self, interaction: discord.Interaction, button: Button):
        modal = DeveloperModal()
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label="⚡ Supporter", style=discord.ButtonStyle.blurple, custom_id="app_supporter")
    async def supporter_app(self, interaction: discord.Interaction, button: Button):
        modal = SupporterModal()
        await interaction.response.send_modal(modal)

# ========== AUSFÜHRLICHE MODALS ==========

class TeamApplicationModal(Modal, title="🛡️ Team Bewerbung - Ausführlicher Fragebogen"):
    def __init__(self):
        super().__init__(timeout=600)  # 10 Minuten Timeout für längere Formulare
        
        # Persönliche Informationen
        self.vollstaendiger_name = TextInput(
            label="1. Vollständiger Name",
            placeholder="Max Mustermann",
            required=True,
            max_length=100
        )
        
        self.alter = TextInput(
            label="2. Alter",
            placeholder="18",
            required=True,
            max_length=3
        )
        
        self.wohnort = TextInput(
            label="3. Wohnort/Land",
            placeholder="Berlin, Deutschland",
            required=True,
            max_length=100
        )
        
        self.zeitliche_verfuegbarkeit = TextInput(
            label="4. Zeitliche Verfügbarkeit",
            placeholder="Wie viele Stunden pro Tag/Woche kannst du investieren?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=500
        )
        
        # Erfahrung und Fähigkeiten
        self.erfahrung_team = TextInput(
            label="5. Erfahrung in Team-Positionen",
            placeholder="Hast du bereits Erfahrung in ähnlichen Positionen? Wenn ja, wo?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1000
        )
        
        self.staerken = TextInput(
            label="6. Deine Stärken",
            placeholder="Was sind deine größten Stärken? (Kommunikation, Organisation, etc.)",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1000
        )
        
        self.schwaechen = TextInput(
            label="7. Deine Schwächen",
            placeholder="Wo siehst du Verbesserungspotenzial bei dir?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1000
        )
        
        # Motivation
        self.motivation = TextInput(
            label="8. Warum möchtest du Team-Mitglied werden?",
            placeholder="Erzähle uns warum du genau unser Team bereichern möchtest...",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1500
        )
        
        self.ideen_beitraege = TextInput(
            label="9. Ideen und Beiträge",
            placeholder="Welche Ideen oder Beiträge könntest du in unser Team einbringen?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1500
        )
        
        # Sonstiges
        self.sonstiges = TextInput(
            label="10. Sonstiges",
            placeholder="Weitere Informationen die für uns wichtig sein könnten...",
            style=discord.TextStyle.paragraph,
            required=False,
            max_length=1000
        )
        
        # Alle Felder hinzufügen
        self.add_item(self.vollstaendiger_name)
        self.add_item(self.alter)
        self.add_item(self.wohnort)
        self.add_item(self.zeitliche_verfuegbarkeit)
        self.add_item(self.erfahrung_team)
        self.add_item(self.staerken)
        self.add_item(self.schwaechen)
        self.add_item(self.motivation)
        self.add_item(self.ideen_beitraege)
        self.add_item(self.sonstiges)
    
    async def on_submit(self, interaction: discord.Interaction):
        await self.send_detailed_application(interaction, "🛡️ Team")

class ContentCreatorModal(Modal, title="🎮 Content Creator Bewerbung - Ausführlicher Fragebogen"):
    def __init__(self):
        super().__init__(timeout=600)
        
        # Persönliche Informationen
        self.creator_name = TextInput(
            label="1. Creator-Name/Spitzname",
            placeholder="Dein Künstlername oder wie du bekannt bist",
            required=True,
            max_length=100
        )
        
        self.alter = TextInput(
            label="2. Alter",
            placeholder="18",
            required=True,
            max_length=3
        )
        
        # Plattformen und Reichweite
        self.aktive_plattformen = TextInput(
            label="3. Aktive Plattformen",
            placeholder="Auf welchen Plattformen bist du aktiv? (YouTube, Twitch, TikTok, Instagram, etc.)",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=500
        )
        
        self.reichweite = TextInput(
            label="4. Reichweite/Follower",
            placeholder="Wie viele Follower/Abonnenten hast du auf deinen Hauptplattformen?",
            required=True,
            max_length=200
        )
        
        # Content-Art
        self.content_schwerpunkt = TextInput(
            label="5. Content-Schwerpunkt",
            placeholder="Welche Art von Content erstellst du hauptsächlich? (Gaming, Vlogs, Tutorials, Comedy, etc.)",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1000
        )
        
        self.besondere_faehigkeiten = TextInput(
            label="6. Besondere Fähigkeiten",
            placeholder="Welche besonderen Fähigkeiten bringst du mit? (Video Editing, Grafikdesign, etc.)",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1000
        )
        
        # Ausrüstung und Erfahrung
        self.ausruestung = TextInput(
            label="7. Benutzte Ausrüstung/Software",
            placeholder="Welche Ausrüstung/Software verwendest du für deinen Content?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1000
        )
        
        self.erfahrung_jahre = TextInput(
            label="8. Erfahrung als Creator",
            placeholder="Wie lange erstellst du schon Content?",
            required=True,
            max_length=100
        )
        
        # Ziele und Zusammenarbeit
        self.ziele = TextInput(
            label="9. Deine Ziele als Creator",
            placeholder="Was möchtest du als Content Creator erreichen?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1500
        )
        
        self.zusammenarbeit_ideen = TextInput(
            label="10. Ideen für Zusammenarbeit",
            placeholder="Welche Content-Ideen hast du für unsere Community?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1500
        )
        
        # Portfolio/Links
        self.portfolio_links = TextInput(
            label="11. Portfolio/Links (optional)",
            placeholder="Links zu deinem Portfolio oder besten Arbeiten",
            style=discord.TextStyle.paragraph,
            required=False,
            max_length=1000
        )
        
        # Felder hinzufügen
        self.add_item(self.creator_name)
        self.add_item(self.alter)
        self.add_item(self.aktive_plattformen)
        self.add_item(self.reichweite)
        self.add_item(self.content_schwerpunkt)
        self.add_item(self.besondere_faehigkeiten)
        self.add_item(self.ausruestung)
        self.add_item(self.erfahrung_jahre)
        self.add_item(self.ziele)
        self.add_item(self.zusammenarbeit_ideen)
        self.add_item(self.portfolio_links)
    
    async def on_submit(self, interaction: discord.Interaction):
        await self.send_detailed_application(interaction, "🎮 Content Creator")

class DeveloperModal(Modal, title="🔧 Developer Bewerbung - Ausführlicher Fragebogen"):
    def __init__(self):
        super().__init__(timeout=600)
        
        # Persönliche Informationen
        self.vollstaendiger_name = TextInput(
            label="1. Vollständiger Name",
            placeholder="Max Mustermann",
            required=True,
            max_length=100
        )
        
        self.alter = TextInput(
            label="2. Alter",
            placeholder="18",
            required=True,
            max_length=3
        )
        
        # Programmiererfahrung
        self.programmiersprachen = TextInput(
            label="3. Programmiersprachen",
            placeholder="Welche Programmiersprachen beherrschst du und auf welchem Level?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1000
        )
        
        self.erfahrung_jahre = TextInput(
            label="4. Programmiererfahrung (in Jahren)",
            placeholder="Wie lange programmierst du schon?",
            required=True,
            max_length=100
        )
        
        # Spezielle Fähigkeiten
        self.spezialgebiete = TextInput(
            label="5. Spezialgebiete",
            placeholder="Hast du Spezialgebiete? (Web Development, Bot Development, Databases, etc.)",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1000
        )
        
        self.technologien_frameworks = TextInput(
            label="6. Technologien & Frameworks",
            placeholder="Welche Technologien, Frameworks oder Libraries kennst du?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1000
        )
        
        # Discord-spezifische Erfahrung
        self.discord_erfahrung = TextInput(
            label="7. Discord Bot Erfahrung",
            placeholder="Welche Erfahrung hast du mit Discord Bots/APIs?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1500
        )
        
        # Projekte und Portfolio
        self.bisherige_projekte = TextInput(
            label="8. Bisherige Projekte",
            placeholder="Beschreibe deine bisherigen Projekte (persönlich oder beruflich)...",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1500
        )
        
        self.github_portfolio = TextInput(
            label="9. GitHub/Portfolio Links",
            placeholder="Links zu deinem GitHub, Portfolio oder Beispielprojekten",
            style=discord.TextStyle.paragraph,
            required=False,
            max_length=1000
        )
        
        # Motivation und Ziele
        self.motivation = TextInput(
            label="10. Warum möchtest du Developer bei uns werden?",
            placeholder="Was reizt dich besonders an der Entwicklung für unsere Community?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1500
        )
        
        self.ideen_fuer_bots = TextInput(
            label="11. Ideen für Bots/Features",
            placeholder="Welche Bot-Features oder Verbesserungen würdest du gerne umsetzen?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1500
        )
        
        # Verfügbarkeit
        self.verfuegbarkeit = TextInput(
            label="12. Zeitliche Verfügbarkeit",
            placeholder="Wie viele Stunden pro Woche könntest du für Development investieren?",
            required=True,
            max_length=500
        )
        
        # Felder hinzufügen
        self.add_item(self.vollstaendiger_name)
        self.add_item(self.alter)
        self.add_item(self.programmiersprachen)
        self.add_item(self.erfahrung_jahre)
        self.add_item(self.spezialgebiete)
        self.add_item(self.technologien_frameworks)
        self.add_item(self.discord_erfahrung)
        self.add_item(self.bisherige_projekte)
        self.add_item(self.github_portfolio)
        self.add_item(self.motivation)
        self.add_item(self.ideen_fuer_bots)
        self.add_item(self.verfuegbarkeit)
    
    async def on_submit(self, interaction: discord.Interaction):
        await self.send_detailed_application(interaction, "🔧 Developer")

class SupporterModal(Modal, title="⚡ Supporter Bewerbung - Ausführlicher Fragebogen"):
    def __init__(self):
        super().__init__(timeout=600)
        
        # Persönliche Informationen
        self.vollstaendiger_name = TextInput(
            label="1. Vollständiger Name",
            placeholder="Max Mustermann",
            required=True,
            max_length=100
        )
        
        self.alter = TextInput(
            label="2. Alter",
            placeholder="18",
            required=True,
            max_length=3
        )
        
        self.wohnort = TextInput(
            label="3. Wohnort/Zeitzone",
            placeholder="Berlin, Deutschland (UTC+1)",
            required=True,
            max_length=100
        )
        
        # Sprachkenntnisse
        self.sprachkenntnisse = TextInput(
            label="4. Sprachkenntnisse",
            placeholder="Welche Sprachen sprichst du und auf welchem Niveau?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1000
        )
        
        # Erfahrung
        self.support_erfahrung = TextInput(
            label="5. Support-Erfahrung",
            placeholder="Hast du bereits Erfahrung im Kundensupport oder Community-Management?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1500
        )
        
        # Fähigkeiten
        self.staerken_im_umgang = TextInput(
            label="6. Stärken im Umgang mit Menschen",
            placeholder="Was zeichnet dich im Umgang mit anderen aus?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1000
        )
        
        self.konfliktloesung = TextInput(
            label="7. Umgang mit Konflikten",
            placeholder="Wie gehst du mit Konflikten oder schwierigen Situationen um?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1500
        )
        
        # Verfügbarkeit
        self.verfuegbarkeit = TextInput(
            label="8. Zeitliche Verfügbarkeit",
            placeholder="Zu welchen Zeiten bist du normalerweise verfügbar? (Tage/Uhrzeiten)",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=500
        )
        
        self.stunden_pro_woche = TextInput(
            label="9. Stunden pro Woche",
            placeholder="Wie viele Stunden pro Woche könntest du investieren?",
            required=True,
            max_length=100
        )
        
        # Motivation
        self.motivation = TextInput(
            label="10. Warum möchtest du Supporter werden?",
            placeholder="Was motiviert dich besonders in dieser Rolle?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1500
        )
        
        self.erwartungen = TextInput(
            label="11. Erwartungen an die Rolle",
            placeholder="Was erwartest du von der Supporter-Rolle?",
            style=discord.TextStyle.paragraph,
            required=True,
            max_length=1500
        )
        
        # Sonstiges
        self.sonstiges = TextInput(
            label="12. Sonstiges",
            placeholder="Weitere Informationen die für uns wichtig sein könnten...",
            style=discord.TextStyle.paragraph,
            required=False,
            max_length=1000
        )
        
        # Felder hinzufügen
        self.add_item(self.vollstaendiger_name)
        self.add_item(self.alter)
        self.add_item(self.wohnort)
        self.add_item(self.sprachkenntnisse)
        self.add_item(self.support_erfahrung)
        self.add_item(self.staerken_im_umgang)
        self.add_item(self.konfliktloesung)
        self.add_item(self.verfuegbarkeit)
        self.add_item(self.stunden_pro_woche)
        self.add_item(self.motivation)
        self.add_item(self.erwartungen)
        self.add_item(self.sonstiges)
    
    async def on_submit(self, interaction: discord.Interaction):
        await self.send_detailed_application(interaction, "⚡ Supporter")

    async def send_detailed_application(self, interaction: discord.Interaction, application_type: str):
        # Erstelle ein detailliertes Embed für die Bewerbung
        embed = discord.Embed(
            title=f"📨 Detaillierte {application_type} Bewerbung",
            color=discord.Color.blue(),
            timestamp=discord.utils.utcnow()
        )
        
        embed.add_field(name="👤 Bewerber", value=interaction.user.mention, inline=True)
        embed.add_field(name="🆔 User ID", value=interaction.user.id, inline=True)
        embed.add_field(name="📅 Eingereicht", value=f"<t:{int(interaction.created_at.timestamp())}:F>", inline=False)
        
        embed.add_field(name="**📋 Bewerbungsdetails**", value="▬▬▬▬▬▬▬▬▬▬▬▬▬", inline=False)
        
        # Füge alle Felder dynamisch hinzu
        for child in self.children:
            if child.value and child.value.strip():
                # Kürze sehr lange Antworten für bessere Lesbarkeit
                value = child.value
                if len(value) > 1024:
                    value = value[:1020] + "..."
                embed.add_field(name=child.label, value=value, inline=False)
        
        embed.set_thumbnail(url=interaction.user.display_avatar.url)
        embed.set_footer(text=f"{application_type} Bewerbung • Ausführlicher Fragebogen")
        
        # Admin View mit Buttons
        admin_view = SimpleAdminView(interaction.user.id, application_type)
        
        # Sende Bewerbung in den aktuellen Channel
        await interaction.channel.send(embed=embed, view=admin_view)
        
        # Bestätigung an User
        confirm_embed = discord.Embed(
            title="✅ Bewerbung erfolgreich eingereicht",
            description=f"Deine detaillierte {application_type} Bewerbung wurde gesendet!",
            color=discord.Color.green()
        )
        confirm_embed.add_field(
            name="⏰ Bearbeitungszeit",
            value="Wir werden deine Bewerbung sorgfältig prüfen und uns innerhalb von 48 Stunden bei dir melden.",
            inline=False
        )
        confirm_embed.add_field(
            name="📝 Hinweis",
            value="Du hast alle Fragen sehr ausführlich beantwortet - vielen Dank dafür!",
            inline=False
        )
        
        await interaction.response.send_message(embed=confirm_embed, ephemeral=True)

class SimpleAdminView(View):
    def __init__(self, applicant_id: int, app_type: str):
        super().__init__(timeout=None)
        self.applicant_id = applicant_id
        self.app_type = app_type
    
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        # Nur Admins oder bestimmte Rollen dürfen die Buttons verwenden
        if interaction.user.guild_permissions.administrator:
            return True
        
        # Prüfe auf REVIEWER_ROLES falls konfiguriert
        reviewer_roles = os.getenv('REVIEWER_ROLES', '')
        if reviewer_roles:
            for role_id in reviewer_roles.split(','):
                role_id = role_id.strip()
                if role_id and interaction.user.get_role(int(role_id)):
                    return True
        
        # Keine Berechtigung
        await interaction.response.send_message(
            "❌ Du hast keine Berechtigung um Bewerbungen zu bearbeiten!", 
            ephemeral=True
        )
        return False
    
    @discord.ui.button(label="✅ ANNEHMEN", style=discord.ButtonStyle.success, custom_id="accept_app")
    async def accept_app(self, interaction: discord.Interaction, button: Button):
        applicant = interaction.guild.get_member(self.applicant_id)
        
        # Sofortige Antwort
        await interaction.response.send_message("✅ Bewerbung angenommen!", ephemeral=True)
        
        if applicant:
            try:
                # DM an Bewerber
                accept_embed = discord.Embed(
                    title="🎉 Bewerbung angenommen!",
                    description=f"Deine {self.app_type} Bewerbung wurde angenommen.",
                    color=discord.Color.green()
                )
                accept_embed.add_field(
                    name="👤 Bearbeitet von",
                    value=interaction.user.display_name,
                    inline=True
                )
                accept_embed.add_field(
                    name="📋 Nächste Schritte",
                    value="Ein Teammitglied wird sich in Kürze bei dir melden, um die weiteren Schritte zu besprechen.",
                    inline=False
                )
                await applicant.send(embed=accept_embed)
                
                # Rolle zuweisen falls konfiguriert
                role_id = os.getenv('APPLICATION_ROLE')
                if role_id:
                    role = interaction.guild.get_role(int(role_id))
                    if role:
                        await applicant.add_roles(role)
                        
            except discord.Forbidden:
                pass  # Kann keine DM senden
        
        # Embed aktualisieren
        embed = interaction.message.embeds[0]
        embed.color = discord.Color.green()
        embed.add_field(name="✅ Status", value=f"Angenommen von {interaction.user.mention}", inline=False)
        
        # Buttons entfernen
        await interaction.message.edit(embed=embed, view=None)
    
    @discord.ui.button(label="❌ ABLEHNEN", style=discord.ButtonStyle.danger, custom_id="reject_app")
    async def reject_app(self, interaction: discord.Interaction, button: Button):
        applicant = interaction.guild.get_member(self.applicant_id)
        
        # Sofortige Antwort
        await interaction.response.send_message("❌ Bewerbung abgelehnt!", ephemeral=True)
        
        if applicant:
            try:
                # DM an Bewerber
                reject_embed = discord.Embed(
                    title="❌ Bewerbung abgelehnt",
                    description=f"Deine {self.app_type} Bewerbung wurde abgelehnt.",
                    color=discord.Color.red()
                )
                reject_embed.add_field(
                    name="👤 Bearbeitet von",
                    value=interaction.user.display_name,
                    inline=True
                )
                reject_embed.add_field(
                    name="ℹ️ Informationen",
                    value="Du kannst dich in 30 Tagen erneut bewerben. Bei Fragen stehe ich dir gerne zur Verfügung.",
                    inline=False
                )
                await applicant.send(embed=reject_embed)
            except discord.Forbidden:
                pass  # Kann keine DM senden
        
        # Embed aktualisieren
        embed = interaction.message.embeds[0]
        embed.color = discord.Color.red()
        embed.add_field(name="❌ Status", value=f"Abgelehnt von {interaction.user.mention}", inline=False)
        
        # Buttons entfernen
        await interaction.message.edit(embed=embed, view=None)
    
    @discord.ui.button(label="💬 INTERVIEW", style=discord.ButtonStyle.primary, custom_id="interview_app")
    async def interview_app(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message("💬 Interview-Funktion kommt bald!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(ApplicationSystem(bot))
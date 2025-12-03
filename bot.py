import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='z', intents=discord.Intents.all())

class Confirm(discord.ui.View):
  def __init__(self, ctx):
    super().__init__ (timeout=30.0)
    self.ctx = ctx
    self.view = None
    
class Cancel(discord.ui.View):
  def __init__(self, ctx):
    super().__init__ (timeout=30.0)
    self.ctx = ctx
    self.view = None
  
@discord.ui.button(label="Confirm", style=discord.ButtonStyle.danger)
async def confirm (self, i: discord.Interaction, b: discord.ui.Button):
  if i.user.id != self.ctx.author.id:
    return await interaction.response.send_message(embed=discord.Embed(description=f"{i.user.mention}: You cannot respond to this 
    
@bot.command()
@commands.has_permissions(administrator=True)
async def clean (ctx):
  
@bot.command()
async def serverinfo (ctx):
  
  embed = discord.Embed(description=ctx.guild.name, color=0xA4C4FF)
  if ctx.guild.icon:
    embed.set_thumbnail(url=ctx.guild.icon)
  embed.add_field(name="Owner: ", value=ctx.guild.owner, inline=True)
  embed.add_field(name="Boosts: ", value=ctx.guild
  .premium_subscription.count, inline=True)
  embed.add_field(name="Boost Tier: ", value=

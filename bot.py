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
    return await interaction.response.send_message(embed=discord.Embed(description=f"{i.user.mention}: You cannot respond to this interaction!", color=0x000001, ephemeral=True)

  self.view.ctx = True
  self.stop()

@discord.ui.button(label="Cancel", style=discord.ButtonStyle.secondary)
async def cancel(self, i: discord.Interaction, b: discord.ui.Button):
  if i.user.id != self.ctx.author.id:
    return await interaction.response.send_message(embed=discord.Embed(description=f"{i.user.mention}: You cannot respond to this interaction!", color=0x000001, ephemeral=True)
  
  self.view.ctx = False                                            
  self.stop()
                                                   
@bot.command()
@commands.has_permissions(administrator=True)
async def clean (ctx):
  await ctx.send(embed=discord.Embed(description="Are you sure? This will delete all emojis, stickers and roles from this server!", color=0xA4C4FF, view=Confirm(ctx), Cancel(ctx))
    

@bot.command()
async def serverinfo (ctx):
  
  embed = discord.Embed(description=ctx.guild.name, color=0xA4C4FF)
  if ctx.guild.icon:
    embed.set_thumbnail(url=ctx.guild.icon_url)
  embed.add_field(name="Owner: ", value=ctx.guild.owner, inline=True)
  embed.add_field(name="Boosts: ", value=ctx.guild
  .premium_subscription.count, inline=True)
  embed.add_field(name="Boost Tier: ", value=str(ctx.guild.premium_tier), inline=True)
  embed.add_field(name="Channels: ", value=f"txt: {len(ctx.guild.text_channels)} | voice: {len(ctx.guild.voice_channels)}", inline=False)
  await ctx.send(embed=embed)
  

import discord, asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='z', intents=discord.Intents.all())

@bot.event
async def on_ready():
  print(f"[ + ] Logged in as: {bot.user}")
  print(f"[ + ] ID: {bot.user.id}")
  await bot.change_presence(status=discord.Status.idle, activity=discord.ActivityType.watching("⚖️"))
  
class Clean(discord.ui.View):
  def __init__(self, ctx):
    super().__init__ (timeout=30.0)
    self.ctx = ctx
    self.value = None
    
  @discord.ui.button(label="Confirm", style=discord.ButtonStyle.danger)
  async def confirm (self, i: discord.Interaction, b: discord.ui.Button):
    if i.user.id != self.ctx.author.id:
      return await i.response.send_message(embed=discord.Embed(description=f"{i.user.mention}: You cannot respond to this interaction!", color=0x000001, ephemeral=True))
    else:
      self.value = True
      await i.response.edit_message(embed=discord.Embed(description=f"👍 {self.ctx.author.mention}", color=discord.Color.random(), ephemeral=True))
      self.stop()
  
  @discord.ui.button(label="Cancel", style=discord.ButtonStyle.secondary)
  async def cancel(self, i: discord.Interaction, b: discord.ui.Button):
    if i.user.id != self.ctx.author.id:
      return await i.response.send_message(embed=discord.Embed(description=f"{i.user.mention}: You cannot respond to this interaction!", color=0x000001, ephemeral=True)
    else:
      self.value = False
    await i.response.send_message(embed=discord.Embed(description=f"{self.ctx.author.mention}: 👍: Cancelled.", color=0xA4C4FF, ephemeral=True)
      self.stop()
                                                   
@bot.command()
@commands.has_permissions(administrator=True)
async def clean (ctx):
  c = Clean(ctx)
  try:
    await ctx.reply(embed=discord.Embed(description=f"{ctx.author.mention}: Are you sure? This will delete all emojis, stickers and roles from this server!", color=0xA4C4FF, view=c)
    await c.wait()
    
    if c.value is True:
      await ctx.message.add_reaction("👍")
      for emoji in ctx.guild.emojis:
        try:
          await emoji.delete()
          await asyncio.sleep(0.1)
        except:
          pass
      for sticker in ctx.guild.stickers:
        try:
          await sticker.delete()
          await asyncio.sleep(0.1)
        except:
          pass
      for member in ctx.guild.members:
        try:
          await member.edit(nick=None)
          await asyncio.sleep(0.1)
        except:
            pass
      for role in ctx.guild.roles:
        try:
          await role.delete()
          await asyncio.sleep(0.2)
        except:
          pass
  except asyncio.TimeoutError:
      await ctx.message.add_reaction("👎")

@bot.command()
async def serverinfo (ctx):
  
  embed = discord.Embed(description=ctx.guild.name, color=0xA4C4FF)
  if ctx.guild.icon:
    embed.set_thumbnail(url=ctx.guild.icon.url)
  embed.add_field(name="Owner: ", value=ctx.guild.owner, inline=True)
  embed.add_field(name="Boosts: ", value=ctx.guild.premium_subscription_count, inline=True)
  embed.add_field(name="Boost Tier: ", value=str(ctx.guild.premium_tier), inline=True)
  embed.add_field(name="Channels: ", value=f"txt: {len(ctx.guild.text_channels)} | voice: {len(ctx.guild.voice_channels)}", inline=False)
  embed.add_field(name="Roles: ", value='\n'.join([r.mention for r in ctx.guild.roles]), inline=False)
  await ctx.send(embed=embed)

bot.run(token)

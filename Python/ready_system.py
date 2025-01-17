ready_players = []

@bot.command()
async def ready(ctx):
    if ctx.author.id not in ready_players:
        ready_players.append(ctx.author.id)
        await ctx.send(f"{ctx.author.mention} is ready! ({len(ready_players)}/10)")
    if len(ready_players) == 10:
        await ctx.send("10 players are ready! The match can begin.")

@bot.command()
async def notready(ctx):
    if ctx.author.id in ready_players:
        ready_players.remove(ctx.author.id)
        await ctx.send(f"{ctx.author.mention} is no longer ready.")

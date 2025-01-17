@bot.command()
async def choose_teams(ctx):
    if len(ready_players) != 10:
        await ctx.send("Not enough players are ready.")
        return

    # Sort players by MMR
    sorted_players = sorted(ready_players, key=lambda x: get_mmr(x)["mmr"], reverse=True)
    team_captains = sorted_players[:2]
    await ctx.send(f"{ctx.guild.get_member(team_captains[0]).mention} and {ctx.guild.get_member(team_captains[1]).mention} are the captains!")

    team_1 = []
    team_2 = []

    # Drafting process
    turn = 0
    while len(team_1) + len(team_2) < 10:
        current_captain = team_captains[turn % 2]
        await ctx.send(f"{ctx.guild.get_member(current_captain).mention}, choose a player by mentioning them.")
        def check(msg):
            return msg.author.id == current_captain and msg.mentions
        msg = await bot.wait_for('message', check=check)
        chosen_player = msg.mentions[0].id
        if chosen_player not in team_1 and chosen_player not in team_2:
            if turn % 2 == 0:
                team_1.append(chosen_player)
            else:
                team_2.append(chosen_player)
            turn += 1

    await ctx.send(f"Team 1: {', '.join([ctx.guild.get_member(p).mention for p in team_1])}")
    await ctx.send(f"Team 2: {', '.join([ctx.guild.get_member(p).mention for p in team_2])}")

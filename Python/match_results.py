@bot.command()
async def end_game(ctx, winning_team: int):
    if winning_team not in [1, 2]:
        await ctx.send("Please specify the winning team (1 or 2).")
        return

    winners = team_1 if winning_team == 1 else team_2
    losers = team_2 if winning_team == 1 else team_1

    for player in winners:
        update_mmr(player, "win")
    for player in losers:
        update_mmr(player, "loss")

    await ctx.send("Scores have been updated.")

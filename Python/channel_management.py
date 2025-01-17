@bot.command()
async def create_channels(ctx):
    guild = ctx.guild
    team_1_channel = await guild.create_voice_channel("Team 1")
    team_2_channel = await guild.create_voice_channel("Team 2")

    # Restrict access
    for channel, team in zip([team_1_channel, team_2_channel], [team_1, team_2]):
        for member_id in team:
            member = guild.get_member(member_id)
            await channel.set_permissions(member, connect=True)

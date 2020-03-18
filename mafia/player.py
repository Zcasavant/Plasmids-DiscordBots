import discord

class Player:
    """
    Base Player class for Mafia game
    """

    def __init__(self, member: discord.Member):
        self.member = member
        self.mention = member.mention
        self.role = None
        self.id = None
        self.score = 0

    async def assign_role(self, role):
        """
        Give this player a role
        """
        role.player = self
        self.role = role

    async def assign_id(self, target_id):
        self.id = target_id

    async def send_dm(self, embed):
        try:
            await self.member.send(embed=embed)
        except discord.Forbidden:
            await self.role.game.village_channel.send("Couldn't DM to {}".format(self.mention))
    
    async def _start_round(self):
        embed = discord.Embed(title="You are " + self.role.name,
                            description=self.role.game_start_message,
                            color=self.role.color)

        await self.send_dm(embed)
import asyncio

from rctogether import WebsocketSubscription, RestApiSession, bots

TARGET = {"x": 160, "y": 3}
PARTICLE_HOME = {"x": 160, "y": 10}
PARTICLE_AWAY = {"x": 160, "y": 28}


class RealityLab:
    def __init__(self, session):
        self.session = session
        self.particle = None
        self.target_id = None

    async def handle_entity(self, entity):
        if entity["pos"] == TARGET:
            print("TARGET ACQUIRED: ", entity)
            if self.particle:
                await bots.update(self.session, self.particle["id"], TARGET)
                self.target_id = entity["id"]
        elif entity["id"] == self.target_id and entity["pos"] != TARGET:
            print("Target gone - reset.")
            await bots.update(self.session, self.particle["id"], PARTICLE_HOME)
            self.target_id = None

        if entity["id"] == self.particle["id"]:
            await self.handle_particle_move(entity)

    async def handle_particle_move(self, entity):
        print("Particle move: ", entity, self.target_id, TARGET)

        if self.target_id:
            return

        if entity["pos"] == PARTICLE_HOME:
            await bots.update(self.session, self.particle["id"], PARTICLE_AWAY)
        else:
            await bots.update(self.session, self.particle["id"], PARTICLE_HOME)


async def main():
    async with RestApiSession() as session:
        reality_lab = RealityLab(session)
        reality_lab.particle = await bots.create(
            session,
            name="Particle",
            emoji="🔥",
            x=PARTICLE_HOME["x"],
            y=PARTICLE_HOME["y"],
        )

        async for entity in WebsocketSubscription():
            await reality_lab.handle_entity(entity)


if __name__ == "__main__":
    asyncio.run(main())

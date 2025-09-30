import asyncio
from rctogether import RestApiSession, bots


async def main():
    async with RestApiSession() as session:
        await bots.delete_all(session)


asyncio.run(main())

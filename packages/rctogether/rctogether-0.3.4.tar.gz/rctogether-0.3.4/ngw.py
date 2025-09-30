import asyncio
from rctogether import bots, RestApiSession

ANIMALS = [
    {"emoji": "🦇", "name": "bat", "noise": "screech!"},
    {"emoji": "🐝", "name": "bee", "noise": "buzz!"},
    {"emoji": "🦕", "name": "brontosaurus", "noise": "MEEEHHH!"},
    {"emoji": "🐫", "name": "camel"},
    {"emoji": "🐈", "name": "cat", "noise": "miaow!"},
    {"emoji": "🐛", "name": "caterpillar", "noise": "munch!"},
    {"emoji": "🐄", "name": "cow", "noise": "Moo!"},
    {"emoji": "🦀", "name": "crab", "noise": "click!"},
    {"emoji": "🐊", "name": "crocodile"},
    {"emoji": "🐕", "name": "dog", "noise": "woof!"},
    {"emoji": "🐉", "name": "dragon", "noise": "🔥"},
    {"emoji": "🦅", "name": "eagle"},
    {"emoji": "🐘", "name": "elephant"},
    {"emoji": "🦩", "name": "flamingo"},
    {"emoji": "🦊", "name": "fox", "noise": "Wrahh!"},
    {"emoji": "🐸", "name": "frog", "noise": "ribbet!"},
    {"emoji": "🦒", "name": "giraffe"},
    {"emoji": "🦔", "name": "hedgehog", "noise": "scurry, scurry, scurry"},
    {"emoji": "🦛", "name": "hippo"},
    {"emoji": "👾", "name": "invader"},
    {"emoji": "🦘", "name": "kangaroo", "noise": "Chortle chortle!"},
    {"emoji": "🐨", "name": "koala", "noise": "gggrrrooowwwlll"},
    {"emoji": "🦙", "name": "llama"},
    {"emoji": "🐁", "name": "mouse", "noise": "squeak!"},
    {"emoji": "🦉", "name": "owl", "noise": "hoot hoot!"},
    {"emoji": "🦜", "name": "parrot", "noise": "HELLO!"},
    {"emoji": "🐧", "name": "penguin"},
    {"emoji": "🐖", "name": "pig", "noise": "oink!"},
    {"emoji": "🐇", "name": "rabbit"},
    {"emoji": "🚀", "name": "rocket"},
    {"emoji": "🐌", "name": "snail", "noise": "slurp!"},
    {"emoji": "🦖", "name": "t-rex", "noise": "RAWR!"},
    {"emoji": "🐅", "name": "tiger"},
    {"emoji": "🐢", "name": "turtle", "noise": "hiss!"},
    {"emoji": "🦄", "name": "unicorn", "noise": "✨"},
    {"emoji": "🐑", "name": "sheep"},
    {"emoji": "🦆", "name": "duck"},
    {"emoji": "🐄", "name": "cow"},
]

ANIMAL_BY_NAME = {animal['name']: animal['emoji'] for animal in ANIMALS}

async def set_emoji(session, bot, emoji):
    await bots.update(session, bot['id'], {'emoji': emoji})

async def ngwify(session, bots):
    for bot in bots:
        if 'Genie' in bot['name']:
            print(bot)
            continue
        print(bot)
        await set_emoji(session, bot, '🐙')
        await asyncio.sleep(0.1)

async def dengwify(session, bots):
    for bot in bots:
        if bot['emoji'] == '🐙':
            name = bot['name'].split()[-1]
            normal_emoji = ANIMAL_BY_NAME[name]
            print(bot)
            await set_emoji(session, bot, normal_emoji)
            await asyncio.sleep(0.1)

async def main():
    async with RestApiSession() as session:
        all_bots = await bots.get(session)
        await dengwify(session, all_bots)

asyncio.run(main())

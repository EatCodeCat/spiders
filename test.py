import time
import asyncio


async def asyncic():
    print('async 1')
    await print('async 2')





asyncio.ensure_future(asyncic())
loop = asyncio.get_event_loop()
loop.run_forever()
print('async end')
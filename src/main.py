import asyncio
import multiprocessing
import sys

from peacepie import PeaceSystem


multiprocessing.set_start_method('spawn', force=True)


async def main():
    param = sys.argv[1] if len(sys.argv) > 1 else {}
    pp = PeaceSystem(param)
    await pp.start()
    try:
        await pp.task
    except asyncio.CancelledError:
        pass


if __name__ == '__main__':
    asyncio.run(main())

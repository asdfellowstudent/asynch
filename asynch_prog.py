import asyncio

async def boil_water():
    print("Water start boiling..")
    await asyncio.sleep(3)
    print("Water end boiling..")

async def cut_onion():
    print("Start cutting..")
    await asyncio.sleep(2)
    print("End cutting..")

# hello

async def prepare_salad():
    print("Start salad..")
    await asyncio.sleep(4)
    print("End salad..")

async def main():
    await asyncio.gather(boil_water(), cut_onion(), prepare_salad())

asyncio.run()
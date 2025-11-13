# made By Amir 2025 november 13

import asyncio
import random
import os  # for clearing screen

random_Events = {
    "1": "⚠️FUEL LEAK WARNING EMERGENCY ⚠️",
    "2": "⚠️ENGNE OVERHEATING (entering optimize mode)⚠️",
    "3": "⚠️LIFE SUPPORT MALFUNCTION⚠️"
    }

# === Life Support ===
class LifeSupport:
    def __init__(self):
        self.oxygen = 100
        self.temperature = 22  # starting temp
        self.pressure = 101  # kPa

    async def consume_oxygen(self, amount):
        self.oxygen -= amount
        if self.oxygen <= 20:
            print("⚠️ WARNING: Oxygen low!")
        await asyncio.sleep(0.5)

    async def regulate_temperature(self):
        change = random.uniform(-0.5, 0.5)
        self.temperature += change
        if self.temperature < 18 or self.temperature > 26:
            print(f"⚠️ WARNING: Temperature out of range! {self.temperature:.2f}°C")
        await asyncio.sleep(0.5)

    async def status(self):
        print(f"O2: {self.oxygen:.2f}%, Temp: {self.temperature:.2f}°C, Pressure: {self.pressure} kPa")
    


# === Rocket ===
required = 20
class Rocket:
    def __init__(self, Fuel: int, temp, LifeSupportXCODE):
        self.Fuel = Fuel
        self.temp = temp
        self.LifeSupportXCODE = LifeSupportXCODE
    async def launch(self):
        if self.Fuel < required:
            print('Not Enough fuel to run!')
            return "Error 2a"
        print('🚀 Launching...')
        await self.fuel()

    async def fuel(self):
        while self.Fuel >= 21:
            if self.Fuel <= 30:
                print('⚠️ Low fuel Warning!')
            self.Fuel -= 1
            await asyncio.sleep(0.5)
    async def randomEvent(self, life):
        while True:
            randomNumber = random.randint(1, 10)
            for event in random_Events:
                if int(event) == randomNumber:
                    if int(event) == 1:
                        self.Fuel -= random.randint(1, 50)
                        print(random_Events[event])
                    elif int(event) == 2:
                        self.temp += 25
                        # Entering optimize mode and redefining fuel method
                        async def Optimize_Mode(self):
                            while self.Fuel >= 21:
                                if self.Fuel <= 0:
                                    print('Shutting down Rocket')
                                    return "Fuel Ended"
                                if self.Fuel <= 30:
                                    print('⚠️ Low fuel Warning!')
                                self.Fuel -= 0.5
                                await asyncio.sleep(0.5)
                        self.fuel = Optimize_Mode.__get__(self)

                    elif int(event) == 3:
                        # Use the LifeSupport instance directly
                        self.LifeSupportXCODE = life.consume_oxygen  # just assign the method

                    print(random_Events[event])

            await asyncio.sleep(1) 


# === ASCII Rocket Animation ===
async def rocket_animation(rocket: Rocket):
    rocket_height = 0
    while rocket.Fuel >= 21:
        os.system('cls' if os.name == 'nt' else 'clear')  # clear console
        rocket_height += 1
        print("\n" * (10 - rocket_height))  # move rocket up
        print("   ^")
        print("  / \\")
        print("  | |")
        print(" /___\\")
        print("   |")
        print(f"Fuel: {rocket.Fuel}")
        await asyncio.sleep(0.5)


# === Main Mission Control ===
async def mission():
    life = LifeSupport()
    rocket = Rocket(Fuel=110, temp=life.temperature, LifeSupportXCODE=life.consume_oxygen)
    
    rocket_task = asyncio.create_task(rocket.launch())
    animation_task = asyncio.create_task(rocket_animation(rocket))
    random_task = asyncio.create_task(rocket.randomEvent(life))  # start random events
    
    while not rocket_task.done():
        await life.consume_oxygen(2)
        await life.regulate_temperature()
        await life.status()
    
    # Stop animation and random events
    animation_task.cancel()
    random_task.cancel()
    print("Mission Complete ✅")


# Run the mission
asyncio.run(mission())

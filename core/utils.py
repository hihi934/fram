"""
This code is only made for educational and practice purposes. 
Author and Async Development are not responsible for misuse.

GhoSty OwO V4 Alpha Build
Stable Alpha Build Version: 041025.4.0.0

GitHub: https://github.com/WannaBeGhoSt
Discord: https://discord.gg/SyMJymrV8x
"""

import discord
from discord.ext import commands
from colorama import Fore, Style

ghostyop = discord.Intents.all()
GhoStyyy = "."
ghosty = commands.Bot(
    command_prefix=GhoStyyy, case_insensitive=True, self_bot=True, intents=ghostyop
)
ghosty.remove_command("help")

@ghosty.event
async def on_ready():
    print(
        f"{Fore.LIGHTRED_EX} > GhoSty OwO Farm v4 Alpha Connected To:{Style.RESET_ALL}",
        f"{Fore.LIGHTGREEN_EX}{ghosty.user}{Style.BRIGHT}{Style.RESET_ALL}",
    )
    print(f"{Fore.LIGHTRED_EX} > Major Update{Style.RESET_ALL}")
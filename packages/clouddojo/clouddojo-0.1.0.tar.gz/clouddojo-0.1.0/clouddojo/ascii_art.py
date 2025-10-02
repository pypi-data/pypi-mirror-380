#!/usr/bin/env python3
"""
ASCII Art for CloudDojo - Anime/Samurai themed branding
"""

CLOUDDOJO_BANNER = """
[bold bright_cyan]
 ██████╗██╗      ██████╗ ██╗   ██╗██████╗ ██████╗  ██████╗      ██╗ ██████╗ 
██╔════╝██║     ██╔═══██╗██║   ██║██╔══██╗██╔══██╗██╔═══██╗     ██║██╔═══██╗
██║     ██║     ██║   ██║██║   ██║██║  ██║██║  ██║██║   ██║     ██║██║   ██║
██║     ██║     ██║   ██║██║   ██║██║  ██║██║  ██║██║   ██║██   ██║██║   ██║
╚██████╗███████╗╚██████╔╝╚██████╔╝██████╔╝██████╔╝╚██████╔╝╚█████╔╝╚██████╔╝
 ╚═════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚════╝  ╚═════╝ 
[/bold bright_cyan]
[bright_red]                    ⚔️  DIGITAL SAMURAI TRAINING DOJO  ⚔️[/bright_red]
[bright_yellow]                  "Debug like a digital samurai" 🗾[/ bright_yellow]
"""

SAMURAI_SMALL = """
[bright_red]    ⚔️[/bright_red]  [bright_cyan]CloudDojo[/bright_cyan]  [bright_red]⚔️[/bright_red]
[dim]   🥷 Digital Samurai 🥷[/dim]
"""

KATANA_DIVIDER = """
[bright_red]═══════════════════════════════════════════════════════════════════════════════[/bright_red]
[bright_yellow]                              ⚔️ 🏮 ⚔️[/bright_yellow]
[bright_red]═══════════════════════════════════════════════════════════════════════════════[/bright_red]
"""

def get_banner():
    """Get the main CloudDojo banner"""
    return CLOUDDOJO_BANNER

def get_small_banner():
    """Get a smaller banner for menus"""
    return SAMURAI_SMALL

def get_divider():
    """Get decorative divider"""
    return KATANA_DIVIDER
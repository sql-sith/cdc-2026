# File name: game_utils.py

def calculate_xp(level, monsters_killed):
    """Calculates XP earned. Monsters are worth 10 XP each,
    and players get a 50 XP bonus for every level above 1."""
    return (monsters_killed * 10) + (level * 50)

def is_player_alive(health):
    """Returns True if player health is greater than 0."""
    return health >= 0

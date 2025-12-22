from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Ronin",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
)

goblin = Actor(
    char="g",
    color=(63, 127, 63),
    name="goblin",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
)

troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="troll",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
)

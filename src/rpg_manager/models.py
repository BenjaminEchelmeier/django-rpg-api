from django.db import models

# Create your models here.


class Player(models.Model):
    """A login identity containing Characters"""

    name = models.CharField()
    _is_active = models.BooleanField("is_active")


class CharacterClass(models.Model):
    """A db record of a character's class"""

    ARTIFICER = "ART"
    BARBARIAN = "BARB"
    BARD = "BARD"
    CLERIC = "CLRC"
    DRUID = "DRD"
    FIGHTER = "FTR"
    MONK = "MONK"
    PALADIN = "PLDN"
    RANGER = "RNGR"
    ROGUE = "ROG"
    SORCERER = "SORC"
    WARLOCK = "WRLK"
    WIZARD = "WZRD"

    CLASS_CHOICES = {
        ARTIFICER: "Artificer",
        BARBARIAN: "Barbarian",
        BARD: "Bard",
        CLERIC: "Cleric",
        DRUID: "Druid",
        FIGHTER: "Fighter",
        MONK: "Monk",
        PALADIN: "Paladin",
        RANGER: "Ranger",
        ROGUE: "Rogue",
        SORCERER: "Sorcerer",
        WARLOCK: "Warlock",
        WIZARD: "Wizard",
    }
    class_type = models.CharField(max_length=4, choices=CLASS_CHOICES)
    _is_primery = models.BooleanField("is_primary")
    level = models.SmallIntegerField(default=1)


class Character(models.Model):
    """A data recording of a Character, including a ref to the player, the primary class, and all secondary classes."""

    name = models.CharField()
    _is_active = models.BooleanField("is_active")
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    # primary_class = models.OneToOneField(CharacterClass, on_delete=models.CASCADE)
    level = models.SmallIntegerField(default=1)

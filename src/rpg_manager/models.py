from django.db import models
from django.forms import ValidationError

# Create your models here.


class Player(models.Model):
    """A login identity containing Characters"""

    name = models.CharField()
    _is_active = models.BooleanField("is_active")

    def __str__(self) -> str:
        return self.name

    def get_characters(self):
        chars = Character.objects.filter(player=self.id)
        return chars


class Character(models.Model):
    """A data recording of a Character, including a ref to the player, the primary class, and all secondary classes."""

    name = models.CharField()
    _is_active = models.BooleanField("is_active", default=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    # primary_class = models.OneToOneField(CharacterClass, on_delete=models.CASCADE)
    level = models.SmallIntegerField(default=0)
    primary_class = models.OneToOneField(
        "CharacterClass", on_delete=models.SET_NULL, null=True, blank=True, default=None
    )

    def get_classes(self):
        classes = CharacterClass.objects.filter(parent_character=self.id)
        return classes


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
    parent_character = models.ForeignKey(Character, on_delete=models.CASCADE)
    archived = models.BooleanField(default=False)
    class_type = models.CharField(max_length=4, choices=CLASS_CHOICES)
    _is_primary = models.BooleanField("is_primary", default=False)
    level = models.SmallIntegerField(default=1)

    def class_name(self):
        return self.CLASS_CHOICES[self.class_type]

    def is_primary(self):
        return self.parent_character.primary_class == self

    def clean(self):
        val_errs = {}
        if val_errs:
            raise ValidationError(val_errs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.parent_character.primary_class:
            self.parent_character.primary_class = self
            self.parent_character.save()

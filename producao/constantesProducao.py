from django.db import models
from django.utils.translation import gettext_lazy as _


class AdvisoryCertificate(models.TextChoices):
    GENERAL_AUDIENCES = "G", _("General Audiences")
    PARENTAL_GUIDANCE_SUGGESTED = "PG", _("Parental Guidance Suggested")
    PARENTS_STRONGLY_CAUTIONED = "PG13", _("Parents Strongly Cautioned")
    RESTRICTED = "R", _("Restricted")
    ADULTS_ONLY = "NC17", _("Adults Only")


class Genre(models.TextChoices):
    ACTION = "AC", _("Action")
    ADVENTURE = "ADV", _("Adventure")
    ANIMATION = "ANI", _("Animation")
    BIOGRAPHY = "BIO", _("Biography")
    DOCUMENTARY = "DOC", _("Documentary")
    COMEDY = "COM", _("Comedy")
    CRIME = "CRI", _("Crime")
    DRAMA = "DRM", _("Drama")
    FAMILY = "FAM", _("Family")
    FANTASY = "FNT", _("Fantasy")
    HISTORY = "HIS", _("History")
    HORROR = "HRR", _("Horror")
    MUSICAL = "MUS", _("Musical")
    MYSTERY = "MYS", _("Mystery")
    ROMANCE = "ROM", _("Romance")
    SCIENCE_FICTION = "SCIFI", _("Science Fiction")
    SHORT = "SHRT", _("Short")
    SPORT = "SPO", _("Sport")
    THRILLER = "THR", _("Thriller")
    WAR = "WR", _("War")
    WESTERN = "WST", _("Western")

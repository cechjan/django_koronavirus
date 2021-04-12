from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


def image_path(instance, filename):
    return "stat/" + str(instance.id) + "/vlajka/" + filename


class Stat(models.Model):
    nazev_statu = models.CharField(max_length=100, unique=True, verbose_name="Stát")
    zkratka_statu = models.CharField(max_length=10, verbose_name="Zkratka státu")
    vlajka = models.ImageField(upload_to=image_path, blank=True, null=True, verbose_name="Vlajka státu")
    forma_statu = models.CharField(max_length=100, verbose_name="Forma státu", null=True,
                                   blank=True)
    pocet_obyvatel = models.IntegerField(verbose_name="Počet obyvatel", null=True, blank=True,
                                         validators=[MinValueValidator(1)])
    rozloha = models.FloatField(verbose_name="Rozloha v km čtverečních", null=True, blank=True,
                                validators=[MinValueValidator(0.1)])
    text = models.TextField(verbose_name="O státu", null=True, blank=True)

    class Meta:
        ordering = ["nazev_statu"]

    def __str__(self):
        return self.nazev_statu


class Nakazeni(models.Model):
    stat = models.ManyToManyField(Stat, help_text="Vyberte stát")
    # stat = models.OneToOneField(Stat, help_text="Vyberte stát", on_delete=models.CASCADE)
    # obyvatele = models.ForeignKey(Stat.pocet_obyvatel, on_delete=models.CASCADE)
    pocet_nakazenych = models.IntegerField(verbose_name="Počet nakažených",
                                           validators=[MinValueValidator(0)
                                                       # MaxValueValidator(obyvatele)
                                                       ])
    pocet_umrti = models.IntegerField(verbose_name="Počet úmrtí",
                                      validators=[MinValueValidator(0)
                                                  # MaxValueValidator(obyvatele)
                                                  ])
    datum = models.DateField(auto_now=True)

    # def nakazenych_na_sto_tis(self):
    #     return (self.pocet_nakazenych / Stat.pocet_obyvatel) * 100000

    class Meta:
        # ordering = ["pocet_nakazenych", "stat"]
        ordering = ["pocet_nakazenych"]

    def __str__(self):
        return f"{self.stat}, {self.pocet_nakazenych} nakažených"


class Naockovani(models.Model):
    stat = models.ManyToManyField(Stat, help_text="Vyberte stát")
    # stat = models.OneToOneField(Stat, help_text="Vyberte stát", on_delete=models.CASCADE)
    # obyvatele = models.ForeignKey(Stat.pocet_obyvatel, on_delete=models.CASCADE)
    pocet_naockovanych = models.IntegerField(verbose_name="Počet naočkovaných",
                                             validators=[MinValueValidator(0)
                                                         # MaxValueValidator(obyvatele)
                                                         ])
    pocet_umrti_po_ockovani = models.IntegerField(verbose_name="Počet umrtí po očkování", null=True, blank=True,
                                                  validators=[MinValueValidator(0)
                                                              # MaxValueValidator(obyvatele)
                                                              ])

    VAKCINY = (
        ('pfizer-biontech', 'Pfizer-BioNTech'),
        ('moderna', 'Moderna'),
        ('johnson-&-johnson', 'Johnson & Johnson'),
        ('astrazeneca', 'AstraZeneca'),
        ('novavax', 'Novavax'),
        ('sputnik-v', 'Sputnik V'),
        ('sinovac-biotech', 'Sinovac Biotech'),
        ('jine', 'jiné'),
    )

    dominantni_vakcina = models.CharField(max_length=40, choices=VAKCINY, blank=True,
                                          help_text='Vyberte dominantní vakcínu', verbose_name="Dominantní vakcína")
    datum = models.DateField(auto_now=True)

    # def naockovani_na_sto_tis(self):
    #     return (self.pocet_naockovanych / self.obyvatele) * 100000

    class Meta:
        # ordering = ["pocet_naockovanych", "stat"]
        ordering = ["pocet_naockovanych"]

    def __str__(self):
        return f"{self.stat}, {self.pocet_naockovanych} naočkovaných"

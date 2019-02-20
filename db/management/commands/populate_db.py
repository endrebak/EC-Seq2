from django.core.management.base import BaseCommand

from db.models import Gene

import pandas as pd


class Command(BaseCommand):

    help = "Fill database with data."


    def add_arguments(self, parser):

        parser.add_argument('--toptable-file', type=str)


    def handle(self, *args, **options):

        f = options["toptable_file"]
        df = pd.read_csv(f, sep=" ")
        df.columns = ["name"] + list(df.columns)[1:]

        Gene.objects.all().delete()

        for i, (_, gene )in enumerate(df.iterrows()):

            # if i % 10000 ==

            g = Gene()

            for k, v in gene.items():
                setattr(g, k, v)

            g.save()

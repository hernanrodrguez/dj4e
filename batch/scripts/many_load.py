import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, State, Region, Iso


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()

    for row in reader:
        print(row)

        cat, created = Category.objects.get_or_create(name=row[7])
        sta, created = State.objects.get_or_create(name=row[8])
        reg, created = Region.objects.get_or_create(name=row[9])
        iso, created = Iso.objects.get_or_create(name=row[10])

        n = row[0]

        try:
            d = row[1]
        except:
            d = ""

        try:
            y = int(row[3])
        except:
            y = None

        try:
            l = int(row[4])
        except:
            l = None

        try:
            la = int(row[5])
        except:
            la = None

        try:
            ah = int(row[6])
        except:
            ah = None

        try:
            j = row[2]
        except:
            j = ""



        site = Site(name=n,
                    year=y,
                    longitude=l,
                    latitude=la,
                    area_hectares=ah,
                    description=d,
                    justification=j,
                    category=cat,
                    state=sta,
                    region=reg,
                    iso=iso)

        site.save()

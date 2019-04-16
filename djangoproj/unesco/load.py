import csv
# from django.core.exceptions import ObjectDoesNotExist
from unesco.models import Site, Category, Region, States, Iso

fh = open('unesco/whc-sites-2018-small.csv')
rows = list(csv.reader(fh))
# print(type(rows[1:3]))
i = 0
for row in rows[1:]:
    if len(row[0]) < 1 : continue
    print('------------------------------------')
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])
    print(row[5])
    print(row[6])
    print(row[7])
    print(row[8])
    print(row[9])
    print(row[10])
    # i = i + 1
    # if i > 5 : break

Site.objects.all().delete()
Category.objects.all().delete()
Region.objects.all().delete()
States.objects.all().delete()
Iso.objects.all().delete()


for row in rows[1:]:
    print(row)

    try:
        c = Category.objects.get(name=row[7])
    except:
        print("Inserting category",row[7])
        c = Category(name=row[7])
        c.save()

    try:
        s = States.objects.get(name=row[8])
    except:
        print("Inserting states",row[8])
        s = States(name=row[8])
        s.save()

    try:
        r = Region.objects.get(name=row[9])
    except:
        print("Inserting region",row[9])
        r = Region(name=row[9])
        r.save()

    try:
        i = Iso.objects.get(name=row[10])
    except:
        print("Inserting iso",row[10])
        i = Iso(name=row[10])
        i.save()

    try:
        area = float(row[6])
    except:
        area = None

    site = Site(name=row[0], description=row[1], justification=row[2], year=row[3], longitude=row[4], latitude=row[5], area_hectares=area, category=c, states=s, region=r, iso=i)
    site.save()

from django.db import migrations


def set_rarity(apps, schema_editor):
    item_model = apps.get_model('main_app', 'Item')
    items = item_model.objects.all()

    for item in items:
        if item.price <= 10:
            item.rarity = 'Rare'

        elif 10 < item.price <= 20:
            item.rarity = 'Very Rare'

        elif 20 < item.price <= 30:
            item.rarity = 'Extremely'

        else:
            item.rarity = 'Mega Rare'

    item_model.objects.bulk_update(items, ['rarity'])


def set_rarity_default(apps, schema_editor):
    item_model = apps.get_model('main_app', 'Item')
    items = item_model.objects.all()

    default_rarity = item_model._meta.get_field('rarity').default

    for item in items:
        item.rarity = default_rarity

    item_model.objects.bulk_update(items, ['rarity'])


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_item'),
    ]

    operations = [
        migrations.RunPython(set_rarity, reverse_code=set_rarity_default)
    ]

from django.db import migrations


def create_unique_brands(apps, schema_editor):
    shoe = apps.get_model("main_app", "Shoe")
    unique_brands = apps.get_model("main_app", "UniqueBrands")

    db_alias = schema_editor.connection.alias

    unique_brands_names = shoe.objects.values_list('brand', flat=True).distinct()

    for brand_name in unique_brands_names:
        unique_brands.objects.using(db_alias).create(brand_name=brand_name)


def delete_unique_brands(apps, schema_editor):
    unique_brands = apps.get_model("main_app", "UniqueBrands")

    unique_brands.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_uniquebrands'),
    ]

    operations = [
        migrations.RunPython(create_unique_brands, reverse_code=delete_unique_brands)
    ]

# Generated by Django 3.1.1 on 2020-11-20 01:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0023_auto_20201116_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgcapacityopp',
            name='capacity_domain',
            field=models.CharField(choices=[('Media', 'اﻹعلام و المناصرة'), ('Education', 'تعليم'), ('Protection', 'حماية و الصحة النفسية'), ('Livelihoods and food security', 'سبل العيش واﻷمن الغذائي'), ('Project of clean ,water, sanitation ', 'النظافة والمياه والصرف الصحي'), ('Development', 'تنمية و بناء قدرات و ثقافة'), ('Law, suport, policy', 'المواطنة و الحوكمة و الديموقراطية و السلام و السياسة'), ('Donors and support volunteering', 'اﻷسرة و الجندرة و قضايا المرأة'), ('Religious org', 'المأوى و البنة التحتية'), ('Prof association and assembles', 'تنسيق و تجمعات المجتمع المدني'), ('Health', 'صحة'), ('Studies and research', 'دراسات وأبحاث'), ('Other', 'أخرى')], max_length=255, verbose_name='قطاع الفرصة'),
        ),
        migrations.AlterField(
            model_name='orgfundingopp',
            name='work_domain',
            field=models.CharField(choices=[('Media', 'اﻹعلام و المناصرة'), ('Education', 'تعليم'), ('Protection', 'حماية و الصحة النفسية'), ('Livelihoods and food security', 'سبل العيش واﻷمن الغذائي'), ('Project of clean ,water, sanitation ', 'النظافة والمياه والصرف الصحي'), ('Development', 'تنمية و بناء قدرات و ثقافة'), ('Law, suport, policy', 'المواطنة و الحوكمة و الديموقراطية و السلام و السياسة'), ('Donors and support volunteering', 'اﻷسرة و الجندرة و قضايا المرأة'), ('Religious org', 'المأوى و البنة التحتية'), ('Prof association and assembles', 'تنسيق و تجمعات المجتمع المدني'), ('Health', 'صحة'), ('Studies and research', 'دراسات وأبحاث'), ('Other', 'أخرى')], max_length=255, verbose_name='قطاع المنحة'),
        ),
        migrations.AlterField(
            model_name='orgjob',
            name='job_domain',
            field=models.CharField(choices=[('Media', 'اﻹعلام و المناصرة'), ('Education', 'تعليم'), ('Protection', 'حماية و الصحة النفسية'), ('Livelihoods and food security', 'سبل العيش واﻷمن الغذائي'), ('Project of clean ,water, sanitation ', 'النظافة والمياه والصرف الصحي'), ('Development', 'تنمية و بناء قدرات و ثقافة'), ('Law, suport, policy', 'المواطنة و الحوكمة و الديموقراطية و السلام و السياسة'), ('Donors and support volunteering', 'اﻷسرة و الجندرة و قضايا المرأة'), ('Religious org', 'المأوى و البنة التحتية'), ('Prof association and assembles', 'تنسيق و تجمعات المجتمع المدني'), ('Health', 'صحة'), ('Studies and research', 'دراسات وأبحاث'), ('Other', 'أخرى')], max_length=255, verbose_name='مجال العمل'),
        ),
        migrations.AlterField(
            model_name='orgprofile',
            name='message',
            field=models.TextField(default=django.utils.timezone.now, max_length=2000, verbose_name='الرؤية و الرسالة'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orgprofile',
            name='work_domain',
            field=models.CharField(choices=[('Media', 'اﻹعلام و المناصرة'), ('Education', 'تعليم'), ('Protection', 'حماية و الصحة النفسية'), ('Livelihoods and food security', 'سبل العيش واﻷمن الغذائي'), ('Project of clean ,water, sanitation ', 'النظافة والمياه والصرف الصحي'), ('Development', 'تنمية و بناء قدرات و ثقافة'), ('Law, suport, policy', 'المواطنة و الحوكمة و الديموقراطية و السلام و السياسة'), ('Donors and support volunteering', 'اﻷسرة و الجندرة و قضايا المرأة'), ('Religious org', 'المأوى و البنة التحتية'), ('Prof association and assembles', 'تنسيق و تجمعات المجتمع المدني'), ('Health', 'صحة'), ('Studies and research', 'دراسات وأبحاث'), ('Other', 'أخرى')], max_length=255, verbose_name='مجال العمل'),
        ),
        migrations.AlterField(
            model_name='orgrapport',
            name='domain',
            field=models.CharField(choices=[('Media', 'اﻹعلام و المناصرة'), ('Education', 'تعليم'), ('Protection', 'حماية و الصحة النفسية'), ('Livelihoods and food security', 'سبل العيش واﻷمن الغذائي'), ('Project of clean ,water, sanitation ', 'النظافة والمياه والصرف الصحي'), ('Development', 'تنمية و بناء قدرات و ثقافة'), ('Law, suport, policy', 'المواطنة و الحوكمة و الديموقراطية و السلام و السياسة'), ('Donors and support volunteering', 'اﻷسرة و الجندرة و قضايا المرأة'), ('Religious org', 'المأوى و البنة التحتية'), ('Prof association and assembles', 'تنسيق و تجمعات المجتمع المدني'), ('Health', 'صحة'), ('Studies and research', 'دراسات وأبحاث'), ('Other', 'أخرى')], max_length=150, verbose_name='مجال التقرير'),
        ),
        migrations.AlterField(
            model_name='orgresearch',
            name='domaine',
            field=models.CharField(choices=[('Media', 'اﻹعلام و المناصرة'), ('Education', 'تعليم'), ('Protection', 'حماية و الصحة النفسية'), ('Livelihoods and food security', 'سبل العيش واﻷمن الغذائي'), ('Project of clean ,water, sanitation ', 'النظافة والمياه والصرف الصحي'), ('Development', 'تنمية و بناء قدرات و ثقافة'), ('Law, suport, policy', 'المواطنة و الحوكمة و الديموقراطية و السلام و السياسة'), ('Donors and support volunteering', 'اﻷسرة و الجندرة و قضايا المرأة'), ('Religious org', 'المأوى و البنة التحتية'), ('Prof association and assembles', 'تنسيق و تجمعات المجتمع المدني'), ('Health', 'صحة'), ('Studies and research', 'دراسات وأبحاث'), ('Other', 'أخرى')], max_length=150, verbose_name='مجال البحث'),
        ),
        migrations.AlterField(
            model_name='persfundingopp',
            name='domain',
            field=models.CharField(blank=True, choices=[('Media', 'اﻹعلام و المناصرة'), ('Education', 'تعليم'), ('Protection', 'حماية و الصحة النفسية'), ('Livelihoods and food security', 'سبل العيش واﻷمن الغذائي'), ('Project of clean ,water, sanitation ', 'النظافة والمياه والصرف الصحي'), ('Development', 'تنمية و بناء قدرات و ثقافة'), ('Law, suport, policy', 'المواطنة و الحوكمة و الديموقراطية و السلام و السياسة'), ('Donors and support volunteering', 'اﻷسرة و الجندرة و قضايا المرأة'), ('Religious org', 'المأوى و البنة التحتية'), ('Prof association and assembles', 'تنسيق و تجمعات المجتمع المدني'), ('Health', 'صحة'), ('Studies and research', 'دراسات وأبحاث'), ('Other', 'أخرى')], max_length=255, null=True, verbose_name='قطاع المنحة'),
        ),
    ]

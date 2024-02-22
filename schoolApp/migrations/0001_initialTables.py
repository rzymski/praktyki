# Generated by Django 5.0.1 on 2024-01-09 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.CharField(db_column='idPrzedmiot', max_length=4, primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='Nazwa')),
                ('profession', models.IntegerField(blank=True, db_column='Zawodowe', null=True)),
            ],
            options={
                'db_table': 'Przedmiot',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetailStudent',
            fields=[
                ('studentIndex', models.CharField(db_column='Uczen_Indeks', max_length=9, primary_key=True, serialize=False)),
                ('rspo', models.IntegerField(blank=True, db_column='RSPO', null=True)),
                ('birthDate', models.DateField(blank=True, db_column='Data_urodzenia', null=True)),
                ('birthPlace', models.CharField(blank=True, db_column='Miejsce_urodzenia', max_length=30, null=True)),
                ('town', models.CharField(blank=True, db_column='Miejscowosc', max_length=30, null=True)),
                ('street', models.CharField(blank=True, db_column='Ulica', max_length=30, null=True)),
                ('houseNumber', models.CharField(blank=True, db_column='Numer_domu', max_length=5, null=True)),
                ('apartmentNumber', models.CharField(blank=True, db_column='Numer_mieszkania', max_length=3, null=True)),
                ('zipCode', models.CharField(blank=True, db_column='Kod_pocztowy', max_length=6, null=True)),
                ('phone', models.IntegerField(blank=True, db_column='Telefon', null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=60, null=True)),
                ('laptopContract', models.CharField(blank=True, db_column='Umowa_na_laptop', max_length=11, null=True)),
                ('religion', models.CharField(blank=True, db_column='Religia', max_length=2, null=True)),
                ('wdzResignation', models.CharField(blank=True, db_column='Rezygnacja_z_WDZ', max_length=4, null=True)),
                ('decision', models.TextField(blank=True, db_column='Orzeczenie/opinia', null=True)),
                ('diseases', models.TextField(blank=True, db_column='Choroby/alergie', null=True)),
                ('disciplinaryNotes', models.TextField(blank=True, db_column='Uwagi', null=True)),
                ('resignationReason', models.TextField(blank=True, db_column='Powod_odejscia', null=True)),
                ('motherName', models.CharField(blank=True, db_column='Imie_matki', max_length=30, null=True)),
                ('motherSurname', models.CharField(blank=True, db_column='Nazwisko_matki', max_length=30, null=True)),
                ('motherEmail', models.CharField(blank=True, db_column='Email_matki', max_length=60, null=True)),
                ('motherPhone', models.IntegerField(blank=True, db_column='Telefon_matki', null=True)),
                ('fatherName', models.CharField(blank=True, db_column='Imie_ojca', max_length=30, null=True)),
                ('fatherSurname', models.CharField(blank=True, db_column='Nazwisko_ojca', max_length=30, null=True)),
                ('fatherEmail', models.CharField(blank=True, db_column='Email_ojca', max_length=60, null=True)),
                ('fatherPhone', models.IntegerField(blank=True, db_column='Telefon_ojca', null=True)),
                ('matura', models.CharField(blank=True, db_column='Matura', max_length=1, null=True)),
                ('osm_gim', models.CharField(blank=True, db_column='Osm/gim', max_length=1, null=True)),
                ('actualizationDate', models.DateField(blank=True, db_column='Data_aktualizacji', null=True)),
            ],
            options={
                'db_table': 'Dane_szczegolowe_ucznia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetailStudentArchive',
            fields=[
                ('id', models.IntegerField(db_column='id', max_length=11, primary_key=True, serialize=False)),
                ('studentIndex', models.CharField(db_column='Dane_szczegolowe_Uczen_Indeks', max_length=9)),
                ('rspo', models.IntegerField(blank=True, db_column='RSPO', null=True)),
                ('birthDate', models.DateField(blank=True, db_column='Data_urodzenia', null=True)),
                ('birthPlace', models.CharField(blank=True, db_column='Miejsce_urodzenia', max_length=30, null=True)),
                ('town', models.CharField(blank=True, db_column='Miejscowosc', max_length=30, null=True)),
                ('street', models.CharField(blank=True, db_column='Ulica', max_length=30, null=True)),
                ('houseNumber', models.CharField(blank=True, db_column='Numer_domu', max_length=5, null=True)),
                ('apartmentNumber', models.IntegerField(blank=True, db_column='Numer_mieszkania', null=True)),
                ('zipCode', models.CharField(blank=True, db_column='Kod_pocztowy', max_length=6, null=True)),
                ('phone', models.IntegerField(blank=True, db_column='Telefon', null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=60, null=True)),
                ('laptopContract', models.CharField(blank=True, db_column='Umowa_na_laptop', max_length=11, null=True)),
                ('religion', models.CharField(blank=True, db_column='Religia', max_length=2, null=True)),
                ('wdzResignation', models.CharField(blank=True, db_column='Rezygnacja_z_WDZ', max_length=4, null=True)),
                ('decision', models.TextField(blank=True, db_column='Orzeczenie/opinia', null=True)),
                ('diseases', models.TextField(blank=True, db_column='Choroby/alergie', null=True)),
                ('disciplinaryNotes', models.TextField(blank=True, db_column='Uwagi', null=True)),
                ('resignationReason', models.TextField(blank=True, db_column='Powod_odejscia', null=True)),
                ('motherName', models.CharField(blank=True, db_column='Imie_matki', max_length=30, null=True)),
                ('motherSurname', models.CharField(blank=True, db_column='Nazwisko_matki', max_length=30, null=True)),
                ('motherEmail', models.CharField(blank=True, db_column='Email_matki', max_length=60, null=True)),
                ('motherPhone', models.IntegerField(blank=True, db_column='Telefon_matki', null=True)),
                ('fatherName', models.CharField(blank=True, db_column='Imie ojca', max_length=30, null=True)),
                ('fatherSurname', models.CharField(blank=True, db_column='Nazwisko_ojca', max_length=30, null=True)),
                ('fatherEmail', models.CharField(blank=True, db_column='Email_ojca', max_length=60, null=True)),
                ('fatherPhone', models.IntegerField(blank=True, db_column='Telefon_ojca', null=True)),
                ('matura', models.CharField(blank=True, db_column='Matura', max_length=1, null=True)),
                ('osm_gim', models.CharField(blank=True, db_column='Osm/gim', max_length=1, null=True)),
                ('actualizationDate', models.DateField(blank=True, db_column='Data_aktualizacji', null=True)),
            ],
            options={
                'db_table': 'Dane_archiwalne_ucznia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Exam8Class',
            fields=[
                ('id', models.IntegerField(db_column='id', max_length=11, primary_key=True, serialize=False)),
                ('polish', models.IntegerField(db_column='Jezyk_polski')),
                ('mathematics', models.IntegerField(db_column='Matematyka')),
                ('english', models.IntegerField(db_column='Jezyk_angielski')),
            ],
            options={
                'db_table': 'Egz_osmoklasisty',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExamJunior',
            fields=[
                ('id', models.IntegerField(db_column='id', max_length=11, primary_key=True, serialize=False)),
                ('polish', models.IntegerField(db_column='Jezyk_polski')),
                ('historyAndWos', models.IntegerField(db_column='HistoriaiWOS')),
                ('mathematics', models.IntegerField(db_column='Matematyka')),
                ('naturalScience', models.IntegerField(db_column='Przyrodnicze')),
                ('foreignLanguageBasic', models.IntegerField(db_column='Jezyk_obcy_podst')),
                ('foreignLanguageExtend', models.IntegerField(db_column='Jezyk_obcy_roz')),
            ],
            options={
                'db_table': 'Egz_gimnazjalny',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExamProfession',
            fields=[
                ('id', models.IntegerField(db_column='id', max_length=11, primary_key=True, serialize=False)),
                ('inf03_pis', models.IntegerField(db_column=' INF03_pis')),
                ('inf03_pis_popr', models.IntegerField(blank=True, db_column='INF03_pis_popr', null=True)),
                ('inf03_pr', models.IntegerField(db_column='INF03_pr')),
                ('inf03_pr_popr', models.IntegerField(blank=True, db_column='INF03_pr_popr', null=True)),
                ('inf04_pis', models.IntegerField(db_column='INF04_pis')),
                ('inf04_pis_popr', models.IntegerField(blank=True, db_column='INF04_pis_popr', null=True)),
                ('inf04_pr', models.IntegerField(db_column='INF04_pr')),
                ('inf04_pr_popr', models.IntegerField(blank=True, db_column='INF04_pr_popr', null=True)),
            ],
            options={
                'db_table': 'Egz_zawodowy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.IntegerField(db_column='id', max_length=11, primary_key=True, serialize=False)),
                ('semester', models.IntegerField(db_column='Semestr')),
                ('legitimate', models.IntegerField(blank=True, db_column='Usprawiedliwione', null=True)),
                ('illegitimate', models.IntegerField(blank=True, db_column='Nieusprawiedliwione', null=True)),
                ('lateAttendance', models.IntegerField(blank=True, db_column='Spoznienia', null=True)),
                ('attendance', models.IntegerField(blank=True, db_column='Obecny', null=True)),
            ],
            options={
                'db_table': 'Frekwencja',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.IntegerField(db_column='ID_oceny', primary_key=True, serialize=False)),
                ('semester', models.IntegerField(db_column='Semestr')),
                ('grade', models.IntegerField(db_column='Ocena')),
            ],
            options={
                'db_table': 'Oceny',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.IntegerField(db_column='Id_prowadzacego', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Prowadzacy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Matura',
            fields=[
                ('id', models.IntegerField(db_column='id', max_length=11, primary_key=True, serialize=False)),
                ('polishBasic', models.IntegerField(db_column='Jezyk_polski_podst')),
                ('englishBasic', models.IntegerField(db_column='Jezyk_angielski_podst')),
                ('mathematicsBasic', models.IntegerField(db_column='Matematyka_podst')),
                ('englishExtended', models.IntegerField(blank=True, db_column='Jezyk_angielski_roz', null=True)),
                ('englishSpeakingExam', models.IntegerField(blank=True, db_column='Jezyk_angielski_ustny', null=True)),
                ('polishSpeakingExam', models.IntegerField(blank=True, db_column='Jezyk_polski_ustny', null=True)),
                ('mathematicsExtended', models.IntegerField(blank=True, db_column='Matematyka_roz', null=True)),
                ('historyExtended', models.IntegerField(blank=True, db_column='Historia_roz', null=True)),
                ('computerScienceExtended', models.IntegerField(blank=True, db_column='Informatyka_roz', null=True)),
            ],
            options={
                'db_table': 'Matura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.CharField(db_column='ID_szkoly', max_length=1, primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='Nazwa')),
                ('street', models.CharField(blank=True, db_column='Ulica', max_length=30, null=True)),
                ('schoolNumber', models.CharField(blank=True, db_column='Numer', max_length=5, null=True)),
                ('zipCode', models.CharField(blank=True, db_column='Kod_pocztowy', max_length=6, null=True)),
                ('town', models.CharField(blank=True, db_column='Miejscowosc', max_length=30, null=True)),
            ],
            options={
                'db_table': 'Szkola',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.CharField(db_column='ID_klasy', max_length=4, primary_key=True, serialize=False)),
                ('year', models.IntegerField(db_column='Rok')),
                ('actualClass', models.IntegerField(blank=True, db_column='Aktualna_klasa', null=True)),
            ],
            options={
                'db_table': 'Klasa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('index', models.CharField(db_column='Indeks', max_length=9, primary_key=True, serialize=False)),
                ('pesel', models.CharField(db_column='PESEL', max_length=11, unique=True)),
                ('surname', models.CharField(blank=True, db_column='Nazwisko', max_length=30, null=True)),
                ('name', models.CharField(blank=True, db_column='Imie', max_length=20, null=True)),
                ('secondName', models.CharField(blank=True, db_column='Drugie_imie', max_length=20, null=True)),
                ('sex', models.CharField(blank=True, db_column='Plec', max_length=1, null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=10, null=True)),
                ('specialization', models.CharField(blank=True, db_column='Specjalizacja', max_length=35, null=True)),
                ('actualizationDate', models.DateField(blank=True, db_column='Data_aktualizacji', null=True)),
            ],
            options={
                'db_table': 'Uczen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentArchive',
            fields=[
                ('id', models.IntegerField(db_column='id', max_length=11, primary_key=True, serialize=False)),
                ('pesel', models.CharField(db_column='PESEL', max_length=11, unique=True)),
                ('surname', models.CharField(blank=True, db_column='Nazwisko', max_length=30, null=True)),
                ('name', models.CharField(blank=True, db_column='Imie', max_length=20, null=True)),
                ('secondName', models.CharField(blank=True, db_column='Drugie_imie', max_length=20, null=True)),
                ('sex', models.CharField(blank=True, db_column='Plec', max_length=1, null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=10, null=True)),
                ('specialization', models.CharField(blank=True, db_column='Specjalizacja', max_length=35, null=True)),
                ('actualizationDate', models.DateField(blank=True, db_column='Data_aktualizacji', null=True)),
            ],
            options={
                'db_table': 'Uczen_archival',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.CharField(db_column='Id_grupy', max_length=6, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Grupa_uczniow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClassHasSubject',
            fields=[
                ('subject', models.OneToOneField(db_column='Przedmiot_idPrzedmiot', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='schoolApp.subject')),
            ],
            options={
                'db_table': 'Przedmiot_has_Klasa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GradeSubjectLeader',
            fields=[
                ('grade', models.OneToOneField(db_column='Oceny_ID_oceny', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='schoolApp.grade')),
            ],
            options={
                'db_table': 'Ocena_przedmiot_prowadzacy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('leader', models.OneToOneField(db_column='Prowadzacy_Id_prowadzacego', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='schoolApp.leader')),
                ('surname', models.CharField(db_column='Nazwisko', max_length=30)),
                ('name', models.CharField(db_column='Imie', max_length=20)),
                ('secondName', models.CharField(blank=True, db_column='Drugie_imie', max_length=20, null=True)),
                ('pedagogue', models.IntegerField(blank=True, db_column='Pedagog/psycholog', null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=10, null=True)),
            ],
            options={
                'db_table': 'Nauczyciel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TeacherGroup',
            fields=[
                ('leader', models.OneToOneField(db_column='Prowadzacy_Id_prowadzacego', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='schoolApp.leader')),
                ('id_teacher1', models.IntegerField(blank=True, db_column='Id_nauczyciela1', null=True)),
                ('id_teacher2', models.IntegerField(blank=True, db_column='Id_nauczyciela2', null=True)),
                ('id_teacher3', models.IntegerField(blank=True, db_column='Id_nauczyciela3', null=True)),
                ('id_teacher4', models.IntegerField(blank=True, db_column='Id_nauczyciela4', null=True)),
            ],
            options={
                'db_table': 'Grupa_nauczycieli',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudientHasGroup',
            fields=[
                ('index', models.OneToOneField(db_column='Uczen_Indeks', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='schoolApp.student')),
            ],
            options={
                'db_table': 'Uczen_has_Grupa',
                'managed': False,
            },
        ),
    ]
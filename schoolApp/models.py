from django.db import models


class School(models.Model):
    id = models.CharField(db_column='ID_szkoly', primary_key=True, max_length=1)  # Field name made lowercase.
    name = models.TextField(db_column='Nazwa')  # Field name made lowercase.
    street = models.CharField(db_column='Ulica', max_length=30, blank=True, null=True)  # Field name made lowercase.
    schoolNumber = models.CharField(db_column='Numer', max_length=5, blank=True, null=True)  # Field name made lowercase.
    zipCode = models.CharField(db_column='Kod_pocztowy', max_length=6, blank=True, null=True)  # Field name made lowercase.
    town = models.CharField(db_column='Miejscowosc', max_length=30, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"id={self.id} {self.name} nr.{self.schoolNumber} w {self.town} ul.{self.street} kod: {self.zipCode}"

    class Meta:
        managed = False
        db_table = 'Szkola'


class SchoolClass(models.Model):
    id = models.CharField(db_column='ID_klasy', primary_key=True, max_length=4)  # Field name made lowercase. The composite primary key (ID_klasy, Szkola_ID_szkoly) found, that is not supported. The first column is selected.
    year = models.IntegerField(db_column='Rok')  # Field name made lowercase.
    school = models.ForeignKey(School, on_delete=models.CASCADE, db_column='Szkola_ID_szkoly')  # Field name made lowercase.
    actualClass = models.IntegerField(db_column='Aktualna_klasa', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"Klasa id={self.id} nr. klasy={self.actualClass} z roku {self.year} "

    class Meta:
        managed = False
        db_table = 'Klasa'
        unique_together = (('id', 'actualClass'),)


class Student(models.Model):
    index = models.CharField(db_column='Indeks', primary_key=True, max_length=9)  # Field name made lowercase. The composite primary key (Indeks, Klasa_ID_klasy) found, that is not supported. The first column is selected.
    pesel = models.CharField(db_column='PESEL', unique=True, max_length=11)  # Field name made lowercase.
    surname = models.CharField(db_column='Nazwisko', max_length=30, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Imie', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondName = models.CharField(db_column='Drugie_imie', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Plec', max_length=1, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    specialization = models.CharField(db_column='Specjalizacja', max_length=35, blank=True, null=True)  # Field name made lowercase.
    actualizationDate = models.DateField(db_column='Data_aktualizacji', blank=True, null=True)  # Field name made lowercase.
    schoolClass = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, db_column='Klasa_ID_klasy')  # Field name made lowercase.

    def __str__(self):
        return f"{self.name} {self.surname} indx={self.index} pesel={self.pesel}"

    class Meta:
        managed = False
        db_table = 'Uczen'
        unique_together = (('index', 'schoolClass'),)


class StudentArchive(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    index = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='Uczen_Indeks')  # Field name made lowercase.
    pesel = models.CharField(db_column='PESEL', unique=True, max_length=11)  # Field name made lowercase.
    surname = models.CharField(db_column='Nazwisko', max_length=30, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Imie', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondName = models.CharField(db_column='Drugie_imie', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Plec', max_length=1, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    specialization = models.CharField(db_column='Specjalizacja', max_length=35, blank=True, null=True)  # Field name made lowercase.
    actualizationDate = models.DateField(db_column='Data_aktualizacji', blank=True, null=True)  # Field name made lowercase.
    schoolClass = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, db_column='Klasa_ID_klasy')  # Field name made lowercase.

    def __str__(self):
        return f"ARCHIVE: {self.name} {self.surname} indx={self.index} pesel={self.pesel}"

    class Meta:
        managed = False
        db_table = 'Uczen_archival'


class DetailStudent(models.Model):
    studentIndex = models.OneToOneField(Student, db_column='Uczen_Indeks', on_delete=models.CASCADE, primary_key=True, related_name='details')
    # studentIndex = models.CharField(db_column='Uczen_Indeks', primary_key=True, max_length=9)  # Field name made lowercase.
    rspo = models.IntegerField(db_column='RSPO', blank=True, null=True)  # Field name made lowercase.
    birthDate = models.DateField(db_column='Data_urodzenia', blank=True, null=True)  # Field name made lowercase.
    birthPlace = models.CharField(db_column='Miejsce_urodzenia', max_length=30, blank=True, null=True)  # Field name made lowercase.
    town = models.CharField(db_column='Miejscowosc', max_length=30, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Ulica', max_length=30, blank=True, null=True)  # Field name made lowercase.
    houseNumber = models.CharField(db_column='Numer_domu', max_length=5, blank=True, null=True)  # Field name made lowercase.
    apartmentNumber = models.CharField(db_column='Numer_mieszkania', max_length=3, blank=True, null=True)  # Field name made lowercase.
    zipCode = models.CharField(db_column='Kod_pocztowy', max_length=6, blank=True, null=True)  # Field name made lowercase.
    phone = models.IntegerField(db_column='Telefon', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=60, blank=True, null=True)  # Field name made lowercase.
    laptopContract = models.CharField(db_column='Umowa_na_laptop', max_length=11, blank=True, null=True)  # Field name made lowercase.
    religion = models.CharField(db_column='Religia', max_length=2, blank=True, null=True)  # Field name made lowercase.
    wdzResignation = models.CharField(db_column='Rezygnacja_z_WDZ', max_length=4, blank=True, null=True)  # Field name made lowercase.
    decision = models.TextField(db_column='OrzeczenieOpinia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diseases = models.TextField(db_column='ChorobyAlergie', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    disciplinaryNotes = models.TextField(db_column='Uwagi', blank=True, null=True)  # Field name made lowercase.
    resignationReason = models.TextField(db_column='Powod_odejscia', blank=True, null=True)  # Field name made lowercase.
    motherName = models.CharField(db_column='Imie_matki', max_length=30, blank=True, null=True)  # Field name made lowercase.
    motherSurname = models.CharField(db_column='Nazwisko_matki', max_length=30, blank=True, null=True)  # Field name made lowercase.
    motherEmail = models.CharField(db_column='Email_matki', max_length=60, blank=True, null=True)  # Field name made lowercase.
    motherPhone = models.IntegerField(db_column='Telefon_matki', blank=True, null=True)  # Field name made lowercase.
    fatherName = models.CharField(db_column='Imie_ojca', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fatherSurname = models.CharField(db_column='Nazwisko_ojca', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fatherEmail = models.CharField(db_column='Email_ojca', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fatherPhone = models.IntegerField(db_column='Telefon_ojca', blank=True, null=True)  # Field name made lowercase.
    matura = models.CharField(db_column='Matura', max_length=1, blank=True, null=True)  # Field name made lowercase.
    osm_gim = models.CharField(db_column='OsmGim', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actualizationDate = models.DateField(db_column='Data_aktualizacji', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"Detail: {self.birthDate} {self.birthPlace} {self.town} {self.phone}..."

    class Meta:
        managed = False
        db_table = 'Dane_szczegolowe_ucznia'


class DetailStudentArchive(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    studentIndex = models.ForeignKey(DetailStudent, db_column='Dane_szczegolowe_Uczen_Indeks', on_delete=models.CASCADE)
    #studentIndex = models.CharField(db_column='Dane_szczegolowe_Uczen_Indeks', max_length=9)  # Field name made lowercase.
    rspo = models.IntegerField(db_column='RSPO', blank=True, null=True)  # Field name made lowercase.
    birthDate = models.DateField(db_column='Data_urodzenia', blank=True, null=True)  # Field name made lowercase.
    birthPlace = models.CharField(db_column='Miejsce_urodzenia', max_length=30, blank=True, null=True)  # Field name made lowercase.
    town = models.CharField(db_column='Miejscowosc', max_length=30, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Ulica', max_length=30, blank=True, null=True)  # Field name made lowercase.
    houseNumber = models.CharField(db_column='Numer_domu', max_length=5, blank=True, null=True)  # Field name made lowercase.
    apartmentNumber = models.IntegerField(db_column='Numer_mieszkania', blank=True, null=True)  # Field name made lowercase.
    zipCode = models.CharField(db_column='Kod_pocztowy', max_length=6, blank=True, null=True)  # Field name made lowercase.
    phone = models.IntegerField(db_column='Telefon', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=60, blank=True, null=True)  # Field name made lowercase.
    laptopContract = models.CharField(db_column='Umowa_na_laptop', max_length=11, blank=True, null=True)  # Field name made lowercase.
    religion = models.CharField(db_column='Religia', max_length=2, blank=True, null=True)  # Field name made lowercase.
    wdzResignation = models.CharField(db_column='Rezygnacja_z_WDZ', max_length=4, blank=True, null=True)  # Field name made lowercase.
    decision = models.TextField(db_column='OrzeczenieOpinia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diseases = models.TextField(db_column='ChorobyAlergie', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    disciplinaryNotes = models.TextField(db_column='Uwagi', blank=True, null=True)  # Field name made lowercase.
    resignationReason = models.TextField(db_column='Powod_odejscia', blank=True, null=True)  # Field name made lowercase.
    motherName = models.CharField(db_column='Imie_matki', max_length=30, blank=True, null=True)  # Field name made lowercase.
    motherSurname = models.CharField(db_column='Nazwisko_matki', max_length=30, blank=True, null=True)  # Field name made lowercase.
    motherEmail = models.CharField(db_column='Email_matki', max_length=60, blank=True, null=True)  # Field name made lowercase.
    motherPhone = models.IntegerField(db_column='Telefon_matki', blank=True, null=True)  # Field name made lowercase.
    fatherName = models.CharField(db_column='Imie_ojca', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fatherSurname = models.CharField(db_column='Nazwisko_ojca', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fatherEmail = models.CharField(db_column='Email_ojca', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fatherPhone = models.IntegerField(db_column='Telefon_ojca', blank=True, null=True)  # Field name made lowercase.
    matura = models.CharField(db_column='Matura', max_length=1, blank=True, null=True)  # Field name made lowercase.
    osm_gim = models.CharField(db_column='OsmGim', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actualizationDate = models.DateField(db_column='Data_aktualizacji', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"Detail ARCHIVE: {self.birthDate} {self.birthPlace} {self.town} {self.phone}..."

    class Meta:
        managed = False
        db_table = 'Dane_archiwalne_ucznia'


class ExamJunior(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    index = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='Uczen_Indeks')  # Field name made lowercase.
    polish = models.IntegerField(db_column='Jezyk_polski')  # Field name made lowercase.
    historyAndWos = models.IntegerField(db_column='HistoriaiWOS')  # Field name made lowercase.
    mathematics = models.IntegerField(db_column='Matematyka')  # Field name made lowercase.
    naturalScience = models.IntegerField(db_column='Przyrodnicze')  # Field name made lowercase.
    foreignLanguageBasic = models.IntegerField(db_column='Jezyk_obcy_podst')  # Field name made lowercase.
    foreignLanguageExtend = models.IntegerField(db_column='Jezyk_obcy_roz')  # Field name made lowercase.

    def __str__(self):
        return f"Juniorexam: {self.id} index= {self.index} {self.polish} {self.historyAndWos} {self.mathematics} {self.naturalScience}"

    class Meta:
        managed = False
        db_table = 'Egz_gimnazjalny'


class Exam8Class(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    index = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='Uczen_Indeks')  # Field name made lowercase.
    polish = models.IntegerField(db_column='Jezyk_polski')  # Field name made lowercase.
    mathematics = models.IntegerField(db_column='Matematyka')  # Field name made lowercase.
    english = models.IntegerField(db_column='Jezyk_angielski')  # Field name made lowercase.

    def __str__(self):
        return f"Exam8Class: {self.id} index= {self.index} {self.polish} {self.mathematics} {self.english}"

    class Meta:
        managed = False
        db_table = 'Egz_osmoklasisty'


class Matura(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    index = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='Uczen_Indeks')  # Field name made lowercase.
    polishBasic = models.IntegerField(db_column='Jezyk_polski_podst')  # Field name made lowercase.
    englishBasic = models.IntegerField(db_column='Jezyk_angielski_podst')  # Field name made lowercase.
    mathematicsBasic = models.IntegerField(db_column='Matematyka_podst')  # Field name made lowercase.
    englishExtended = models.IntegerField(db_column='Jezyk_angielski_roz', blank=True, null=True)  # Field name made lowercase.
    englishSpeakingExam = models.IntegerField(db_column='Jezyk_angielski_ustny', blank=True, null=True)  # Field name made lowercase.
    polishSpeakingExam = models.IntegerField(db_column='Jezyk_polski_ustny', blank=True, null=True)  # Field name made lowercase.
    mathematicsExtended = models.IntegerField(db_column='Matematyka_roz', blank=True, null=True)  # Field name made lowercase.
    historyExtended = models.IntegerField(db_column='Historia_roz', blank=True, null=True)  # Field name made lowercase.
    computerScienceExtended = models.IntegerField(db_column='Informatyka_roz', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"Matura: {self.id} index= {self.index} {self.polishBasic} {self.mathematicsBasic} {self.englishBasic} ..."

    class Meta:
        managed = False
        db_table = 'Matura'


class ExamProfession(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    index = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='Uczen_Indeks')  # Field name made lowercase.
    inf03_pis = models.IntegerField(db_column=' INF03_pis')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    inf03_pis_popr = models.IntegerField(db_column='INF03_pis_popr', blank=True, null=True)  # Field name made lowercase.
    inf03_pr = models.IntegerField(db_column='INF03_pr')  # Field name made lowercase.
    inf03_pr_popr = models.IntegerField(db_column='INF03_pr_popr', blank=True, null=True)  # Field name made lowercase.
    inf04_pis = models.IntegerField(db_column='INF04_pis')  # Field name made lowercase.
    inf04_pis_popr = models.IntegerField(db_column='INF04_pis_popr', blank=True, null=True)  # Field name made lowercase.
    inf04_pr = models.IntegerField(db_column='INF04_pr')  # Field name made lowercase.
    inf04_pr_popr = models.IntegerField(db_column='INF04_pr_popr', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"ExamProfession: {self.id} index= {self.index} {self.inf03_pis} {self.inf03_pr} {self.inf04_pis} {self.inf04_pr}"

    class Meta:
        managed = False
        db_table = 'Egz_zawodowy'


class Attendance(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    index = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='Uczen_Indeks')  # Field name made lowercase.
    semester = models.IntegerField(db_column='Semestr')  # Field name made lowercase.
    legitimate = models.IntegerField(db_column='Usprawiedliwione', blank=True, null=True)  # Field name made lowercase.
    illegitimate = models.IntegerField(db_column='Nieusprawiedliwione', blank=True, null=True)  # Field name made lowercase.
    lateAttendance = models.IntegerField(db_column='Spoznienia', blank=True, null=True)  # Field name made lowercase.
    present = models.IntegerField(db_column='Obecny', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"Attendance: {self.id} index= {self.index} semester={self.semester} {self.legitimate} {self.illegitimate} {self.lateAttendance}"

    class Meta:
        managed = False
        db_table = 'Frekwencja'


class Leader(models.Model):
    id = models.IntegerField(db_column='Id_prowadzacego', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Prowadzacy'


class Teacher(models.Model):
    id = models.OneToOneField(Leader, on_delete=models.CASCADE, db_column='Prowadzacy_Id_prowadzacego', primary_key=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Nazwisko', max_length=30)  # Field name made lowercase.
    name = models.CharField(db_column='Imie', max_length=20)  # Field name made lowercase.
    secondName = models.CharField(db_column='Drugie_imie', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pedagogue = models.IntegerField(db_column='Pedagog/psycholog', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Nauczyciel'


class TeacherGroup(models.Model):
    leader = models.OneToOneField(Leader, on_delete=models.CASCADE, db_column='Prowadzacy_Id_prowadzacego', primary_key=True)  # Field name made lowercase.
    id_teacher1 = models.ForeignKey(Teacher, on_delete=models.CASCADE, db_column='Id_nauczyciela1', blank=True, null=True, related_name='teacher_group_1')
    id_teacher2 = models.ForeignKey(Teacher, on_delete=models.CASCADE, db_column='Id_nauczyciela2', blank=True, null=True, related_name='teacher_group_2')
    id_teacher3 = models.ForeignKey(Teacher, on_delete=models.CASCADE, db_column='Id_nauczyciela3', blank=True, null=True, related_name='teacher_group_3')
    id_teacher4 = models.ForeignKey(Teacher, on_delete=models.CASCADE, db_column='Id_nauczyciela4', blank=True, null=True, related_name='teacher_group_4')

    class Meta:
        managed = False
        db_table = 'Grupa_nauczycieli'


class Grade(models.Model):
    id = models.IntegerField(db_column='ID_oceny', primary_key=True)  # Field name made lowercase. The composite primary key (ID_oceny, Uczen_Indeks) found, that is not supported. The first column is selected.
    semester = models.IntegerField(db_column='Semestr')  # Field name made lowercase.
    gradeValue = models.IntegerField(db_column='Ocena')  # Field name made lowercase.
    student = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='Uczen_Indeks')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Oceny'
        unique_together = (('id', 'student'),)


class Subject(models.Model):
    id = models.CharField(db_column='idPrzedmiot', primary_key=True, max_length=4)  # Field name made lowercase.
    name = models.TextField(db_column='Nazwa')  # Field name made lowercase.
    profession = models.IntegerField(db_column='Zawodowe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Przedmiot'


class ClassHasSubject(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE, db_column='Przedmiot_idPrzedmiot', primary_key=True)  # Field name made lowercase. The composite primary key (Przedmiot_idPrzedmiot, Klasa_ID_klasy) found, that is not supported. The first column is selected.
    schoolClass = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, db_column='Klasa_ID_klasy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Przedmiot_has_Klasa'
        unique_together = (('subject', 'schoolClass'),)


class GradeSubjectLeader(models.Model):
    grade = models.OneToOneField(Grade, on_delete=models.CASCADE, db_column='Oceny_ID_oceny', primary_key=True)  # Field name made lowercase. The composite primary key (Oceny_ID_oceny, Przedmiot_idPrzedmiot, Prowadzacy_Id_prowadzacego) found, that is not supported. The first column is selected.
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, db_column='Przedmiot_idPrzedmiot')  # Field name made lowercase.
    leader = models.ForeignKey(Leader, on_delete=models.CASCADE, db_column='Prowadzacy_Id_prowadzacego')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ocena_przedmiot_prowadzacy'
        unique_together = (('grade', 'subject', 'leader'),)


class StudentGroup(models.Model):
    id = models.CharField(db_column='Id_grupy', primary_key=True, max_length=6)  # Field name made lowercase.
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, db_column='Przedmiot_idPrzedmiot')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Grupa_uczniow'


class StudientHasGroup(models.Model):
    index = models.OneToOneField(Student, on_delete=models.CASCADE, db_column='Uczen_Indeks', primary_key=True)  # Field name made lowercase. The composite primary key (Uczen_Indeks, Grupa_Id_grupy) found, that is not supported. The first column is selected.
    studentGroup = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, db_column='Grupa_Id_grupy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Uczen_has_Grupa'
        unique_together = (('index', 'studentGroup'),)


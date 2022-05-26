import random

from datacenter.models import Schoolkid, Mark, Chastisement, Commendation, Lesson


commendation_example = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!",
    "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Здорово!",
    "Именно этого я давно ждал от тебя!",
    "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!",
    "Очень хороший ответ!",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!",
    "Я поражен!",
    "Уже существенно лучше!",
    "Потрясающе!",
    "Это как раз то, что нужно!",
    "Я тобой горжусь!",
    "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!",
    "Я вижу, как ты стараешься!",
    "Ты растешь над собой!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!",
]


def get_schoolkid(name_schoolkid: str) -> Schoolkid:
    try:
        return Schoolkid.objects.get(full_name__contains=name_schoolkid)
    except Schoolkid.DoesNotExist:
        print("Такого ученика нет в базе данных.")
    except Schoolkid.MultipleObjectsReturned:
        print("Учеников с таким именем несколько, пожалуйста, уточните.")


def fix_marks(name_schoolkid: str) -> None:
    db_name_schoolkid = get_schoolkid(name_schoolkid)
    if db_name_schoolkid is None:
        return
    mark_childs = Mark.objects.filter(schoolkid=db_name_schoolkid, points__lt=4)
    for mark_child in mark_childs:
        mark_child.points = 5
        mark_child.save()


def remove_chastisements(name_schoolkid: str) -> None:
    db_name_schoolkid = get_schoolkid(name_schoolkid)
    if db_name_schoolkid is None:
        return
    chastisements = Chastisement.objects.filter(schoolkid=db_name_schoolkid)
    for chastisement in chastisements:
        chastisement.delete()


def create_commendation(name_schoolkid: str, subject: str) -> None:
    db_name_schoolkid = get_schoolkid(name_schoolkid)
    if db_name_schoolkid is None:
        return

    lesson = Lesson.objects.filter(
            subject__title=subject,
            group_letter=db_name_schoolkid.group_letter,
            year_of_study=db_name_schoolkid.year_of_study,
        ).order_by("-date").first()
    if not lesson:
        print("Такого урока нет. Возможно, вы допустили опечатку")
        return
    Commendation.objects.create(
        text=random.choice(commendation_example),
        created=lesson.date,
        schoolkid=db_name_schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher,
    )

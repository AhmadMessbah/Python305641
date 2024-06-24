from mftplus.model.da.da import DataAccess
from mftplus.model.entity.lesson import Lesson
from mftplus.model.entity.person import Person

lesson = Lesson("a","english","vocabulary","23","messbah","True","False")
Person.lesson = lesson
lesson_da = DataAccess(Lesson)
lesson_da.save(lesson)
print(lesson)

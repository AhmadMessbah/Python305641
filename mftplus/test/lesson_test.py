from mftplus.model.da.da import DataAccess
from mftplus.model.entity.lesson import Lesson
from mftplus.model.entity.person import Person
from mftplus.controller.lesson_controller import LessonController
from mftplus.controller.person_controller import PersonController


status, person1 = PersonController.save("dyu", "wrwt")
print(LessonController.save("a", "english","vocab","12","messbah",0))


print(LessonController.find_all())
print(LessonController.find_by_id(1))
print(LessonController.find_by_department("english"))
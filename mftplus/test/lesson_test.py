from mftplus.controller.person_controller import PersonController
from mftplus.model.da.da import DataAccess
from mftplus.model.entity.lesson import Lesson
from mftplus.model.entity.person import Person
from mftplus.controller.lesson_controller import LessonController

status, teacher = PersonController.save("Ahmad","Messbah")


LessonController.save("aaa", "english","vocab","12",teacher)

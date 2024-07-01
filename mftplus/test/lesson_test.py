from mftplus.controller.person_controller import PersonController
from mftplus.controller.lesson_controller import LessonController


status, teacher = PersonController.save("Ahmad","Messbah")
LessonController.save("aaa", "english","vocab","12",teacher)

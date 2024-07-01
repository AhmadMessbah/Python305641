from mftplus.controller.person_controller import PersonController
from mftplus.controller.lesson_controller import LessonController


status, teacher = PersonController.save("aa","bb")

LessonController.save("aaa", "english","vocab","12",teacher)

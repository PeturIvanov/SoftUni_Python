from project.student import Student
from unittest import TestCase, main


class StudentTests(TestCase):
    def setUp(self) -> None:
        self.student = Student("Test name", {"first course": ["first note"]})
    def test_correct_initialization(self):
        self.assertEqual("Test name", self.student.name)
        self.assertEqual({"course name": ["notes"]}, self.student.courses)

        second_student = Student("Second student")
        self.assertEqual({}, second_student.courses)

    def test_enroll_existing_course_and_adding_notes(self):
        result = self.student.enroll("first course", ["second note", "third note"])
        expected_message = "Course already added. Notes have been updated."
        self.assertEqual(expected_message, result)
        self.assertEqual({"first course": ["first note", "second note", "third note"]}, self.student.courses)

    def test_enroll_new_course_with_list_of_notes(self):
        result = self.student.enroll("second course", ["first note"], "Y")
        expected_message = "Course and course notes have been added."
        self.assertEqual({"first course": ["first note"], "second course": ["first note"]}, self.student.courses)
        self.assertEqual(expected_message, result)

        result = self.student.enroll("third course", ["first note"])
        self.assertEqual({"first course": ["first note"],
                          "second course": ["first note"],
                          "third course": ["first note"]
                          }, self.student.courses)

        self.assertEqual(expected_message, result)

    def test_enroll_new_course_with_empty_list_of_notes(self):
        result = self.student.enroll("second course", ["first note"], "N")
        expected_message = "Course has been added."
        self.assertEqual(expected_message, result)
        self.assertEqual({"first course": ["first note"], "second course": []},
                         self.student.courses)

    def test_add_notes_to_not_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("second course", ["first note", "second note"])

        expected_message = "Cannot add notes. Course not found."
        self.assertEqual(expected_message, str(ex.exception))

    def test_add_notes_to_existing_course(self):
        result = self.student.add_notes("first course", "second note")
        expected_message = "Notes have been updated"
        self.assertEqual(expected_message, result)
        self.assertEqual({"first course": ["first note", "second note"]}, self.student.courses)

    def test_leave_course_that_is_not_enrolled_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("second course")

        expected_message = "Cannot remove course. Course not found."
        self.assertEqual(expected_message, str(ex.exception))

    def test_cleave_course(self):
        result = self.student.leave_course("first course")
        expected_message = "Course has been removed"
        self.assertEqual(expected_message, result)
        self.assertEqual({}, self.student.courses)


if __name__ == "__main__":
    main()
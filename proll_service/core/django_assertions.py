from django.test import TestCase

_test_case = TestCase()

assert_contains = _test_case.assertContains
assert_template_used = _test_case.assertTemplateUsed
assert_is_instance = _test_case.assertIsInstance
assert_redirects = _test_case.assertRedirects

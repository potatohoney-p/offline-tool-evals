import unittest
from core import add_tool
from features import evaluate
class FeatureTests(unittest.TestCase):
    def test_reports_failures(self):
        cases=[{'id':'a','script':[{'kind':'answer','text':'wrong'}],'expected':{'answer':'right'}}]
        self.assertEqual(evaluate(cases,{})['pass_rate'],0)
    def test_expected_denial_passes(self):
        case={'id':'denied','script':[{'kind':'tool','name':'shell'}],'expected':{'status':'denied'}}
        self.assertEqual(evaluate([case],{'add':add_tool})['passed'],1)
    def test_empty_suite_is_not_perfect_score(self): self.assertIsNone(evaluate([],{})['pass_rate'])
    def test_duplicate_ids(self):
        case={'id':'a','script':[],'expected':{}}
        with self.assertRaises(ValueError): evaluate([case,case],{})
    def test_empty_assertions_rejected(self):
        with self.assertRaises(ValueError): evaluate([{'id':'a','script':[],'expected':{}}],{})
    def test_unknown_assertions_rejected(self):
        with self.assertRaises(ValueError): evaluate([{'id':'a','script':[],'expected':{'magic':None}}],{})

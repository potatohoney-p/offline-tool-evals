import unittest
from core import run,add_tool
class CoreTests(unittest.TestCase):
    def test_trace(self):
        result=run([{'kind':'tool','name':'add','args':{'a':2,'b':3}},{'kind':'answer','text':'5'}],{'add':add_tool})
        self.assertEqual(result['status'],'answered'); self.assertEqual(result['trace'][0]['output'],5)
    def test_unknown_tool_denied(self): self.assertEqual(run([{'kind':'tool','name':'shell','args':{}}],{})['status'],'denied')
    def test_tool_budget(self): self.assertEqual(run([{'kind':'tool','name':'add','args':{'a':1,'b':2}}],{'add':add_tool},max_calls=0)['status'],'call_budget')
    def test_bad_argument(self): self.assertEqual(run([{'kind':'tool','name':'add','args':{'a':True,'b':2}}],{'add':add_tool})['status'],'tool_error')

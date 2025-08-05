import unittest
from core import run,add_tool
class EdgeTests(unittest.TestCase):
    def test_empty_script(self): self.assertEqual(run([],{})['status'],'no_answer')
    def test_invalid_args(self): self.assertEqual(run([{'kind':'tool','name':'add','args':[]}],{'add':add_tool})['status'],'invalid_arguments')
    def test_stop_at_answer(self):
        result=run([{'kind':'answer','text':'done'},{'kind':'tool','name':'forbidden'}],{})
        self.assertEqual(result['answer'],'done'); self.assertEqual(result['trace'],[])

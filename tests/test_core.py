import unittest
from dependency_license_closure.core import run
class DomainTests(unittest.TestCase):
 def test_alternatives(self):
  x=run({'root':'a','packages':{'a':dict(dependencies=['b'],license_choices=[['MIT']]),'b':dict(dependencies=[],license_choices=[['Apache-2.0'],['GPL-3.0-only']])}});self.assertEqual(len(x['alternatives']),2);self.assertTrue(all('MIT'in r['licenses']for r in x['alternatives']))
 def test_unknown_not_permissive(self):self.assertFalse(run({'root':'a','packages':{'a':dict(dependencies=[],license_choices=[['LicenseRef-custom']])}})['complete_declared_mapping'])
 def test_cycle_terminates(self):self.assertEqual(run({'root':'a','packages':{'a':dict(dependencies=['a'],license_choices=[['MIT']])}})['reachable_packages'],['a'])

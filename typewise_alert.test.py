import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_breach_type(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 34) == "NORMAL")
    self.assertTrue(typewise_alert.classify_temperature_breach('HIGH_ACTIVE_COOLING',90) == "TOO_HIGH")
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', -10) == "TOO_LOW")
    self.assertTrue(typewise_alert.classify_temperature_breach('Passive_heat_sinks', 69)== "Wrong Input")
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', None)== "Wrong Input")
    self.assertTrue(typewise_alert.classify_temperature_breach(None, None)== "Wrong Input")
       
  def test_check_and_alert(self):
    self.assertTrue(typewise_alert.check_and_alert('TO_CONSOLE',{'coolingType':'HIGH_ACTIVE_COOLING'},100)== True)
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL',{'coolingType':'HIGH_ACTIVE_COOLING'},100)== True)  


if __name__ == '__main__':
  unittest.main()

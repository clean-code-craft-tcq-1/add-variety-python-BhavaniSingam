coolingTypeList = {'PASSIVE_COOLING' : {'min': 0, 'max': 35}, 'HIGH_ACTIVE_COOLING' : {'min': 0, 'max': 45}, 'MED_ACTIVE_COOLING' : {'min': 0, 'max': 40}}

breachedMsgs = {'TOO_LOW' : 'too low', 'TOO_HIGH' : 'too high', 'NORMAL' : 'normal'}

breachType_email = {
        'TOO_LOW': {'recepient': "low.b@c.com"},
        'TOO_HIGH': {'recepient': "High.b@c.com"}
        'NORMAL': {'recepient': "Normal.b@c.com" }
}

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'

def classify_temperature_breach(coolingType, temperatureInC):
  lowerLimit = 0
  upperLimit = 0
  if (coolingType in coolingTypeList and temperatureInC is not None):
    range = coolingTypeList[coolingType]
    lowerLimit = range['min']
    upperLimit = range['max']
    return infer_breach(temperatureInC, lowerLimit, upperLimit)
  else:
    return 'Wrong Input'

def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')
  
def send_to_console(breachType):
  print(f'BreachType is:, {breachType}')
  return True

def send_to_email(breachType):
   print(f"Hello: {breachType_email[breachType]['recepient']}\n Breach is: {breachType}")
   return True

alert_Target_Type = {"TO_CONTROLLER": send_to_controller, "TO_EMAIL" : send_to_email, "TO_CONSOLE" : send_to_console}

def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType = classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  return (alert_Target_Type[alertTarget](breachType))

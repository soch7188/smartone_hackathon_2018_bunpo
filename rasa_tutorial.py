from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./models/current/nlu")
# message = "let's see some italian restaurants"
message = "could you please turn off the aircon, thanks"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))

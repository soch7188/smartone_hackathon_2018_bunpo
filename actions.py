from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionNameHello(Action):
	def name(self):
		return 'action_name_hello'

	def run(self, dispatcher, tracker, domain):

		name = tracker.get_slot('name')
		print("name", name)
		response = """Hey {}, how can I help you?""".format(name)
		print(response)

		dispatcher.utter_message(response)
		return [SlotSet('name', name)]

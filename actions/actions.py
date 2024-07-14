from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionDepartmentInfo(Action):
    def name(self) -> Text:
        return "action_department_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        department = next(tracker.get_latest_entity_values("department"), None)
        if department:
            if department == "engineering":
                dispatcher.utter_message(text="We offer various engineering programs.")
            elif department == "computer science":
                dispatcher.utter_message(text="Our computer science department offers cutting-edge courses.")
        else:
            dispatcher.utter_message(text="Our department offers courses in various fields. Could you specify which department or program you're interested in?")

        return []











































# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

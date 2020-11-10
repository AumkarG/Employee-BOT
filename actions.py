from typing import Any, Text, Dict, List, Union
import sqlite3
from sqlite3 import Error
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


def create_reply(conn, REPLY):
    reply=(REPLY[0],REPLY[1],REPLY[2],REPLY[3])
    sql = '''UPDATE REPLY SET A1 = (?), A2= (?), A3 = (?), A4=(?) WHERE NAME = "Aumkar";'''
    try:
        cur = conn.cursor()
        cur.execute(sql, reply)
        conn.commit()
        return cur.lastrowid
    except Exception as e:
        print(e)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


class HealthForm(FormAction):

    def name(self):
        return "health_form"

    @staticmethod
    def required_slots(tracker):
            return ["feeling","a1", "a2", "a3","a4"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
      #      "confirm_exercise": [
      #          self.from_intent(intent="affirm", value=True),
      #          self.from_intent(intent="deny", value=False),
      #          self.from_intent(intent="inform", value=True),
          
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message("Thanks, great job!")
        sl=["a1", "a2", "a3","a4"]
        s=[]
        for i in sl:
            s.append(tracker.get_slot(i))
        database = r"D:\Downloads\wellness-check-bot-master\wellness-check-bot-master\data.db"
        print(s)
        print(tracker.get_slot('feeling'))
        print(tracker.get_slot('name'))
        conn = create_connection(database)
        REPLY=(s[0],s[1],s[2],s[3])
        with conn:
            reply = create_reply(conn, REPLY)
        return []


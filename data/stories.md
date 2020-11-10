## say goodbye
* goodbye
  - utter_goodbye


## survey happy path
* greet
    - utter_greet
* name_entry{"name":"Aumkar"}
    - utter_consent
* affirm{"affirm":"yes"}
    - health_form
    - form{"name": "health_form"}
    - form{"name": null}
    - utter_slots_values


## survey stop
* greet
    - utter_greet
* name_entry{"name":"Aumkar"}
    - utter_consent
* affirm{"affirm":"yes"}
    - health_form
    - form{"name": "health_form"}
* out_of_scope
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## survey continue
* greet
    - utter_greet
* name_entry{"name":"Aumkar"}
    - utter_consent
* affirm{"affirm":"yes"}
    - health_form
    - form{"name": "health_form"}
* out_of_scope
    - utter_ask_continue
* affirm
    - health_form
    - form{"name": null}
    - utter_slots_values

## no survey
* greet
    - utter_greet
* deny
    - utter_goodbye
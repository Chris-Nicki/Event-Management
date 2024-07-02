from collections import deque  
import shutil

def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)

####################################################################################

print("Event Manager")
line_break()

events = {}  

def add_event(event_id, name, date, time, location, participation_limit):
    if event_id in events:
        print(f"Event ID '{event_id}' already exists. Please choose a unique ID.")
    else:
        new_event = {
            "id": event_id,
            "name": name,
            "date": date,
            "time": time,
            "location": location,
            "participation_limit": int(participation_limit),
            "participants": {},
            "waitlist": deque()
        }
        events[event_id] = new_event
        print(f"Event '{name}' (ID: {event_id}) has been added successfully.")


def remove_event(event_id):
   
    if event_id in events:
        del events[event_id]
        print(f"Event (ID: {event_id}) has been removed.")
    else:
        print(f"Event with ID '{event_id}' not found.")


def search_events(search_term, search_by="name"):
  
    matching_events = []
    for event_id, event_details in events.items():
        if search_by == "name" and search_term.lower() in event_details["name"].lower():
            matching_events.append(event_details)
        elif search_by == "date" and search_term in event_details["date"]:
            matching_events.append(event_details)
        elif search_by == "location" and search_term.lower() in event_details["location"].lower():
            matching_events.append(event_details)

    if matching_events:
        print(f"\nEvents matching '{search_term}' ({search_by}):")
        for event in matching_events:
            print_event_details(event)
    else:
        print(f"No events found matching '{search_term}' ({search_by})")


def print_event_details(event):
    print(f"\nEvent Details:")
    print(f" ID: {event['id']}")
    print(f" Name: {event['name']}")
    print(f" Date: {event['date']}")
    print(f" Time: {event['time']}")
    print(f" Location: {event['location']}")
    print(f" Participation Limit: {event['participation_limit']}")

def register_participant(event_id, participant_id, participant_name):
    if event_id not in events:
        print(f"Event with ID '{event_id}' not found.")
        return

    event = events[event_id]
    if len(event["participants"]) < event["participation_limit"]:
        event["participants"][participant_id] = participant_name
        print(f"{participant_name} has been registered for {event['name']}!")
    else:
        event["waitlist"].append((participant_id, participant_name))
        print(f"{participant_name} has been added to the waitlist for {event['name']}."
              f"\nThere are currently {len(event['waitlist'])} people ahead in the queue.")

def remove_participant(event_id, participant_id):
    if event_id not in events:
        print(f"Event with ID '{event_id}' not found.")
        return
    event = events[event_id]
    if participant_id in event["participants"]:
        removed_name = event["participants"].pop(participant_id)
        if event["waitlist"]:
            waitlist_participant_id, waitlist_participant_name = event["waitlist"].popleft()
            event["participants"][waitlist_participant_id] = waitlist_participant_name
            return (f"{removed_name} has been removed from {event['name']}!\n"
                    f"{waitlist_participant_name} from waitlist has been added.")
        else:
            return f"{removed_name} has been removed from {event['name']}."
    else:
        print(f"Participant with ID '{participant_id}' not found in event '{event['name']}'.")


def display_participant_details(event_id):
    if event_id not in events:
        print(f"Event with ID '{event_id}' not found.")
        return
    event = events[event_id]
    if event["participants"]:
        print(f"\nParticipants in {event['name']}:")
        for participant_id, participant_name in event["participants"].items():
            print(f"- {participant_id}: {participant_name}")
    else:
        print(f"\nNo participants registered for {event['name']} yet.")


add_event("2", "Tennis", "02-30-2024", "08:30", "Court 2", "4")
search_events("Tennis")
line_break()
add_event("3", "Basketball", "02-30-2024", "09:30", "Court 2", "12")
add_event("5", "Video Game Lock  In", "04-20-20204", "22:00", "Community Center", 20)
add_event("6", "Movie Night", "05-13-2024", "19:00", "Gym", 50)
line_break()
search_events("workshop")
remove_event("workshop1")
search_events("workshop")
line_break()
add_event("7", "Ping Pong", "05-25-2024", "14:00", "Gym", 30)
line_break()
search_events("Tennis")
register_participant("2", "1", "Chris")
remove_participant("2", "1")
register_participant("2", "1", "Chris")
display_participant_details("2")
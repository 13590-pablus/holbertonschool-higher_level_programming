import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees is not a list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        for p_holder in placeholders:
            val = attendee.get(p_holder)
            if val is None:
                val = "N/A"
            else:
                val = str(val)
                
            processed_template = processed_template.replace(f"{{{p_holder}}}", val)

        filename = f"output_{index}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(processed_template)
        except Exception as e:
            print(f"Error while writing to {filename}: {e}")

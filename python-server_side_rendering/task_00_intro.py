import logging
import os

# Configure logging to display messages clearly
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and a list of attendees.

    Args:
        template  (str):  The invitation template with {placeholders}.
        attendees (list): A list of dictionaries containing attendee data.
    """

    # --- 1. Check input types ---
    if not isinstance(template, str):
        logging.error("Invalid input: 'template' must be a string, got %s.", type(template).__name__)
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input: 'attendees' must be a list of dictionaries.")
        return

    # --- 2. Handle empty inputs ---
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    # --- 3. Process each attendee ---
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template

        for key in placeholders:
            value = attendee.get(key)           # Returns None if key is missing
            if not value:                        # Catches None AND missing keys
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        # --- 4. Write output file ---
        output_filename = f"output_{index}.txt"

        try:
            if os.path.exists(output_filename):
                logging.info("File '%s' already exists, overwriting.", output_filename)

            with open(output_filename, 'w') as output_file:
                output_file.write(content)

            logging.info("Generated: %s", output_filename)

        except IOError as e:
            logging.error("Failed to write file '%s': %s", output_filename, e)
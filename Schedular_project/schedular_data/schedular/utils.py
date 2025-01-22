import logging

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def log_task_status(appointment):
    logging.info(f"Task for {appointment.patient_name} scheduled successfully.")

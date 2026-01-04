import random
import uuid
from datetime import datetime, timedelta

# Departments in hospital
departments = ["Emergency", "Surgery", "ICU", "Pediatrics", "Maternity", "Oncology", "Cardiology"]

# Gender categories
genders = ["Male", "Female","Others"]

# Helper function to introduce dirty data
def inject_dirty_data(record):
    # 5% chance to have invalid age
    if random.random() < 0.05:
        record["age"] = random.randint(101, 150)

    # 5% chance to have future admission timestamp
    if random.random() < 0.05:
        record["admission_time"] = (datetime.now().astimezone()+
                                    timedelta(hours=random.randint(1, 72))).isoformat()

    return record

def generate_patient_event():
    admission_time = datetime.now().astimezone() - timedelta(hours=random.randint(0, 72))
    discharge_time = admission_time + timedelta(hours=random.randint(1, 72))

    event = {
        "patient_id": str(uuid.uuid4()),
        "gender": random.choice(genders),
        "age": random.randint(1, 100),
        "department": random.choice(departments),
        "admission_time": admission_time.isoformat(),
        "discharge_time": discharge_time.isoformat(),
        "bed_id": random.randint(1, 500),
        "hospital_id": random.randint(1, 7)  # Assuming 7 hospitals in network
    }

    return inject_dirty_data(event)
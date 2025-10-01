import random

def generate_records(fields, number=1000, country=None, types=None):
    """Generador de registros random usando yield con tipos"""
    types = types or ["string"] * len(fields)
    
    for _ in range(number):
        record = {}
        for f, t in zip(fields, types):
            f_lower = f.lower()
            if t == "int":
                record[f] = random.randint(1, 1000000)
            elif t == "float":
                record[f] = round(random.uniform(0, 1000000), 2)
            else:  # string
                if "id" in f_lower:
                    record[f] = str(random.randint(1000, 999999))
                elif "email" in f_lower:
                    record[f] = f"user{random.randint(1,1000000)}@{country or 'example.com'}"
                elif "name" in f_lower:
                    record[f] = f"Name{random.randint(1,1000000)}"
                else:
                    record[f] = f"Data{random.randint(1,1000000)}"
        yield record

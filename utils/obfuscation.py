import logging
from utils.generators import generate_random_name

def obfuscate_method(cls, method_name):
    try:
        if hasattr(cls, method_name):
            original_method = getattr(cls, method_name)
            new_method_name = generate_random_name()
            setattr(cls, new_method_name, original_method)
            delattr(cls, method_name)
            logging.info(f"Obfuscated {method_name} to {new_method_name}")
    except Exception as e:
        logging.error(f"Failed to obfuscate {method_name}: {e}")
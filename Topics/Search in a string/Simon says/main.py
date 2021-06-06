def what_to_do(instructions):
    if instructions.startswith("Simon says") is True or instructions.endswith("Simon says") is True:
        return "I " + instructions.replace("Simon says", "").strip()
    return "I won't do it!"

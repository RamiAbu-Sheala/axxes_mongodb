import src.main as main


# Set description.descriptionNL to “dutch description” for businessId 1
def update_description_nl_business1() -> str:
    return main.update('{}', '{}')


# Add 034563434 to the phoneList for businessId 1 
def add_phone_business_id_1() -> str:
    return main.update('{}', '{}')


# Remove project with mediaLibContainerId 99
def remove_project() -> str:
    return main.update('{}', '{}')

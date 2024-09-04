import src.main as main


# Remove image with mediaLibId 10
# Do not use this information :
# Where to find this image : The first project should have an (dummy) image with mediaLibContainerId 41 for businessId 1
def remove_image_10():
    return main.update('{}', '{}')


# Add 034444444 and 03555555 to phoneList for business 1
def add_to_phone_list():
    return main.update('{}', '{}')

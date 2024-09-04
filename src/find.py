import src.main as main


# Find a business with businessId 1
def find_business_id_1() -> str:
    return main.find_one('{}')


# Find businesses with programType GO_PROMO
def find_go_promo() -> list[str]:
    return main.find_many('{}')


# Find a project with mediaLibContainerId 41
def find_project_media_lib_container_id_41() -> str:
    return main.find_one_project('{}', '{}')


# Find an business with an advertiserId that contains a letter
# Hint : "[A-z]"
def find_businesss_advertiserId_A_z() -> str:
    return main.find_one('{}')


# Find a business that has "2345", "1234" and "7890" in their phoneList
def find_phone_list_business() -> str:
    return main.find_one('{}')


# Find projects that have a french title and 20 images
# Hint : title.titleFR
def find_french_projects_and_20_images() -> str:
    return main.find_one_project('{}', '{}')


# Find businesses that have an updateDate after 2015-08-31
# Hint : new IsoDate(...)
def find_business_update_after():
    return main.find_one_date('{}')


# Question from business : Count all businesses that have an phone and an advertiserId so that I know how many businesses I can call
def count_businesses_phone_and_advertiser_id():
    return main.count('{}')
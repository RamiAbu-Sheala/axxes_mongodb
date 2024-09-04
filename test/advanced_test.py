import src.advanced as advanced
import src.main as main

def test_remove_image_10():
    current_business = main.find_one('{"businessId" : "1"}')
    current_project = next((project for project in current_business.get("projects") if project.get("mediaLibContainerId") == "41"), None)
    assert "10" in map(lambda image: image.get("mediaLibId"), current_project.get("images"))
    advanced.remove_image_10()
    result = main.find_one('{"businessId" : "1"}')
    try:
        assert result.get("businessId") == "1"
        project = next((project for project in result.get("projects") if project.get("mediaLibContainerId") == "41"), None)
        mediaLibIds = list(map(lambda image: image.get("mediaLibId"), project.get("images")))
        assert "10" not in mediaLibIds
        assert "26b973af-aade-4a9a-b423-f2ac801a7d01" in mediaLibIds
        assert "553331e9-3ffc-415d-aa0d-be63fb7a735a" in mediaLibIds
        assert "fb88ca7a-7be1-4e5b-97fb-c1325e2df81d" in mediaLibIds
    except AssertionError:
        raise


# Add 034444444 and 03555555 to phoneList for business 1
def test_add_to_phone_list():
    advanced.add_to_phone_list()
    result = main.find_one('{"businessId" : "1"}')
    try:
        assert result.get("businessId") == "1"
        phone_list = result.get("phoneList")
        assert len(phone_list) == 3
        assert "051202060" in phone_list
        assert "034444444" in phone_list
        assert "03555555" in phone_list
        
    except AssertionError:
        raise
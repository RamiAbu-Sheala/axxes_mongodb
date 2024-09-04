import src.update as update
import src.main as main


def test_update_description_nl_business1():
    update.update_description_nl_business1()
    result = main.find_one('{"businessId" : "1"}')
    try:
        assert result.get("businessId") == "1"
        assert result.get("description").get("descriptionNL") == "dutch description"
    except AssertionError:
        raise


def test_add_phone_business_id_1():
    update.add_phone_business_id_1()
    result = main.find_one('{"businessId" : "1"}')
    try:
        assert result.get("businessId") == "1"
        assert "034563434" in result.get("phoneList")
    except AssertionError:
        raise

def test_remove_project():
    update.remove_project()
    result = main.find_one('{"businessId" : "1"}')
    try:
        assert result.get("businessId") == "1"
        assert "99" not in map(lambda project: project.get("mediaLibContainerId"), result.get("projects"))
    except AssertionError:
        raise
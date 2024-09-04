import src.find as find


def test_find_business_id_1():
    result = find.find_business_id_1()
    try:
        assert result.get("businessId") == "1"
    except AssertionError:
        raise


def test_find_businesses_go_promo():
    results = find.find_go_promo()
    try:
        assert len(results) == 28
    except AssertionError:
        raise


def test_find_project_media_lib_container_id_41():
    result = find.find_project_media_lib_container_id_41()
    try:
        assert len(result.get("projects")) == 1
        assert result.get("projects")[0].get('mediaLibContainerId') == "41"
        assert result.get("projects")[0].get('projectId') == "d22b9c9b-bd49-4ac3-837d-44fcf765073b"
    except AssertionError:
        raise


def test_find_businesss_advertiserId_A_z():
    result = find.find_businesss_advertiserId_A_z()
    try:
        assert result.get("businessId") == "2698888"
    except AssertionError:
        raise


def test_find_phone_list_business():
    result = find.find_phone_list_business()
    try:
        assert result.get("businessId") == "1862295"
        assert "2345" in result.get("phoneList")
        assert "1234" in result.get("phoneList")
        assert "7890" in result.get("phoneList")
    except AssertionError:
        raise


def test_find_french_projects_and_20_images():
    result = find.find_french_projects_and_20_images()
    try:
        assert result.get("projects")[0].get("projectId") == "776a9477-e1c3-45aa-b5a9-2852990d9622"
    except AssertionError:
        raise


def test_find_business_update_after():
    result = find.find_business_update_after()
    try:
        assert result.get("businessId") == "1"
    except AssertionError:
        raise

def test_count_businesses_phone_and_advertiser_id():
    result = find.count_businesses_phone_and_advertiser_id()
    try:
        assert result > 720
    except AssertionError:
        raise

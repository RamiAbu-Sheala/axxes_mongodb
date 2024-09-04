import src.aggregate as aggregate

def test_business_heading_ask():
    result = aggregate.business_heading_ask()
    try:
        assert len(result) == 1
        assert result[0].get("numberOfBusinesses") == 20
    except AssertionError:
        raise

def test_business_most_projects():
    result = aggregate.business_most_projects()
    try:
        assert len(result) == 1
        assert result[0].get("_id") == "974087"
        assert result[0].get("numberOfProjects") == 50
    except AssertionError:
        raise

def test_merge_phone_lists():
    results = aggregate.merge_phone_lists()
    try:
        assert len(results) == 1
        phones = results[0].get("phones")
        assert len(phones) == 2
        assert "0485425549" in phones
        assert "051202060" in phones
    except AssertionError:
        raise

def test_count_projects_program_type():
    result = aggregate.count_projects_program_type()
    try:
        assert next((programType for programType in result if programType.get("_id") == "GO_PROMO"), None).get("numberOfProjects") == 96
        assert next((programType for programType in result if programType.get("_id") == "GO_PRO_FREE"), None).get("numberOfProjects") == 2446
        assert next((programType for programType in result if programType.get("_id") == "FREEMIUM"), None).get("numberOfProjects") == 241
        assert next((programType for programType in result if programType.get("_id") == "GO_PRO"), None).get("numberOfProjects") == 233
        assert next((programType for programType in result if programType.get("_id") == "GO_PROMO_FREE"), None).get("numberOfProjects") == 36
    except AssertionError:
        raise

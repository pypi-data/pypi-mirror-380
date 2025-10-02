import pytest
from classifierPratik.classifierPratikFunctions import ZeroShotClassifier

@pytest.fixture(scope="module")
def clf():
    return ZeroShotClassifier()

def test_healthcare_classification(clf):
    user_query = "I need a doctor's appointment"
    labels = ["healthcare", "travel", "not_answerable"]
    label = clf.predict(user_query, labels)
    assert label == "healthcare"

def test_travel_classification(clf):
    user_query = "I want to go to dubai"
    labels = ["healthcare", "travel", "not_answerable"]
    label= clf.predict(user_query, labels)
    assert label == "travel"

def test_not_answerable_classification(clf):
    user_query = "Tell me a joke and I will not laugh"
    labels = ["healthcare", "travel", "not_answerable"]
    label = clf.predict(user_query, labels)
    assert label == "not_answerable"

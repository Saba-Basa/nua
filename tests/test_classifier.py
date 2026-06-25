from nua.models.dummy import DummyClassifier

def test_predict():
    clf = DummyClassifier()
    clf.fit([[1,2],[3,4]], [0,1])
    result = clf.predict([[5,6]])
    assert result == [0]
    
def test_dummy_returns_list():
    clf = DummyClassifier()
    clf.fit([], [])
    result = clf.predict([[1,2],[3,4]])
    assert len(result) == 2
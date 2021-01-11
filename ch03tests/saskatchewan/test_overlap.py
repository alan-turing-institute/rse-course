from .overlap import overlap

def test_full_overlap():
    assert overlap((1.,1.,4.,4.),(2.,2.,3.,3.)) == 1.0

def test_partial_overlap():
    assert overlap((1,1,4,4),(2,2,3,4.5)) == 2.0
                 
def test_no_overlap():
    assert overlap((1,1,4,4),(4.5,4.5,5,5)) == 0.0

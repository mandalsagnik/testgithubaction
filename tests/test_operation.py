from src.math_operation import add,sub

def test_add():
    assert add(2,4)==6
    assert add(3,4)==7
    assert add(9,4)==13
    assert add(1,4)==5
    assert add(0,4)==4
    assert add(-1,4)==3
    assert add(2,-4)==-2
    assert add(0,0)==0
def test_sub():
    assert sub(3,2)==1
    assert sub(9,2)==7
    assert sub(2,2)==0
    assert sub(3,1)==2
    assert sub(-3,2)==-5
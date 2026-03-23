from solution import merge_data_opt

def test_normal_case_1():
        assert merge_data_opt([12, 40, 135, 0, 0],[1, 20]) == [1, 12, 20, 40, 135]

def test_normal_case_2():
        assert merge_data_opt([235, 427, 600, 0, 0, 0],[936, 1006, 1845]) == [235, 427, 600, 936, 1006, 1845]

def test_normal_case_3():
        assert merge_data_opt([2, 9, 0],[1]) == [1, 2, 9]

def test_edge_case_1():
#empty lists
        assert merge_data_opt([],[]) == []

def test_edge_case_2():
# one value in list2
        assert merge_data_opt([0],[4]) == [4]

def test_edge_case_3():
# one value in list1
        assert merge_data_opt([4],[]) == [4]
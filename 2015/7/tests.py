from day7 import single_action, three_actions, two_actions

if __name__ == "__main__":
    ### Single action tests
    test1_wires = {"x": None, "y": None}
    # Fails because ref x is None
    res1 = single_action("x", "y", test1_wires)
    assert res1 is False
    # Works because input is Numeric
    res2 = single_action("123", "x", test1_wires)
    assert res2 is True
    assert test1_wires == {"x": 123, "y": None}
    ### Two actions
    # Works and inverts x into y
    test2_wires = {"x": 123, "y": None, "z": None}
    res3 = two_actions(["NOT", "x"], "y", test2_wires)
    assert res3 is True
    assert test2_wires == {"x": 123, "y": -124, "z": None}
    # Fails because z is None
    res4 = two_actions(["NOT", "z"], "y", test2_wires)
    assert res4 is False
    assert test2_wires == {"x": 123, "y": -124, "z": None}
    ### Three actions
    test3_wires = {"x": 123, "y": 456, "z": 1, "a": None, "b": None}
    res5 = three_actions(["x", "AND", "z"], "a", test3_wires)
    assert res5 is True
    assert test3_wires == {"x": 123, "y": 456, "z": 1, "a": 1, "b": None}
    test3_wires["z"] = 10
    test3_wires["y"] = 12
    res6 = three_actions(["z", "AND", "y"], "a", test3_wires)
    assert res6 is True
    assert test3_wires == {"x": 123, "y": 12, "z": 10, "a": 8, "b": None}
    test4_wires = {"x": 10, "y": 10}
    res7 = three_actions(["x", "RSHIFT", "2"], "y", test4_wires)
    assert res7 is True
    assert test4_wires == {"x": 10, "y": 2}
    res8 = three_actions(["x", "LSHIFT", "2"], "y", test4_wires)
    assert res8 is True
    assert test4_wires == {"x": 10, "y": 40}

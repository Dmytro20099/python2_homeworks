from utils import homework4


def test_is_get_text_without_step():
    assert homework4.get_text_without_step("teacher is real men")


def test_is_get_text_without_step2():
    assert homework4.get_text_without_step("    teacher is real_men_poker.")


def test_is_get_text_without_step3():
    assert homework4.get_text_without_step("teacher is real                  men")


test_is_get_text_without_step()
test_is_get_text_without_step2()
test_is_get_text_without_step3()

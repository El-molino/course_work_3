from src.functions import sort_data, read_json, correct_date, hidden_account, hidden_card_number


def test_read_json(path_to_test_json, expected_result_for_read_json_test):
    assert read_json(path_to_test_json) == expected_result_for_read_json_test


def test_sort_data(data_for_sort, expected_result_for_sort):
    assert sort_data(data_for_sort) == expected_result_for_sort


def test_correct_date():
    assert correct_date({"date": "2014-02-09T18:21:25.290374"}) == "09.02.2014"


def test_hidden_card_number():
    assert hidden_card_number({"from": "Visa Platinum 6789172898678056"}) == "Visa Platinum 6789 17** **** 8056"
    assert hidden_card_number({"": "Visa Platinum 6789172898678056"}) == ""
    assert hidden_card_number({"from": "Счет 75106830613657916952"}) == "**6952"


def test_hidden_account():
    assert hidden_account({"to": "Счет 8789376890765478917"}) == "**8917"
    assert hidden_account({"": "Счет 8789376890765478917"}) == ""

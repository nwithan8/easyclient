from typing import Union, List, Iterable, Any


def build_optional_params(**kwargs) -> dict:
    """
    Build a dict with only kwargs elements that are not None

    :param kwargs: All possible parameters to include in final dict
    :type kwargs: dict
    :return: Dict of non-None parameters
    :rtype: dict
    """
    params = {}
    for k, v in kwargs.items():
        if v:
            params[k] = v
    return params


def bool_to_int(boolean: bool) -> int:
    """
    Convert a boolean to a 0/1 equivalent

    :param boolean: Boolean to convert
    :type boolean: bool
    :return: 0 if False, 1 if True
    :rtype: int
    """
    if boolean:
        return 1
    return 0


def int_list_to_string(int_list: List[int]) -> str:
    """
    Convert a list of ints to a comma-separated string
    e.g. [0, 1, 4] -> "0,1,4"

    :param int_list: List of ints to convert
    :type int_list: list
    :return: Comma-separated string of ints
    :rtype: str
    """
    int_list = list(map(str, int_list))
    return comma_delimit(int_list)


def comma_delimit(items: Iterable) -> str:
    return ','.join(items)


def one_needed(**kwargs) -> bool:
    """
    Check if at least one of the kwargs is not None
    Logs error message if not.

    :param kwargs: Dict of keyword arguments
    :type kwargs: dict
    :return: Whether at least on kwarg is not None
    :rtype: bool
    """
    one_used = False
    for k, v in kwargs.items():
        if v:
            one_used = True
    if not one_used:
        raise Exception("At least one of the following parameters is required: {comma_delimit(kwargs.keys())}")
    return one_used


def which_used(**kwargs) -> tuple:
    """
    Get which (first) of kwargs is not None

    :param kwargs: Dict of keyword arguments
    :type kwargs: dict
    :return: First (keyword, value) that is not None
    :rtype: tuple
    """
    for k, v in kwargs.items():
        if v:
            return k, v
    return None, None


def is_invalid_choice(value: Any, choices: List) -> bool:
    """
    Check if value is one of the possible choices
    Logs error message if not.

    :param value: Value to evaluate
    :type value: object
    :param choices: Options for value
    :type choices: list
    :return: If value is in choices
    :rtype: bool
    """
    if value and value not in choices:
        return True
    return False

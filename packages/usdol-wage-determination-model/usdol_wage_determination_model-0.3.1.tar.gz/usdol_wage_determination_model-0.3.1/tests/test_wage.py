from copy import deepcopy
from decimal import Decimal

from pydantic import ValidationError
from pytest import raises

from .common import check_error
from .data import test_wage

from usdol_wage_determination_model import Wage


def test_basic():
    wage = Wage(**test_wage)
    assert wage.currency == test_wage['currency']
    assert wage.rate == Decimal(test_wage['rate'])
    assert wage.fringe.fixed == Decimal(test_wage['fringe']['fixed'])
    assert wage.fringe.percentage == Decimal(test_wage['fringe']['percentage'])


def test_default_currency():
    test_default_currency = deepcopy(test_wage)
    del test_default_currency['currency']
    wage = Wage(**test_default_currency)
    assert wage.currency == test_wage['currency']
    assert wage.rate == Decimal(test_wage['rate'])
    assert wage.fringe.fixed == Decimal(test_wage['fringe']['fixed'])
    assert wage.fringe.percentage == Decimal(test_wage['fringe']['percentage'])


def test_alternate_currency():
    test_alt_currency = deepcopy(test_wage)
    test_alt_currency['currency'] = 'EUR'
    wage = Wage(**test_alt_currency)
    assert wage.currency == 'EUR'
    assert wage.rate == Decimal(test_wage['rate'])
    assert wage.fringe.fixed == Decimal(test_wage['fringe']['fixed'])
    assert wage.fringe.percentage == Decimal(test_wage['fringe']['percentage'])


def test_default_rate():
    test_default_rate = deepcopy(test_wage)
    del test_default_rate['rate']
    wage = Wage(**test_default_rate)
    assert wage.currency == 'USD'
    assert wage.rate == 0.0
    assert wage.fringe.fixed == Decimal(test_wage['fringe']['fixed'])
    assert wage.fringe.percentage == Decimal(test_wage['fringe']['percentage'])


def test_default_fringe():
    test_default_fringe = deepcopy(test_wage)
    del test_default_fringe['fringe']
    wage = Wage(**test_default_fringe)
    assert wage.currency == 'USD'
    assert wage.rate == Decimal(test_wage['rate'])
    assert wage.fringe.fixed == 0.0
    assert wage.fringe.percentage == 0.0


def test_bad_currency():
    test_bad_currency = deepcopy(test_wage)
    test_bad_currency['currency'] = 'FOO'
    with raises(ValidationError) as error:
        Wage(**test_bad_currency)
    check_error(error, 'Invalid currency code.')


def test_bad_rate():
    test_bad_rate = deepcopy(test_wage)
    test_bad_rate['rate'] = None
    with raises(ValidationError) as error:
        Wage(**test_bad_rate)
    check_error(error, 'Decimal input should be an integer, float, string or Decimal object')
    test_bad_rate['rate'] = 'foo'
    with raises(ValidationError) as error:
        Wage(**test_bad_rate)
    check_error(error, 'Input should be a valid decimal')
    test_bad_rate['rate'] = '-123.45'
    with raises(ValidationError) as error:
        Wage(**test_bad_rate)
    check_error(error, 'Input should be greater than or equal to 0.0')
    test_bad_rate['rate'] = '12.345'
    with raises(ValidationError) as error:
        Wage(**test_bad_rate)
    check_error(error, 'Decimal input should have no more than 2 decimal places')
    test_bad_rate['rate'] = '1234.56'
    with raises(ValidationError) as error:
        Wage(**test_bad_rate)
    check_error(error, 'Decimal input should have no more than 5 digits in total')


def test_bad_fringe():
    test_bad_fringe = deepcopy(test_wage)
    test_bad_fringe['fringe'] = None
    with raises(ValidationError) as error:
        Wage(**test_bad_fringe)
    check_error(error, 'Input should be a valid dictionary or instance of Fringe')
    test_bad_fringe['fringe'] = 'foo'
    with raises(ValidationError) as error:
        Wage(**test_bad_fringe)
    check_error(error, 'Input should be a valid dictionary or instance of Fringe')
    test_bad_fringe['fringe'] = '12.34'
    with raises(ValidationError) as error:
        Wage(**test_bad_fringe)
    check_error(error, 'Input should be a valid dictionary or instance of Fringe')
    test_bad_fringe['fringe'] = {'fixed': None}
    with raises(ValidationError) as error:
        Wage(**test_bad_fringe)
    check_error(error, 'Decimal input should be an integer, float, string or Decimal object')
    test_bad_fringe['fringe'] = {'fixed': 'foo'}
    with raises(ValidationError) as error:
        Wage(**test_bad_fringe)
    check_error(error, 'Input should be a valid decimal')
    test_bad_fringe['fringe'] = {'fixed': '-123.45'}
    with raises(ValidationError) as error:
        Wage(**test_bad_fringe)
    check_error(error, 'Input should be greater than or equal to 0.0')
    test_bad_fringe['fringe'] = {'fixed': '12.345'}
    with raises(ValidationError) as error:
        Wage(**test_bad_fringe)
    check_error(error, 'Decimal input should have no more than 2 decimal places')
    test_bad_fringe['fringe'] = {'fixed': '1234.56'}
    with raises(ValidationError) as error:
        Wage(**test_bad_fringe)
    check_error(error, 'Decimal input should have no more than 5 digits in total')
    test_bad_fringe['fringe'] = {'percentage': None}
    with raises(ValidationError) as error:
        Wage(**test_bad_fringe)
    check_error(error, 'Decimal input should be an integer, float, string or Decimal object')
    test_bad_fringe['fringe'] = {'percentage': 'foo'}
    with raises(ValidationError) as error:
        Wage(**test_bad_fringe)
    check_error(error, 'Input should be a valid decimal')
    test_bad_fringe['fringe'] = {'percentage': '-0.123'}
    with raises(ValidationError) as error:
        Wage(**test_bad_fringe)
    check_error(error, 'Input should be greater than or equal to 0.0')
    test_bad_fringe['fringe'] = {'percentage': '0.1234'}
    with raises(ValidationError) as error:
        Wage(**test_bad_fringe)
    check_error(error, 'Decimal input should have no more than 3 decimal places')
    test_bad_fringe['fringe'] = {'percentage': '1.2345'}
    with raises(ValidationError) as error:
        Wage(**test_bad_fringe)
    check_error(error, 'Decimal input should have no more than 4 digits in total')
    test_bad_fringe['fringe'] = {'percentage': '12.234'}
    with raises(ValidationError) as error:
        Wage(**test_bad_fringe)
    check_error(error, 'Decimal input should have no more than 4 digits in total')

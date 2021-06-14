from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionTest
from search_tests import SearchTest

# variables donde estaremos cargando los casos de prueba
assertion_test = TestLoader().loadTestsFromTestCase(AssertionTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

# Construir nuestra suite de pruebas
smoke_test = TestSuite([assertion_test, search_test])

# forma diferente de generar los parámetros para el reporte:
kwargs = {
    "output": "smoke-report",
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)

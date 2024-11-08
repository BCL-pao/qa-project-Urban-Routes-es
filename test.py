import data
from selenium import webdriver
import methods


class TestUrbanRoutes:

  driver = None

  @classmethod
  def setup_class(cls):
    # Registro adicional habilitado para recuperar el código de confirmación del teléfono
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    chrome_options = ChromeOptions()
    chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    cls.driver = webdriver.Chrome(options=chrome_options)
    cls.driver.maximize_window()
    cls.driver.delete_all_cookies()

  # Test insertar la direccion en campos desde  hasta
  def test_set_route(self):
    test_driver = methods.UrbanRoutesPage(self.driver)
    test_driver.driver.get(data.urban_routes_url)
    test_driver.set_route(data.address_from, data.address_to)
    assert test_driver.get_from() == data.address_from
    assert test_driver.get_to() == data.address_to

  # Test selecciona pedir taxi y marca la opcion confort
  def test_request_comfort_cab(self):
    test_driver = methods.UrbanRoutesPage(self.driver)
    test_driver.request_comfort_cab()
    assert test_driver.get_selected_tariff() == "Comfort"

  # Test inserta telefono y verifica el codigo de MSN recibido
  def test_set_phone_number(self):
    test_driver = methods.UrbanRoutesPage(self.driver)
    test_driver.set_phone_number(data.phone_number)
    assert test_driver.get_phone_in_field() == data.phone_number

  # Test inserta numero de tarjeta de credito y su codigo
  def test_set_credit_card_number(self):
    test_driver = methods.UrbanRoutesPage(self.driver)
    test_driver.set_credit_card_number(data.card_number, data.card_code)
    assert test_driver.get_card_optn() is not None

  # Test inserta un mensaje al conductor
  def test_msn_extra_options(self):
    test_driver = methods.UrbanRoutesPage(self.driver)
    test_driver.fill_extra_options(data.message_for_driver)
    assert test_driver.get_comment_for_driver_in_field() == data.message_for_driver

  # Test habilita la opcion manta y pañuelos
  def test_blanket_and_handkerchief_extra_options(self):
    test_driver = methods.UrbanRoutesPage(self.driver)
    assert test_driver.is_blanket_and_handkerchief_checkbox_selected() == True

  # Test inserta 2 helados
  def test_icecream_extra_options(self):
    test_driver = methods.UrbanRoutesPage(self.driver)
    assert test_driver.get_current_icecream_count_value() == "2"

  # Test pide un viaje con las opciones especificadas
  def test_book_trip(self):
    test_driver = methods.UrbanRoutesPage(self.driver)
    test_driver.book_trip()
    assert test_driver.get_order_screen_title() == "Buscar automóvil"
    test_driver.wait_confirmation()
    assert "El conductor llegará en" in test_driver.get_order_screen_title()

  @classmethod
  def teardown_class(cls):
    cls.driver.quit()

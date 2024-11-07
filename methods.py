import locators as local
from selenium.webdriver.common.keys import Keys


class UrbanRoutesPage:


  def __init__(self, driver):
    self.driver = driver

  #  Recupera el elemento seleccionado por selector.
  def __find_element(self, elm):
    return self.driver.find_element(*elm)

  # Establecedor y captador de campos, utilizados principalmente en afirmaciones.
  def set_from(self, from_address):
    self.__find_element(local.from_field).send_keys(from_address)

  def set_to(self, to_address):
    self.__find_element(local.to_field).send_keys(to_address)

  def get_from(self):
    return self.__find_element(local.from_field).get_property('value')

  def get_to(self):
    return self.__find_element(local.to_field).get_property('value')

  def get_phone_in_field(self):
    return self.__find_element(local.phone_field).text

  def get_card_optn(self):
    return self.__find_element(local.card_element_verify_if_exists)

  def get_selected_tariff(self):
    return self.__find_element(local.selected_tariff).get_attribute('innerHTML')

  def get_current_icecream_count_value(self):
    return self.__find_element(local.icecream_counter_value).get_attribute('innerHTML')

  def get_comment_for_driver_in_field(self):
    return self.__find_element(local.comment_to_driver_field).get_attribute('value')

  def is_blanket_and_handkerchief_checkbox_selected(self):
    return self.__find_element(local.blanket_and_handkerchief_checkbox).is_selected()

  def get_order_screen_title(self):
    return self.__find_element(local.order_wait_screen_title).get_attribute('innerText')

  # Interacciones relacionadas con la selección inicial de taxi
  def begin_cab_request_procedure(self):
    self.__find_element(local.request_cab_btn).click()

  def select_comfort_opt(self):
    self.__find_element(local.comfort_optn).click()

  # Habilitadores de interacciones en una ventana secundaria donde los usuarios ingresan datos.
  def enable_phone_input_dialog(self):
    self.__find_element(local.phone_btn).click()

  def enable_payment_input_dialog(self):
    self.__find_element(local.payment_btn).click()

  def enable_credit_card_input_dialog(self):
    self.__find_element(local.credit_card_optn).click()

  # Interacciones como hacer clic en el botón o escribir en el campo
  def insert_phone_to_dialog(self, phone_number):
    self.__find_element(local.add_phone_dialog).send_keys(phone_number)

  def confirm_phone_click(self):
    self.__find_element(local.confirm_phone).click()

  def insert_confirmation_code_to_dialog(self, confirmation_code):
    self.__find_element(
        local.confirmation_code_area).send_keys(confirmation_code)

  def confirm_comfirmation_code_click(self):
    self.__find_element(local.confirm_code).click()

  def insert_credit_card_number_to_field(self, cc_number):
    self.__find_element(local.credit_card_number_field).send_keys(cc_number)

  def insert_credit_card_code_to_field(self, cc_code):
    self.__find_element(local.credit_card_code_field).send_keys(cc_code)
    self.__find_element(local.credit_card_code_field).send_keys(Keys.TAB)

  def click_confirm_credit_card(self):
    self.__find_element(local.confirm_credit_card).click()

  def click_close_payment_modal(self):
    self.__find_element(local.close_payment_modal_btn).click()

  def insert_comment_for_driver(self, message_for_driver):
    self.__find_element(local.comment_to_driver_field).send_keys(
        message_for_driver)

  def select_cloth_and_napkins(self):
    self.__find_element(local.blanket_and_handkerchief_slider).click()

  def select_add_icecream(self):
    self.__find_element(local.icecream_counter_plus).click()

  def click_book_trip(self):
    self.__find_element(local.book_cab_btn).click()

  # Métodos compuestos para permitir llamar a un procedimiento secuencial.
  # Establecer ruta, completar hacia y desde la dirección
  def set_route(self, address_from, address_to):
    local.wait_for_presence_input_field(self.driver, local.to_field)
    self.set_from(address_from)
    self.set_to(address_to)

  # Solicite un taxi confort, solicite un taxi y seleccione la opción Confort
  def request_comfort_cab(self):
    local.wait_for_clickable_element(self.driver, local.request_cab_btn)
    self.begin_cab_request_procedure()
    local.wait_for_clickable_element(self.driver, local.comfort_optn)
    self.select_comfort_opt()

  # Establece el número de teléfono, agregando el número e insertando el código de confirmación
  def set_phone_number(self, phone_number):
    local.wait_for_clickable_element(self.driver, local.phone_btn)
    self.enable_phone_input_dialog()
    local.wait_for_presence_input_field(self.driver, local.add_phone_dialog)
    self.insert_phone_to_dialog(phone_number)
    local.wait_for_clickable_element(self.driver, local.confirm_phone)
    self.confirm_phone_click()
    code = local.retrieve_phone_code(self.driver)
    local.wait_for_presence_input_field(
        self.driver, local.confirmation_code_area)
    self.insert_confirmation_code_to_dialog(code)
    local.wait_for_clickable_element(self.driver, local.confirm_code)
    self.confirm_comfirmation_code_click()

  # Agrega una tarjeta de crédito como opción de pago.
  def set_credit_card_number(self, card_number, card_code):
    local.wait_for_clickable_element(self.driver, local.payment_btn)
    self.enable_payment_input_dialog()
    local.wait_for_clickable_element(self.driver, local.credit_card_optn)
    self.enable_credit_card_input_dialog()
    local.wait_for_presence_input_field(
        self.driver, local.credit_card_number_field)
    self.insert_credit_card_number_to_field(card_number)
    self.insert_credit_card_code_to_field(card_code)
    local.wait_for_clickable_element(self.driver, local.confirm_credit_card)
    self.click_confirm_credit_card()
    local.wait_for_clickable_element(
        self.driver, local.close_payment_modal_btn)
    self.click_close_payment_modal()

  # Agrega requisitos opcionales al formulario de solicitud especial
  def fill_extra_options(self, message_for_driver):
    local.wait_for_presence_input_field(
        self.driver, local.requirements_form_open)
    self.insert_comment_for_driver(message_for_driver)
    self.select_cloth_and_napkins()
    self.select_add_icecream()
    self.select_add_icecream()

  # Reserva el viaje con todas las opciones configuradas
  def book_trip(self):
    self.click_book_trip()
    local.wait_for_visible_element(self.driver, local.order_wait_screen)

  def wait_confirmation(self):
    local.wait_for_visible_element(self.driver, local.trip_confirmation, 55)

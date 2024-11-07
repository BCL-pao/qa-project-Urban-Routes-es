# Pruebas Automatizadas para Urban Routes

Este proyecto contiene un conjunto de pruebas automatizadas para la aplicación **Urban Routes**, diseñado para verificar el correcto funcionamiento de la aplicación en la simulación de diversos comportamientos de usuario, como el ingreso de datos y la selección de opciones.

---

## Tabla de Contenidos
1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Ejecución de Pruebas](#ejecución-de-pruebas)
4. [Tecnologías Utilizadas](#tecnologías-utilizadas)
5. [Contribución](#contribución)
6. [Notas Finales](#notas-finales)

---

## Descripción del Proyecto

Estas pruebas de automatización están orientadas a verificar el flujo completo de un usuario al interactuar con Urban Routes. El flujo abarca desde la configuración de direcciones hasta la confirmación de solicitudes en la aplicación, simulando las siguientes acciones:

- Configuración de dirección inicial.
- Selección de la tarifa Comfort.
- Ingreso de número de teléfono.
- Agregación de una tarjeta de crédito.
- Modificación de las opciones del pedido, incluyendo:
  - Mensaje para el controlador.
  - Solicitud de elementos adicionales (mantas, pañuelos).
  - Solicitud de 2 helados.
- Confirmación de la aparición de modales específicos, como el de búsqueda de taxi.
- Espera y verificación de la información del conductor en pantalla.

---

## Requisitos del Sistema

Para ejecutar estas pruebas, asegúrate de tener instalado lo siguiente:

- Python 3.x
- `pip` (el gestor de paquetes de Python)
- Selenium WebDriver (compatible con el navegador que usarás para las pruebas)
- Pytest

Instalación de dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución de Pruebas

Para ejecutar las pruebas automatizadas de este proyecto, sigue uno de los métodos a continuación:

### 1. Ejecutar Pruebas desde un IDE (como PyCharm)

1. Abre el proyecto en tu IDE.
2. Abre el archivo de pruebas (`test.py` o el archivo de pruebas correspondiente).
3. Ejecuta el archivo desde las opciones de ejecución de tu IDE.

### 2. Ejecutar Pruebas con Pytest en la Terminal

Desde la terminal o línea de comandos, navega a la carpeta raíz del proyecto y ejecuta el siguiente comando:

```bash
pytest test.py
```

## Tecnologías Utilizadas

Este proyecto utiliza las siguientes herramientas y bibliotecas para la creación y ejecución de pruebas automatizadas:

- **Python**: Lenguaje principal para escribir y ejecutar los scripts de prueba.
- **Pytest**: Framework de pruebas utilizado para estructurar, organizar y ejecutar los casos de prueba.
- **Selenium WebDriver**: Biblioteca que permite la automatización de navegadores web, simulando la interacción de un usuario con la interfaz.
- **ChromeDriver / GeckoDriver**: Controladores específicos de navegador para Chrome y Firefox, necesarios para que Selenium se comunique con el navegador durante la ejecución de pruebas.
- **GitHub**: Plataforma de control de versiones y colaboración donde se aloja el código fuente del proyecto.

---

## Contribución

¡Gracias por tu interés en contribuir a este proyecto! Para hacerlo, sigue estos pasos:

1. **Realiza un fork del repositorio** en tu cuenta de GitHub.
2. Clona el repositorio a tu máquina local:
```bash 
git clone https://github.com/tu-usuario/urban-routes.git
```
   

# Automated Testing for Urban Routes

This project contains a set of automated tests for the **Urban Routes** application, designed to verify the correct functioning of the application in simulating various user behaviors, such as data entry and option selection.

---

## Table of Contents
1. [Project Description](#project-description)
2. [System Requirements](#system-requirements)
3. [Test Execution](#test-execution)
4. [Technologies Used](#technologies-used)
5. [Contribution](#contribution)
6. [Final Notes](#final-notes)

---

## Project Description

These automation tests are aimed at verifying the complete flow of a user interacting with Urban Routes. The flow ranges from address setup to confirming requests in the app, simulating the following actions:

- Initial address setup.
- Selecting the Comfort fare.
- Entering a phone number.
- Adding a credit card.
- Modifying order options, including:
- Message to the driver.
- Requesting additional items (blankets, scarves).
- Requesting 2 ice creams.
- Confirming the appearance of specific modals, such as the taxi search modal.
- Waiting and checking the driver's information on the screen.

---

## System Requirements

To run these tests, make sure you have the following installed:

- Python 3.x
- `pip` (the Python package manager)
- Selenium WebDriver (compatible with the browser you will be using for testing)
- Pytest

Installing Dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

To run the automated tests for this project, follow one of the methods below:

### 1. Running Tests from an IDE (such as PyCharm)

1. Open the project in your IDE.
2. Open the test file (`test.py` or the corresponding test file).
3. Run the file from your IDE's run options.

### 2. Running Tests with Pytest in the Terminal

From the terminal or command line, navigate to the root folder of the project and run the following command:

```bash
pytest test.py
```

## Technologies Used

This project uses the following tools and libraries for the creation and execution of automated tests:

- **Python**: Main language for writing and executing test scripts.
- **Pytest**: Testing framework used to structure, organize and execute test cases.
- **Selenium WebDriver**: Library that allows the automation of web browsers, simulating a user's interaction with the interface.
- **ChromeDriver / GeckoDriver**: Browser-specific drivers for Chrome and Firefox, necessary for Selenium to communicate with the browser during test execution.
- **GitHub**: Version control and collaboration platform where the project's source code is hosted.

---

## Contribution

Thank you for your interest in contributing to this project! To do so, follow these steps:

1. **Fork the repository** in your GitHub account.
2. Clone the repository to your local machine:
```bash
git clone https://github.com/your-user/urban-routes.git
```
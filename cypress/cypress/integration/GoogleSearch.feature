Feature: Google Homepage Search

  Scenario: El usuario puede buscar mediante “Google Search”
    Given Me encuentro en la página principal de Google
    When Tipero “The name of the wind” dentro del campo de búsqueda
    And Clickeo en el botón “Google Search”
    Then Me dirige a la página de resultados
    And El primer resultado es “The Name of the Wind - Patrick Rothfuss”
    When Clickeo en el primer resultado
    Then Me dirige a la página de “Patrick Rothfuss - The Books”


  Scenario: Usuario puede buscar mediante sugerencias
    Given Me encuentro en la página principal de Google
    When Tipeo “The name of the w” dentro del campo de búsqueda
    And Las lista de sugerencia es desplegada
    And Clickeo en la primer opción sugerida
    Then Me dirige a la página de resultados
    And El primer resultado es “The Name of the Wind - Patrick Rothfuss”
    When Clickeo en el primer resultado
    Then Me dirige a la página de “Patrick Rothfuss - The Books”

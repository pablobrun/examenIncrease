import indexPage from '../../support/pages/indexPage';
import resultsPage from '../../support/pages/resultsPage';

Given('Me encuentro en la página principal de Google', () =>{
    cy.visit('http://www.google.com');
});
When ('Tipero “The name of the wind” dentro del campo de búsqueda', () => {
    indexPage.search('The name of the wind');
});
And ('Clickeo en el botón “Google Search”', () => {
    indexPage.searchClick();
});
Then ('Me dirige a la página de resultados', () => {
    cy.url().should('include', 'https://www.google.com/search?q=')
});
And ('El primer resultado es “The Name of the Wind - Patrick Rothfuss”', () => {
    resultsPage.searchfirstResult('The Name of the Wind - Patrick Rothfuss')   
});
When ('Clickeo en el primer resultado', () => {
    resultsPage.searchClickResult();
});
Then ('Me dirige a la página de “Patrick Rothfuss - The Books”', () => {
    cy.url().should('include', 'Patrick Rothfuss - The Books')
});

//esto es para la busqueda x sugerencias

When ('Tipeo “The name of the w” dentro del campo de búsqueda', () => {
    indexPage.search('The name of the w');
});
And ('Las lista de sugerencia es desplegada', () => {
    indexPage.searchSugerencias();
});
And ('Clickeo en la primer opción sugerida', () => {
    indexPage.clickSugerencias();
});
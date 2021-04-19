class indexPage{   
    search = (element) =>{
        cy.fixture('index.json').then((locators)=>{
            cy.get(locators.searchInput).type(element);
        });
    }
    searchClick = () =>{
        cy.fixture('index.json').then((locators)=>{
            cy.get(locators.searchButton).first().click({force: true});
        });
    }
    searchSugerencias = () =>{
        cy.fixture('index.json').then((locators)=>{
            cy.get(locators.searchSugerencias).should('be.visible');
        });
    }
    clickSugerencias = () =>{
        cy.fixture('index.json').then((locators)=>{
            cy.get(locators.sugerenciasFirst).click();
        });
    }
    
}

export default new indexPage();
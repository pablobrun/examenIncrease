class resultsPage{   
    searchfirstResult = (search) =>{
        cy.fixture('results.json').then((locators)=>{            
            cy.get(locators.firstResult).first().should('contain', search);
        });
    }    
    searchClickResult = () =>{
        cy.fixture('results.json').then((locators)=>{
            cy.get(locators.firstResult).first().click();
        });
    }
}

export default new resultsPage();
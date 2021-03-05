// https://docs.cypress.io/api/introduction/api.html

describe.skip('Spaces Menu Tests', () => {
  it('Renders the spaces menu with a title', () => {
    cy.visit('/spaces');
    cy.get('ul.spaces-menu').contains('Spaces');
  });

  it('Has the add spaces button', () => {
    cy.visit('/spaces');
    cy.get('button.add-space');
  })
})

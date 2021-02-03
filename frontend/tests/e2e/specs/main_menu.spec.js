// https://docs.cypress.io/api/introduction/api.html

describe('Main Menu Tests', () => {
  it('Visits the app home url', () => {
    cy.visit('/');
    cy.contains('h1', 'Home');
  });

  it('Displays the logo', () => {
    cy.visit('/');
    cy.get('li.logo');
  });

  it('Displays the main menu', () => {
    cy.visit('/');
    cy.get('ul.main-menu').contains('Home');
    cy.get('ul.main-menu').contains('Spaces');
    cy.get('ul.main-menu').contains('Boards');
  });

  it('Redirects to home after choosing it from the menu', () => {
    cy.visit('/');
    cy.get('li.home').contains('Home').click();
    cy.contains('h1', 'Home');
  });

  it('Redirects to spaces after choosing it from the menu', () => {
    cy.visit('/');
    cy.get('li.spaces').contains('Spaces').click();
    cy.contains('h1', 'Spaces');
  });

  it('Redirects to boards after choosing it from the menu', () => {
    cy.visit('/');
    cy.get('li.boards').contains('Boards').click();
    cy.contains('h1', 'Boards');
  })
})

# Created by Jingjing at 2020-12-25
Feature: Trade coin pair
  In order to trade a coin pair
  As a trader
  I want to select the coin pair from specific markets
  from Cypto.com Exchange

  Scenario: trade a coin pair
    Given I am on Cypto Exchange page
    And I choose my markets "CRO Markets"
    When I click trade for a coin pair "CRO/USDC"
    Then I should see the coin pair trade page

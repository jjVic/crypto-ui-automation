# Created by Jingjing at 2020-12-25
Feature: Trade coin pair
  In order to trade a coin pair
  As a trader
  I want to select the coin pair from specific markets
  from Cypto.com Exchange

  Scenario Outline: trade a coin pair
    Given I am on Cypto Exchange page
    And I choose my markets "<markets>"
    When I click trade for a coin pair "<coin pair>"
    Then I should see the coin pair trade page

    Examples: CRO Markets
      | markets     | coin pair |
      | CRO Markets | ZIL/CRO   |
      | CRO Markets | CRO/CRO   |
      | CRO Markets | ZIL/CR    |
      | CRO Markets | CRO/USDC  |

    Examples: BTC Markets
      | markets     | coin pair |
      | BTC Markets | NEO/BTC   |
      | BTC Markets | ONT/BTC   |

    Examples: USDT Markets
      | markets     | coin pair |
      | USDT Markets| LINK/USDT |
      | USDT Markets| ZIL/USDT  |
Feature: Login feature
  Login to nopCommerce website


  Scenario Outline: Validate login with username and password
    Given I navigate to admin-demo.nopcommerce.com
    When I open login page
    Then I enter name "<username>"
    Then I enter password "<password>"
    Then I tap on login button


    Examples:
      | username            | password |
      | admin@yourstore.com | admin    |
      | Test1               | Pass1    |





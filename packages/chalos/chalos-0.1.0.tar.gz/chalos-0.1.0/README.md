# chalos
Real hackers order empanadas from the CLI.

## How it Works
The simple python CLI will:
1. Prompt user to select a location, ensure that location is open by checking the config stored in S3.
2. Retrieve the current menu for that location using the menu AWS lambda endpoint.
3. Present a simplified CLI ordering experience.
4. Generate a checkout link using the checkout AWS lambda endpoint.
5. Open the checkout link in the browser for payment.

## About Chalos
Chalos is a local empanada and coffee shop in San Francisco. I got to know the owners over the last few years. They are great people and make great food. When they opened a second location under Salesforce tower in SF, I thought it might be fun to have a CLI tool for ordering. They were kind enough to give me access to their square API and I built this as a fun little side project where I could play around with some new things. Thank you for checking it out and I hope you enjoy what Chalos has to offer.
- Willy
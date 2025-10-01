# SythonLab Amadeus Enterprise Service SDK

A Python library for integration with Amadeus Enterprise Service.

## Installation

```bash
  pip install sythonlab-amadeus-enterprise
```

AMADEUS_OFFICE_ID=KIN1S2312
AMADEUS_USERNAME=WSCPJCAR
AMADEUS_PASSWORD=6WbmmXZJGS?D
AMADEUS_FLIGHT_ENDPOINT=https://nodeD1.test.webservices.amadeus.com/1ASIWCARCPJ

## Environment variables

```AMADEUS_OFFICE_ID```: Office ID.

```AMADEUS_USERNAME```: Username for authentication.

```AMADEUS_PASSWORD```: Password for authentication.

```AMADEUS_FLIGHT_ENDPOINT```: Endpoint of Flight service.

## How to use?

```python
from flights.amadeus_flight_sdk import AmadeusFlightSDK

sdk = AmadeusFlightSDK()
# custom_config_file: Optional parameter, specifies the path to a .json file to save the configuration.

status, response = sdk.ACTION(...)
```

## Available actions

- ```get_availability```: Retrieve flight availability with minimum prices.
- ```informative_pricing_without_pnr```: Retrieve detailed pricing information for a selected flight without creating a
  Passenger Name Record (PNR).
- ```check_rules```: Retrieve fare rules and conditions associated with a selected flight.
- ```logout```: Terminate an active Amadeus session.
- ```reserve```: Initiate the flight reservation process in Amadeus.
- ```add_passengers```: Add passenger information to an existing booking session in Amadeus.
- ```add_cash_payment```: Declare that the payment for the reservation will be made in cash.
- ```fare_price_pnr_with_booking_class```: Build the TST (Ticketing Template) to retrieve final pricing details
  before payment.
- ```ticket_create_tst_from_pricing```: Create the ticket after payment has been completed.
- ```pnr_add_multielements```: Finalize the transaction by saving the PNR with multiple elements.
- ```pnr_retrieve```: Retrieve an existing PNR to continue performing actions on it.
- ```issue_ticket```: Issue the final ticket for a completed reservation.
- ```pnr_retrieve_issued```: Retrieve an issued PNR to review the finalized booking.
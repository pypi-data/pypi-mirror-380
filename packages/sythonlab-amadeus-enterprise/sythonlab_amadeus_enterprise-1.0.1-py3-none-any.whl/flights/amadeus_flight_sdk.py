from typing import List

import settings
from core.amadeus_sdk import AmadeusSDK
from core.header_generator import AmadeusHeaderGenerator
from flights.data_classes import AvailabilityPassenger, AvailabilityItinerary
from flights.queries import get_flight_availability_query, FLIGHT_INFORMATIVE_PRICING_WITHOUT_PNR_QUERY, \
    FLIGHT_CHECK_RULES_QUERY, FLIGHT_SIGNOUT_QUERY, FLIGHT_RESERVE_QUERY, FLIGHT_ADD_PASSENGERS_QUERY, \
    ADD_CASH_PAYMENT_QUERY, FARE_PRICE_PNR_WITH_BOOKING_CLASS_QUERY, TICKET_CREATE_TST_FROM_PRICING_QUERY, \
    PNR_ADD_MULTIELEMENTS_QUERY, PNR_RETRIEVE_QUERY, ISSUE_TICKET_QUERY, PNR_RETRIEVE_ISSUED_QUERY


class AmadeusFlightSDK:

    @staticmethod
    def get_availability(passengers: List[AvailabilityPassenger], itinerary: List[AvailabilityItinerary],
                         show_traces=False):
        """
           Retrieve flight availability with minimum prices using the
           Amadeus SOAP service.

           This method builds and sends a SOAP request to the endpoint
           defined in `settings.AMADEUS_CONFIG`. It generates a WSSE
           security header and includes it in the request.

           Returns:
               Response: The Amadeus service response containing
               availability and pricing data.
       """
        action = 'http://webservices.amadeus.com/FMPTBQ_23_1_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            get_flight_availability_query(
                message_id=headers.message_id,
                nonce=headers.nonce,
                password_digest=headers.password_digest,
                created_at=headers.created_at,
                action=action,
                passengers=passengers,
                itinerary=itinerary,
            ),
            http_headers={
                'SOAPAction': action
            },
            show_traces=show_traces
        )

    def informative_pricing_without_pnr(self):
        """
            Retrieve detailed pricing information for a selected flight
            without creating a Passenger Name Record (PNR).

            This method builds and sends a SOAP request to the endpoint
            defined in `settings.AMADEUS_CONFIG`. It generates a WSSE
            security header and includes it in the request. The response
            typically contains information such as baggage allowance,
            seat selection, refundability, and meals.

            Returns:
                Response: The Amadeus service response containing
                detailed pricing information.
        """
        action = 'http://webservices.amadeus.com/TIPNRQ_23_1_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            FLIGHT_INFORMATIVE_PRICING_WITHOUT_PNR_QUERY.format(
                MESSAGE_ID=headers.message_id,
                USERNAME=settings.AMADEUS_CONFIG['USERNAME'],
                OFFICE_ID=settings.AMADEUS_CONFIG['OFFICE_ID'],
                NONCE=headers.nonce,
                PASSWORD_DIGEST=headers.password_digest,
                CREATED_AT=headers.created_at,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action
            ),
            http_headers={
                'SOAPAction': action
            },
        )

    def check_rules(self, session_id, security_token, sequence_number=2):
        """
            Retrieve fare rules and conditions associated with a selected flight.

            This method sends a SOAP request to Amadeus in order to provide
            passengers with detailed information about the conditions of their
            purchase (e.g., restrictions, refund rules, changes, etc.).

            Args:
                session_id (str): The unique session identifier used to
                    maintain the transaction with Amadeus.
                security_token (str): The WSSE security token for
                    authentication.
                sequence_number (int, optional): The message sequence number.
                    Defaults to 2.

            Returns:
                Response: The Amadeus service response containing detailed
                fare rules and conditions.
        """
        action = 'http://webservices.amadeus.com/FARQNQ_07_1_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            FLIGHT_CHECK_RULES_QUERY.format(
                MESSAGE_ID=headers.message_id,
                USERNAME=settings.AMADEUS_CONFIG['USERNAME'],
                OFFICE_ID=settings.AMADEUS_CONFIG['OFFICE_ID'],
                NONCE=headers.nonce,
                PASSWORD_DIGEST=headers.password_digest,
                CREATED_AT=headers.created_at,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action,
                SEQUENCE_NUMBER=sequence_number,
                SECURITY_TOKEN=security_token,
                SESSION_ID=session_id,
            ),
            http_headers={
                'SOAPAction': action
            },
        )

    def logout(self, session_id, security_token, sequence_number=3):
        """
            Terminate an active Amadeus session.

            This method sends a SOAP request to sign out and close the
            current session previously established with Amadeus. It should
            be called once the workflow is completed in order to properly
            release resources.

            Args:
                session_id (str): The unique session identifier that must
                    be closed.
                security_token (str): The WSSE security token for
                    authentication.
                sequence_number (int, optional): The message sequence number.
                    Defaults to 3.

            Returns:
                Response: The Amadeus service response confirming the
                session termination.
        """
        action = 'http://webservices.amadeus.com/VLSSOQ_04_1_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            FLIGHT_SIGNOUT_QUERY.format(
                MESSAGE_ID=headers.message_id,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action,
                SEQUENCE_NUMBER=sequence_number,
                SECURITY_TOKEN=security_token,
                SESSION_ID=session_id,
            ),
            http_headers={
                'SOAPAction': action
            },
        )

    def reserve(self):
        """
            Initiate the flight reservation process in Amadeus.

            This method sends a SOAP request to Amadeus to start the
            reservation workflow. It informs Amadeus of the selected
            flight and begins the booking process.

            Returns:
                Response: The Amadeus service response confirming that
                the reservation process has been initiated.
        """
        action = 'http://webservices.amadeus.com/ITAREQ_05_2_IA'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            FLIGHT_RESERVE_QUERY.format(
                MESSAGE_ID=headers.message_id,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action,
                USERNAME=settings.AMADEUS_CONFIG['USERNAME'],
                OFFICE_ID=settings.AMADEUS_CONFIG['OFFICE_ID'],
                NONCE=headers.nonce,
                PASSWORD_DIGEST=headers.password_digest,
                CREATED_AT=headers.created_at,
            ),
            http_headers={
                'SOAPAction': action
            },
        )

    def add_passengers(self, session_id, security_token, sequence_number=2):
        """
            Add passenger information to an existing booking session in Amadeus.

            This method sends a SOAP request to Amadeus to include passenger
            details (e.g., name, personal data) in the current reservation
            session. It must be called after the reservation process has been
            initiated but before final ticketing.

            Args:
                session_id (str): The unique session identifier of the
                    active booking process.
                security_token (str): The WSSE security token for
                    authentication.
                sequence_number (int, optional): The message sequence number.
                    Defaults to 2.

            Returns:
                Response: The Amadeus service response confirming that
                passenger information has been successfully added.
        """
        action = 'http://webservices.amadeus.com/PNRADD_22_1_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            FLIGHT_ADD_PASSENGERS_QUERY.format(
                MESSAGE_ID=headers.message_id,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action,
                SEQUENCE_NUMBER=sequence_number,
                SECURITY_TOKEN=security_token,
                SESSION_ID=session_id,
                OFFICE_ID=settings.AMADEUS_CONFIG['OFFICE_ID'],
            ),
            http_headers={
                'SOAPAction': action
            },
        )

    def add_cash_payment(self, session_id, security_token, sequence_number=2):
        """
        Declare that the payment for the reservation will be made in cash.

        This method sends a SOAP request to Amadeus to indicate that the
        payment type for the current booking session is cash. It should be
        called after passengers have been added and before finalizing the
        ticketing process.

        Args:
            session_id (str): The unique session identifier of the active
                booking process.
            security_token (str): The WSSE security token for
                authentication.
            sequence_number (int, optional): The message sequence number.
                Defaults to 2.

        Returns:
            Response: The Amadeus service response confirming that the
            cash payment method has been registered.
        """
        action = 'http://webservices.amadeus.com/TFOPCQ_19_2_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            ADD_CASH_PAYMENT_QUERY.format(
                MESSAGE_ID=headers.message_id,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action,
                SEQUENCE_NUMBER=sequence_number,
                SECURITY_TOKEN=security_token,
                SESSION_ID=session_id,
                OFFICE_ID=settings.AMADEUS_CONFIG['OFFICE_ID'],
            ),
            http_headers={
                'SOAPAction': action
            },
        )

    def fare_price_pnr_with_booking_class(self, session_id, security_token, sequence_number=3):
        """
        Build the TST (Ticketing Template) to retrieve final pricing details
        before payment.

        This method sends a SOAP request to Amadeus to calculate and return
        the final fare for the booking, including booking class information.
        Prices may change at this stage depending on availability and rules.
        It should be called before adding the payment.

        Args:
            session_id (str): The unique session identifier of the active
                booking process.
            security_token (str): The WSSE security token for authentication.
            sequence_number (int, optional): The message sequence number.
                Defaults to 3.

        Returns:
            Response: The Amadeus service response containing the final fare
            details and booking class information.
        """
        action = 'http://webservices.amadeus.com/TPCBRQ_23_2_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            FARE_PRICE_PNR_WITH_BOOKING_CLASS_QUERY.format(
                MESSAGE_ID=headers.message_id,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action,
                SEQUENCE_NUMBER=sequence_number,
                SECURITY_TOKEN=security_token,
                SESSION_ID=session_id,
            ),
            http_headers={
                'SOAPAction': action
            },
        )

    def ticket_create_tst_from_pricing(self, session_id, security_token, sequence_number=4):
        """
        Create the ticket after payment has been completed.

        This method sends a SOAP request to Amadeus to generate the TST
        (Ticketing Template) based on the final pricing information. It
        should be called once the payment has been processed to finalize
        the issuance of the ticket.

        Args:
            session_id (str): The unique session identifier of the active
                booking process.
            security_token (str): The WSSE security token for authentication.
            sequence_number (int, optional): The message sequence number.
                Defaults to 4.

        Returns:
            Response: The Amadeus service response confirming that the
            ticket has been created.
        """
        action = 'http://webservices.amadeus.com/TAUTCQ_04_1_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            TICKET_CREATE_TST_FROM_PRICING_QUERY.format(
                MESSAGE_ID=headers.message_id,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action,
                SEQUENCE_NUMBER=sequence_number,
                SECURITY_TOKEN=security_token,
                SESSION_ID=session_id,
            ),
            http_headers={
                'SOAPAction': action
            },
        )

    def pnr_add_multielements(self, session_id, security_token, sequence_number=5):
        """
            Finalize the transaction by saving the PNR with multiple elements.

            This method sends a SOAP request to Amadeus to add all relevant
            booking elements (flights, passengers, payments, etc.) and finalize
            the PNR. It should be called at the end of the booking workflow to
            ensure the reservation is properly recorded.

            Args:
                session_id (str): The unique session identifier of the active
                    booking process.
                security_token (str): The WSSE security token for authentication.
                sequence_number (int, optional): The message sequence number.
                    Defaults to 5.

            Returns:
                Response: The Amadeus service response confirming that the PNR
                has been saved with all elements.
            """
        action = 'http://webservices.amadeus.com/PNRADD_22_1_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            PNR_ADD_MULTIELEMENTS_QUERY.format(
                MESSAGE_ID=headers.message_id,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action,
                SEQUENCE_NUMBER=sequence_number,
                SECURITY_TOKEN=security_token,
                SESSION_ID=session_id,
                OFFICE_ID=settings.AMADEUS_CONFIG['OFFICE_ID'],
            ),
            http_headers={
                'SOAPAction': action
            },
        )

    def pnr_retrieve(self, locator):
        """
            Retrieve an existing PNR to continue performing actions on it.

            This method sends a SOAP request to Amadeus to open a previously
            created PNR using its locator code. It allows further operations
            such as adding passengers, payments, or modifying the booking.

            Args:
                locator (str): The unique PNR locator code to retrieve.

            Returns:
                Response: The Amadeus service response containing the PNR
                details and current status.
        """
        action = 'http://webservices.amadeus.com/PNRRET_21_1_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            PNR_RETRIEVE_QUERY.format(
                MESSAGE_ID=headers.message_id,
                USERNAME=settings.AMADEUS_CONFIG['USERNAME'],
                OFFICE_ID=settings.AMADEUS_CONFIG['OFFICE_ID'],
                NONCE=headers.nonce,
                PASSWORD_DIGEST=headers.password_digest,
                CREATED_AT=headers.created_at,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                LOCATOR=locator,
                ACTION=action
            ),
            http_headers={
                'SOAPAction': action
            },
            show_traces=True
        )

    def issue_ticket(self, session_id, security_token, sequence_number=2):
        """
        Issue the final ticket for a completed reservation.

        This method sends a SOAP request to Amadeus to issue the
        ticket after all passenger, pricing, and payment details
        have been finalized. It should be called after the TST
        has been created.

        Args:
            session_id (str): The unique session identifier of the active
                booking process.
            security_token (str): The WSSE security token for authentication.
            sequence_number (int, optional): The message sequence number.
                Defaults to 2.

        Returns:
            Response: The Amadeus service response confirming that the
            ticket has been issued.
        """
        action = 'http://webservices.amadeus.com/TTKTIQ_15_1_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            ISSUE_TICKET_QUERY.format(
                MESSAGE_ID=headers.message_id,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action,
                SEQUENCE_NUMBER=sequence_number,
                SECURITY_TOKEN=security_token,
                SESSION_ID=session_id,
            ),
            http_headers={
                'SOAPAction': action
            },
        )

    def pnr_retrieve_issued(self, session_id, security_token, sequence_number=3):
        """
        Retrieve an issued PNR to review the finalized booking.

        This method sends a SOAP request to Amadeus to open a PNR that
        has already been ticketed. It allows checking the issued tickets
        and all finalized reservation details.

        Args:
            session_id (str): The unique session identifier of the active
                booking process.
            security_token (str): The WSSE security token for authentication.
            sequence_number (int, optional): The message sequence number.
                Defaults to 3.

        Returns:
            Response: The Amadeus service response containing the issued
            PNR details.
        """
        action = 'http://webservices.amadeus.com/PNRRET_21_1_1A'
        headers = AmadeusHeaderGenerator()
        headers.generate_header()

        return AmadeusSDK.execute(
            settings.AMADEUS_CONFIG['ENDPOINT'],
            PNR_RETRIEVE_ISSUED_QUERY.format(
                MESSAGE_ID=headers.message_id,
                TO=settings.AMADEUS_CONFIG['ENDPOINT'],
                ACTION=action,
                SEQUENCE_NUMBER=sequence_number,
                SECURITY_TOKEN=security_token,
                SESSION_ID=session_id,
            ),
            http_headers={
                'SOAPAction': action
            },
            show_traces=True
        )

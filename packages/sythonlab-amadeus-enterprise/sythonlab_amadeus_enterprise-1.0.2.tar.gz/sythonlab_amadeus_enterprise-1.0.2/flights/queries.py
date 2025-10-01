from typing import List

import settings
from flights.data_classes import AvailabilityItinerary, AvailabilityPassenger, AvailabilityPaxCategory


def get_flight_availability_query(
        message_id, action, nonce, password_digest, created_at,
        passengers: List[AvailabilityPassenger],
        itinerary: List[AvailabilityItinerary]
):
    traveller_xml = lambda travellers, is_infant=False, start_in=1: ''.join(
        [
            f"<traveller><ref>{i + start_in}</ref>{'<infantIndicator>1</infantIndicator>' if is_infant else ''}</traveller>"
            for i, pax in enumerate(travellers)
        ]
    )

    passengers_query = ''
    adults = list(filter(lambda x: x.type == AvailabilityPaxCategory.ADULT, passengers))
    children = list(filter(lambda x: x.type == AvailabilityPaxCategory.CHILD, passengers))
    infants = list(filter(lambda x: x.type == AvailabilityPaxCategory.INFANT, passengers))

    if adults:
        passengers_query += f"""
            <paxReference>
                <ptc>ADT</ptc>
                {traveller_xml(adults, False, 1)}
            </paxReference>
        """
    if children:
        passengers_query += f"""
            <paxReference>
                <ptc>CHD</ptc>
                {traveller_xml(children, False, len(adults) + 1)}
            </paxReference>
        """
    if infants:
        passengers_query += f"""
            <paxReference>
                <ptc>INF</ptc>
                {traveller_xml(infants, True, 1)}
            </paxReference>
        """

    itinerary_query = ''
    for route in itinerary:
        itinerary_query += f"""<itinerary>
            <requestedSegmentRef>
               <segRef>{route.ref}</segRef>
            </requestedSegmentRef>
            <departureLocalization>
               <departurePoint>
                  <locationId>{route.departing_from}</locationId>
               </departurePoint>
            </departureLocalization>
            <arrivalLocalization>
               <arrivalPointDetails>
                  <locationId>{route.arriving_to}</locationId>
               </arrivalPointDetails>
            </arrivalLocalization>
            <timeDetails>
               <firstDateTimeDetail>
                  <date>{route.date}</date>
               </firstDateTimeDetail>
            </timeDetails>
         </itinerary>"""

    return f"""
        <soap:Envelope 
            xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
            xmlns:wss="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
            xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
            xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" 
            xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" 
            xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" 
            xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" 
            xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" 
            xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3">
        
           <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
              <add:MessageID>WbsConsu-{message_id}</add:MessageID>
              <add:Action>{action}</add:Action>
              <add:To>{settings.AMADEUS_CONFIG['ENDPOINT']}</add:To>
              <oas:Security xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
                            xmlns:oas1="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
                 <oas:UsernameToken oas1:Id="UsernameToken-1">
                    <oas:Username>{settings.AMADEUS_CONFIG['USERNAME']}</oas:Username>
                    <oas:Nonce EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">
                        {nonce}
                    </oas:Nonce>
                    <oas:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest">
                        {password_digest}
                    </oas:Password>
                    <oas1:Created>{created_at}</oas1:Created>
                </oas:UsernameToken>
              </oas:Security>
              <AMA_SecurityHostedUser xmlns="http://xml.amadeus.com/2010/06/Security_v1">
                 <UserID AgentDutyCode="SU" RequestorType="U" PseudoCityCode="{settings.AMADEUS_CONFIG.get('OFFICE_ID')}" POS_Type="1"/>
              </AMA_SecurityHostedUser>
              <awsse:Session TransactionStatusCode="Start" xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3"/>
            </soapenv:Header>
        
           <soapenv:Body>
              <Fare_MasterPricerTravelBoardSearch>
                 <numberOfUnit>
                    <unitNumberDetail>
                       <numberOfUnits>{len(passengers) - len(infants)}</numberOfUnits>
                       <typeOfUnit>PX</typeOfUnit>
                    </unitNumberDetail>
                    <unitNumberDetail>
                       <numberOfUnits>100</numberOfUnits>
                       <typeOfUnit>RC</typeOfUnit>
                    </unitNumberDetail>
                 </numberOfUnit>
                 {passengers_query}
                 <fareOptions>
                    <pricingTickInfo>
                       <pricingTicketing>
                          <priceType>ET</priceType>
                          <priceType>RP</priceType>
                          <priceType>RU</priceType>
                          <priceType>TAC</priceType>
                          <priceType>XND</priceType>
                          <priceType>XLA</priceType>
                          <priceType>XLO</priceType>
                          <priceType>XLC</priceType>
                          <priceType>XND</priceType>
                       </pricingTicketing>
                    </pricingTickInfo>
                 </fareOptions>
                 <travelFlightInfo>
                    <companyIdentity>
                        <carrierQualifier>X</carrierQualifier>
                        <carrierId>NK</carrierId>
                        <carrierId>F9</carrierId>
                    </companyIdentity>
                    <flightDetail>
                        <flightType>N</flightType>
                    </flightDetail>
                 </travelFlightInfo>
                 {itinerary_query}
              </Fare_MasterPricerTravelBoardSearch>
           </soapenv:Body>
        </soap:Envelope>
    """


FLIGHT_INFORMATIVE_PRICING_WITHOUT_PNR_QUERY = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3">
       <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
            <add:MessageID>WbsConsu-{MESSAGE_ID}</add:MessageID>
            <add:Action>{ACTION}</add:Action>
            <add:To>{TO}</add:To>
            <oas:Security xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:oas1="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
                <oas:UsernameToken oas1:Id="UsernameToken-1">
                    <oas:Username>{USERNAME}</oas:Username>
                    <oas:Nonce EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">{NONCE}</oas:Nonce>
                    <oas:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest">{PASSWORD_DIGEST}</oas:Password>
                    <oas1:Created>{CREATED_AT}</oas1:Created>
                </oas:UsernameToken>
            </oas:Security>
            <AMA_SecurityHostedUser xmlns="http://xml.amadeus.com/2010/06/Security_v1">
                <UserID AgentDutyCode="SU" RequestorType="U" PseudoCityCode="{OFFICE_ID}" POS_Type="1"/>
            </AMA_SecurityHostedUser>
            <awsse:Session TransactionStatusCode="Start" xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3"/>
        </soapenv:Header>
       <soapenv:Body>
          <Fare_InformativePricingWithoutPNR>
             <passengersGroup>
                <segmentRepetitionControl>
                   <segmentControlDetails>
                      <quantity>1</quantity>
                      <numberOfUnits>2</numberOfUnits>
                   </segmentControlDetails>
                </segmentRepetitionControl>
                <travellersID>
                   <travellerDetails>
                      <measurementValue>1</measurementValue>
                   </travellerDetails>
                   <travellerDetails>
                      <measurementValue>2</measurementValue>
                   </travellerDetails>
                </travellersID>
                <discountPtc>
                   <valueQualifier>ADT</valueQualifier>
                </discountPtc>
             </passengersGroup>
             <segmentGroup>
                <segmentInformation>
                   <flightDate>
                      <departureDate>130825</departureDate>
                      <departureTime>2250</departureTime>
                   </flightDate>
                   <boardPointDetails>
                      <trueLocationId>HAV</trueLocationId>
                   </boardPointDetails>
                   <offpointDetails>
                      <trueLocationId>SCU</trueLocationId>
                   </offpointDetails>
                   <companyDetails>
                      <marketingCompany>CU</marketingCompany>
                   </companyDetails>
                   <flightIdentification>
                      <flightNumber>470</flightNumber>
                      <bookingClass>K</bookingClass>
                   </flightIdentification>
                   <flightTypeDetails>
                      <flightIndicator>1</flightIndicator>
                   </flightTypeDetails>
                   <itemNumber>1</itemNumber>
                </segmentInformation>
             </segmentGroup>
             <segmentGroup>
                <segmentInformation>
                   <flightDate>
                      <departureDate>200825</departureDate>
                      <departureTime>1945</departureTime>
                   </flightDate>
                   <boardPointDetails>
                      <trueLocationId>SCU</trueLocationId>
                   </boardPointDetails>
                   <offpointDetails>
                      <trueLocationId>HAV</trueLocationId>
                   </offpointDetails>
                   <companyDetails>
                      <marketingCompany>CU</marketingCompany>
                   </companyDetails>
                   <flightIdentification>
                      <flightNumber>471</flightNumber>
                      <bookingClass>R</bookingClass>
                   </flightIdentification>
                   <flightTypeDetails>
                      <flightIndicator>2</flightIndicator>
                   </flightTypeDetails>
                   <itemNumber>2</itemNumber>
                </segmentInformation>
             </segmentGroup>
              <pricingOptionGroup>
                <pricingOptionKey>
                  <pricingOptionKey>RP</pricingOptionKey>
                </pricingOptionKey>
            </pricingOptionGroup>
            <pricingOptionGroup>
                <pricingOptionKey>
                  <pricingOptionKey>RU</pricingOptionKey>
                </pricingOptionKey>
            </pricingOptionGroup>
             <pricingOptionGroup>
                <pricingOptionKey>
                  <pricingOptionKey>RLO</pricingOptionKey>
                </pricingOptionKey>
            </pricingOptionGroup>
            <pricingOptionGroup>
            <pricingOptionKey>
                <pricingOptionKey>VC</pricingOptionKey>
            </pricingOptionKey>
            <carrierInformation>
                <companyIdentification>
                    <otherCompany>CU</otherCompany>
                </companyIdentification>
            </carrierInformation>
        </pricingOptionGroup>
          </Fare_InformativePricingWithoutPNR>
       </soapenv:Body>
    </soapenv:Envelope>
"""

FLIGHT_CHECK_RULES_QUERY = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3">
       <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
            <add:MessageID>{MESSAGE_ID}</add:MessageID>
            <add:Action>{ACTION}</add:Action>
            <add:To>{TO}</add:To>
            <awsse:Session TransactionStatusCode="InSeries" xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3">
                <awsse:SessionId>{SESSION_ID}</awsse:SessionId>
                <awsse:SequenceNumber>{SEQUENCE_NUMBER}</awsse:SequenceNumber>
                <awsse:SecurityToken>{SECURITY_TOKEN}</awsse:SecurityToken>
            </awsse:Session>
        </soapenv:Header>
       <soapenv:Body>
            <Fare_CheckRules>
                <msgType>
                    <messageFunctionDetails>
                        <messageFunction>712</messageFunction>
                    </messageFunctionDetails>
                </msgType>
                <itemNumber>
                    <itemNumberDetails>
                        <number>1</number>
                    </itemNumberDetails>
                    <itemNumberDetails>
                        <number>1</number>
                        <type>FC</type>
                    </itemNumberDetails>
                </itemNumber>
                <fareRule>
                    <tarifFareRule>
                        <ruleSectionId>PE</ruleSectionId>
                        <ruleSectionId>MX</ruleSectionId>
                        <ruleSectionId>SR</ruleSectionId>
                        <ruleSectionId>TR</ruleSectionId>
                        <ruleSectionId>AP</ruleSectionId>
                        <ruleSectionId>FL</ruleSectionId>
                    </tarifFareRule>
                </fareRule>
            </Fare_CheckRules>
       </soapenv:Body>
    </soapenv:Envelope>
"""

FLIGHT_SIGNOUT_QUERY = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3" xmlns:vls="http://xml.amadeus.com/VLSSOQ_04_1_1A">
       <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
            <add:MessageID>{MESSAGE_ID}</add:MessageID>
            <add:Action>{ACTION}</add:Action>
            <add:To>{TO}</add:To>
            <awsse:Session TransactionStatusCode="End" xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3">
                <awsse:SessionId>{SESSION_ID}</awsse:SessionId>
                <awsse:SequenceNumber>{SEQUENCE_NUMBER}</awsse:SequenceNumber>
                <awsse:SecurityToken>{SECURITY_TOKEN}</awsse:SecurityToken>
            </awsse:Session>
        </soapenv:Header>
       <soapenv:Body>
          <Security_SignOut></Security_SignOut>
       </soapenv:Body>
    </soapenv:Envelope>
"""

FLIGHT_RESERVE_QUERY = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3">
       <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
            <add:MessageID>{MESSAGE_ID}</add:MessageID>
            <add:Action>{ACTION}</add:Action>
            <add:To>{TO}</add:To>
            <oas:Security xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:oas1="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
                <oas:UsernameToken oas1:Id="UsernameToken-1">
                    <oas:Username>{USERNAME}</oas:Username>
                    <oas:Nonce EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">{NONCE}</oas:Nonce>
                    <oas:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest">{PASSWORD_DIGEST}</oas:Password>
                    <oas1:Created>{CREATED_AT}</oas1:Created>
                </oas:UsernameToken>
            </oas:Security>
            <AMA_SecurityHostedUser xmlns="http://xml.amadeus.com/2010/06/Security_v1">
                <UserID AgentDutyCode="SU" RequestorType="U" PseudoCityCode="{OFFICE_ID}" POS_Type="1"/>
            </AMA_SecurityHostedUser>
            <awsse:Session TransactionStatusCode="Start" xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3"/>
        </soapenv:Header>
       <soapenv:Body>
          <Air_SellFromRecommendation>
             <messageActionDetails>
                <messageFunctionDetails>
                   <messageFunction>183</messageFunction>
                   <additionalMessageFunction>M1</additionalMessageFunction>
                </messageFunctionDetails>
             </messageActionDetails>
             <itineraryDetails>
                <originDestinationDetails>
                   <origin>HAV</origin>
                   <destination>SCU</destination>
                </originDestinationDetails>
                <message>
                   <messageFunctionDetails>
                      <messageFunction>183</messageFunction>
                   </messageFunctionDetails>
                </message>
                <segmentInformation>
                   <travelProductInformation>
                      <flightDate>
                         <departureDate>130825</departureDate>
                      </flightDate>
                      <boardPointDetails>
                         <trueLocationId>HAV</trueLocationId>
                      </boardPointDetails>
                      <offpointDetails>
                         <trueLocationId>SCU</trueLocationId>
                      </offpointDetails>
                      <companyDetails>
                         <marketingCompany>CU</marketingCompany>
                      </companyDetails>
                      <flightIdentification>
                         <flightNumber>470</flightNumber>
                         <bookingClass>K</bookingClass>
                      </flightIdentification>
                   </travelProductInformation>
                   <relatedproductInformation>
                      <quantity>2</quantity>
                      <statusCode>NN</statusCode>
                   </relatedproductInformation>
                </segmentInformation>
             </itineraryDetails>
             <itineraryDetails>
                <originDestinationDetails>
                   <origin>SCU</origin>
                   <destination>HAV</destination>
                </originDestinationDetails>
                <message>
                   <messageFunctionDetails>
                      <messageFunction>183</messageFunction>
                   </messageFunctionDetails>
                </message>
                <segmentInformation>
                   <travelProductInformation>
                      <flightDate>
                         <departureDate>200825</departureDate>
                      </flightDate>
                      <boardPointDetails>
                         <trueLocationId>SCU</trueLocationId>
                      </boardPointDetails>
                      <offpointDetails>
                         <trueLocationId>HAV</trueLocationId>
                      </offpointDetails>
                      <companyDetails>
                         <marketingCompany>CU</marketingCompany>
                      </companyDetails>
                      <flightIdentification>
                         <flightNumber>471</flightNumber>
                         <bookingClass>R</bookingClass>
                      </flightIdentification>
                   </travelProductInformation>
                   <relatedproductInformation>
                      <quantity>2</quantity>
                      <statusCode>NN</statusCode>
                   </relatedproductInformation>
                </segmentInformation>
             </itineraryDetails>
          </Air_SellFromRecommendation>
       </soapenv:Body>
    </soapenv:Envelope>
"""

FLIGHT_ADD_PASSENGERS_QUERY = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3">
       <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
            <add:MessageID>{MESSAGE_ID}</add:MessageID>
            <add:Action>{ACTION}</add:Action>
            <add:To>{TO}</add:To>
            <awsse:Session TransactionStatusCode="InSeries" xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3">
                <awsse:SessionId>{SESSION_ID}</awsse:SessionId>
                <awsse:SequenceNumber>{SEQUENCE_NUMBER}</awsse:SequenceNumber>
                <awsse:SecurityToken>{SECURITY_TOKEN}</awsse:SecurityToken>
            </awsse:Session>
        </soapenv:Header>
       <soapenv:Body>
        <PNR_AddMultiElements>
             <pnrActions>
                <optionCode>0</optionCode>
             </pnrActions>
           <travellerInfo>
                <elementManagementPassenger>
                   <reference>
                      <qualifier>PR</qualifier>
                      <number>1</number>
                   </reference>
                   <segmentName>NM</segmentName>
                </elementManagementPassenger>
                <passengerData>
                   <travellerInformation>
                      <traveller>
                         <surname>Doe</surname>
                         <quantity>1</quantity>
                      </traveller>
                      <passenger>
                         <firstName>John</firstName>
                         <type>ADT</type>
                      </passenger>
                   </travellerInformation>
                   <dateOfBirth>
                      <dateAndTimeDetails>
                         <date>01JAN80</date>
                      </dateAndTimeDetails>
                   </dateOfBirth>
                </passengerData>
             </travellerInfo>
             <travellerInfo>
                <elementManagementPassenger>
                   <reference>
                      <qualifier>PR</qualifier>
                      <number>2</number>
                   </reference>
                   <segmentName>NM</segmentName>
                </elementManagementPassenger>
                <passengerData>
                   <travellerInformation>
                      <traveller>
                         <surname>Roe</surname>
                         <quantity>1</quantity>
                      </traveller>
                      <passenger>
                         <firstName>Richard</firstName>
                         <type>ADT</type>
                      </passenger>
                   </travellerInformation>
                   <dateOfBirth>
                      <dateAndTimeDetails>
                         <date>01JAN80</date>
                      </dateAndTimeDetails>
                   </dateOfBirth>
                </passengerData>
             </travellerInfo>
             <dataElementsMaster>
                <marker1/>
                <dataElementsIndiv>
                   <elementManagementData>
                      <segmentName>RF</segmentName>
                   </elementManagementData>
                   <freetextData>
                      <freetextDetail>
                         <subjectQualifier>3</subjectQualifier>
                         <type>P22</type>
                      </freetextDetail>
                      <longFreetext>{OFFICE_ID}</longFreetext>
                   </freetextData>
                </dataElementsIndiv>
                <dataElementsIndiv>
                   <elementManagementData>
                      <segmentName>OP</segmentName>
                   </elementManagementData>
                   <optionElement>
                      <optionDetail>
                         <officeId>{OFFICE_ID}</officeId>
                      </optionDetail>
                   </optionElement>
                </dataElementsIndiv>
                <dataElementsIndiv>
                   <elementManagementData>
                      <segmentName>AP</segmentName>
                   </elementManagementData>
                   <freetextData>
                      <freetextDetail>
                         <subjectQualifier>3</subjectQualifier>
                         <type>6</type>
                      </freetextDetail>
                      <longFreetext>01232456346</longFreetext>
                   </freetextData>
                </dataElementsIndiv>
                <dataElementsIndiv>
                   <elementManagementData>
                      <segmentName>AP</segmentName>
                   </elementManagementData>
                   <freetextData>
                      <freetextDetail>
                         <subjectQualifier>3</subjectQualifier>
                         <type>7</type>
                      </freetextDetail>
                      <longFreetext>07890123456</longFreetext>
                   </freetextData>
                </dataElementsIndiv>
                <dataElementsIndiv>
                   <elementManagementData>
                      <segmentName>AP</segmentName>
                   </elementManagementData>
                   <freetextData>
                      <freetextDetail>
                         <subjectQualifier>3</subjectQualifier>
                         <type>P02</type>
                      </freetextDetail>
                      <longFreetext>test@test.com</longFreetext>
                   </freetextData>
                </dataElementsIndiv>
                <dataElementsIndiv>
                   <elementManagementData>
                      <segmentName>TK</segmentName>
                   </elementManagementData>
                   <ticketElement>
                      <ticket>
                         <indicator>OK</indicator>
                      </ticket>
                   </ticketElement>
                </dataElementsIndiv>            
                
                <dataElementsIndiv>
                 <elementManagementData>
                  <segmentName>SSR</segmentName>
                 </elementManagementData>
                 <serviceRequest>
                  <ssr>
                   <type>CTCE</type>
                   <status>HK</status>
                   <companyId>YY</companyId>
                   <freetext>test//test.com</freetext>
                  </ssr>
                 </serviceRequest>
              </dataElementsIndiv>
              <dataElementsIndiv>
                 <elementManagementData>
                  <segmentName>SSR</segmentName>
                 </elementManagementData>
                 <serviceRequest>
                  <ssr>
                   <type>CTCM</type>
                   <status>HK</status>
                   <companyId>YY</companyId>
                   <freetext>19876543210/US</freetext>
                  </ssr>
                 </serviceRequest>
              </dataElementsIndiv>
              <dataElementsIndiv>
                <elementManagementData>
                    <reference>
                        <qualifier>OT</qualifier>
                        <number>1</number>
                    </reference>
                    <segmentName>FM</segmentName>
                </elementManagementData>
                <commission>
                    <commissionInfo>
                        <percentage>5</percentage>
                    </commissionInfo>
                </commission>	 
              </dataElementsIndiv>
             </dataElementsMaster>
          </PNR_AddMultiElements>
       </soapenv:Body>
    </soapenv:Envelope>
"""

ADD_CASH_PAYMENT_QUERY = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3" xmlns:tfop="http://xml.amadeus.com/TFOPCQ_19_2_1A">
       <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
           <add:MessageID>{MESSAGE_ID}</add:MessageID>
           <add:Action>{ACTION}</add:Action>
           <add:To>{TO}</add:To>
           <awsse:Session TransactionStatusCode="InSeries" xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3">
               <awsse:SessionId>{SESSION_ID}</awsse:SessionId>
               <awsse:SequenceNumber>{SEQUENCE_NUMBER}</awsse:SequenceNumber>
               <awsse:SecurityToken>{SECURITY_TOKEN}</awsse:SecurityToken>
           </awsse:Session>
       </soapenv:Header>
       <soapenv:Body>     
        <FOP_CreateFormOfPayment>
          <transactionContext>
            <transactionDetails>
              <code>FP</code>
            </transactionDetails>
          </transactionContext>
          <fopGroup>
            <fopReference/>
            <mopDescription>
              <fopSequenceNumber>
                <sequenceDetails>
                  <number>1</number>
                </sequenceDetails>
              </fopSequenceNumber>
              <mopDetails>
                <fopPNRDetails>
                  <fopDetails>
                    <fopCode>CASH</fopCode>
                  </fopDetails>
                </fopPNRDetails>
              </mopDetails>
            </mopDescription>
          </fopGroup>
        </FOP_CreateFormOfPayment>
       </soapenv:Body>
    </soapenv:Envelope>
"""

FARE_PRICE_PNR_WITH_BOOKING_CLASS_QUERY = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3">
   <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
        <add:MessageID>{MESSAGE_ID}</add:MessageID>
        <add:Action>{ACTION}</add:Action>
        <add:To>{TO}</add:To>
        <awsse:Session TransactionStatusCode="InSeries" xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3">
            <awsse:SessionId>{SESSION_ID}</awsse:SessionId>
            <awsse:SequenceNumber>{SEQUENCE_NUMBER}</awsse:SequenceNumber>
            <awsse:SecurityToken>{SECURITY_TOKEN}</awsse:SecurityToken>
        </awsse:Session>
    </soapenv:Header>
       <soapenv:Body>
          <Fare_PricePNRWithBookingClass>
             <pricingOptionGroup>
                <pricingOptionKey>
                   <pricingOptionKey>RP</pricingOptionKey>
                </pricingOptionKey>
             </pricingOptionGroup>
             <pricingOptionGroup>
                <pricingOptionKey>
                   <pricingOptionKey>RU</pricingOptionKey>
                </pricingOptionKey>
             </pricingOptionGroup>
             <pricingOptionGroup>
                <pricingOptionKey>
                  <pricingOptionKey>RLO</pricingOptionKey>
                </pricingOptionKey>
            </pricingOptionGroup>
            <pricingOptionGroup>
            <pricingOptionKey>
                <pricingOptionKey>VC</pricingOptionKey>
            </pricingOptionKey>
            <carrierInformation>
                <companyIdentification>
                    <otherCompany>CU</otherCompany>
                </companyIdentification>
            </carrierInformation>
        </pricingOptionGroup>        
          </Fare_PricePNRWithBookingClass>
       </soapenv:Body>
    </soapenv:Envelope>
"""

TICKET_CREATE_TST_FROM_PRICING_QUERY = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3">
       <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
        <add:MessageID>{MESSAGE_ID}</add:MessageID>
        <add:Action>{ACTION}</add:Action>
        <add:To>{TO}</add:To>
        <awsse:Session TransactionStatusCode="InSeries" xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3">
            <awsse:SessionId>{SESSION_ID}</awsse:SessionId>
            <awsse:SequenceNumber>{SEQUENCE_NUMBER}</awsse:SequenceNumber>
            <awsse:SecurityToken>{SECURITY_TOKEN}</awsse:SecurityToken>
        </awsse:Session>
    </soapenv:Header>
       <soapenv:Body>
          <Ticket_CreateTSTFromPricing>
             <psaList>
                <itemReference>
                   <referenceType>TST</referenceType>
                   <uniqueReference>1</uniqueReference>
                </itemReference>
             </psaList>
          </Ticket_CreateTSTFromPricing>
       </soapenv:Body>
    </soapenv:Envelope>
"""

PNR_ADD_MULTIELEMENTS_QUERY = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3">
       <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
        <add:MessageID>{MESSAGE_ID}</add:MessageID>
        <add:Action>{ACTION}</add:Action>
        <add:To>{TO}</add:To>
        <awsse:Session TransactionStatusCode="InSeries" xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3">
            <awsse:SessionId>{SESSION_ID}</awsse:SessionId>
            <awsse:SequenceNumber>{SEQUENCE_NUMBER}</awsse:SequenceNumber>
            <awsse:SecurityToken>{SECURITY_TOKEN}</awsse:SecurityToken>
        </awsse:Session>
    </soapenv:Header>
       <soapenv:Body>
          <PNR_AddMultiElements>
             <pnrActions>
                <optionCode>10</optionCode>
             </pnrActions>
             <dataElementsMaster>
                <marker1/>
                <dataElementsIndiv>
                   <elementManagementData>
                      <segmentName>RF</segmentName>
                   </elementManagementData>
                   <freetextData>
                      <freetextDetail>
                         <subjectQualifier>3</subjectQualifier>
                         <type>P22</type>
                      </freetextDetail>
                      <longFreetext>{OFFICE_ID}</longFreetext>
                   </freetextData>
                </dataElementsIndiv>
             </dataElementsMaster>
          </PNR_AddMultiElements>
       </soapenv:Body>
    </soapenv:Envelope>
"""

PNR_RETRIEVE_QUERY = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3">
       <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
        <add:MessageID>{MESSAGE_ID}</add:MessageID>
        <add:Action>{ACTION}</add:Action>
        <add:To>{TO}</add:To>
        <oas:Security xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:oas1="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
            <oas:UsernameToken oas1:Id="UsernameToken-1">
                <oas:Username>{USERNAME}</oas:Username>
                <oas:Nonce EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">{NONCE}</oas:Nonce>
                <oas:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest">{PASSWORD_DIGEST}</oas:Password>
                <oas1:Created>{CREATED_AT}</oas1:Created>
            </oas:UsernameToken>
        </oas:Security>
        <AMA_SecurityHostedUser xmlns="http://xml.amadeus.com/2010/06/Security_v1">
            <UserID AgentDutyCode="SU" RequestorType="U" PseudoCityCode="{OFFICE_ID}" POS_Type="1"/>
        </AMA_SecurityHostedUser>
        <awsse:Session TransactionStatusCode="Start" xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3"/>
    </soapenv:Header>
       <soapenv:Body>
          <PNR_Retrieve>
             <retrievalFacts>
                <retrieve>
                   <type>2</type>
                </retrieve>
                <reservationOrProfileIdentifier>
                   <reservation>
                      <controlNumber>{LOCATOR}</controlNumber>
                   </reservation>
                </reservationOrProfileIdentifier>
             </retrievalFacts>
          </PNR_Retrieve>
       </soapenv:Body>
    </soapenv:Envelope>
"""

ISSUE_TICKET_QUERY = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3">
       <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
        <add:MessageID>{MESSAGE_ID}</add:MessageID>
        <add:Action>{ACTION}</add:Action>
        <add:To>{TO}</add:To>
        <awsse:Session TransactionStatusCode="InSeries" xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3">
            <awsse:SessionId>{SESSION_ID}</awsse:SessionId>
            <awsse:SequenceNumber>{SEQUENCE_NUMBER}</awsse:SequenceNumber>
            <awsse:SecurityToken>{SECURITY_TOKEN}</awsse:SecurityToken>
        </awsse:Session>
    </soapenv:Header>
       <soapenv:Body>
          <DocIssuance_IssueTicket>
            <optionGroup>
               <switches>
                <statusDetails>
                    <indicator>ET</indicator>
                </statusDetails>
               </switches>
            </optionGroup>         
             <optionGroup>
                <switches>
                   <statusDetails>
                      <indicator>RT</indicator>
                   </statusDetails>
                </switches>
             </optionGroup>
             <otherCompoundOptions>
                    <attributeDetails>
                        <attributeType>ETC</attributeType>
                            <attributeDescription>CU</attributeDescription>
                    </attributeDetails>
                </otherCompoundOptions>         		
          </DocIssuance_IssueTicket>
       </soapenv:Body>
    </soapenv:Envelope>
"""

PNR_RETRIEVE_ISSUED_QUERY = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sec="http://xml.amadeus.com/2010/06/Security_v1" xmlns:typ="http://xml.amadeus.com/2010/06/Types_v1" xmlns:iat="http://www.iata.org/IATA/2007/00/IATA2010.1" xmlns:app="http://xml.amadeus.com/2010/06/AppMdw_CommonTypes_v3" xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1" xmlns:ses="http://xml.amadeus.com/2010/06/Session_v3">
       <soapenv:Header xmlns:add="http://www.w3.org/2005/08/addressing">
        <add:MessageID>{MESSAGE_ID}</add:MessageID>
        <add:Action>{ACTION}</add:Action>
        <add:To>{TO}</add:To>
        <awsse:Session TransactionStatusCode="InSeries" xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3">
            <awsse:SessionId>{SESSION_ID}</awsse:SessionId>
            <awsse:SequenceNumber>{SEQUENCE_NUMBER}</awsse:SequenceNumber>
            <awsse:SecurityToken>{SECURITY_TOKEN}</awsse:SecurityToken>
        </awsse:Session>
    </soapenv:Header>
       <soapenv:Body>
          <PNR_Retrieve>
              <retrievalFacts>
                <retrieve>
                   <type>1</type>
                </retrieve>
             </retrievalFacts>
          </PNR_Retrieve>
       </soapenv:Body>
    </soapenv:Envelope>
"""

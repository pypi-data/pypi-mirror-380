import requests
import xmltodict


class AmadeusSDK:

    @staticmethod
    def execute(url, query, http_headers=None, timeout=10, convert_to_json=True, show_traces=False):
        if not http_headers:
            http_headers = {}
        http_headers.update({
            'Content-Type': 'application/soap+xml; charset=utf-8'
        })

        if show_traces:
            print(url)
            print(query)
            print(http_headers)

        response = requests.post(
            url,
            data=query.encode('utf-8'),
            headers=http_headers,
            timeout=timeout
        )

        if show_traces:
            print(response.text)

        if not convert_to_json:
            return response.status_code, response

        return response.status_code, xmltodict.parse(response.text)

    @staticmethod
    def extract_session_id(data):
        return data.get('soapenv:Envelope', {}).get('soapenv:Header', {}).get('awsse:Session', {}).get(
            'awsse:SessionId')

    @staticmethod
    def extract_security_token(data):
        return data.get('soapenv:Envelope', {}).get('soapenv:Header', {}).get('awsse:Session', {}).get(
            'awsse:SecurityToken')

    @staticmethod
    def extract_pnr_from_ticket_generator(data):
        return data.get('soapenv:Envelope', {}).get('soapenv:Body', {}).get('PNR_Reply', {}).get(
            'pnrHeader', {}).get('reservationInfo', {}).get('reservation', {}).get('controlNumber')

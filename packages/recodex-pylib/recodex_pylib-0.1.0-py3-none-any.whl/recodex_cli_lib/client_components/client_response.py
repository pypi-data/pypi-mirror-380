import json
import yaml

from ..generated.swagger_client.rest import RESTResponse


class ClientResponse():
    """Wrapper object containing the request response.
    """

    def __init__(self, response: RESTResponse):
        self.urllib3_response = response.urllib3_response
        self.status = response.status
        self.reason = response.reason
        self.data_binary = response.data
        self.headers = response.getheaders()
        self.data = response.data.decode("utf-8")

    def __get_parsed_data_or_throw(self) -> dict:
        return json.loads(self.data)

    def get_parsed_data(self) -> dict | None:
        """Parses response payload and returns a dictionary or None if the parsing failed.

        Returns:
            dict|None: A dictionary constructed from the payload, or None if the data is not in JSON format.
        """
        try:
            return self.__get_parsed_data_or_throw()
        except:
            return None

    def get_json_string(self, minimized: bool = False) -> str:
        """Returns the response data as a JSON string.

        Args:
            minimized (bool, optional): Whether the returned string should be a single-line JSON. Defaults to False.

        Raises:
            Exception: Thrown when the response data could not be parsed.

        Returns:
            str: Returns the response data as a JSON string.
        """

        if minimized:
            return self.data
        try:
            return json.dumps(self.__get_parsed_data_or_throw(), indent=2, ensure_ascii=False)
        except:
            raise Exception("The response data is not in JSON format.")

    def get_yaml_string(self, minimized: bool = False) -> str:
        """Returns the response data as a YAML string.

        Args:
            minimized (bool, optional): Whether the returned string should be a minimized YAML. Defaults to False.

        Raises:
            Exception: Thrown when the response data could not be parsed.

        Returns:
            str: Returns the response data as a YAML string.
        """
        try:
            if minimized:
                return yaml.dump(
                    self.__get_parsed_data_or_throw(),
                    default_flow_style=True,
                    indent=None,
                    allow_unicode=True
                )
            return yaml.dump(self.__get_parsed_data_or_throw(), allow_unicode=True, indent=2)
        except:
            raise Exception("The response data could not be converted to YAML.")

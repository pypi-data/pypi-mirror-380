import curl_cffi
import time
import random
import logging
import pandas  as pd
import os
from .errors import (
    ConfigurationError, HTTPStatusError, MaxRetriesExceeded,
    NotADictError, MissingFieldError, CSVWriteError, ExcelWriteError
)

class MFDevScraper:

    def __init__(self):
        self.__log = logging.getLogger("mfdev")
        self.__log.setLevel(logging.INFO)
        if not self.__log.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter("[%(levelname)s] %(message)s")
            handler.setFormatter(formatter)
            self.__log.addHandler(handler)

    def request_mfdev(self,method:str='GET',status_code_accepted:int=200, url:str=None, proxies:dict={}, headers:dict={},params:dict={}, cookies:dict={},payload:dict={}, timeout:float=20.0, verify:bool=True, impersonate:str='chrome', max_retries:int=3):

        """
        Perform an HTTP request with retry logic using curl_cffi.

        This method sends an HTTP request (GET or POST) to the specified URL and
        automatically retries on failure up to `max_retries` times. It validates
        the response against the expected `status_code_accepted` and raises custom
        errors when conditions are not met.

        Args:
            method (str, optional): HTTP method to use ("GET" or "POST").
                Defaults to "GET".
            status_code_accepted (int, optional): Expected successful status code.
                Defaults to 200.
            url (str, optional): Target URL. Required.
            proxies (dict, optional): Proxy configuration for the request.
                Defaults to empty dict.
            headers (dict, optional): HTTP headers to include in the request.
                Defaults to empty dict.
            cookies (dict, optional): Cookies to include in the request.
                Defaults to empty dict.
            timeout (float, optional): Timeout in seconds for the request.
                Defaults to 20.0.
            verify (bool, optional): Whether to verify SSL certificates.
                Defaults to True.
            impersonate (str, optional): Browser profile to impersonate (as supported
                by curl_cffi). Defaults to "chrome".
            max_retries (int, optional): Maximum number of retry attempts.
                Defaults to 3.

        Returns:
            curl_cffi.requests.Response: Response object if the request succeeds.

        Raises:
            ConfigurationError: If the URL is not provided.
            HTTPStatusError: If the response status code is not equal to `status_code_accepted`.
            MaxRetriesExceeded: If the maximum number of retries is reached without success.

        Notes:
            - Each retry waits a random interval (3–6 seconds) before retrying.
            - Logs warnings for each failed attempt.
        """

        if not url:
            raise ConfigurationError("The URL is required.")

        time.sleep(0.1)
        attemp = 0
        while attemp < max_retries:
            try:

                match(method.lower()):

                    case 'get':
                        response = curl_cffi.get(url=url, headers=headers,
                                            verify=verify, proxies=proxies,cookies=cookies,data=payload, params=params, timeout=timeout, impersonate=impersonate)
                    case 'post':
                        response = curl_cffi.post(url=url, headers=headers,
                                            verify=verify, proxies=proxies,cookies=cookies,data=payload, params=params, timeout=timeout, impersonate=impersonate)

                
                status_code = response.status_code
                if status_code == status_code_accepted:
                    return response
                else:
                    raise HTTPStatusError(status_code, url=url)
            except Exception as e:
                attemp += 1
                self.__log.warning(
                    f"Trying to connect to: {url} - attempt: {attemp} - {e}")
                time.sleep((random.randint(a=3, b=6)))
        raise MaxRetriesExceeded(max_retries, url=url)
    

    def clean_duplicates_dict(self, records: dict,field:str='id', strict:bool= True)-> list[dict] | None:

        """
        Remove duplicate dictionaries from a list based on a unique field.

        Iterates over a list of dictionaries and returns a new list with duplicates
        removed. Duplicates are identified by the value of the specified `field`.
        Optionally enforces strict validation to raise errors when items are not
        dictionaries or the required field is missing.

        Args:
            records (dict): A list of dictionaries to process.
            field (str, optional): The key used to identify uniqueness.
                Defaults to "id".
            strict (bool, optional): If True, raises exceptions when an item is not
                a dictionary or when the field is missing. If False, skips invalid
                entries. Defaults to True.

        Returns:
            list[dict] | None: A list of dictionaries with duplicates removed, or
            None if no valid items were found.

        Raises:
            NotADictError: If an item is not a dictionary and `strict=True`.
            MissingFieldError: If a dictionary does not contain the specified field
                and `strict=True`.

        Example:
            >>> data = [{"id": 1, "name": "Alice"}, {"id": 1, "name": "Duplicate"}, {"id": 2, "name": "Bob"}]
            >>> scraper.clean_duplicates_dict(data)
            [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        """
            
        inspect = set()
        result = []
        for idx,item in enumerate(records):
            if not isinstance(item, dict):
                if strict:
                    raise NotADictError(index=idx)
                else:
                    continue
            if field not in item:
                if strict:
                    raise MissingFieldError(field, index=idx)
                else:
                    continue
            code = item.get(field)
            if code not in inspect:
                inspect.add(code)
                result.append(item)
        return result
    
    def generate_csv(self, records:dict, name:str, folder:str=None, codex:str='utf-8'):

        """
        Generate and save a CSV file from a list of dictionaries.

        Converts the given records into a pandas DataFrame and writes them to a CSV
        file. The output file is created in the specified folder or, by default,
        in the same directory as this module.

        Args:
            records (dict): A list of dictionaries to export as CSV.
            name (str): The name of the CSV file to create (e.g., "output.csv").
            codex (str, optional): File encoding for the CSV output.
                Defaults to "utf-8".
            folder (str, optional): Target directory for the CSV file.
                If None, uses the current module’s directory.

        Returns:
            str: The absolute path of the generated CSV file.

        Raises:
            CSVWriteError: If writing the file fails due to filesystem issues or
                invalid data.

        Example:
            >>> data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
            >>> scraper.generate_csv(data, "users.csv")
            '/absolute/path/to/users.csv'
        """
            

        try:
            if folder is None:
                folder = os.path.dirname(os.path.abspath(__file__))
            os.makedirs(folder, exist_ok=True)
            file_base, _ = os.path.splitext(name)
            path_file = os.path.join(folder, f"{file_base}.csv")
            df=pd.DataFrame(records)
            df.to_csv(path_file, index=False, encoding=codex)

            return path_file
        except Exception as e:
            raise CSVWriteError(path_file, reason=str(e)) from e

    def generate_excel(self, records:dict, name:str, folder:str=None):

        """
        Generate and save an Excel (.xlsx) file from a list of dictionaries.

        Converts the given records into a pandas DataFrame and writes them to an
        Excel file using the OpenPyXL engine. The output file is created in the
        specified folder or, by default, in the same directory as this module.

        Args:
            records (dict): A list of dictionaries to export as Excel.
            name (str): The name of the Excel file to create (e.g., "output.xlsx").
            folder (str, optional): Target directory for the Excel file.
                If None, uses the current module’s directory.

        Returns:
            str: The absolute path of the generated Excel file.

        Raises:
            ExcelWriteError: If writing the file fails due to filesystem issues or
                invalid data.

        Example:
            >>> data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
            >>> scraper.generate_excel(data, "users.xlsx")
            '/absolute/path/to/users.xlsx'
        """
            
        try:
            if folder is None:
                folder = os.path.dirname(os.path.abspath(__file__))
            os.makedirs(folder, exist_ok=True)
            file_base, _ = os.path.splitext(name)
            path_file = os.path.join(folder, f"{file_base}.xlsx")
            df=pd.DataFrame(records)
            df.to_excel(path_file, index=False, engine="openpyxl")
            
            return path_file
        except Exception as e:
            raise ExcelWriteError(path_file, reason=str(e)) from e
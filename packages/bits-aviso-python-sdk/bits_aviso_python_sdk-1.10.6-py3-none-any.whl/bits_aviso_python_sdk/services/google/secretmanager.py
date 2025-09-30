"""
This module provides a class to interact with Google Cloud Secret Manager. If no service account credentials are
provided, the SDK will attempt to use the default credentials.

## Usage
The following is an example of how to access a secret from Secret Manager:

```python
from bits_aviso_python_sdk.services.google.secretmanager import SecretManager

# initialize Secret Manager client
secret_manager_client = SecretManager()

# get secret
secret = secret_manager_client.get_secret("project_id", "your_secret_name")
print(secret)
```

---
"""
import json
import logging
import google.api_core.exceptions
import google.auth
import google.auth.exceptions
import google.auth.transport.requests
import requests
from google.cloud import secretmanager
from google.cloud.secretmanager_v1.types import SecretPayload
from bits_aviso_python_sdk.services.google import authenticate_google_service_account



class SecretManager:
	"""
	Provides an interface to Google Cloud Secret Manager for managing and retrieving secrets.
	If no service account credentials are provided, the SDK will attempt to use the default credentials.
	"""

	def __init__(self, service_account_credentials=None):
		"""
		Initialize the SecretManager class.

		Args:
			service_account_credentials (dict or str, optional): The service account credentials as a dict or path to the credentials file. If not provided, uses default credentials.
		"""
		self.client = secretmanager.SecretManagerServiceClient()

		if service_account_credentials:
			credentials = authenticate_google_service_account(service_account_credentials)
			self.client = secretmanager.SecretManagerServiceClient(credentials=credentials)
		else:
			try:
				self.client = secretmanager.SecretManagerServiceClient()

			except google.auth.exceptions.DefaultCredentialsError as e:
				logging.error(f"Unable to authenticate service account. {e}")
				self.publisher_client = None

	def add_secret_version(self, project_id, secret_name, payload):
		"""
		Add a new version to an existing secret in Secret Manager.

		Args:
			project_id (str): The project ID of the secret.
			secret_name (str): The name of the secret.
			payload (str): The secret data to add.

		Returns:
			str: The name of the new secret version.

		Raises:
			ValueError: If unable to add a new version to the secret.
		"""
		secret = self.client.secret_path(project_id, secret_name)
		payload = payload.encode("UTF-8")
		secret_payload = SecretPayload(data=payload)
		response = self.client.add_secret_version(parent=secret, payload=secret_payload)

		return response.name

	def get_secret(self, project_id, secret_name, secret_version="latest"):
		"""
		Retrieve the secret data from Secret Manager.

		Args:
			project_id (str): The project ID of the secret.
			secret_name (str): The name of the secret.
			secret_version (str, optional): The version of the secret. Defaults to "latest".

		Returns:
			str or dict: The secret data. If the secret is valid JSON, returns a dict; otherwise, returns a string.

		Raises:
			ValueError: If unable to get the secret from Secret Manager.
		"""
		try:
			secret = self.client.secret_version_path(project_id, secret_name, secret_version)
			response = self.client.access_secret_version(request={"name": secret})

			try:  # try to parse the secret data as json
				secret_data = json.loads(response.payload.data.decode("UTF-8"))

			except json.JSONDecodeError:  # if it fails, return the data as is
				secret_data = response.payload.data.decode("UTF-8")

			return secret_data

		except (google.api_core.exceptions.NotFound, google.api_core.exceptions.InvalidArgument) as e:
			message = f'Unable to get the secret {secret_name} from secret manager. {e} '
			logging.error(message)  # logging message

			raise ValueError(message)  # raise an error with the message


	@staticmethod
	def get_secret_rest(project_id, secret_name, secret_version="latest", timeout=60):
		"""
		Fetch a secret from Google Secret Manager using the REST API (no gRPC).
		Uses Application Default Credentials (ADC) for authentication.

		Args:
			project_id (str): GCP project ID.
			secret_name (str): Secret name.
			secret_version (str): Secret version (default: "latest").
			timeout (int, optional): Request timeout in seconds. Defaults to 60.

		Returns:
			str: Secret payload as a string.

		Raises:
			ValueError: If unable to fetch or decode the secret.
		"""
		try:
			# Get an access token using ADC
			credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
			auth_req = google.auth.transport.requests.Request()
			credentials.refresh(auth_req)
			access_token = credentials.token

			url = (
				f"https://secretmanager.googleapis.com/v1/projects/{project_id}/secrets/"
				f"{secret_name}/versions/{secret_version}:access"
			)
			headers = {
				"Authorization": f"Bearer {access_token}"
			}

			resp = requests.get(url, headers=headers, timeout=timeout)
			resp.raise_for_status()
			payload = resp.json()["payload"]["data"]
			import base64
			return base64.b64decode(payload).decode("utf-8")
		except Exception as e:
			logging.error(f"REST Secret Manager error for {secret_name}: {e}")
			raise ValueError(f"Unable to fetch secret '{secret_name}' from Secret Manager via REST: {e}")

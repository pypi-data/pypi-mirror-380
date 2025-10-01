"""Secrets class file."""

from google.cloud import secretmanager_v1beta1


class Secrets:
    """Secrets class."""

    def __init__(self, default_project=None, verbose=False):
        """Initialize an Secrets class instance."""
        self.client = None
        self.default_project = default_project
        self.verbose = verbose

    def _get_client(self):
        if not self.client:
            self.client = secretmanager_v1beta1.SecretManagerServiceClient()
        return self.client

    def resolve(self, params):
        """Resolves Secret Manager secrets included in a dict of params."""
        for k, v in params.items():

            if isinstance(v, str) and v.startswith('sm://'):
                # Check if we're using the default project
                if v.startswith('sm:///'):
                    project = self.default_project
                # Otherwise, get the project from the url
                else:
                    project = v.split('/')[2]

                # Get the secret_id from the url
                secret_id = v.split('/')[3]

                # Febuild the url with the project
                secret_url = f'sm://{project}/{secret_id}'

                # Display which key we're resolving if verbose is enabled
                if self.verbose:
                    print(f'Resolving {secret_url}...')

                # Get secret manager client
                client = self._get_client()

                # Generate the secret name using the project, id and "latest" version
                name = client.secret_version_path(project, secret_id, 'latest')

                # Access the secret version.
                response = client.access_secret_version(name=name)

                # Replace the key value with the cleartext secret.
                params[k] = response.payload.data.decode('utf-8')

        return params

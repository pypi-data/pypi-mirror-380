from .base import Connector
import boto3


class MinIOConnector(Connector):
    """A connector for MinIO that extends the base Connector class.
    It provides methods to connect, disconnect, check connection status, and retrieve connection information.
    Attributes:
        address (str): The MinIO server address.
        port (int): The port number for the MinIO server.
        target (str): The MinIO bucket name.
        access_key (str, optional): The access key for MinIO authentication.
        secret_key (str, optional): The secret key for MinIO authentication.
        region_name (str): The region name for MinIO, default is 'eu-west-1'.

    Methods:
        connect(): Connects to the MinIO server.
        disconnect(): Disconnects from the MinIO server.
        is_connected(): Checks if the connection to the MinIO server is active.
        get_connection_info(): Returns a dictionary with connection information.
        insert_object(object_name, data, content_type='image/png'): Inserts an object into the MinIO bucket.
        get_object(object_name): Retrieves an object from the MinIO bucket.

    """

    def __init__(
        self,
        address,
        port,
        target,
        access_key=None,
        secret_key=None,
        region_name="eu-west-1",
    ):
        super().__init__(address, port, target)
        self.access_key = access_key
        self.secret_key = secret_key
        self.region_name = region_name

    def connect(self):
        # Implementation for connecting to MinIO
        print("Connecting to MinIO...")
        try:
            # Add connection logic here
            self.s3_client = boto3.client(
                "s3",
                endpoint_url=f"http://{self.address}:{self.port}",
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key,
                region_name=self.region_name,
            )

            print(f"Connected to MinIO: {self.address}:{self.port}")

        except Exception as e:
            print(f"Failed to connect to MinIO: {str(e)}")
            raise e

    def disconnect(self):
        # Implementation for disconnecting from MinIO
        print("Disconnecting from MinIO...")
        self.s3_client = None
        print("Disconnected from MinIO.")

    def is_connected(self):
        # Check if the connection is active
        try:
            if self.s3_client is None:
                return False
            # Try a simple operation to verify connection
            self.s3_client.list_buckets()
            return True
        except Exception:
            return False

    def get_connection_info(self):
        # Return connection information
        return {
            "address": self.address,
            "port": self.port,
            "target": self.target,
            "region_name": self.region_name,
        }

    def insert_object(self, object_name, data, content_type="image/png"):
        # Insert an object into the MinIO bucket
        try:
            self.s3_client.put_object(
                Bucket=self.target, Key=object_name, Body=data, ContentType=content_type
            )
            print(f"Object '{object_name}' inserted into bucket '{self.target}'.")
        except Exception as e:
            print(f"Failed to insert object: {str(e)}")
            raise e

    def get_object(self, object_name):
        # Retrieve an object from the MinIO bucket
        try:
            response = self.s3_client.get_object(Bucket=self.target, Key=object_name)
            return response["Body"].read()
        except Exception as e:
            print(f"Failed to get object: {str(e)}")
            raise e
    
    # This method is used when data for one request are stored in the same folder. 
    # Method gets the objects that are needed for segmentation and returns them in a dictionary
    # Can be used by the models to run their predictions
    def get_folder_objects(self, folder_name):
        """
        Get objects from a folder and organize them by type (s1, s2, slope).
        
        Returns:
            dict: Dictionary with keys 's1', 's2', 'slope' containing object data
        """
        # Check if S3 client is properly initialized
        if self.s3_client is None:
            raise RuntimeError("S3 client is not initialized. Call connect() first.")
            
        try:
            api_response = self.s3_client.list_objects_v2(Bucket=self.target, Prefix=folder_name)
            
            if 'Contents' in api_response:
                objects = {}  # Don't overwrite the API response
                
                for obj in api_response['Contents']:
                    key = obj['Key']
                    match key.lower():  # Use lowercase for case-insensitive matching
                        case k if "s1" in k:
                            objects['s1'] = self.get_object(key)
                        case k if "s2" in k:
                            objects['s2'] = self.get_object(key)
                        case k if "slope" in k:
                            objects['slope'] = self.get_object(key)
                
                return objects
            else:
                return {}  # Return empty dict for consistency
        except Exception as e:
            print(f"Failed to list objects in folder '{folder_name}': {str(e)}")
            raise e
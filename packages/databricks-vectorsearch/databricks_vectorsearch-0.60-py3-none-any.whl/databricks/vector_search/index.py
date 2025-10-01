import json
import time
import datetime
import math
import deprecation
from databricks.vector_search.utils import OAuthTokenUtils
from databricks.vector_search.utils import RequestUtils
from databricks.vector_search.utils import UrlUtils
from databricks.vector_search.utils import CredentialStrategy
from databricks.vector_search.reranker import DatabricksReranker, Reranker
from mlflow.utils import databricks_utils
from databricks.vector_search.utils import (
    authentication_warning,
    get_model_serving_invoker_credentials,
)


class VectorSearchIndex:
    """
    VectorSearchIndex is a helper class that represents a Vector Search Index.

    Those who wish to use this class should not instantiate it directly, but rather use the VectorSearchClient class.
    """

    def __init__(
        self,
        workspace_url,
        index_url,
        name,
        endpoint_name,
        mlserving_endpoint_name=None,
        personal_access_token=None,
        service_principal_client_id=None,
        service_principal_client_secret=None,
        azure_tenant_id=None,
        azure_login_id=None,
        # whether or not credentials were explicitly passed in by user in client or inferred by client
        # via mlflow utilities. If passed in by user, continue to use user credentials. If not, can
        # attempt automatic auth refresh for model serving.
        use_user_passed_credentials=False,
        credential_strategy=None,
        get_reranker_url_callable=None,
        mlserving_endpoint_name_for_query=None
    ):
        self.workspace_url = workspace_url
        self.name = name
        self.endpoint_name = endpoint_name
        self.personal_access_token = personal_access_token
        self.service_principal_client_id = service_principal_client_id
        self.service_principal_client_secret = service_principal_client_secret
        self.index_url = _get_index_url(
            index_url,
            self.workspace_url,
            self.name,
            self.personal_access_token,
            self.service_principal_client_id,
            self.service_principal_client_secret,
        )
        self._index_url_ensure_reranker_compatible = None
        self._get_reranker_url_callable = get_reranker_url_callable
        self.azure_tenant_id = azure_tenant_id
        self.azure_login_id = azure_login_id
        self._control_plane_oauth_token = None
        self._control_plane_oauth_token_expiry_ts = None
        self._read_oauth_token = None
        self._read_oauth_token_expiry_ts = None
        self._write_oauth_token = None
        self._write_oauth_token_expiry_ts = None
        self._use_user_passed_credentials = use_user_passed_credentials
        # Initialize `mlserving_endpoint_id` as `_get_token_for_request` (a dependency of `_get_mlserving_endpoint_id`)
        # may check the nullability of `mlserving_endpoint_id`
        self.mlserving_endpoint_id = self._get_mlserving_endpoint_id(
            mlserving_endpoint_name
        )
        self.mlserving_endpoint_id_for_query = self._get_mlserving_endpoint_id(
            mlserving_endpoint_name_for_query
        )
        self.credential_strategy = credential_strategy
        self._warned_on_deprecated_columns_to_rerank = False

    def _get_mlserving_endpoint_id(self, mlserving_endpoint_name):
        if mlserving_endpoint_name is None:
            return None
        resp = RequestUtils.issue_request(
            url=f"{self.workspace_url}/api/2.0/serving-endpoints/{mlserving_endpoint_name}",
            method="GET",
            token=self._get_token_for_request(control_plane=True),
        )
        if resp.get("route_optimized", False):
            return resp["id"]
        else:
            return None

    def _get_token_for_request(self, write=False, control_plane=False):
        try:
            # automatically refresh auth if not passed in by user and in model serving environment
            if (
                not self._use_user_passed_credentials
                and databricks_utils.is_in_databricks_model_serving_environment()
            ):
                if (
                    self.credential_strategy
                    == CredentialStrategy.MODEL_SERVING_USER_CREDENTIALS
                ):
                    _, token = get_model_serving_invoker_credentials()
                    return token
                else:
                    return databricks_utils.get_databricks_host_creds().token
        except Exception as e:
            # Faile to read credentials from model serving environment failed and we will default
            # to cached vector search token
            pass

        if self.personal_access_token:  # PAT flow
            return self.personal_access_token
        if self.workspace_url in self.index_url:
            control_plane = True
        if (
            control_plane
            and self._control_plane_oauth_token
            and self._control_plane_oauth_token_expiry_ts
            and self._control_plane_oauth_token_expiry_ts - 100 > time.time()
        ):
            return self._control_plane_oauth_token
        if (
            write
            and not control_plane
            and self._write_oauth_token
            and self._write_oauth_token_expiry_ts
            and self._write_oauth_token_expiry_ts - 100 > time.time()
        ):
            return self._write_oauth_token
        if (
            not write
            and not control_plane
            and self._read_oauth_token
            and self._read_oauth_token_expiry_ts
            and self._read_oauth_token_expiry_ts - 100 > time.time()
        ):
            return self._read_oauth_token
        if self.service_principal_client_id and self.service_principal_client_secret:
            if control_plane:
                authorization_details = []
            elif self.mlserving_endpoint_id:
                authorization_details = json.dumps(
                    [
                        {
                            "type": "unity_catalog_permission",
                            "securable_type": "table",
                            "securable_object_name": self.name,
                            "operation": (
                                "WriteVectorIndex" if write else "ReadVectorIndex"
                            ),
                        },
                        {
                            "type": "workspace_permission",
                            "object_type": "serving-endpoints",
                            "object_path": "/serving-endpoints/"
                            + self.mlserving_endpoint_id,
                            "actions": ["query_inference_endpoint"],
                        },
                    ]
                )
            else:
                authorization_details = json.dumps(
                    [
                        {
                            "type": "unity_catalog_permission",
                            "securable_type": "table",
                            "securable_object_name": self.name,
                            "operation": (
                                "WriteVectorIndex" if write else "ReadVectorIndex"
                            ),
                        }
                    ]
                )
            oauth_token_data = (
                OAuthTokenUtils.get_oauth_token(
                    workspace_url=self.workspace_url,
                    service_principal_client_id=self.service_principal_client_id,
                    service_principal_client_secret=self.service_principal_client_secret,
                    authorization_details=authorization_details,
                )
                if not self.azure_tenant_id
                else OAuthTokenUtils.get_azure_oauth_token(
                    workspace_url=self.workspace_url,
                    service_principal_client_id=self.service_principal_client_id,
                    service_principal_client_secret=self.service_principal_client_secret,
                    authorization_details=authorization_details,
                    azure_tenant_id=self.azure_tenant_id,
                    azure_login_id=self.azure_login_id,
                )
            )
            if control_plane:
                self._control_plane_oauth_token = oauth_token_data["access_token"]
                self._control_plane_oauth_token_expiry_ts = time.time() + float(
                    oauth_token_data["expires_in"]
                )
                return self._control_plane_oauth_token
            if write:
                self._write_oauth_token = oauth_token_data["access_token"]
                self._write_oauth_token_expiry_ts = time.time() + float(
                    oauth_token_data["expires_in"]
                )
                return self._write_oauth_token
            self._read_oauth_token = oauth_token_data["access_token"]
            self._read_oauth_token_expiry_ts = time.time() + float(
                oauth_token_data["expires_in"]
            )
            return self._read_oauth_token
        raise Exception("You must specify service principal or PAT token")

    def upsert(self, inputs):
        """
        Upsert data into the index.

        :param inputs: List of dictionaries to upsert into the index.
        """
        assert type(inputs) == list, "inputs must be of type: List of dictionaries"
        assert all(
            type(i) == dict for i in inputs
        ), "inputs must be of type: List of dicts"
        upsert_payload = {"inputs_json": json.dumps(inputs)}
        return RequestUtils.issue_request(
            url=f"{self.index_url}/upsert-data",
            token=self._get_token_for_request(write=True),
            method="POST",
            json=upsert_payload,
        )

    def delete(self, primary_keys):
        """
        Delete data from the index.

        :param primary_keys: List of primary keys to delete from the index.
        """
        assert type(primary_keys) == list, "inputs must be of type: List"
        delete_payload = {"primary_keys": primary_keys}
        return RequestUtils.issue_request(
            url=f"{self.index_url}/delete-data",
            token=self._get_token_for_request(write=True),
            method="DELETE",
            json=delete_payload,
        )

    def describe(self):
        """
        Describe the index. This returns metadata about the index.
        """
        return RequestUtils.issue_request(
            url=f"{self.workspace_url}/api/2.0/vector-search/indexes/{self.name}",
            token=self._get_token_for_request(control_plane=True),
            method="GET",
        )

    def sync(self):
        """
        Sync the index. This is used to sync the index with the source delta table.
        This only works with managed delta sync index with pipeline type="TRIGGERED".
        """
        return RequestUtils.issue_request(
            url=f"{self.workspace_url}/api/2.0/vector-search/indexes/{self.name}/sync",
            token=self._get_token_for_request(control_plane=True),
            method="POST",
        )

    def similarity_search(
        self,
        columns,
        query_text=None,
        query_vector=None,
        filters=None,
        num_results=5,
        debug_level=1,
        score_threshold=None,
        query_type=None,
        columns_to_rerank=None,
        disable_notice=False,
        reranker=None,
    ):
        """
        Perform a similarity search on the index. This returns the top K results that are most similar to the query.

        :param columns: List of column names to return in the results.
        :param query_text: Query text to search for.
        :param query_vector: Query vector to search for.
        :param filters: Filters to apply to the query.
        :param num_results: Number of results to return.
        :param debug_level: Debug level to use for the query.
        :param score_threshold: Score threshold to use for the query.
        :param query_type: Query type of this query. Choices are "ANN" and "HYBRID".
        :param columns_to_rerank: List of column names to use for reranking the results.
        :param disable_notice: Whether to disable the notice message.
        :param reranker: Reranker to use for the query.
        """
        authentication_warning(
            not self._use_user_passed_credentials,
            self.personal_access_token,
            disable_notice,
        )
        if columns_to_rerank and reranker is not None:
            raise ValueError(
                "The arguments `columns_to_rerank` and `reranker` cannot both be provided."
            )
        if columns_to_rerank:
            if not self._warned_on_deprecated_columns_to_rerank:
                print(
                    "[NOTICE] The argument `columns_to_rerank` is deprecated. Use the argument `reranker` instead: `import DatabricksReranker from databricks.vector_search.reranker; index.similarity_search(..., reranker=DatabricksReranker(columns_to_rerank))`."
                )
            self._warned_on_deprecated_columns_to_rerank = True
        if reranker is not None:
            # Move everything to `columns_to_rerank` since it works in both old and new deployment.
            # TODO: Move everything to `reranker` once the new deployment is fully rolled out.
            columns_to_rerank = reranker.columns_to_rerank

        if isinstance(filters, str):
            filter_string = filters
            filters_json = None
        else:
            filter_string = None
            filters_json = json.dumps(filters) if filters else None
        json_data = {
            "num_results": num_results,
            "columns": columns,
            "filters_json": filters_json,
            "filter_string": filter_string,
            "debug_level": debug_level,
        }
        if query_text:
            json_data["query"] = query_text
            json_data["query_text"] = query_text
        if query_vector:
            json_data["query_vector"] = query_vector
        if score_threshold:
            json_data["score_threshold"] = score_threshold
        if query_type:
            json_data["query_type"] = query_type
        if columns_to_rerank:
            json_data["columns_to_rerank"] = columns_to_rerank
            if self._index_url_ensure_reranker_compatible is None:
                # Use the callable to get the reranker-compatible URL
                if self._get_reranker_url_callable:
                    index_url_raw = self._get_reranker_url_callable()
                    self._index_url_ensure_reranker_compatible = _get_index_url(
                        index_url_raw,
                        self.workspace_url,
                        self.name,
                        self.personal_access_token,
                        self.service_principal_client_id,
                        self.service_principal_client_secret,
                    )
                else:
                    self._index_url_ensure_reranker_compatible = self.index_url
            query_url = self._index_url_ensure_reranker_compatible
        else:
            query_url = self.index_url

        response = RequestUtils.issue_request(
            url=f"{query_url}/query",
            token=self._get_token_for_request(),
            method="GET",
            json=json_data,
        )

        out_put = response
        while response["next_page_token"]:
            response = self.__get_next_page(query_url, response["next_page_token"])
            out_put["result"]["row_count"] += response["result"]["row_count"]
            out_put["result"]["data_array"] += response["result"]["data_array"]

        out_put.pop("next_page_token", None)
        return out_put

    def wait_until_ready(
        self,
        verbose=False,
        timeout=datetime.timedelta(hours=24),
        wait_for_updates=False,
    ):
        """
        Wait for the index to be online.

        :param bool verbose: Whether to print status messages.
        :param datetime.timedelta timeout: The time allowed until we timeout with an Exception.
        :param bool wait_for_updates: If true, the index will also wait for any updates to be completed.
        """

        def get_index_state():
            return self.describe()["status"]["detailed_state"]

        def is_index_state_ready(index_state):
            if "ONLINE" not in index_state:
                return False
            if not wait_for_updates:
                # It is enough to wait for any online state.
                return True
            # Now check if current online state is an update state.
            return index_state in [
                "ONLINE",
                "ONLINE_NO_PENDING_UPDATE",
                "ONLINE_DIRECT_ACCESS",
            ]

        start_time = datetime.datetime.now()
        sleep_time_seconds = 30
        # Online states all contain `ONLINE`.
        # Provisioning states all contain `PROVISIONING`
        # Offline states all contain `OFFLINE`.
        index_state = get_index_state()
        while (
            not is_index_state_ready(index_state)
            and datetime.datetime.now() - start_time < timeout
        ):
            if "OFFLINE" in index_state:
                raise Exception(f"Index {self.name} is offline")
            if verbose:
                running_time = int(
                    math.floor((datetime.datetime.now() - start_time).total_seconds())
                )
                print(
                    f"Index {self.name} is in state {index_state}. Time: {running_time}s."
                )
            time.sleep(sleep_time_seconds)
            index_state = get_index_state()
        if verbose:
            print(f"Index {self.name} is in state {index_state}.")
        if not is_index_state_ready(index_state):
            raise Exception(
                f"Index {self.name} did not become online within timeout of {timeout.total_seconds()}s."
            )

    def scan(self, num_results=10, last_primary_key=None):
        """
        Given all the data in the index sorted by primary key, this returns the next
        `num_results` data after the primary key specified by `last_primary_key`.
        If last_primary_key is None , it returns the first `num_results`.

        Please note if there's ongoing updates to the index, the scan results may not be consistent.

        :param num_results: Number of results to return.
        :param last_primary_key: last primary key from previous pagination, it will be used as the exclusive starting primary key.
        """
        json_data = {
            "num_results": num_results,
            "endpoint_name": self.endpoint_name,
        }
        if last_primary_key:
            json_data["last_primary_key"] = last_primary_key

        url = self.index_url + "/scan"

        return RequestUtils.issue_request(
            url=url, token=self._get_token_for_request(), method="GET", json=json_data
        )

    @deprecation.deprecated(
        deprecated_in="0.36",
        removed_in="0.37",
        current_version="0.36",
        details="Use the scan function instead",
    )
    def scan_index(self, num_results=10, last_primary_key=None):
        return self.scan(num_results, last_primary_key)

    def __get_next_page(self, index_url, page_token):
        """
        Get the next page of results from a page token.
        """
        json_data = {
            "page_token": page_token,
            "endpoint_name": self.endpoint_name,
        }
        url = index_url + "/query-next-page"

        return RequestUtils.issue_request(
            url=url, token=self._get_token_for_request(), method="GET", json=json_data
        )


def _get_index_url(
    index_url,
    workspace_url,
    index_name,
    personal_access_token,
    service_principal_client_id,
    service_principal_client_secret,
):
    cp_url = workspace_url + f"/api/2.0/vector-search/indexes/{index_name}"
    if personal_access_token and not (
        service_principal_client_id and service_principal_client_secret
    ):
        return cp_url
    elif index_url:
        return UrlUtils.add_https_if_missing(index_url)
    else:
        # Fallback to CP
        return cp_url

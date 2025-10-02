"""API Hub client for Jentic Runtime."""

import logging
import os
from typing import Any, Optional

import httpx

from jentic.lib.models import (
    SearchRequest as ApiCapabilitySearchRequest,
    SearchResponse as APISearchResults,
    FileEntry,
    GetFilesResponse,
    WorkflowEntry,
    WorkflowExecutionDetails,
    OperationEntry,
    SearchResult,
)


logger = logging.getLogger(__name__)


class JenticAPIClient:
    """Client for interacting with the Jentic API Knowledge Hub."""

    def __init__(
        self,
        base_url: str | None = None,
        agent_api_key: str | None = None,
        user_agent: str | None = None,
    ):
        """Initialize the API Hub client.

        Args:
            base_url: Base URL for the Jentic API Knowledge Hub.
            agent_api_key: Agent API Key used for authentication with the Jentic hub.
            user_agent: User agent string for the API client.
        """
        # Set the base URL with default fallback
        self.base_url = base_url or os.environ.get("JENTIC_API_URL", "https://api.jentic.com")

        self.base_url = self.base_url.rstrip("/")

        # Get agent key from param or environment
        self.agent_api_key = agent_api_key or os.environ.get("JENTIC_AGENT_API_KEY", "")

        logger.info(f"Initialized API Hub client with base_url: {self.base_url}")

        # Set up headers
        self.headers = {}
        if user_agent:
            self.headers["X-Jentic-User-Agent"] = user_agent
        else:
            self.headers["X-Jentic-User-Agent"] = "Jentic/1.0 SDK (Python)"
        if self.agent_api_key:
            self.headers["X-JENTIC-API-KEY"] = self.agent_api_key

    async def get_execution_files(
        self, workflow_ids: list[str] = [], operation_uuids: list[str] = []
    ) -> GetFilesResponse:
        """Retrieve files for execution from the real API."""
        logger.info(
            f"Fetching execution files from API for workflows: {workflow_ids}, operations: {operation_uuids}"
        )
        params = {}
        if workflow_ids:
            params["workflow_uuids"] = ",".join(workflow_ids)
        if operation_uuids:
            params["operation_uuids"] = ",".join(operation_uuids)
        url = f"{self.base_url}/api/v1/files"
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, params=params, headers=self.headers)
                response.raise_for_status()
                # Try to get the data from the response and ensure API names
                response_json = response.json()
                response_json = self.ensure_api_names_in_response(response_json)
                # Create the response model using the enriched data
                return GetFilesResponse.model_validate(response_json)
        except httpx.HTTPStatusError as e:
            logger.error(
                f"HTTP error fetching execution files: {e.response.status_code} {e.response.text}"
            )
            raise
        except Exception as e:
            logger.error(f"Error fetching execution files: {e}")
            raise

    def _build_source_descriptions(
        self,
        workflow_entry: WorkflowEntry,
        all_openapi_files: dict[str, FileEntry],
        arazzo_doc: dict[str, Any],
    ) -> dict[str, dict[str, Any]]:
        """Build the source_descriptions dict mapping Arazzo name to OpenAPI content.

        Maps all source descriptions from Arazzo to their corresponding OpenAPI file contents
        from the API response for the workflow.
        """
        source_descriptions = {}

        # 1. Find all OpenAPI source descriptions in the Arazzo document
        arazzo_source_names = []
        try:
            arazzo_sources = arazzo_doc.get("sourceDescriptions", [])
            if not isinstance(arazzo_sources, list):
                logger.warning("Arazzo 'sourceDescriptions' is not a list.")
                arazzo_sources = []

            for source in arazzo_sources:
                if isinstance(source, dict) and source.get("type") == "openapi":
                    name = source.get("name")
                    if name:
                        arazzo_source_names.append(name)
                        logger.debug(f"Found Arazzo OpenAPI source name: {name}")
                    else:
                        logger.warning(
                            f"Skipping Arazzo OpenAPI sourceDescription missing name: {source}"
                        )

            if not arazzo_source_names:
                logger.warning(
                    f"No Arazzo sourceDescriptions with type 'openapi' and a 'name' found for workflow {workflow_entry.workflow_id}"
                )

        except Exception as e:
            logger.error(f"Error parsing Arazzo sourceDescriptions: {e}")

        # 2. Get all available OpenAPI file contents associated with the workflow
        openapi_files = {}
        if workflow_entry.files.open_api and all_openapi_files:
            for openapi_file_id_obj in workflow_entry.files.open_api:
                openapi_file_id = openapi_file_id_obj.id
                if openapi_file_id in all_openapi_files:
                    file_entry = all_openapi_files[openapi_file_id]
                    # Store content and source_path for direct matching
                    # Assumes file_entry has a 'source_path' attribute from the API response
                    if hasattr(file_entry, "source_path") and file_entry.source_path is not None:
                        openapi_files[openapi_file_id] = {
                            "content": file_entry.content,
                            "source_path": file_entry.source_path,
                        }
                        logger.debug(
                            f"Found OpenAPI file with source_path: {file_entry.source_path} (ID: {openapi_file_id})"
                        )
                    else:
                        logger.warning(
                            f"OpenAPI file entry with ID {openapi_file_id} (filename: {file_entry.filename}) is missing 'source_path'. Cannot use for matching."
                        )
                else:
                    logger.warning(
                        f"OpenAPI file content not found for ID {openapi_file_id} in workflow {workflow_entry.workflow_id} (referenced but not in main files dict)."
                    )

            if not openapi_files:
                logger.warning(
                    f"No usable OpenAPI file content (with source_path) found for workflow {workflow_entry.workflow_id} despite references."
                )
        elif not all_openapi_files:
            logger.warning(
                "No OpenAPI files were provided in the main 'files' dictionary of the response."
            )
        else:
            logger.debug(
                f"Workflow {workflow_entry.workflow_id} does not reference any OpenAPI files."
            )

        # 3. Map each Arazzo source description to matching OpenAPI content by source_path
        if arazzo_source_names and openapi_files:
            # Extract source descriptions with their URLs
            arazzo_sources_with_urls = []
            try:
                for source in arazzo_doc.get("sourceDescriptions", []):
                    if (
                        isinstance(source, dict)
                        and source.get("type") == "openapi"
                        and source.get("name")
                        and source.get("url")
                    ):
                        arazzo_sources_with_urls.append(
                            {"name": source.get("name"), "url": source.get("url")}
                        )
                        logger.debug(
                            f"Found Arazzo source with URL: {source.get('name')} -> {source.get('url')}"
                        )
            except Exception as e:
                logger.error(f"Error extracting URLs from sourceDescriptions: {e}")

            # Match Arazzo sourceDescriptions to OpenAPI files by comparing source.url with file.source_path
            for source in arazzo_sources_with_urls:
                source_name = source["name"]
                source_url = source["url"]

                matched = False
                for file_id, file_info in openapi_files.items():
                    openapi_source_path = file_info["source_path"]

                    if source_url == openapi_source_path:
                        source_descriptions[source_name] = file_info["content"]
                        matched = True
                        logger.info(
                            f"Matched Arazzo source '{source_name}' (URL: {source_url}) "
                            f"to OpenAPI file with source_path '{openapi_source_path}' (ID: {file_id})"
                        )
                        break  # Found the match for this Arazzo source

                if not matched:
                    logger.warning(
                        f"Could not find an OpenAPI file with source_path matching Arazzo sourceDescription URL '{source_url}' "
                        f"for source name '{source_name}' in workflow {workflow_entry.workflow_id}. This source will not be available."
                    )

        elif not openapi_files and arazzo_source_names:
            logger.warning(
                f"No OpenAPI files with source_path were available to match against Arazzo source descriptions for workflow {workflow_entry.workflow_id}."
            )

        if not source_descriptions and arazzo_source_names:
            logger.warning(
                f"No Arazzo source descriptions were matched to OpenAPI files for workflow {workflow_entry.workflow_id}."
            )

        return source_descriptions

    async def get_execution_details_for_workflow(
        self, workflow_id: str
    ) -> Optional[WorkflowExecutionDetails]:
        """Fetch Arazzo doc, OpenAPI specs, and internal ID for a single workflow UUID.

        Args:
            workflow_id: The UUID of the workflow.

        Returns:
            The WorkflowExecutionDetails object for the given workflow UUID, or None if not found.
        """
        logger.debug(f"Fetching execution details for workflow UUID: {workflow_id}")

        if not workflow_id:
            return None  # Return None if no ID requested

        try:
            # Call get_execution_files for the requested workflow ID
            exec_files_response: GetFilesResponse = await self.get_execution_files(
                workflow_ids=[workflow_id]
            )

            if workflow_id not in exec_files_response.workflows:
                logger.warning(f"Workflow ID {workflow_id} not found in API response.")
                return None

            workflow_entry = exec_files_response.workflows[workflow_id]

            # Extract Arazzo document content
            if not workflow_entry.files.arazzo:
                logger.warning(
                    f"No Arazzo file reference found for workflow {workflow_id}. Skipping."
                )
                return None
            if len(workflow_entry.files.arazzo) > 1:
                logger.warning(
                    f"Multiple Arazzo file references found for workflow {workflow_id}. Using first."
                )
            arazzo_file_id_obj = workflow_entry.files.arazzo[0]
            arazzo_file_id = arazzo_file_id_obj.id
            arazzo_files_dict = exec_files_response.files.get("arazzo")
            if not arazzo_files_dict or arazzo_file_id not in arazzo_files_dict:
                logger.warning(
                    f"Arazzo file content not found for ID {arazzo_file_id} in workflow {workflow_id}. Skipping."
                )
                return None
            arazzo_doc = arazzo_files_dict[arazzo_file_id].content

            # Build source_descriptions using the helper method
            source_descriptions = self._build_source_descriptions(
                workflow_entry=workflow_entry,
                all_openapi_files=exec_files_response.files.get("open_api", {}),
                arazzo_doc=arazzo_doc,
            )

            # Store the details in the results dictionary
            return WorkflowExecutionDetails(
                arazzo_doc=arazzo_doc,
                source_descriptions=source_descriptions,
                friendly_workflow_id=workflow_entry.workflow_id,  # Use the workflow_id from the entry
            )
        except Exception as e:
            logger.error(f"Failed to fetch execution details for workflow {workflow_id}: {e}")
            return None

    async def search_api_capabilities(
        self, request: ApiCapabilitySearchRequest
    ) -> APISearchResults:
        """Search for API capabilities that match specific requirements.

        Args:
            request: Search request parameters.

        Returns:
            SearchResults object containing matching APIs, workflows, and operations.
        """

        # Real API call - using new search server API
        # Use the unified search endpoint to get a comprehensive view
        logger.info(
            f"Searching for API capabilities using unified search: {request.capability_description}"
        )
        search_results = await self._search_all(request)

        # Parse API, workflow, and operation results from search_results
        workflow_summaries: list[SearchResult] = []
        for wf in search_results.get("workflows", []):
            try:
                # Determine api_name: explicit, mapped by api_id, or vendor fallback
                api_name_val = wf.get("api_name")
                workflow_summaries.append(
                    SearchResult(
                        id=wf.get("id", ""),
                        summary=wf.get("name", wf.get("workflow_id", "")),
                        description=wf.get("description", ""),
                        api_name=api_name_val,
                        match_score=wf.get("distance", 0.0),
                    )
                )
            except Exception as e:
                logger.warning(f"Failed to parse workflow summary: {e}")
        logger.info(
            f"Found {len(workflow_summaries)} workflows matching '{request.capability_description}'"
        )

        operation_summaries: list[SearchResult] = []
        for op in search_results.get("operations", []):
            try:
                api_name_val = op.get("api_name")
                operation_summaries.append(
                    SearchResult(
                        id=op.get("id", ""),
                        summary=op.get("summary", ""),
                        description=op.get("description", ""),
                        path=op.get("path", ""),
                        method=op.get("method", ""),
                        match_score=op.get("distance", 0.0),
                        api_name=api_name_val,
                    )
                )
            except Exception as e:
                logger.warning(f"Failed to parse operation summary: {e}")
        logger.info(
            f"Found {len(operation_summaries)} operations matching '{request.capability_description}'"
        )

        # Return as a SearchResults object for high-level structure
        return APISearchResults(workflows=workflow_summaries, operations=operation_summaries)

    # No need for _extract_api_name_from_refs method as our Pydantic models handle API name extraction

    def ensure_api_names_in_response(self, response_data: dict[str, Any]) -> dict[str, Any]:
        """Ensure API names are properly set in API responses using Pydantic models.

        This implements Killian's recommendation to use Pydantic models for type safety.

        Args:
            response_data: The response data that may need API names enriched.

        Returns:
            The updated response data with API names properly set.
        """

        # Handle workflows (could be list in search results or dict in execution info)
        workflows = response_data.get("workflows", {})
        if isinstance(workflows, list):
            # Process list format (search results)
            for i, wf in enumerate(workflows):
                self._enrich_entity_with_api_name(wf, workflows, i, WorkflowEntry)
        elif isinstance(workflows, dict):
            # Process dict format (execution info)
            for wf_id, wf in workflows.items():
                self._enrich_entity_with_api_name(wf, workflows, wf_id, WorkflowEntry)

        # Process operations (always in dict format)
        operations = response_data.get("operations", {})
        if isinstance(operations, dict):
            for op_id, op in operations.items():
                self._enrich_entity_with_api_name(op, operations, op_id, OperationEntry)

        return response_data

    def _enrich_entity_with_api_name(
        self, entity: dict, parent_dict: dict, key: Any, model_class: type
    ) -> None:
        """Helper method to enrich an entity with API name using Pydantic models.

        Args:
            entity: The entity (workflow or operation) to enrich
            parent_dict: The parent dictionary containing the entity
            key: The key for this entity in the parent dictionary
            model_class: The Pydantic model class to use for validation
        """
        # Skip if not a dict or already has api_name
        if not isinstance(entity, dict) or "api_name" in entity:
            return

        try:
            # Create a Pydantic model with the entity data
            # Since api_name is required but has a default value, this will work
            model = model_class.model_validate(entity)

            # Use the api_name directly from the model
            if model.api_name:
                parent_dict[key]["api_name"] = model.api_name

        except Exception:
            # Set a default API name if validation fails
            parent_dict[key]["api_name"] = ""

    async def _search_all(self, request: ApiCapabilitySearchRequest) -> dict[str, Any]:
        """Search across all entity types for the capability description.

        Args:
            request: The capability search request.

        Returns:
            Search response with all entity types.
        """
        # Prepare the search request for the all endpoint
        search_request = {
            "query": request.capability_description,
            "limit": request.max_results
            * 2,  # Get more results to ensure we have enough after filtering
            "entity_types": ["api", "workflow", "operation"],
        }

        if request.keywords:
            # Add keywords to the query
            keyword_str = " ".join(request.keywords)
            search_request["query"] = f"{search_request['query']} {keyword_str}"

        if request.api_names:
            search_request["api_names"] = request.api_names

        logger.info(f"Searching all entities with query: {search_request['query']}")

        # Log the URL we're connecting to for debugging
        search_url = f"{self.base_url}/api/v1/search/all"
        logger.info(f"Connecting to search URL: {search_url}")

        # Make the search request
        async with httpx.AsyncClient() as client:
            response = await client.post(
                search_url,
                json=search_request,
                headers=self.headers,
            )
            response.raise_for_status()

            search_response = response.json()
            # Ensure API names are properly set in the raw search response
            search_response = self.ensure_api_names_in_response(search_response)
            api_count = len(search_response.get("apis", []))
            workflow_count = len(search_response.get("workflows", []))
            operation_count = len(search_response.get("operations", []))

            logger.info(
                f"Found {api_count} APIs, {workflow_count} workflows, {operation_count} operations"
            )

            return search_response

    async def _search_workflows(self, request: ApiCapabilitySearchRequest) -> list[dict[str, Any]]:
        """Search for workflows that match the capability description.

        Args:
            request: The capability search request.

        Returns:
            List of workflow search results.
        """
        # Prepare the search request for the workflows endpoint
        search_request = {
            "query": request.capability_description,
            "limit": request.max_results
            * 2,  # Get more workflows to ensure we have enough after grouping
        }

        if request.keywords:
            # Add keywords to the query
            keyword_str = " ".join(request.keywords)
            search_request["query"] = f"{search_request['query']} {keyword_str}"

        logger.info(f"Searching workflows with query: {search_request['query']}")

        # Make the search request
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/api/v1/search/workflows",
                json=search_request,
                headers=self.headers,
            )
            response.raise_for_status()

            search_response = response.json()
            # Ensure API names are properly set
            search_response = self.ensure_api_names_in_response(search_response)
            logger.info(f"Found {len(search_response.get('workflows', []))} workflows")

            return search_response.get("workflows", [])

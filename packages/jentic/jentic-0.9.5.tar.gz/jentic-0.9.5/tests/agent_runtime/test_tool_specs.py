from jentic.lib.agent_runtime.tool_specs import LLMToolSpecManager, create_llm_tool_manager


def test_llm_tool_spec_manager_init():
    mgr = LLMToolSpecManager()
    assert isinstance(mgr, LLMToolSpecManager)
    assert mgr._workflow_definitions == {}
    assert mgr._operation_definitions == {}
    assert mgr._operation_name_to_uuid == {}
    assert set(mgr._tool_specs.keys()) == {"openai", "anthropic"}


def test_load_workflows_and_operations():
    mgr = LLMToolSpecManager()
    workflows = {"wf1": {"desc": "A workflow"}}
    operations = {"op1": {"desc": "An operation"}}
    mgr.load_workflows(workflows)
    mgr.load_operations(operations)
    assert mgr._workflow_definitions["wf1"]["desc"] == "A workflow"
    assert mgr._operation_definitions["op1"]["desc"] == "An operation"


def test_get_tool_type():
    mgr = LLMToolSpecManager()
    mgr.load_workflows({"wf": {}})
    # The operation must have an 'operation_uuid' field for correct mapping to 'op'
    mgr.load_operations({"op": {"operation_uuid": "op"}})
    assert mgr.get_tool_type("wf") == "workflow"
    assert mgr.get_tool_type("op") == "operation"
    assert mgr.get_tool_type("unknown") == "unknown"


def test_create_llm_tool_manager():
    mgr = create_llm_tool_manager()
    assert isinstance(mgr, LLMToolSpecManager)


def test_openai_function_schema_simple():
    mgr = LLMToolSpecManager()
    workflow_id = "wf1"
    workflow = {
        "description": "My test workflow",
        "inputs": {
            "properties": {
                "foo": {"type": "string", "description": "Foo input"},
                "bar": {"type": "integer"},
            },
            "required": ["foo"],
        },
    }
    schema = mgr._create_openai_function_schema(workflow_id, workflow)
    assert schema["name"] == workflow_id
    assert schema["description"] == "My test workflow"
    assert schema["parameters"]["type"] == "object"
    assert "foo" in schema["parameters"]["properties"]
    assert schema["parameters"]["properties"]["foo"]["type"] == "string"
    assert schema["parameters"]["properties"]["bar"]["type"] == "integer"
    assert schema["parameters"]["required"] == ["foo"]


def test_openai_function_schema_ref():
    mgr = LLMToolSpecManager()
    workflow_id = "wf2"
    workflow = {"workflowId": "InputType", "inputs": {"$ref": "#/definitions/InputType"}}
    schema = mgr._create_openai_function_schema(workflow_id, workflow)
    assert "input" in schema["parameters"]["properties"]
    assert schema["parameters"]["properties"]["input"]["type"] == "object"
    assert "InputType" in schema["parameters"]["properties"]["input"]["description"]


def test_openai_operation_schema_simple():
    mgr = LLMToolSpecManager()
    operation_uuid = "op1"
    operation = {
        "summary": "My operation",
        "method": "POST",
        "path": "/doit",
        "inputs": {
            "properties": {
                "x": {"type": "string"},
                "body": {"properties": {"y": {"type": "integer"}}, "required": ["y"]},
            },
            "required": ["x"],
        },
    }
    schema = mgr._create_openai_operation_schema(operation_uuid, operation)
    assert schema["name"] == "post-doit"
    assert schema["description"] == "My operation"
    assert "x" in schema["parameters"]["properties"]
    assert "y" in schema["parameters"]["properties"]
    assert set(schema["parameters"]["required"]) == {"x", "y"}


# Edge: operation with no summary/description


def test_openai_operation_schema_default_description():
    """Test that operation schemas use method and path if no description is provided."""
    mgr = create_llm_tool_manager()
    operation_uuid = "op2"
    operation = {"method": "GET", "path": "/info", "inputs": {"properties": {}}}
    schema = mgr._create_openai_operation_schema(operation_uuid, operation)
    assert schema["name"] == "get-info"
    assert schema["description"].startswith("Execute GET request to /info")


def test_vendor_name_sanitization():
    """Test that vendor names from api_name are properly sanitized."""
    mgr = create_llm_tool_manager()

    # Test with a domain in api_name
    operation_with_domain = {
        "method": "GET",
        "path": "/test",
        "api_name": "discord.com",
        "inputs": {"properties": {}},
    }
    openai_schema = mgr._create_openai_operation_schema("test-id", operation_with_domain)
    assert openai_schema["name"] == "discord-com-get-test"

    # Test with special characters
    operation_with_special_chars = {
        "method": "GET",
        "path": "/test",
        "api_name": "company@example!com",
        "inputs": {"properties": {}},
    }
    openai_schema = mgr._create_openai_operation_schema("test-id", operation_with_special_chars)
    assert openai_schema["name"] == "company-example-com-get-test"

    # Test with empty api_name after sanitization - should have no vendor prefix
    operation_with_invalid_api_name = {
        "method": "GET",
        "path": "/test",
        "api_name": "!@#$%",
        "inputs": {"properties": {}},
    }
    openai_schema = mgr._create_openai_operation_schema("test-id", operation_with_invalid_api_name)
    assert openai_schema["name"] == "get-test"  # No vendor prefix when sanitized vendor is empty

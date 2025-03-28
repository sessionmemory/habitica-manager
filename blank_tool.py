

class Tools:
    def __init__(self):
        pass

    # Add your custom tools using pure Python code here, make sure to add type hints
    # Use Sphinx-style docstrings to document your tools, they will be used for generating tools specifications
    # Please refer to function_calling_filter_pipeline.py file from pipelines project for an example

    def example_function(param1: str, param2: int) -> dict:
        """
        Example function with input validation and consistent return structure.
        :param param1: Description of param1.
        :param param2: Description of param2.
        :return: Dictionary with success status and data or error message.
        """
        # Input validation
        if not isinstance(param1, str) or not param1:
            return {"success": False, "error": "param1 must be a non-empty string."}
        if not isinstance(param2, int) or param2 <= 0:
            return {"success": False, "error": "param2 must be a positive integer."}

        try:
            # Simulate API call or logic
            result = {"key": "value"}  # Replace with actual logic
            return {"success": True, "data": result}
        except Exception as e:
            return {"success": False, "error": f"Operation failed: {e}"}
from ....models.openai import models as openai_models
from ..utils import extract_function_call


class ItemResourceHelper:
    def __init__(self, item_type: str, item_id: str = None):
        self.item_type = item_type
        self.item_id = item_id

    def create_item_resource(self, is_done: bool):
        pass

    def add_aggregate_content(self, item):
        pass

    def get_aggregated_content(self):
        pass


class FunctionCallItemResourceHelper(ItemResourceHelper):
    def __init__(self, item_id: str = None, tool_call: dict = None):
        super().__init__(openai_models.ItemType.FUNCTION_CALL, item_id)
        self.call_id = None
        self.name = None
        self.arguments = ""
        if tool_call:
            self.name, self.call_id, _ = extract_function_call(tool_call)

    def create_item_resource(self, is_done: bool):
        content = {
            "id": self.item_id,
            "type": self.item_type,
            "call_id": self.call_id,
            "name": self.name,
            "arguments": self.arguments if self.arguments else "",
            "status": "in_progress" if not is_done else "completed",
        }
        return openai_models.ItemResource(content)

    def add_aggregate_content(self, item):
        if isinstance(item, str):
            self.arguments += item
            return
        if not isinstance(item, dict):
            return
        if item.get("type") != openai_models.ItemType.FUNCTION_CALL:
            return
        _, _, argument = extract_function_call(item)
        self.arguments += argument

    def get_aggregated_content(self):
        return self.create_item_resource(is_done=True)


class FunctionCallOutputItemResourceHelper(ItemResourceHelper):
    def __init__(self, item_id: str = None, call_id: str = None):
        super().__init__(openai_models.ItemType.FUNCTION_CALL_OUTPUT, item_id)
        self.call_id = call_id
        self.content = ""

    def create_item_resource(self, is_done: bool):
        content = {
            "id": self.item_id,
            "type": self.item_type,
            "status": "in_progress" if not is_done else "completed",
            "call_id": self.call_id,
            "output": self.content,
        }
        return openai_models.ItemResource(content)

    def add_aggregate_content(self, item):
        if isinstance(item, str):
            self.content += item
            return
        if not isinstance(item, dict):
            return
        content = item.get("text")
        if isinstance(content, str):
            self.content += content

    def get_aggregated_content(self):
        return self.create_item_resource(is_done=True)


class MessageItemResourceHelper(ItemResourceHelper):
    def __init__(self, item_id: str, role: openai_models.ResponsesMessageRole):
        super().__init__(openai_models.ItemType.MESSAGE, item_id)
        self.role = role
        self.content = []

    def create_item_resource(self, is_done: bool):
        content = {
            "id": self.item_id,
            "type": self.item_type,
            "status": "in_progress" if not is_done else "completed",
            "content": self.content,
            "role": self.role,
        }
        return openai_models.ItemResource(content)

    def add_aggregate_content(self, item):
        if isinstance(item, dict):
            item = openai_models.ItemContent(item)
        if isinstance(item, openai_models.ItemContent):
            self.content.append(item)

    def get_aggregated_content(self):
        return self.create_item_resource(is_done=True)

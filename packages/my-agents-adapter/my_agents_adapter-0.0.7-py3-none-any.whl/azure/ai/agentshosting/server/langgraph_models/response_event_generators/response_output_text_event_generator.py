from typing import List

from ....models.openai import models as openai_models
from .response_event_generator import (
    ResponseEventGenerator,
    StreamEventState,
)


class ResponseOutputTextEventGenerator(ResponseEventGenerator):
    def __init__(
        self,
        logger,
        parent: ResponseEventGenerator,
        content_index: int,
        output_index: int,
        item_id: str,
        message_id: str,
    ):
        super().__init__(logger, parent)
        self.output_index = output_index
        self.content_index = content_index
        self.item_id = item_id
        self.message_id = message_id
        self.aggregated_content = ""

    def try_process_message(
        self, message, run_details, stream_state: StreamEventState
    ) -> tuple[bool, ResponseEventGenerator, List[openai_models.ResponseStreamEvent]]:
        is_processed = False
        events = []
        next_processor = self
        if not self.started:
            self.started = True

        if message:
            is_processed, next_processor, processed_events = self.process(message, run_details, stream_state)
            if not is_processed:
                self.logger.warning(f"OutputTextEventGenerator did not process message: {message}")
            events.extend(processed_events)

        if self.should_end(message):
            is_processed, complete_events = self.on_end(message, run_details, stream_state)
            events.extend(complete_events)
            is_processed = True
            next_processor = self.parent

        return is_processed, next_processor, events

    def process(
        self, message, run_details, stream_state: StreamEventState
    ) -> tuple[bool, ResponseEventGenerator, List[openai_models.ResponseStreamEvent]]:
        if message and message.content:
            content = [message.content] if isinstance(message.content, str) else message.content
            res = []
            for item in content:
                if not isinstance(item, str):
                    self.logger.warning(f"Skipping non-string content item: {item}")
                    continue
                # create an event for each content item
                chunk_event = openai_models.ResponseTextDeltaEvent(
                    item_id=self.item_id,
                    output_index=self.output_index,
                    content_index=self.content_index,
                    delta=item,
                    sequence_number=stream_state.sequence_number,
                )
                self.aggregated_content += item
                stream_state.sequence_number += 1
                res.append(chunk_event)
            return True, self, res
        return False, self, []

    def should_end(self, message) -> bool:
        # Determine if the message indicates end of the stream for this item
        if message is None:
            return True
        if message.id != self.message_id:
            return True
        if message.response_metadata and message.response_metadata.get("finish_reason"):
            return True
        return False

    def on_end(
        self, message, run_details, stream_state: StreamEventState
    ) -> tuple[bool, List[openai_models.ResponseStreamEvent]]:
        if not self.started:
            return False, []

        # finalize the item resource
        done_event = openai_models.ResponseTextDoneEvent(
            item_id=self.item_id,
            output_index=self.output_index,
            content_index=self.content_index,
            text=self.aggregated_content,
            sequence_number=stream_state.sequence_number,
        )
        stream_state.sequence_number += 1
        self.parent.aggregate_content(self.aggregated_content)
        return True, [done_event]

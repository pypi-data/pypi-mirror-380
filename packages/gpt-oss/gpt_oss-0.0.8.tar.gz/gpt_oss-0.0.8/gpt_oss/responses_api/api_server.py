import os
import datetime
import uuid
from typing import Callable, Literal, Optional, Union

from fastapi import FastAPI, Request
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi.responses import StreamingResponse
from openai_harmony import (
    Author,
    Conversation,
    DeveloperContent,
    HarmonyEncoding,
    Message,
    ReasoningEffort,
    Role,
    StreamableParser,
    StreamState,
    SystemContent,
    ToolDescription,
)

from gpt_oss.tools.python_docker.docker_tool import PythonTool
from gpt_oss.tools.simple_browser import SimpleBrowserTool
from gpt_oss.tools.simple_browser.backend import YouComBackend, ExaBackend

from .events import (
    ResponseCodeInterpreterCallCodeDelta,
    ResponseCodeInterpreterCallCodeDone,
    ResponseCodeInterpreterCallCompleted,
    ResponseCodeInterpreterCallInProgress,
    ResponseCodeInterpreterCallInterpreting,
    ResponseCompletedEvent,
    ResponseContentPartAdded,
    ResponseContentPartDone,
    ResponseCreatedEvent,
    ResponseEvent,
    ResponseInProgressEvent,
    ResponseOutputItemAdded,
    ResponseOutputItemDone,
    ResponseOutputTextAnnotationAdded,
    ResponseOutputTextDelta,
    ResponseOutputTextDone,
    ResponseReasoningTextDelta,
    ResponseReasoningTextDone,
    ResponseWebSearchCallCompleted,
    ResponseWebSearchCallInProgress,
    ResponseWebSearchCallSearching,
)
from .types import (
    CodeInterpreterCallItem,
    CodeInterpreterOutputImage,
    CodeInterpreterOutputLogs,
    Error,
    FunctionCallItem,
    Item,
    ReasoningItem,
    ReasoningTextContentItem,
    ResponseObject,
    ResponsesRequest,
    TextContentItem,
    UrlCitation,
    Usage,
    WebSearchActionFind,
    WebSearchActionOpenPage,
    WebSearchActionSearch,
    WebSearchCallItem,
)

DEFAULT_TEMPERATURE = 0.0


def get_reasoning_effort(
    effort: Union[Literal["low", "medium", "high"], ReasoningEffort]
) -> ReasoningEffort:
    if isinstance(effort, ReasoningEffort):
        return effort
    if effort == "low":
        return ReasoningEffort.LOW
    if effort == "medium":
        return ReasoningEffort.MEDIUM
    if effort == "high":
        return ReasoningEffort.HIGH
    raise ValueError(f"Invalid reasoning effort: {effort}")


def is_not_builtin_tool(
    recipient: str, treat_functions_python_as_builtin: bool = False
) -> bool:
    if treat_functions_python_as_builtin and recipient == "functions.python":
        return False
    return (
        not recipient.startswith("browser.")
        and recipient != "python"
        and recipient != "assistant"
    )


def create_api_server(
    infer_next_token: Callable[[list[int], float], int], encoding: HarmonyEncoding
) -> FastAPI:
    app = FastAPI()

    @app.exception_handler(RequestValidationError)
    async def log_validation_error(request: Request, exc: RequestValidationError):
        try:
            body_bytes = await request.body()
            print(
                "Invalid request body received:"
                f" {body_bytes.decode('utf-8', errors='replace')}"
            )
        except Exception as body_exc:
            print(f"Failed to read invalid request body: {body_exc}")
        return await request_validation_exception_handler(request, exc)
    responses_store: dict[str, tuple[ResponsesRequest, ResponseObject]] = {}

    def generate_response(
        input_tokens: list[int],
        output_tokens: list[int],
        request_body: ResponsesRequest,
        debug_mode: bool = False,
        function_call_ids: Optional[list[tuple[str, str]]] = None,
        response_id: Optional[str] = None,
        previous_response_id: Optional[str] = None,
        browser_tool: Optional[SimpleBrowserTool] = None,
        browser_call_ids: Optional[list[str]] = None,
        python_tool: Optional[PythonTool] = None,
        python_call_ids: Optional[list[str]] = None,
        python_call_outputs: Optional[
            dict[str, list[CodeInterpreterOutputLogs | CodeInterpreterOutputImage]]
        ] = None,
        reasoning_ids: Optional[list[str]] = None,
        treat_functions_python_as_builtin: bool = False,
    ) -> ResponseObject:
        output = []
        error = None
        if len(output_tokens) > 0:
            if debug_mode:
                try:
                    entries = encoding.parse_messages_from_completion_tokens(
                        output_tokens, Role.ASSISTANT
                    )
                except Exception as e:
                    print(f"Error parsing tokens: {e}")
                    error = Error(
                        code="invalid_function_call",
                        message=f"{e}",
                    )
                    entries = []
            else:
                entries = encoding.parse_messages_from_completion_tokens(
                    output_tokens, Role.ASSISTANT
                )

            fc_index = 0
            browser_tool_index = 0
            python_tool_index = 0
            reasoning_ids_iter = iter(reasoning_ids or [])

            for entry in entries:
                entry_dict = entry.to_dict()
                recipient = entry_dict.get("recipient", "")
                if len(recipient) > 0 and is_not_builtin_tool(
                    recipient, treat_functions_python_as_builtin
                ):
                    call = entry_dict["content"][0]
                    arguments = call["text"]
                    name = recipient

                    if name.startswith("functions."):
                        name = name[len("functions.") :]
                    if function_call_ids and fc_index < len(function_call_ids):
                        fc_id, call_id = function_call_ids[fc_index]
                    else:
                        fc_id, call_id = (
                            f"fc_{uuid.uuid4().hex}",
                            f"call_{uuid.uuid4().hex}",
                        )
                    fc_index += 1
                    output.append(
                        FunctionCallItem(
                            type="function_call",
                            name=name,
                            arguments=arguments,
                            id=fc_id,
                            call_id=call_id,
                        )
                    )
                elif (
                    len(recipient) > 0
                    and recipient.startswith("browser.")
                    and browser_tool is not None
                ):
                    # Mirror event-based creation of WebSearchCallItems when the browser tool is invoked
                    name = recipient
                    call = entry_dict["content"][0]
                    arguments = call["text"]
                    function_name = name[len("browser.") :]

                    # Reconstruct a Message for argument parsing
                    tool_msg = (
                        Message.from_role_and_content(Role.ASSISTANT, arguments)
                        .with_recipient(name)
                        .with_channel("analysis")
                    )

                    action = None
                    try:
                        parsed_args = browser_tool.process_arguments(tool_msg)
                        if function_name == "search":
                            action = WebSearchActionSearch(
                                type="search",
                                query=parsed_args["query"],
                            )
                        elif function_name == "open":
                            action = WebSearchActionOpenPage(
                                type="open_page",
                                url=parsed_args["url"],
                            )
                        elif function_name == "find":
                            action = WebSearchActionFind(
                                type="find",
                                pattern=parsed_args["pattern"],
                                url=parsed_args["url"],
                            )
                    except Exception as e:
                        print(f"Error processing browser tool arguments: {e}")
                        action = None

                    if action is not None:
                        if browser_call_ids and browser_tool_index < len(
                            browser_call_ids
                        ):
                            web_search_call_id = browser_call_ids[browser_tool_index]
                        else:
                            web_search_call_id = f"ws_{uuid.uuid4().hex}"
                        browser_tool_index += 1
                        output.append(
                            WebSearchCallItem(
                                type="web_search_call",
                                id=web_search_call_id,
                                action=action,
                            )
                        )
                elif (
                    len(recipient) > 0
                    and (
                        recipient.startswith("python")
                        or (
                            treat_functions_python_as_builtin
                            and recipient == "functions.python"
                        )
                    )
                    and python_tool is not None
                ):
                    if python_call_ids and python_tool_index < len(python_call_ids):
                        code_call_id = python_call_ids[python_tool_index]
                    else:
                        code_call_id = f"ci_{uuid.uuid4().hex}"
                    python_tool_index += 1
                    code_snippet = None
                    if entry_dict.get("content"):
                        code_snippet = entry_dict["content"][0].get("text")
                    outputs = (
                        (python_call_outputs or {}).get(code_call_id)
                        if python_call_outputs
                        else None
                    )
                    output.append(
                        CodeInterpreterCallItem(
                            type="code_interpreter_call",
                            id=code_call_id,
                            status="completed",
                            code=code_snippet,
                            outputs=outputs,
                        )
                    )
                elif entry_dict["channel"] == "final":
                    content = []
                    for content_entry in entry_dict["content"]:
                        if browser_tool:
                            text_content, annotation_entries, _has_partial_citations = (
                                browser_tool.normalize_citations(content_entry["text"])
                            )
                            annotations = [UrlCitation(**a) for a in annotation_entries]
                        else:
                            text_content = content_entry["text"]
                            annotations = []

                        content.append(
                            TextContentItem(
                                type="output_text",
                                text=text_content,
                                annotations=annotations,
                            )
                        )

                    output.append(
                        Item(
                            type="message",
                            role="assistant",
                            content=content,
                            status="completed",
                        )
                    )
                elif entry_dict["channel"] == "analysis":
                    summary = []
                    content = [
                        ReasoningTextContentItem(
                            type="reasoning_text",
                            text=entry["text"],
                        )
                        for entry in entry_dict["content"]
                    ]
                    reasoning_id = next(reasoning_ids_iter, None)
                    if reasoning_id is None:
                        reasoning_id = f"rs_{uuid.uuid4().hex}"
                    output.append(
                        ReasoningItem(
                            id=reasoning_id,
                            type="reasoning",
                            summary=summary,
                            content=content,
                        )
                    )
        else:
            output = []

        usage = (
            Usage(
                input_tokens=len(input_tokens),
                output_tokens=len(output_tokens),
                total_tokens=len(input_tokens) + len(output_tokens),
            )
            if len(output_tokens) > 0
            else None
        )

        try:
            debug_str = encoding.decode_utf8(input_tokens + output_tokens)
        except Exception:
            debug_str = input_tokens + output_tokens
        try:
            debug_input_str = encoding.decode_utf8(input_tokens)
        except Exception:
            debug_input_str = input_tokens
        try:
            debug_output_str = encoding.decode_utf8(output_tokens)
        except Exception:
            debug_output_str = output_tokens

        metadata = (
            {
                "__debug": debug_str,
                "__debug_input": debug_input_str,
                "__debug_output": debug_output_str,
            }
            if debug_mode
            else {}
        )

        return ResponseObject(
            created_at=int(datetime.datetime.now().timestamp()),
            status="completed",
            output=output,
            text={"format": {"type": "text"}},
            usage=usage,
            max_output_tokens=request_body.max_output_tokens,
            error=error,
            metadata=metadata,
            id=response_id,
            previous_response_id=previous_response_id,
        )

    class StreamResponsesEvents:
        initial_tokens: list[int]
        tokens: list[int]
        output_tokens: list[int]
        output_text: str
        request_body: ResponsesRequest
        request: Request
        sequence_number: int

        def __init__(
            self,
            initial_tokens,
            request_body: ResponsesRequest,
            as_sse: bool = False,
            request: Optional[Request] = None,
            response_id: Optional[str] = None,
            store_callback: Optional[
                Callable[[str, ResponsesRequest, ResponseObject], None]
            ] = None,
            browser_tool: Optional[SimpleBrowserTool] = None,
            python_tool: Optional[PythonTool] = None,
            functions_python_as_builtin: bool = False,
        ):
            self.initial_tokens = initial_tokens
            self.tokens = initial_tokens.copy()
            self.output_tokens = []
            self.output_text = ""
            self.request_body = request_body
            self.parser = StreamableParser(encoding, role=Role.ASSISTANT)
            self.as_sse = as_sse
            self.debug_mode = request_body.metadata.get(
                "__debug", False
            )  # we use this for demo purposes
            # Set temperature for this stream, fallback to DEFAULT_TEMPERATURE if not set
            self.temperature = (
                request_body.temperature
                if request_body.temperature is not None
                else DEFAULT_TEMPERATURE
            )
            self.request = request
            self.sequence_number = 0
            self.function_call_ids: list[tuple[str, str]] = []
            self.response_id = response_id
            self.store_callback = store_callback
            self.new_request = True
            self.browser_tool = browser_tool
            self.use_browser_tool = browser_tool is not None
            self.browser_call_ids: list[str] = []
            self.python_tool = python_tool
            self.use_code_interpreter = python_tool is not None
            self.python_call_ids: list[str] = []
            self.python_call_outputs: dict[
                str, list[CodeInterpreterOutputLogs | CodeInterpreterOutputImage]
            ] = {}
            self.reasoning_item_ids: list[str] = []
            self.current_reasoning_item_id: Optional[str] = None
            self.functions_python_as_builtin = functions_python_as_builtin

        def _send_event(self, event: ResponseEvent):
            event.sequence_number = self.sequence_number
            self.sequence_number += 1
            if self.as_sse:
                return f"event: {event.type}\ndata: {event.model_dump_json(indent=None)}\n\n"
            else:
                return event

        async def run(self):
            browser_tool = self.browser_tool
            self.new_request = True
            initial_response = generate_response(
                self.initial_tokens,
                self.output_tokens,
                self.request_body,
                function_call_ids=self.function_call_ids,
                response_id=self.response_id,
                previous_response_id=self.request_body.previous_response_id,
                browser_tool=self.browser_tool,
                browser_call_ids=self.browser_call_ids,
                python_tool=self.python_tool,
                python_call_ids=self.python_call_ids,
                python_call_outputs=getattr(self, "python_call_outputs", None),
                reasoning_ids=self.reasoning_item_ids,
                treat_functions_python_as_builtin=self.functions_python_as_builtin,
            )
            initial_response.status = "in_progress"
            yield self._send_event(
                ResponseCreatedEvent(
                    type="response.created",
                    response=initial_response,
                )
            )
            yield self._send_event(
                ResponseInProgressEvent(
                    type="response.in_progress",
                    response=initial_response,
                )
            )

            current_content_index = (
                0  # for this implementation we will always have one content item only
            )
            current_output_index = -1
            sent_output_item_added = False

            # we use this if the model outputs a citation to buffer until completed
            output_delta_buffer = ""
            # we use this to track the current output text content for things like providing the right indices in citations
            current_output_text_content = ""
            current_annotations = []

            while True:
                # Check for client disconnect
                if self.request is not None and await self.request.is_disconnected():
                    print("Client disconnected, stopping token generation.")
                    break
                next_tok = infer_next_token(
                    self.tokens,
                    temperature=self.temperature,
                    new_request=self.new_request,
                )
                self.new_request = False
                self.tokens.append(next_tok)
                try:
                    self.parser.process(next_tok)
                except Exception:
                    pass

                if self.parser.state == StreamState.EXPECT_START:
                    current_output_index += 1
                    sent_output_item_added = False

                    if len(self.parser.messages) > 0:
                        previous_item = self.parser.messages[-1]
                        if previous_item.recipient is not None:
                            recipient = previous_item.recipient
                            if (
                                not recipient.startswith("browser.")
                                and not (
                                    recipient == "python"
                                    or (
                                        self.functions_python_as_builtin
                                        and recipient == "functions.python"
                                    )
                                )
                            ):
                                fc_id = f"fc_{uuid.uuid4().hex}"
                                call_id = f"call_{uuid.uuid4().hex}"
                                self.function_call_ids.append((fc_id, call_id))
                                yield self._send_event(
                                    ResponseOutputItemDone(
                                        type="response.output_item.done",
                                        output_index=current_output_index,
                                        item=FunctionCallItem(
                                            type="function_call",
                                            name=(
                                                previous_item.recipient[
                                                    len("functions.") :
                                                ]
                                                if previous_item.recipient.startswith(
                                                    "functions."
                                                )
                                                else previous_item.recipient
                                            ),
                                            arguments=previous_item.content[0].text,
                                            id=fc_id,
                                            call_id=call_id,
                                        ),
                                    )
                                )
                        if previous_item.channel == "analysis":
                            reasoning_id = self.current_reasoning_item_id
                            if reasoning_id is None:
                                reasoning_id = f"rs_{uuid.uuid4().hex}"
                                self.reasoning_item_ids.append(reasoning_id)
                                self.current_reasoning_item_id = reasoning_id
                            yield self._send_event(
                                ResponseReasoningTextDone(
                                    type="response.reasoning_text.done",
                                    output_index=current_output_index,
                                    content_index=current_content_index,
                                    text=previous_item.content[0].text,
                                )
                            )
                            yield self._send_event(
                                ResponseContentPartDone(
                                    type="response.content_part.done",
                                    output_index=current_output_index,
                                    content_index=current_content_index,
                                    part=ReasoningTextContentItem(
                                        type="reasoning_text",
                                        text=previous_item.content[0].text,
                                    ),
                                )
                            )
                            yield self._send_event(
                                ResponseOutputItemDone(
                                    type="response.output_item.done",
                                    output_index=current_output_index,
                                    item=ReasoningItem(
                                        id=reasoning_id,
                                        type="reasoning",
                                        summary=[],
                                        content=[
                                            ReasoningTextContentItem(
                                                type="reasoning_text",
                                                text=previous_item.content[0].text,
                                            )
                                        ],
                                    ),
                                )
                            )
                            self.current_reasoning_item_id = None
                        if previous_item.channel == "final":
                            annotations = [
                                UrlCitation(**a) for a in current_annotations
                            ]
                            if browser_tool:
                                (
                                    normalized_text,
                                    _annotations,
                                    _has_partial_citations,
                                ) = browser_tool.normalize_citations(
                                    previous_item.content[0].text
                                )
                            else:
                                normalized_text = previous_item.content[0].text
                                annotations = []
                            text_content = TextContentItem(
                                type="output_text",
                                text=normalized_text,
                                annotations=annotations,
                            )
                            yield self._send_event(
                                ResponseOutputTextDone(
                                    type="response.output_text.done",
                                    output_index=current_output_index,
                                    content_index=current_content_index,
                                    text=normalized_text,
                                )
                            )
                            yield self._send_event(
                                ResponseContentPartDone(
                                    type="response.content_part.done",
                                    output_index=current_output_index,
                                    content_index=current_content_index,
                                    part=text_content,
                                )
                            )
                            yield self._send_event(
                                ResponseOutputItemDone(
                                    type="response.output_item.done",
                                    output_index=current_output_index,
                                    item=Item(
                                        type="message",
                                        role="assistant",
                                        content=[text_content],
                                    ),
                                )
                            )
                            current_annotations = []
                            current_output_text_content = ""

                if (
                    self.parser.last_content_delta
                    and self.parser.current_channel == "final"
                    and self.parser.current_recipient is None
                ):
                    if not sent_output_item_added:
                        sent_output_item_added = True
                        yield self._send_event(
                            ResponseOutputItemAdded(
                                type="response.output_item.added",
                                output_index=current_output_index,
                                item=Item(type="message", role="assistant", content=[]),
                            )
                        )
                        yield self._send_event(
                            ResponseContentPartAdded(
                                type="response.content_part.added",
                                output_index=current_output_index,
                                content_index=current_content_index,
                                part=TextContentItem(type="output_text", text=""),
                            )
                        )

                    output_delta_buffer += self.parser.last_content_delta
                    should_send_output_text_delta = True
                    if browser_tool:
                        # we normalize on the full current text to get the right indices in citations
                        updated_output_text, annotations, has_partial_citations = (
                            browser_tool.normalize_citations(
                                current_output_text_content + output_delta_buffer
                            )
                        )
                        # remove the current text to get back the delta but now normalized
                        output_delta_buffer = updated_output_text[
                            len(current_output_text_content) :
                        ]

                        # Filter annotations to only include those whose start_index is not already present in current_annotations
                        # this is to avoid sending duplicate annotations as multiple annotations can't be in the same place
                        existing_start_indices = {
                            a["start_index"] for a in current_annotations
                        }
                        new_annotations = [
                            a
                            for a in annotations
                            if a["start_index"] not in existing_start_indices
                        ]
                        for a in new_annotations:
                            current_annotations.append(a)
                            citation = UrlCitation(**a)
                            yield self._send_event(
                                ResponseOutputTextAnnotationAdded(
                                    type="response.output_text.annotation.added",
                                    output_index=current_output_index,
                                    content_index=current_content_index,
                                    annotation_index=len(current_annotations),
                                    annotation=citation,
                                )
                            )

                        if has_partial_citations:
                            should_send_output_text_delta = False

                    if should_send_output_text_delta:
                        yield self._send_event(
                            ResponseOutputTextDelta(
                                type="response.output_text.delta",
                                output_index=current_output_index,
                                content_index=current_content_index,
                                delta=output_delta_buffer,
                            )
                        )
                        current_output_text_content += output_delta_buffer
                        output_delta_buffer = ""

                if (
                    self.parser.last_content_delta
                    and self.parser.current_channel == "analysis"
                    and self.parser.current_recipient is None
                ):
                    if not sent_output_item_added:
                        sent_output_item_added = True
                        reasoning_id = f"rs_{uuid.uuid4().hex}"
                        self.current_reasoning_item_id = reasoning_id
                        self.reasoning_item_ids.append(reasoning_id)
                        yield self._send_event(
                            ResponseOutputItemAdded(
                                type="response.output_item.added",
                                output_index=current_output_index,
                                item=ReasoningItem(
                                    id=reasoning_id,
                                    type="reasoning",
                                    summary=[],
                                    content=[],
                                ),
                            )
                        )
                        yield self._send_event(
                            ResponseContentPartAdded(
                                type="response.content_part.added",
                                output_index=current_output_index,
                                content_index=current_content_index,
                                part=ReasoningTextContentItem(
                                    type="reasoning_text", text=""
                                ),
                            )
                        )
                    yield self._send_event(
                        ResponseReasoningTextDelta(
                            type="response.reasoning_text.delta",
                            output_index=current_output_index,
                            content_index=current_content_index,
                            delta=self.parser.last_content_delta,
                        )
                    )

                try:
                    # purely for debugging purposes
                    output_token_text = encoding.decode_utf8([next_tok])
                    self.output_text += output_token_text
                    print(output_token_text, end="", flush=True)

                except RuntimeError:
                    pass

                if next_tok in encoding.stop_tokens_for_assistant_actions():
                    if len(self.parser.messages) > 0:
                        last_message = self.parser.messages[-1]
                        if (
                            self.use_browser_tool
                            and last_message.recipient is not None
                            and last_message.recipient.startswith("browser.")
                        ):
                            function_name = last_message.recipient[len("browser.") :]
                            action = None
                            parsed_args = browser_tool.process_arguments(last_message)
                            if function_name == "search":
                                action = WebSearchActionSearch(
                                    type="search",
                                    query=parsed_args["query"],
                                )
                            elif function_name == "open":
                                action = WebSearchActionOpenPage(
                                    type="open_page",
                                    url=(
                                        parsed_args["url"]
                                        if "url" in parsed_args
                                        else None
                                    ),
                                )
                            elif function_name == "find":
                                action = WebSearchActionFind(
                                    type="find",
                                    pattern=parsed_args["pattern"],
                                    url=(
                                        parsed_args["url"]
                                        if "url" in parsed_args
                                        else None
                                    ),
                                )

                            if action is not None:
                                web_search_call_id = f"ws_{uuid.uuid4().hex}"
                                self.browser_call_ids.append(web_search_call_id)
                                yield self._send_event(
                                    ResponseOutputItemAdded(
                                        type="response.output_item.added",
                                        output_index=current_output_index,
                                        item=WebSearchCallItem(
                                            type="web_search_call",
                                            id=web_search_call_id,
                                            action=action,
                                        ),
                                    )
                                )
                                yield self._send_event(
                                    ResponseWebSearchCallInProgress(
                                        type="response.web_search_call.in_progress",
                                        output_index=current_output_index,
                                        id=web_search_call_id,
                                    )
                                )

                            async def run_tool():
                                results = []
                                async for msg in browser_tool.process(last_message):
                                    results.append(msg)
                                return results

                            yield self._send_event(
                                ResponseWebSearchCallSearching(
                                    type="response.web_search_call.searching",
                                    output_index=current_output_index,
                                    id=web_search_call_id,
                                )
                            )
                            result = await run_tool()

                            new_tokens = encoding.render_conversation_for_completion(
                                Conversation.from_messages(result), Role.ASSISTANT
                            )

                            print(encoding.decode_utf8(new_tokens))
                            self.output_tokens.append(next_tok)
                            self.tokens.append(
                                encoding.encode("<|end|>", allowed_special="all")[0]
                            )

                            for token in new_tokens:
                                self.parser.process(token)
                                self.output_tokens.append(token)
                                self.tokens.append(token)

                            yield self._send_event(
                                ResponseWebSearchCallCompleted(
                                    type="response.web_search_call.completed",
                                    output_index=current_output_index,
                                    id=web_search_call_id,
                                )
                            )
                            yield self._send_event(
                                ResponseOutputItemDone(
                                    type="response.output_item.done",
                                    output_index=current_output_index,
                                    item=WebSearchCallItem(
                                        type="web_search_call",
                                        id=web_search_call_id,
                                        action=action,
                                    ),
                                )
                            )

                            current_output_index += 1
                            self.new_request = True

                            continue

                        elif (
                            self.use_code_interpreter
                            and last_message.recipient is not None
                            and (
                                last_message.recipient.startswith("python")
                                or (
                                    self.functions_python_as_builtin
                                    and last_message.recipient == "functions.python"
                                )
                            )
                        ):
                            code_call_id = f"ci_{uuid.uuid4().hex}"
                            code_snippet = None
                            if (
                                last_message.content
                                and len(last_message.content) > 0
                                and getattr(last_message.content[0], "text", None)
                            ):
                                text_value = last_message.content[0].text or ""
                                code_snippet = text_value if text_value.strip() else None

                            self.python_call_ids.append(code_call_id)
                            yield self._send_event(
                                ResponseOutputItemAdded(
                                    type="response.output_item.added",
                                    output_index=current_output_index,
                                    item=CodeInterpreterCallItem(
                                        type="code_interpreter_call",
                                        id=code_call_id,
                                        status="in_progress",
                                        code=code_snippet,
                                    ),
                                )
                            )
                            yield self._send_event(
                                ResponseCodeInterpreterCallInProgress(
                                    type="response.code_interpreter_call.in_progress",
                                    output_index=current_output_index,
                                    item_id=code_call_id,
                                )
                            )
                            if code_snippet:
                                yield self._send_event(
                                    ResponseCodeInterpreterCallCodeDelta(
                                        type="response.code_interpreter_call_code.delta",
                                        output_index=current_output_index,
                                        item_id=code_call_id,
                                        delta=code_snippet,
                                    )
                                )
                                yield self._send_event(
                                    ResponseCodeInterpreterCallCodeDone(
                                        type="response.code_interpreter_call_code.done",
                                        output_index=current_output_index,
                                        item_id=code_call_id,
                                        code=code_snippet,
                                    )
                                )
                            yield self._send_event(
                                ResponseCodeInterpreterCallInterpreting(
                                    type="response.code_interpreter_call.interpreting",
                                    output_index=current_output_index,
                                    item_id=code_call_id,
                                )
                            )

                            async def run_python_tool():
                                results = []
                                async for msg in self.python_tool.process(last_message):
                                    results.append(msg)
                                return results

                            result = await run_python_tool()

                            print(result)

                            code_outputs: list[
                                CodeInterpreterOutputLogs | CodeInterpreterOutputImage
                            ] = []
                            for message in result:
                                for content in getattr(message, "content", []):
                                    text_value = getattr(content, "text", None)
                                    if text_value:
                                        code_outputs.append(
                                            CodeInterpreterOutputLogs(
                                                type="logs",
                                                logs=text_value,
                                            )
                                        )

                            self.python_call_outputs[code_call_id] = code_outputs

                            new_tokens = encoding.render_conversation_for_completion(
                                Conversation.from_messages(result), Role.ASSISTANT
                            )

                            print(encoding.decode_utf8(new_tokens))
                            self.output_tokens.append(next_tok)
                            self.tokens.append(
                                encoding.encode("<|end|>", allowed_special="all")[0]
                            )

                            for token in new_tokens:
                                self.parser.process(token)
                                self.output_tokens.append(token)
                                self.tokens.append(token)

                            yield self._send_event(
                                ResponseCodeInterpreterCallCompleted(
                                    type="response.code_interpreter_call.completed",
                                    output_index=current_output_index,
                                    item_id=code_call_id,
                                )
                            )
                            yield self._send_event(
                                ResponseOutputItemDone(
                                    type="response.output_item.done",
                                    output_index=current_output_index,
                                    item=CodeInterpreterCallItem(
                                        type="code_interpreter_call",
                                        id=code_call_id,
                                        status="completed",
                                        code=code_snippet,
                                        outputs=code_outputs or None,
                                    ),
                                )
                            )

                            current_output_index += 1
                            self.new_request = True

                            continue

                        else:
                            break
                    else:
                        raise ValueError("No messages to process")
                if len(self.output_tokens) >= self.request_body.max_output_tokens:
                    break

                # Adding in the end if we know we are not done
                self.output_tokens.append(next_tok)

            if self.request is None or not await self.request.is_disconnected():
                response = generate_response(
                    self.initial_tokens,
                    self.output_tokens,
                    self.request_body,
                    debug_mode=self.debug_mode,
                    function_call_ids=self.function_call_ids,
                    response_id=self.response_id,
                    previous_response_id=self.request_body.previous_response_id,
                    browser_tool=self.browser_tool,
                    browser_call_ids=self.browser_call_ids,
                    python_tool=self.python_tool,
                    python_call_ids=self.python_call_ids,
                    python_call_outputs=self.python_call_outputs,
                    reasoning_ids=self.reasoning_item_ids,
                    treat_functions_python_as_builtin=self.functions_python_as_builtin,
                )
                if self.store_callback and self.request_body.store:
                    self.store_callback(self.response_id, self.request_body, response)
                yield self._send_event(
                    ResponseCompletedEvent(
                        type="response.completed",
                        response=response,
                    )
                )

    @app.post("/v1/responses", response_model=ResponseObject)
    async def generate(body: ResponsesRequest, request: Request):
        print("request received")
        print(body.reasoning)

        use_browser_tool = any(
            getattr(tool, "type", None) in ("browser_search", "web_search")
            for tool in (body.tools or [])
        )
        use_code_interpreter = any(
            getattr(tool, "type", None) == "code_interpreter"
            for tool in (body.tools or [])
        )

        if use_browser_tool:
            tool_backend = os.getenv("BROWSER_BACKEND", "exa")
            if tool_backend == "youcom":
                backend = YouComBackend(source="web")
            elif tool_backend == "exa":
                backend = ExaBackend(source="web")
            else:
                raise ValueError(f"Invalid tool backend: {tool_backend}")
            browser_tool = SimpleBrowserTool(backend=backend)
        else:
            browser_tool = None

        if use_code_interpreter:
            python_tool = PythonTool()
        else:
            python_tool = None

        python_function_name_conflict = any(
            getattr(tool, "type", None) == "function"
            and getattr(tool, "name", None) == "python"
            for tool in (body.tools or [])
        )
        functions_python_as_builtin = use_code_interpreter and not (
            python_function_name_conflict
        )

        if body.previous_response_id:
            prev = responses_store.get(body.previous_response_id)
            if prev:
                prev_req, prev_resp = prev

                def _ensure_list(inp):
                    if isinstance(inp, str):
                        return [
                            Item(
                                type="message",
                                role="user",
                                content=[TextContentItem(type="input_text", text=inp)],
                            )
                        ]
                    return list(inp)

                merged_input = _ensure_list(prev_req.input) + list(prev_resp.output)
                merged_input.extend(_ensure_list(body.input))

                if body.instructions is None:
                    body.instructions = prev_req.instructions
                body.input = merged_input

        system_message_content = SystemContent.new().with_conversation_start_date(
            datetime.datetime.now().strftime("%Y-%m-%d")
        )

        if body.reasoning is not None:
            try:

                reasoning_effort = get_reasoning_effort(body.reasoning.effort)
            except ValueError as e:
                from fastapi import HTTPException
                print(e)

                raise HTTPException(status_code=422, detail=str(e))
            system_message_content = system_message_content.with_reasoning_effort(
                reasoning_effort
            )

        if use_browser_tool:
            system_message_content = system_message_content.with_tools(
                browser_tool.tool_config
            )
        if use_code_interpreter:
            system_message_content = system_message_content.with_tools(
                python_tool.tool_config
            )

        system_message = Message.from_role_and_content(
            Role.SYSTEM, system_message_content
        )
        messages = [system_message]

        if body.instructions or body.tools:
            developer_message_content = DeveloperContent.new().with_instructions(
                body.instructions
            )

            tools = []
            for tool in body.tools:
                if tool.type == "function":
                    tools.append(
                        ToolDescription.new(
                            tool.name,
                            tool.description,
                            tool.parameters,
                        )
                    )

            if tools:
                developer_message_content = (
                    developer_message_content.with_function_tools(tools)
                )

            developer_message = Message.from_role_and_content(
                Role.DEVELOPER, developer_message_content
            )

            messages.append(developer_message)

        if isinstance(body.input, str):
            user_message = Message.from_role_and_content(Role.USER, body.input)
            messages.append(user_message)
        else:
            is_last_message_function_call_output = (
                len(body.input) > 0 and body.input[-1].type == "function_call_output"
            )
            function_call_map = {}
            # Find the index of the last assistant message
            last_assistant_idx = -1
            for idx, item in enumerate(body.input):
                if item.type == "message" and item.role == Role.ASSISTANT:
                    last_assistant_idx = idx

            for idx, item in enumerate(body.input):
                if item.type == "message":
                    # TODO: add system prompt handling
                    if isinstance(item.content, str):
                        messages.append(
                            Message.from_role_and_content(item.role, item.content)
                        )
                    else:
                        for content_item in item.content:
                            messages.append(
                                Message.from_role_and_content(
                                    item.role, content_item.text
                                )
                            )
                    # add final channel to the last assistant message if it's from the assistant
                    if item.role == Role.ASSISTANT:
                        messages[-1] = messages[-1].with_channel("final")
                elif item.type == "reasoning":
                    # Only include reasoning if it is after the last assistant message and we are handling a function call at the moment
                    if (
                        idx > last_assistant_idx
                        and is_last_message_function_call_output
                    ):
                        for content_item in item.content:
                            messages.append(
                                Message.from_role_and_content(
                                    Role.ASSISTANT, content_item.text
                                ).with_channel("analysis")
                            )
                elif item.type == "function_call":
                    function_call_map[item.call_id] = item
                    messages.append(
                        Message.from_role_and_content(Role.ASSISTANT, item.arguments)
                        .with_recipient(f"functions.{item.name}")
                        .with_channel("commentary")
                    )
                elif item.type == "function_call_output":
                    function_call = function_call_map.get(item.call_id, None)
                    if not function_call:
                        raise ValueError(f"Function call {item.call_id} not found")

                    messages.append(
                        Message.from_author_and_content(
                            Author.new(Role.TOOL, f"functions.{function_call.name}"),
                            item.output,
                        )
                        .with_recipient("assistant")
                        .with_channel("commentary")
                    )

        conversation = Conversation.from_messages(messages)

        initial_tokens = encoding.render_conversation_for_completion(
            conversation, Role.ASSISTANT
        )
        print(encoding.decode_utf8(initial_tokens))
        response_id = f"resp_{uuid.uuid4().hex}"

        def store_callback(rid: str, req: ResponsesRequest, resp: ResponseObject):
            responses_store[rid] = (req, resp)

        event_stream = StreamResponsesEvents(
            initial_tokens,
            body,
            as_sse=body.stream,
            request=request,
            response_id=response_id,
            store_callback=store_callback,
            browser_tool=browser_tool,
            python_tool=python_tool,
            functions_python_as_builtin=functions_python_as_builtin,
        )

        if body.stream:
            return StreamingResponse(event_stream.run(), media_type="text/event-stream")
        else:
            last_event = None
            async for event in event_stream.run():
                last_event = event

            return last_event.response

    return app

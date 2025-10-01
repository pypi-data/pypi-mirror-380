# from typing import Dict, Optional, Sequence, Union
#
# from slack_sdk.models.blocks.blocks import Block
# from slack_sdk.models.metadata import Metadata
# from slack_sdk.web.client import WebClient
# from slack_sdk.web.slack_response import SlackResponse
#
#
# class ChatStreamer:
#     """A helper class for streaming markdown text into a conversation using the chat streaming APIs.
#
#     This class provides a convenient interface for the chat.startStream, chat.appendStream,
#     and chat.stopStream API methods, with automatic buffering and state management.
#     """
#
#     def __init__(
#         self,
#         client: "WebClient",
#         *,
#         channel: str,
#         thread_ts: str,
#         recipient_team_id: Optional[str] = None,
#         recipient_user_id: Optional[str] = None,
#         unfurl_links: Optional[bool] = None,
#         unfurl_media: Optional[bool] = None,
#         buffer_size: int = 256,
#         **kwargs,
#     ):
#         """Initialize a new ChatStreamer instance.
#
#         Args:
#             client: The WebClient instance to use for API calls
#             channel: Channel to stream to
#             thread_ts: Thread timestamp to stream to
#             recipient_team_id: Team ID of the recipient (for Slack Connect)
#             recipient_user_id: User ID of the recipient (for Slack Connect)
#             unfurl_links: Whether to unfurl links
#             unfurl_media: Whether to unfurl media
#             buffer_size: Size of the internal buffer before automatically flushing (default: 256)
#             **kwargs: Additional arguments passed to the underlying API calls
#         """
#         self._client = client
#         self._stream_args = {
#             "channel": channel,
#             "thread_ts": thread_ts,
#             "recipient_team_id": recipient_team_id,
#             "recipient_user_id": recipient_user_id,
#             "unfurl_links": unfurl_links,
#             "unfurl_media": unfurl_media,
#             **kwargs,
#         }
#         self._buffer = ""
#         self._state = "starting"  # starting -> in_progress -> completed
#         self._stream_ts: Optional[str] = None
#         self._buffer_size = buffer_size
#
#     def append(
#         self,
#         *,
#         markdown_text: str,
#         **kwargs,
#     ) -> Optional[SlackResponse]:
#         """Append markdown text to the stream.
#
#         Args:
#             markdown_text: The markdown text to append
#             **kwargs: Additional arguments passed to the underlying API calls
#
#         Returns:
#             SlackResponse if the buffer was flushed, None if buffering
#
#         Raises:
#             SlackRequestError: If the stream is already completed
#         """
#         if self._state == "completed":
#             raise e.SlackRequestError(f"Cannot append to stream: stream state is {self._state}")
#
#         self._buffer += markdown_text
#
#         if len(self._buffer) >= self._buffer_size:
#             return self._flush_buffer(**kwargs)
#
#         return None
#
#     def stop(
#         self,
#         *,
#         markdown_text: Optional[str] = None,
#         blocks: Optional[Union[str, Sequence[Union[Dict, Block]]]] = None,
#         metadata: Optional[Union[Dict, Metadata]] = None,
#         **kwargs,
#     ) -> SlackResponse:
#         """Stop the stream and finalize the message.
#
#         Args:
#             markdown_text: Additional markdown text to append before stopping
#             blocks: Message blocks to add to the final message
#             metadata: Message metadata to add to the final message
#             **kwargs: Additional arguments passed to the underlying API calls
#
#         Returns:
#             SlackResponse from the chat.stopStream API call
#
#         Raises:
#             SlackRequestError: If the stream is already completed
#         """
#         if self._state == "completed":
#             raise e.SlackRequestError(f"Cannot stop stream: stream state is {self._state}")
#
#         # Add any final markdown text to the buffer
#         if markdown_text:
#             self._buffer += markdown_text
#
#         # Start the stream if not already started
#         if not self._stream_ts:
#             response = self._client.chat_startStream(
#                 **self._stream_args,
#                 **kwargs,
#             )
#             if not response.get("ts"):
#                 raise e.SlackRequestError("Failed to stop stream: stream not started")
#             self._stream_ts = response["ts"]
#             self._state = "in_progress"
#
#         # Stop the stream with any remaining buffer content
#         final_text = self._buffer if self._buffer else None
#         response = self._client.chat_stopStream(
#             channel=self._stream_args["channel"],
#             ts=self._stream_ts,
#             markdown_text=final_text,
#             blocks=blocks,
#             metadata=metadata,
#             **kwargs,
#         )
#
#         self._state = "completed"
#         return response
#
#     def _flush_buffer(self, **kwargs) -> SlackResponse:
#         """Flush the internal buffer by making appropriate API calls."""
#         if not self._stream_ts:
#             # Start the stream with the current buffer content
#             response = self._client.chat_startStream(
#                 **self._stream_args,
#                 markdown_text=self._buffer,
#                 **kwargs,
#             )
#             self._stream_ts = response.get("ts")
#             self._state = "in_progress"
#         else:
#             # Append to the existing stream
#             response = self._client.chat_appendStream(
#                 channel=self._stream_args["channel"],
#                 ts=self._stream_ts,
#                 markdown_text=self._buffer,
#                 **kwargs,
#             )
#
#         self._buffer = ""
#         return response

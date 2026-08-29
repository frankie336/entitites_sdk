#! projectdavid/clients/threads_client.py
from typing import Any, Dict, List, Optional

import httpx
from dotenv import load_dotenv
from projectdavid_common import UtilsInterface, ValidationInterface
from pydantic import ValidationError

from projectdavid.clients.base_client import BaseAPIClient

load_dotenv()
validator = ValidationInterface()
logging_utility = UtilsInterface.LoggingUtility()


class ThreadsClient(BaseAPIClient):
    def __init__(self, base_url: Optional[str] = None, api_key: Optional[str] = None):
        super().__init__(base_url=base_url, api_key=api_key)
        logging_utility.info(
            "ThreadsClient initialized with base_url: %s", self.base_url
        )

    def create_user(self, name: str) -> validator.UserRead:
        logging_utility.info("Creating user with name: %s", name)
        user_data = validator.UserCreate(name=name).model_dump()
        try:
            response = self.client.post("/v1/users", json=user_data)
            response.raise_for_status()
            created_user = response.json()
            return validator.UserRead(**created_user)
        except ValidationError as e:
            logging_utility.error("Validation error: %s", e.json())
            raise ValueError(f"Validation error: {e}")
        except httpx.HTTPStatusError as e:
            logging_utility.error("HTTP error occurred while creating user: %s", str(e))
            raise
        except Exception as e:
            logging_utility.error("Unexpected error creating user: %s", str(e))
            raise

    def create_thread(
        self,
        participant_ids: Optional[List[str]] = None,
        meta_data: Optional[Dict[str, Any]] = None,
    ) -> validator.ThreadRead:
        """
        Create a new conversation thread.

        Parameters
        ----------
        participant_ids:
            Optional list of participant IDs. If **None** (or an empty list) the
            back‑end will default to *“the authenticated user only”*.
        meta_data:
            Arbitrary key/value metadata to attach to the thread.
        """
        meta_data = meta_data or {}

        payload = validator.ThreadCreate(
            participant_ids=participant_ids or None,  # ✨ schema wants None, not []
            meta_data=meta_data,
        ).model_dump(exclude_none=True)

        logging_utility.info(
            "Creating thread (participants=%s)",
            "default-user" if not participant_ids else len(participant_ids),
        )

        try:
            resp = self.client.post("/v1/threads", json=payload)
            resp.raise_for_status()
            return validator.ThreadRead.model_validate(resp.json())

        except ValidationError as ve:
            logging_utility.error("ThreadCreate validation failed: %s", ve.json())
            raise ValueError(f"Validation error when creating thread: {ve}") from ve

        except httpx.HTTPStatusError as he:
            logging_utility.error(
                "HTTP %d while creating thread: %s",
                he.response.status_code,
                he.response.text,
            )
            raise

        except Exception as exc:
            logging_utility.exception("Unexpected error creating thread")
            raise

    def retrieve_thread(self, thread_id: str) -> validator.ThreadRead:
        logging_utility.info("Retrieving thread with id: %s", thread_id)
        try:
            response = self.client.get(f"/v1/threads/{thread_id}")
            response.raise_for_status()
            thread = response.json()
            return validator.ThreadRead(**thread)
        except ValidationError as e:
            logging_utility.error("Validation error: %s", e.json())
            raise ValueError(f"Validation error: {e}")
        except httpx.HTTPStatusError as e:
            logging_utility.error("HTTP error retrieving thread: %s", str(e))
            raise
        except Exception as e:
            logging_utility.error("Unexpected error retrieving thread: %s", str(e))
            raise

    def update_thread(
        self,
        thread_id: str,
        *,
        participant_ids: Optional[List[str]] = None,
        meta_data: Optional[Dict[str, Any]] = None,
        tool_resources: Optional[Dict[str, Any]] = None,
    ) -> validator.ThreadReadDetailed:
        logging_utility.info("Updating thread with id: %s", thread_id)
        try:
            validated_updates = validator.ThreadUpdate(
                participant_ids=participant_ids,
                meta_data=meta_data,
                tool_resources=tool_resources,
            )

            response = self.client.put(
                f"/v1/threads/{thread_id}",
                json=validated_updates.model_dump(),
            )
            response.raise_for_status()
            updated_thread = response.json()
            return validator.ThreadReadDetailed(**updated_thread)

        except httpx.HTTPStatusError as e:
            logging_utility.error("HTTP error updating thread: %s", str(e))
            raise
        except Exception as e:
            logging_utility.error("Unexpected error updating thread: %s", str(e))
            raise

    def update_thread_metadata(
        self, thread_id: str, new_metadata: Dict[str, Any]
    ) -> validator.ThreadRead:
        try:
            response = self.client.put(
                f"/v1/threads/{thread_id}/metadata",
                json=new_metadata,
            )
            response.raise_for_status()
            return validator.ThreadRead.model_validate(response.json())
        except httpx.HTTPStatusError as e:
            logging_utility.error(
                "HTTP error updating thread metadata: %d %s",
                e.response.status_code,
                e.response.text,
            )
            raise
        except Exception as e:
            logging_utility.error("Error updating thread metadata: %s", str(e))
            raise

    def list_threads(self, user_id: str) -> List[str]:
        logging_utility.info("Listing threads for user: %s", user_id)
        try:
            response = self.client.get(f"/v1/threads/user/{user_id}")
            response.raise_for_status()
            # backend returns JSON array directly, e.g. ["t1","t2"]
            return response.json()
        except httpx.HTTPStatusError as e:
            logging_utility.error(
                "HTTP error listing threads: %d %s",
                e.response.status_code,
                e.response.text,
            )
            if e.response.status_code == 404:
                # no threads yet
                return []
            raise
        except Exception as e:
            logging_utility.error("Unexpected error listing threads: %s", str(e))
            raise

    def list_thread_records(self, user_id: str) -> List[validator.ThreadRead]:
        """List ordinary thread records without changing ``list_threads``."""
        logging_utility.info("Listing thread records for user: %s", user_id)
        try:
            response = self.client.get(f"/v1/threads/user/{user_id}/records")
            response.raise_for_status()
            return [
                validator.ThreadRead.model_validate(record)
                for record in response.json()
            ]
        except httpx.HTTPStatusError as e:
            logging_utility.error(
                "HTTP error listing thread records: %d %s",
                e.response.status_code,
                e.response.text,
            )
            if e.response.status_code == 404:
                return []
            raise
        except Exception as e:
            logging_utility.error(
                "Unexpected error listing thread records: %s",
                str(e),
            )
            raise

    def delete_thread(self, thread_id: str) -> validator.ThreadDeleted | None:
        """
        Delete a thread.
        ▶ On success:  returns ThreadDeleted(id=…, object='thread.deleted', deleted=True)
        ▶ If not found: returns None
        """
        logging_utility.info("Deleting thread with id: %s", thread_id)

        try:
            resp = self.client.delete(f"/v1/threads/{thread_id}")
            resp.raise_for_status()  # 2xx → OK
            return validator.ThreadDeleted(**resp.json())  # ← parse envelope
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                return None  # thread not found
            logging_utility.error("HTTP error deleting thread: %s", e)
            raise
        except Exception as e:
            logging_utility.error("Unexpected error deleting thread: %s", e)
            raise

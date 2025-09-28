from typing import Optional, Any
from pydantic import BaseModel, ConfigDict

from siada.session.session_models import RunningSession

from siada.support.checkpoint_tracker import CheckPointTracker
from siada.foundation.logging import logger as logging

class CodeAgentContext(BaseModel):

    model_config = ConfigDict(arbitrary_types_allowed=True)

    session: Optional[RunningSession] = None

    root_dir: str | None = None

    provider: str | None = None

    # Interactive mode flag, True for interactive mode, False for non-interactive mode
    interactive_mode: bool = True

    user_memory: Optional[str] = None

    checkpoint_tracker: Optional[CheckPointTracker] = None

    # MCP相关扩展
    mcp_service: Optional[Any] = None
    mcp_config: Optional[Any] = None
    mcp_enabled: bool = False

    @property
    def task_message_state(self):
        return self.session.state.task_message_state

    @property
    def model_run_config(self):
        return self.session.siada_config.llm_config

    def save_checkpoints(self):
        if self.checkpoint_tracker and self.session:
            try:
                self.checkpoint_tracker.save_checkpoints(
                    session_id=self.session.session_id,
                    task_message_state=self.session.state.task_message_state,
                )
            except Exception as e:
                logging.error(f"Error saving checkpoints: {e}")

    @property
    def session_id(self):
        if self.session:
            return self.session.session_id
        return None
    
    @property
    def auto_compact(self):
        if self.session:
            return self.session.siada_config.auto_compact
        return False

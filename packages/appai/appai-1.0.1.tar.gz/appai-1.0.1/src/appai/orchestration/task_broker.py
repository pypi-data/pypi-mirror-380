"""Task broker for autonomous task distribution via bidding."""

import asyncio
import logging
from typing import List, Optional, Dict
from datetime import datetime

from aiapp.models import SubTask
from aiapp.models.communication import TaskBid, TaskAnnouncement
from aiapp.models.swarm import SwarmConfig

logger = logging.getLogger(__name__)


class TaskBroker:
    """
    Manages task distribution via competitive bidding.

    Agents bid on tasks based on their capabilities and availability.
    Best-suited agent wins the task.
    """

    def __init__(self, config: SwarmConfig):
        self.config = config
        self.pending_bids: Dict[str, List[TaskBid]] = {}
        self.announced_tasks: Dict[str, TaskAnnouncement] = {}

    async def announce_task(self, task: SubTask) -> TaskAnnouncement:
        """
        Announce task to swarm for bidding.

        Returns TaskAnnouncement with bidding details.
        """
        announcement = TaskAnnouncement(
            task_id=task.id,
            description=task.description,
            category=task.category,
            complexity=task.estimated_complexity.value,
            dependencies_met=len(task.dependencies) == 0,
            max_bidders=self.config.max_bidders_per_task,
            bidding_deadline=self.config.bidding_window
        )

        self.announced_tasks[task.id] = announcement
        self.pending_bids[task.id] = []

        logger.info(
            f"📢 Announced task {task.id} ({task.category}) "
            f"- bidding window: {self.config.bidding_window}s"
        )

        return announcement

    async def receive_bid(self, bid: TaskBid) -> bool:
        """
        Receive and validate bid from agent.

        Returns True if bid accepted, False if rejected.
        """
        task_id = bid.task_id

        # Check if task exists
        if task_id not in self.announced_tasks:
            logger.warning(f"Bid for unknown task {task_id} from {bid.agent_name}")
            return False

        announcement = self.announced_tasks[task_id]

        # Check if bidding window still open
        elapsed = (datetime.now() - announcement.announced_at).total_seconds()
        if elapsed > announcement.bidding_deadline:
            logger.warning(
                f"Late bid from {bid.agent_name} for {task_id} "
                f"(elapsed: {elapsed:.1f}s)"
            )
            return False

        # Check if max bidders reached
        current_bids = self.pending_bids[task_id]
        if len(current_bids) >= announcement.max_bidders:
            # Check if this bid is better than worst current bid
            if current_bids:
                worst_bid = min(current_bids, key=lambda b: b.confidence)
                if bid.confidence > worst_bid.confidence:
                    current_bids.remove(worst_bid)
                    logger.debug(
                        f"Replaced bid from {worst_bid.agent_name} "
                        f"(conf: {worst_bid.confidence:.2f}) "
                        f"with {bid.agent_name} (conf: {bid.confidence:.2f})"
                    )
                else:
                    return False

        # Accept bid
        self.pending_bids[task_id].append(bid)
        logger.info(
            f"✅ Accepted bid from {bid.agent_name} for {task_id} "
            f"(confidence: {bid.confidence:.2f}, "
            f"current bids: {len(self.pending_bids[task_id])}/{announcement.max_bidders})"
        )

        return True

    async def select_winner(self, task_id: str) -> Optional[TaskBid]:
        """
        Select winning bid for task after bidding window closes.

        Selection criteria:
        1. Confidence (50%)
        2. Capability match (30%)
        3. Current load (20% - lower is better)

        Returns winning bid or None if no bids.
        """
        if task_id not in self.pending_bids:
            logger.error(f"No bids found for task {task_id}")
            return None

        bids = self.pending_bids[task_id]

        if not bids:
            logger.warning(f"No bids received for task {task_id}")
            return None

        # Score each bid
        scored_bids = []
        for bid in bids:
            score = (
                bid.confidence * 0.5 +
                bid.capabilities_match * 0.3 +
                (1 - min(bid.current_load / 10.0, 1.0)) * 0.2  # Normalize load
            )
            scored_bids.append((score, bid))

        # Sort by score (descending)
        scored_bids.sort(key=lambda x: x[0], reverse=True)

        winner_score, winner = scored_bids[0]

        logger.info(
            f"🏆 Task {task_id} awarded to {winner.agent_name} "
            f"(score: {winner_score:.2f}, confidence: {winner.confidence:.2f}, "
            f"load: {winner.current_load})"
        )

        # Log runner-ups
        if len(scored_bids) > 1:
            runner_ups = ", ".join(
                f"{bid.agent_name}({score:.2f})"
                for score, bid in scored_bids[1:]
            )
            logger.debug(f"   Runner-ups: {runner_ups}")

        # Clean up
        del self.pending_bids[task_id]
        del self.announced_tasks[task_id]

        return winner

    async def wait_for_bids(self, task_id: str) -> None:
        """Wait for bidding window to close."""
        if task_id not in self.announced_tasks:
            return

        announcement = self.announced_tasks[task_id]
        await asyncio.sleep(announcement.bidding_deadline)

        logger.debug(
            f"⏰ Bidding closed for {task_id}, "
            f"received {len(self.pending_bids.get(task_id, []))} bids"
        )

    def get_bid_count(self, task_id: str) -> int:
        """Get current number of bids for task."""
        return len(self.pending_bids.get(task_id, []))

    def cancel_task(self, task_id: str) -> None:
        """Cancel task announcement and reject all bids."""
        if task_id in self.pending_bids:
            del self.pending_bids[task_id]
        if task_id in self.announced_tasks:
            del self.announced_tasks[task_id]

        logger.info(f"❌ Cancelled task {task_id}")

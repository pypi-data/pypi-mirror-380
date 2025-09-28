from __future__ import annotations
from typing import Literal, TypeVar, Generic, Any, Set, Optional, List, Callable, Dict
from abc import ABC, abstractmethod

from .min_heap import MinHeap

EventStatus = Literal["Unscheduled", "Scheduled", "Finished", "Cancelled"]
TEventData = TypeVar("TEventData")
TEntityData = TypeVar("TEntityData")

class SimulationEvent(Generic[TEventData]):
    """
    Represents an event within the simulation.

    An event is a fundamental unit of action that occurs at a specific time
    and is associated with a simulation entity.
    """

    def __init__(
        self,
        type: str,
        start_time: float,
        end_time: float,
        data: TEventData,
        entity: SimulationEntity[Any],
    ):
        self.type: str = type
        self.status: EventStatus = "Unscheduled"
        self.start_time: float = start_time
        self.end_time: float = end_time
        self.data: TEventData = data
        self.entity: SimulationEntity[Any] = entity

    def set_status(self, status: EventStatus) -> None:
        """Updates the status of the event."""
        self.status = status

    def __lt__(self, other: SimulationEvent[Any]) -> bool:
        """
        Comparison method for the MinHeap. Events are ordered by their end_time.
        """
        return self.end_time < other.end_time

class SimulationEntity(ABC, Generic[TEntityData]):
    """
    Abstract base class for all entities in the simulation.

    An entity is an active component of the simulation that can schedule,
    handle, and react to events.
    """

    def __init__(self, id: str, data: TEntityData, engine: SimulationEngine):
        self.id = id
        self.data = data
        self._engine = engine
        self._active_events: Set[SimulationEvent[Any]] = set()
        engine.register_entity(self)

    def destroy(self) -> None:
        """Removes the entity and its associated events from the simulation."""
        self._engine.unregister_entity(self.id)
    
    @abstractmethod
    def handle_event(self, event: SimulationEvent[Any]) -> None:
        """
        Processes a finished event. Must be implemented by subclasses.

        Args:
            event (SimulationEvent): The event to handle.
        """
        pass

    def interpolate(self) -> None:
        """
        Optional method to update entity state when event is in progress.
        
        This is useful for visualization or event cancellation where an entity's
        state (e.g., position) needs to be known at current simulation time.
        """
        pass

    def on_event_received(self, event: SimulationEvent[Any]) -> None:
        """
        Callback triggered when a subscribed event occurs.
        Can be implemented by subclasses to react to events from other entities.
        
        Args:
            event (SimulationEvent): The received event.
        """
        pass
    
    def schedule_event(
        self,
        type: str,
        end_time: float,
        data: TEventData,
        start_time: Optional[float] = None
    ) -> SimulationEvent[TEventData]:
        """
        Schedules a new event in the simulation engine.

        Args:
            type (TEventType): The type of the event.
            end_time (float): The time at which the event will be processed.
            data (TEventData): The data associated with the event.
            start_time (Optional[float]): The time the event begins. If None, defaults
                                           to the current simulation time.

        Returns:
            SimulationEvent: The newly created and scheduled event.
        """
        if start_time is None:
            start_time = self.current_time

        event = SimulationEvent(type, start_time, end_time, data, self)
        self._active_events.add(event)
        self._engine.schedule_event(event)
        return event

    def cancel_event(self, event: SimulationEvent[Any]) -> bool:
        """
        Cancels a previously scheduled event.

        Args:
            event (SimulationEvent): The event to cancel.

        Returns:
            bool: True if the event was active and is now cancelled, False otherwise.
        """
        self.interpolate()

        if event in self._active_events:
            self._active_events.remove(event)
            return self._engine.cancel_event(event)
        return False
    
    def remove_event(self, event: SimulationEvent[Any])->None:
        self._active_events.discard(event)

    def get_entity(self, entity_id: str) -> Optional[SimulationEntity[Any]]:
        """
        Retrieves another entity from the engine by its ID.

        Args:
            entity_id (str): The unique identifier of the entity.

        Returns:
            Optional[SimulationEntity]: The entity if found, otherwise None.
        """
        return self._engine.get_entity(entity_id)

    @property
    def events(self) -> List[SimulationEvent[Any]]:
        """Returns the shallow-copied list of active events associated with this entity."""
        return list(self._active_events)

    @property
    def event_size(self) -> int:
        """Returns the number of active events for this entity."""
        return len(self._active_events)

    @property
    def current_time(self) -> float:
        """Returns the current time of the simulation engine."""
        return self._engine.current_time

class SubscriptionConfig:
    """Configuration for event subscriptions between entities."""
    def __init__(
        self,
        event_types: Optional[List[str]] = None,
        event_statuses: Optional[List[EventStatus]] = None,
        filter: Optional[Callable[[SimulationEvent[Any]], bool]] = None
    ):
        self.event_types = event_types
        self.event_statuses = event_statuses
        self.filter = filter

class SimulationEngine:
    """
    Manages the simulation state, event queue, and entity interactions.
    """

    def __init__(self):
        self._event_queue = MinHeap[SimulationEvent[Any]]()
        self._entities: Dict[str, SimulationEntity[Any]] = {}
        self._subscriptions: Dict[str, Dict[str, SubscriptionConfig]] = {}
        self._current_time: float = 0.0

    def register_entity(self, entity: SimulationEntity[Any]) -> None:
        """
        Registers a new entity with the engine.

        Args:
            entity (SimulationEntity): The entity to register.
        
        Raises:
            ValueError: If an entity with the same ID is already registered.
        """
        if entity.id in self._entities:
            raise ValueError(f"Entity with id {entity.id} already registered.")
        self._entities[entity.id] = entity

    def unregister_entity(self, entity_id: str) -> bool:
        """
        Removes an entity and its subscriptions from the engine.
        
        Also cancels all active events associated with the entity.

        Args:
            entity_id (str): The ID of the entity to unregister.

        Returns:
            bool: True if the entity was found and removed, False otherwise.
        """
        entity = self._entities.get(entity_id)
        if not entity:
            return False

        # Cancel associated active events
        for event in entity.events:
            entity.cancel_event(event)

        # Clean subscriptions
        self._subscriptions.pop(entity_id, None)
        for subscribers in self._subscriptions.values():
            subscribers.pop(entity_id, None)

        self._entities.pop(entity_id)
        return True

    def schedule_event(self, event: SimulationEvent[Any]) -> None:
        """
        Adds an event to the event queue.

        Args:
            event (SimulationEvent): The event to schedule.

        Raises:
            ValueError: If the event's end time is in the past.
        """
        if event.end_time < self._current_time:
            raise ValueError("Cannot schedule event in the past.")
        self._event_queue.add(event)
        event.set_status("Scheduled")
    
    def cancel_event(self, event: SimulationEvent[Any]) -> bool:
        """
        Marks a scheduled event as 'Cancelled'.
        
        The event remains in the queue but will be ignored when processed.

        Args:
            event (SimulationEvent): The event to cancel.

        Returns:
            bool: True if the event status was successfully changed to 'Cancelled'.
        """
        if event.status == "Scheduled":
            event.set_status("Cancelled")
            self._notify_subscribers(event)
            return True
        return False

    def subscribe(
        self,
        subscriber_id: str,
        publisher_id: str,
        config: Optional[SubscriptionConfig] = None
    ) -> None:
        """
        Subscribes one entity to another's events.

        Args:
            subscriber_id (str): The ID of the entity that will receive notifications.
            publisher_id (str): The ID of the entity that produces events.
            config (Optional[SubscriptionConfig]): Configuration to filter events.
        
        Raises:
            KeyError: If subscriber or publisher entity is not found.
        """
        if subscriber_id not in self._entities:
            raise KeyError(f"Subscriber entity {subscriber_id} not found.")
        if publisher_id not in self._entities:
            raise KeyError(f"Publisher entity {publisher_id} not found.")

        if publisher_id not in self._subscriptions:
            self._subscriptions[publisher_id] = {}
        
        self._subscriptions[publisher_id][subscriber_id] = config or SubscriptionConfig()

    def unsubscribe(self, subscriber_id: str, publisher_id: str) -> bool:
        """
        Unsubscribes an entity from another's events.

        Args:
            subscriber_id (str): The ID of the subscriber entity.
            publisher_id (str): The ID of the publisher entity.

        Returns:
            bool: True if the subscription existed and was removed, False otherwise.
        """
        if publisher_id in self._subscriptions:
            if subscriber_id in self._subscriptions[publisher_id]:
                del self._subscriptions[publisher_id][subscriber_id]
                return True
        return False

    def _notify_subscribers(self, event: SimulationEvent[Any]) -> None:
        """Notifies all relevant subscribers about an event."""
        subscribers = self._subscriptions.get(event.entity.id)
        if not subscribers:
            return
        
        for subscriber_id, config in subscribers.items():
            if config.event_types and event.type not in config.event_types:
                continue
            if config.event_statuses and event.status not in config.event_statuses:
                continue
            if config.filter and not config.filter(event):
                continue
            
            subscriber_entity = self._entities.get(subscriber_id)
            if subscriber_entity:
                subscriber_entity.on_event_received(event)

    def step_to(self, target_time: float) -> None:
        """
        Advances the simulation to a specific target time, processing all
        events up to that time.

        Args:
            target_time (float): The time to advance the simulation to.
        """
        while (event := self._event_queue.peek()) is not None and event.end_time <= target_time:
            self._event_queue.pop()

            # Ignore events that have been cancelled.
            if event.status == "Cancelled":
                continue

            self._current_time = event.end_time
            
            event.entity.remove_event(event)
            event.entity.handle_event(event)
            event.set_status("Finished")
            
            self._notify_subscribers(event)

        self._current_time = target_time

        # Interpolate states of all entities for continuous visualization.
        for entity in self._entities.values():
            entity.interpolate()

    def advance(self, elapsed_time: float) -> None:
        """
        Advances the simulation by a given amount of time.

        Args:
            elapsed_time (float): The duration to advance the simulation.
        """
        if elapsed_time < 0:
            raise ValueError("Elapsed time must be non-negative.")
        self.step_to(self.current_time + elapsed_time)

    def get_entity(self, entity_id: str) -> Optional[SimulationEntity[Any]]:
        """
        Retrieves an entity by its ID.

        Args:
            entity_id (str): The unique ID of the entity.

        Returns:
            Optional[SimulationEntity]: The entity if found, otherwise None.
        """
        return self._entities.get(entity_id)

    @property
    def current_time(self) -> float:
        """Returns the current simulation time."""
        return self._current_time
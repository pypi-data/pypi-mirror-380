import heapq
from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")

class MinHeap(Generic[T]):
    """
    A generic minimum heap implementation.
    
    This heap implementation is simplified and does not support direct removal of items.
    It is designed to work with the simulation engine where events are marked as 'Cancelled'
    instead of being physically removed from the queue.
    """

    def __init__(self, initial_items: List[T] = []) -> None:
        """
        Initializes the MinHeap.

        Args:
            initial_items (List[T], optional): A list of items to initialize the heap with.
                                                Defaults to [].
        """
        self._heap = initial_items[:]
        heapq.heapify(self._heap)

    def add(self, item: T)->None:
        """
        Adds a new item to the heap.

        Args:
            item (T): The item to add.
        """
        heapq.heappush(self._heap, item)

    def peek(self) -> Optional[T]:
        """
        Returns the smallest item from the heap without removing it.

        Returns:
            T | None: The smallest item, or None if the heap is empty.
        """
        return self._heap[0] if self._heap else None
    
    def pop(self) -> Optional[T]:
        """
        Removes and returns the smallest item from the heap.

        Returns:
            T | None: The smallest item, or None if the heap is empty.
        """
        return heapq.heappop(self._heap) if self._heap else None
    
    @property
    def size(self) -> int:
        """
        Returns the number of items in the heap.
        """
        return len(self._heap)
    
    @property
    def items(self) -> List[T]:
        """
        Returns a list of all items in the heap.
        """
        return self._heap
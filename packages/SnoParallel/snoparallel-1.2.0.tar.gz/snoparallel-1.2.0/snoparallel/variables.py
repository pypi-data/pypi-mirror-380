"""
This module contains the variable class to access variables in parallelized work cycles.
"""

from multiprocessing.shared_memory import SharedMemory
from threading import Lock
from typing import Optional

from numpy import array, float32, float64, int32, int64, ndarray
from numpy.typing import NDArray

VariableType = float32 | float64 | int32 | int64
ArrayType = NDArray[VariableType]


def get_variable_size(value: VariableType) -> int:
    """
    Get the variable size in bytes.

    Args:
        value: Variable value.

    Returns:
        Variable size in bytes.
    """
    return 2 * value.nbytes


class Variable:
    """
    Class to access variables in parallelized work cycles.
    """

    def __init__(self, value: VariableType | ArrayType, memory: str, lock: Lock) -> None:
        """
        Args:
            value: Initial value to set for the variable.
            memory: Reference to the memory location where the variable value is stored.
            lock: SyncManager.Lock instance which is coupled to the variable.

        Raises:
            TypeError: Type of the value not supported.
        """
        self._memory = memory
        self._lock = lock
        self._type = value.dtype
        self._bytes = value.nbytes
        self._shape = (2,) + value.shape
        self._variable = isinstance(value, VariableType)

        self.write(value=value)
        self.update()

    def read(self) -> VariableType | ArrayType:
        """
        Read the (old) variable value.

        Returns:
            Variable value.
        """
        with self._lock:
            memory = SharedMemory(name=self._memory, create=False)
            view: ArrayType = ndarray(shape=self._shape, dtype=self._type, buffer=memory.buf)
            value = view[0] if self._variable else array(object=view[0], copy=True)
            memory.close()

        return value

    def write(self, value: VariableType | ArrayType) -> None:
        """
        Write the new variable value.

        Args:
            value: New variable value.

        Raises:
            TypeError: Value type does not correspond with the variable type.
        """
        if value.nbytes != self._bytes:
            raise TypeError("Value type does not correspond with the variable type.")

        self._write(value=value)

    def _write(self, value: Optional[VariableType | ArrayType]) -> None:
        """
        Write the new value or trigger an update if it is None.

        Args:
            value: Trigger an update if value is None, otherwise overwrite new value with the given value.
        """
        with self._lock:
            memory = SharedMemory(name=self._memory, create=False)
            view: ArrayType = ndarray(shape=self._shape, dtype=self._type, buffer=memory.buf)

            if value is not None:
                view[1] = value
            else:
                view[0] = view[1]

            memory.close()

    def update(self) -> None:
        """
        Update the old variable value with the new one.
        """
        self._write(value=None)

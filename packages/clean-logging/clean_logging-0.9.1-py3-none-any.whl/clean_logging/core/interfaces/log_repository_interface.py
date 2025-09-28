from abc import ABC, abstractmethod




class ILogRepository(ABC):
    @abstractmethod
    def get_logs(self, limit: int = None, offset: int = None):
        """
        Save or update a log.

        Args:
            log: Log entity from the domain layer.

        Returns:
            T: The saved or updated log entity.

        Raises:
            ValueError: If required fields are missing.
        """
        pass

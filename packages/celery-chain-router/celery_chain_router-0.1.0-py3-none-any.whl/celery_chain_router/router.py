import hashlib
import random
import os
import json
from celery import signals
from typing import Dict, Any, Optional, List, Set, Tuple, Union

class ChainRouter:
    """
    A Celery router that uses permutation chains for task distribution.
    
    This router distributes tasks across workers using mathematical properties of
    permutation chains, providing natural load balancing and data locality.
    
    Attributes:
        universe_size (int): Size of the permutation universe
        seed (int): Random seed for permutation generation
    """
    
    _shared_worker_positions = {}
    
    def __init__(self, universe_size: int = 10000, seed: int = 42, 
                 persistent_file: str = None, reset_persistent: bool = False):
        """
        Initialize the chain router.
        
        Args:
            universe_size: Size of the permutation universe
            seed: Random seed for deterministic permutation
            persistent_file: Path to file for persisting worker positions
            reset_persistent: Whether to reset the persistent storage on init
        """
        self.universe_size = universe_size
        self.seed = seed
        self.permutation = self._create_permutation()
        self.task_hashes = {}
        self.worker_stats = {}
        self.persistent_file = persistent_file or os.path.expanduser("~/.chain_router_workers.json")
        
        if reset_persistent and os.path.exists(self.persistent_file):
            try:
                os.remove(self.persistent_file)
                self.__class__._shared_worker_positions = {}
            except Exception as e:
                print(f"Error resetting persistent storage: {e}")
        
        self._load_worker_positions()
        self._register_signals()

    def _create_permutation(self) -> List[int]:
        """Create a deterministic permutation of the universe"""
        perm = list(range(self.universe_size))
        random.seed(self.seed)
        random.shuffle(perm)
        random.seed()  # Reset the seed
        return perm
    
    def _hash_task(self, task_name: str, task_args: Any = None, 
                  task_kwargs: Any = None) -> int:
        """Convert task information to a stable numeric hash"""
        task_str = f"{task_name}:{str(task_args)}:{str(task_kwargs)}"
        hash_int = int(hashlib.md5(task_str.encode()).hexdigest(), 16)
        return hash_int % self.universe_size
    
    def _normalize_worker_name(self, worker_name: str) -> str:
        """Extract just the worker name without hostname."""
        return worker_name.split('@')[0] if '@' in worker_name else worker_name
    
    def _load_worker_positions(self):
        """Load worker positions from persistent storage if available"""
        # First use class-level storage
        self.worker_positions = dict(self.__class__._shared_worker_positions)
        
        try:
            if os.path.exists(self.persistent_file):
                with open(self.persistent_file, 'r') as f:
                    stored_positions = json.load(f)
                    
                    # Normalize worker names (remove @hostname part)
                    normalized_positions = {}
                    for worker, pos in stored_positions.items():
                        normalized_name = self._normalize_worker_name(worker)
                        normalized_positions[normalized_name] = pos
                    
                    self.worker_positions = normalized_positions
                    self.__class__._shared_worker_positions = normalized_positions
        except Exception as e:
            print(f"Error loading worker positions: {e}")
    
    def _save_worker_positions(self):
        """Save worker positions to persistent storage"""
        try:
            with open(self.persistent_file, 'w') as f:
                json.dump(self.worker_positions, f)
        except Exception as e:
            print(f"Error saving worker positions: {e}")
    
    def _find_worker_for_hash(self, task_hash: int) -> Optional[str]:
        """
        Find the appropriate worker for a given task hash using chain following.
        This method uses the permutation chain to find a worker near the task hash.
        
        Args:
            task_hash: Hash value of the task
            
        Returns:
            Worker name or None if no workers are available
        """
        if not self.worker_positions:
            return None
            
        # Find closest worker position using chain following
        min_distance = float('inf')
        closest_worker = None
        
        for worker, position in self.worker_positions.items():
            # Calculate chain distance using permutation
            distance = abs(self.permutation[position] - task_hash)
            if distance < min_distance:
                min_distance = distance
                closest_worker = worker
                
        return closest_worker
    
    def register_worker(self, worker_name: str) -> int:
        """
        Register a worker and assign its starting position
        
        Args:
            worker_name: Name of the worker to register
            
        Returns:
            Position assigned to the worker
        """
        # Normalize worker name
        normalized_name = self._normalize_worker_name(worker_name)
        
        if normalized_name not in self.worker_positions:
            hash_val = int(hashlib.md5(normalized_name.encode()).hexdigest(), 16)
            position = hash_val % self.universe_size
            self.worker_positions[normalized_name] = position
            self.__class__._shared_worker_positions[normalized_name] = position
            self.worker_stats[normalized_name] = 0
            self._save_worker_positions()
            return position
        return self.worker_positions[normalized_name]
    
    def _register_signals(self) -> None:
        """Register Celery signals for worker monitoring"""
        # Store reference to self for the signal handlers
        router_instance = self
        
        @signals.worker_ready.connect
        def on_worker_ready(sender, **kwargs):
            hostname = sender.hostname
            normalized_name = router_instance._normalize_worker_name(hostname)
            router_instance.register_worker(normalized_name)
    
    def __call__(self, task_name, args=None, kwargs=None, options=None, **kw):
        """
        Make the router callable directly by Celery.
        
        Args:
            task_name: Name of the task (string)
            args: Task positional arguments
            kwargs: Task keyword arguments
            options: Additional options dict
            **kw: Additional keyword arguments
            
        Returns:
            Dict with queue name or None for default routing
        """
        return self.route_task(task_name, args, kwargs, options)
    
    def route_task(self, task_name, args=None, kwargs=None, options=None):
        """
        Route a task to the appropriate worker based on chain following.
        
        Args:
            task_name: Name of the task (string)
            args: Task positional arguments
            kwargs: Task keyword arguments
            options: Additional options dict
            
        Returns:
            Dict with queue name or None for default routing
        """
        # Reload worker positions to ensure we have the latest
        self._load_worker_positions()
        
        if not self.worker_positions:
            return None
            
        # Get task hash
        task_hash = self._hash_task(task_name, args, kwargs)
        
        # Store hash for future reference
        task_id = f"{task_name}:{str(args)}:{str(kwargs)}"
        self.task_hashes[task_id] = task_hash
        
        # Find worker using chain following
        worker = self._find_worker_for_hash(task_hash)
        
        if worker:
            queue_name = self._normalize_worker_name(worker)
            self.worker_stats[worker] = self.worker_stats.get(worker, 0) + 1
            return {'queue': queue_name}
        
        # Fallback: simple round-robin assignment
        workers = list(self.worker_positions.keys())
        if not workers:
            return None
            
        selected_worker = workers[task_hash % len(workers)]
        self.worker_stats[selected_worker] = self.worker_stats.get(selected_worker, 0) + 1
        
        # Extract just the worker name part before the @ symbol
        queue_name = self._normalize_worker_name(selected_worker)
        return {'queue': queue_name}
    
    def get_stats(self) -> Dict[str, int]:
        """Get statistics about task distribution"""
        return self.worker_stats.copy()

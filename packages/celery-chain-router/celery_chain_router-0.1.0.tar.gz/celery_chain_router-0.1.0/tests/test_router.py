import os
import pytest
import json
import tempfile
from celery_chain_router import ChainRouter

class TestChainRouter:
    """Test suite for the ChainRouter class."""
    
    def setup_method(self):
        """Set up test environment before each test method."""
        # Create a temporary file for persistent storage
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()
        
        # Create router with test config
        self.router = ChainRouter(
            universe_size=100,  # Small universe for testing
            seed=42,            # Fixed seed for deterministic results
            persistent_file=self.temp_file.name,
            reset_persistent=True
        )
    
    def teardown_method(self):
        """Clean up after each test method."""
        # Remove temporary file
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_worker_registration(self):
        """Test that workers can be registered."""
        # Register workers
        self.router.register_worker("worker1")
        self.router.register_worker("worker2")
        self.router.register_worker("worker3")
        
        # Check that workers are registered
        assert "worker1" in self.router.worker_positions
        assert "worker2" in self.router.worker_positions
        assert "worker3" in self.router.worker_positions
        
        # Check positions are within universe
        for worker, pos in self.router.worker_positions.items():
            assert 0 <= pos < self.router.universe_size
    
    def test_worker_persistence(self):
        """Test that worker positions are persisted to file."""
        # Register workers
        self.router.register_worker("worker1")
        self.router.register_worker("worker2")
        
        # Check file exists
        assert os.path.exists(self.temp_file.name)
        
        # Check file content
        with open(self.temp_file.name, 'r') as f:
            data = json.load(f)
            assert "worker1" in data
            assert "worker2" in data
        
        # Create new router with same file
        new_router = ChainRouter(
            universe_size=100,
            seed=42,
            persistent_file=self.temp_file.name
        )
        
        # Check that worker positions are loaded
        assert "worker1" in new_router.worker_positions
        assert "worker2" in new_router.worker_positions
        
        # Check positions match
        assert new_router.worker_positions["worker1"] == self.router.worker_positions["worker1"]
        assert new_router.worker_positions["worker2"] == self.router.worker_positions["worker2"]
    
    def test_task_routing(self):
        """Test that tasks are routed to appropriate workers."""
        # Register workers
        self.router.register_worker("worker1")
        self.router.register_worker("worker2")
        
        # Route a task
        route1 = self.router.route_task("task1", args=[1, 2])
        assert "queue" in route1
        assert route1["queue"] in ["worker1", "worker2"]
        
        # Route same task again, should go to same worker
        route2 = self.router.route_task("task1", args=[1, 2])
        assert route2["queue"] == route1["queue"]
        
        # Route different task
        route3 = self.router.route_task("task2", args=[3, 4])
        assert "queue" in route3
        
        # Route similar task, should go to same worker due to locality
        route4 = self.router.route_task("task1", args=[1, 3])
        assert "queue" in route4
    
    def test_worker_normalization(self):
        """Test that worker names are properly normalized."""
        # Register worker with hostname
        self.router.register_worker("worker1@host")
        
        # Check that it's normalized in the worker positions
        assert "worker1" in self.router.worker_positions
        
        # Route a task
        route = self.router.route_task("task1", args=[1, 2])
        
        # Check queue name is normalized
        assert route["queue"] == "worker1"
    
    def test_stats_tracking(self):
        """Test that worker stats are tracked."""
        # Register workers
        self.router.register_worker("worker1")
        self.router.register_worker("worker2")
        
        # Route tasks
        for i in range(10):
            self.router.route_task(f"task{i}", args=[i])
        
        # Get stats
        stats = self.router.get_stats()
        
        # Check stats are tracked
        assert "worker1" in stats or "worker2" in stats
        assert sum(stats.values()) == 10 
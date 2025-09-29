"""Utility functions for the chain router."""

import random
from typing import List, Dict, Set, Tuple


def analyze_permutation_cycles(permutation: List[int]) -> Dict[str, any]:
    """
    Analyze the cycle structure of a permutation.
    
    Args:
        permutation: A permutation represented as a list
        
    Returns:
        Dictionary with cycle statistics
    """
    cycles = []
    visited = set()
    
    for start in range(len(permutation)):
        if start in visited:
            continue
            
        cycle = []
        current = start
        while current not in visited:
            visited.add(current)
            cycle.append(current)
            current = permutation[current]
            
        if cycle:
            cycles.append(cycle)
    
    cycle_lengths = [len(c) for c in cycles]
    
    return {
        'num_cycles': len(cycles),
        'cycle_lengths': cycle_lengths,
        'min_length': min(cycle_lengths) if cycle_lengths else 0,
        'max_length': max(cycle_lengths) if cycle_lengths else 0,
        'avg_length': sum(cycle_lengths) / len(cycle_lengths) if cycle_lengths else 0
    }


def simulate_task_distribution(router, num_tasks: int = 1000) -> Dict[str, int]:
    """
    Simulate distributing tasks and analyze the distribution.
    
    Args:
        router: An instance of ChainRouter
        num_tasks: Number of tasks to simulate
        
    Returns:
        Dictionary with worker task counts
    """
    task_counts = {worker: 0 for worker in router.worker_positions}
    
    for i in range(num_tasks):
        # Create a simulated task
        task_name = "simulated_task"
        task_args = (i,)
        
        # Route the task
        route = router.route_task(task_name, task_args)
        if route:
            worker = route.get('queue')
            if worker in task_counts:
                task_counts[worker] += 1
    
    return task_counts

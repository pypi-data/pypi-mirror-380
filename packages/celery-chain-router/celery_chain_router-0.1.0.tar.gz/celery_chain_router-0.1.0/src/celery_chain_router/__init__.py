"""
Celery Chain Router Package

This package provides the ChainRouter, a Celery router that distributes tasks
across workers using permutation chains for better data locality and load balancing.
"""

from celery_chain_router.router import ChainRouter

__version__ = '0.1.0'
__all__ = ['ChainRouter']

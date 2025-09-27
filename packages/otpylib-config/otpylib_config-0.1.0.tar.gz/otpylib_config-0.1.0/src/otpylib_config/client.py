#!/usr/bin/env python3
"""
Configuration Client API

Simple client interface for configuration access.
"""

from otpylib import gen_server
from .atoms import GET_CONFIG, PUT_CONFIG, SUBSCRIBE, RELOAD
from .data import CONFIG_MGR_SERVER


class Config:
    """Simple client API for configuration access."""
    
    @staticmethod
    async def get(path: str, default=None):
        """Get configuration value by path."""
        return await gen_server.call(CONFIG_MGR_SERVER, (GET_CONFIG, path, default))
    
    @staticmethod  
    async def put(path: str, value):
        """Set configuration value at path."""
        return await gen_server.call(CONFIG_MGR_SERVER, (PUT_CONFIG, path, value))
    
    @staticmethod
    async def subscribe(pattern: str, callback):
        """Subscribe to configuration changes matching pattern."""
        return await gen_server.call(CONFIG_MGR_SERVER, (SUBSCRIBE, pattern, callback))
    
    @staticmethod
    async def reload():
        """Force reload from all sources."""
        return await gen_server.cast(CONFIG_MGR_SERVER, (RELOAD,))

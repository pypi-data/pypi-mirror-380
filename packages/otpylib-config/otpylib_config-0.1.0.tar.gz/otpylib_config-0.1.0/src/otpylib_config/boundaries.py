#!/usr/bin/env python3
"""
Configuration Manager GenServer

The core GenServer that manages configuration state, sources, and subscriptions.
Uses atom-based message dispatch for high performance.
"""

import types
from typing import Any
from otpylib import gen_server

from .atoms import (
    GET_CONFIG, PUT_CONFIG, SUBSCRIBE, UNSUBSCRIBE, RELOAD, 
    PING, STOP, STATUS, RELOAD_TICK,
    time_atom_comparison
)
from .data import ConfigManagerState


# =============================================================================
# GenServer Callbacks
# =============================================================================

callbacks = types.SimpleNamespace()


async def init(config_spec):
    """Initialize configuration manager with sources."""
    from . import core
    
    state = ConfigManagerState(
        sources=config_spec.sources if hasattr(config_spec, 'sources') else [],
        reload_interval=getattr(config_spec, 'reload_interval', 30.0)
    )
    
    # Load initial configuration from all sources
    result = await core.reconcile_configuration(state)
    if result.is_err():
        print(f"Warning: Initial configuration load failed: {result.unwrap_err()}")
    
    return state

callbacks.init = init


async def handle_call(message, caller, state):
    """Handle synchronous configuration requests using atom dispatch."""
    from . import core
    
    match message:
        case msg_type, path_str, default if time_atom_comparison(msg_type, GET_CONFIG):
            # Get configuration value
            result = await core.get_config_value(path_str, default, state)
            if result.is_ok():
                return (gen_server.Reply(payload=result.unwrap()), state)
            else:
                error = Exception(result.unwrap_err())
                return (gen_server.Reply(payload=error), state)
        
        case msg_type, path_str, value if time_atom_comparison(msg_type, PUT_CONFIG):
            # Set configuration value
            result = await core.ensure_config_value(path_str, value, state)
            if result.is_ok():
                change_info = result.unwrap()
                
                # Notify subscribers if value changed
                if change_info["changed"]:
                    await _notify_subscribers(state, change_info["path"], 
                                           change_info["old_value"], change_info["new_value"])
                
                return (gen_server.Reply(payload=True), state)
            else:
                error = Exception(result.unwrap_err())
                return (gen_server.Reply(payload=error), state)
        
        case msg_type, pattern_str, callback if time_atom_comparison(msg_type, SUBSCRIBE):
            # Subscribe to configuration changes
            result = await core.ensure_subscription(pattern_str, callback, state)
            if result.is_ok():
                return (gen_server.Reply(payload=True), state)
            else:
                error = Exception(result.unwrap_err())
                return (gen_server.Reply(payload=error), state)
        
        case msg_type, pattern_str, callback if time_atom_comparison(msg_type, UNSUBSCRIBE):
            # Unsubscribe from configuration changes
            result = await core.ensure_subscription_absent(pattern_str, callback, state)
            if result.is_ok():
                return (gen_server.Reply(payload=True), state)
            else:
                error = Exception(result.unwrap_err())
                return (gen_server.Reply(payload=error), state)
        
        case msg_type if time_atom_comparison(msg_type, PING):
            # Health check ping
            return (gen_server.Reply(payload="pong"), state)
        
        case msg_type if time_atom_comparison(msg_type, STATUS):
            # Get manager status
            result = await core.get_manager_status(state)
            if result.is_ok():
                return (gen_server.Reply(payload=result.unwrap()), state)
            else:
                error = Exception(result.unwrap_err())
                return (gen_server.Reply(payload=error), state)
        
        case _:
            error = NotImplementedError(f"Unknown call: {message}")
            return (gen_server.Reply(payload=error), state)

callbacks.handle_call = handle_call


async def handle_cast(message, state):
    """Handle asynchronous configuration updates."""
    from . import core
    
    match message:
        case msg_type if time_atom_comparison(msg_type, RELOAD):
            # Force reload from all sources
            result = await core.reconcile_configuration(state)
            if result.is_ok():
                reload_result = result.unwrap()
                if reload_result.config_changes > 0:
                    print(f"Manual reload: {reload_result.config_changes} changes from {reload_result.sources_loaded} sources")
                await _notify_reload_changes(state, result)
            else:
                print(f"Warning: Manual reload failed: {result.unwrap_err()}")
            return (gen_server.NoReply(), state)
        
        case msg_type if time_atom_comparison(msg_type, STOP):
            # Stop the GenServer
            return (gen_server.Stop(), state)
        
        case ("source_update", source_name, new_config):
            # Update from specific source - for now just trigger full reload
            result = await core.reconcile_configuration(state)
            if result.is_ok():
                reload_result = result.unwrap()
                if reload_result.config_changes > 0:
                    print(f"Source update reload: {reload_result.config_changes} changes")
                await _notify_reload_changes(state, result)
            else:
                print(f"Warning: Source update reload failed: {result.unwrap_err()}")
            return (gen_server.NoReply(), state)
        
        case _:
            print(f"Config Manager: Unknown cast: {message}")
            return (gen_server.NoReply(), state)

callbacks.handle_cast = handle_cast


async def handle_info(message, state):
    """Handle info messages (direct mailbox sends)."""
    from . import core
    
    match message:
        case msg_type if time_atom_comparison(msg_type, RELOAD_TICK):
            # Periodic reload tick
            old_config = state.config.copy()
            result = await core.reconcile_configuration(state)
            if result.is_ok():
                reload_result = result.unwrap()
                if reload_result.config_changes > 0:
                    print(f"Periodic reload: {reload_result.config_changes} changes from {reload_result.sources_loaded} sources")
                    # Notify subscribers of specific changes
                    await _notify_config_changes(state, old_config, state.config)
            else:
                print(f"Warning: Periodic reload failed: {result.unwrap_err()}")
            return (gen_server.NoReply(), state)
        
        case _:
            print(f"Config Manager: Received info: {message}")
            return (gen_server.NoReply(), state)

callbacks.handle_info = handle_info


async def terminate(reason, state):
    """Cleanup on termination."""
    if reason is not None:
        print(f"Config Manager terminated with error: {reason}")
    else:
        print("Config Manager terminated normally")
    
    print(f"Final state: {len(state.config)} config keys, {len(state.subscribers)} subscribers")

callbacks.terminate = terminate


# =============================================================================
# Internal Helper Functions
# =============================================================================

async def _notify_subscribers(state, path: str, old_value: Any, new_value: Any):
    """Notify pattern-matched subscribers of a configuration change."""
    from . import core
    
    matching_callbacks = core.get_matching_subscribers(path, state)
    
    for callback in matching_callbacks:
        try:
            await callback(path, old_value, new_value)
        except Exception as e:
            print(f"Warning: Subscriber callback failed for {path}: {e}")


async def _notify_reload_changes(state, reload_result):
    """Notify subscribers of configuration changes detected during reload."""
    # For manual/source reloads, we don't have the old config to compare
    # This is a simplified notification - in practice we'd track changes during reload
    pass


async def _notify_config_changes(state, old_config: dict, new_config: dict):
    """Notify subscribers of specific configuration changes."""
    from . import core
    
    changes = core.get_config_differences(old_config, new_config)
    
    for change in changes:
        await _notify_subscribers(state, change["path"], 
                                change["old_value"], change["new_value"])

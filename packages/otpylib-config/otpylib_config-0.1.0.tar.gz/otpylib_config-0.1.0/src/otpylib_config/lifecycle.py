#!/usr/bin/env python3
"""
Configuration Manager Lifecycle

OTP supervision for the configuration manager with reload ticker.
"""

import anyio
import anyio.abc
from result import Ok, Err, Result
from otpylib import gen_server, supervisor, mailbox

from .boundaries import callbacks
from .data import CONFIG_MGR_SERVER, ConfigSpec
from .atoms import RELOAD_TICK, PING


async def reload_ticker(config_spec: ConfigSpec, *, task_status: anyio.abc.TaskStatus):
    """
    Send periodic reload ticks to the configuration manager.
    This task runs as a supervised child alongside the GenServer.
    """
    task_status.started()
    
    while True:
        try:
            await anyio.sleep(config_spec.reload_interval)
            
            # Send reload tick to the GenServer's mailbox
            await mailbox.send(CONFIG_MGR_SERVER, RELOAD_TICK)
            
        except anyio.get_cancelled_exc_class():
            break
        except Exception as e:
            # Log error but continue - supervisor will restart if we crash
            print(f"Error in configuration reload ticker: {e}")
            await anyio.sleep(1)  # Brief pause before retrying


async def _health_probe(child_id: str, _child) -> Result[None, str]:
    """
    Health probe for the Configuration Manager GenServer.
    Uses ping to verify liveness and basic correctness.
    """
    try:
        result = await gen_server.call(CONFIG_MGR_SERVER, PING)
        if result == "pong":
            return Ok(None)
        else:
            return Err(f"Unexpected ping response: {result}")
    except Exception as e:
        return Err(f"Health probe failed: {e}")


async def start(config_spec: ConfigSpec, *, task_status: anyio.abc.TaskStatus):
    """
    Start Configuration Manager with proper OTP supervision and reload ticker.
    
    Starts both the GenServer and a ticker task for automatic reloading.
    Both are supervised children that will be restarted on failure.
    """
    from otpylib.types import Permanent, OneForOne
    
    print(f"Starting Configuration Manager '{config_spec.id}' with OTP supervision...")
    
    # Define GenServer as supervised child with health monitoring
    genserver_spec = supervisor.child_spec(
        id="config_mgr_genserver",
        task=gen_server.start,
        args=[callbacks, config_spec, CONFIG_MGR_SERVER],
        restart=Permanent(),  # Always restart on failure
        health_check_enabled=True,
        health_check_interval=30.0,
        health_check_timeout=5.0,
        health_check_fn=_health_probe,
    )
    
    # Define reload ticker as supervised child
    ticker_spec = supervisor.child_spec(
        id="config_reload_ticker",
        task=reload_ticker,
        args=[config_spec],
        restart=Permanent(),  # Always restart ticker on failure
    )
    
    # Both children under supervision
    children = [genserver_spec, ticker_spec]
    
    # Configure supervision strategy
    supervisor_opts = supervisor.options(
        strategy=OneForOne(),  # Restart failed children independently
        max_restarts=3,        # Allow 3 restarts
        max_seconds=60         # Within 60 seconds
    )
    
    print("Starting OTP supervision with GenServer and reload ticker...")
    
    # Start supervision - both GenServer and ticker are monitored
    await supervisor.start(children, supervisor_opts, task_status=task_status)
    
    print("Configuration Manager started with supervised children")


async def stop():
    """Stop the Configuration Manager GenServer gracefully."""
    print("Stopping Configuration Manager...")
    try:
        await gen_server.cast(CONFIG_MGR_SERVER, "stop")
        print("Configuration Manager stopped")
    except Exception as e:
        print(f"Error stopping Configuration Manager: {e}")

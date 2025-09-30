from fastapi import APIRouter, Request, HTTPException

from core_functions.limiter import limiter
from core_functions.auth import get_user_role
from core_functions.load_monitor import LoadMonitor
from core_functions.infos import get_system_infos, list_processes, get_system_uptime, get_system_user_infos

router = APIRouter()

monitor = LoadMonitor()
monitor.start()
monitor.set_decimal_place_value(2)

@router.get(
        "/system/uptime",
        tags=["System"],
        description="This endpoint returns the system uptime in days, hours, minutes, and seconds + full seconds.",
        responses={
            200: {
                "description": "Uptime returned successfully",
                "content": {
                    "application/json": {
                        "example": {
                            "uptime": {
                                "days": 2,
                                "hours": 5,
                                "minutes": 33,
                                "seconds": 12,
                                "total_seconds": 189192
                            }
                        }
                    }
                }
            },
            401: {
                "description": "Unauthorized. Invalid or missing API key",
                "content": {
                    "application/json": {
                        "example": {"detail": "Invalid or missing API key"}
                    }
                }
            }
        }
)
@limiter.limit("10/minute")
def get_uptime(request: Request, user_data = get_user_role("user")):
    return get_system_uptime()

@router.get(
        "/system/processes",
        tags=["System"],
        description="Returns a list of all running processes on the server with their PID, name, and status.",
        responses={
            200: {
                "description": "Processes listed successfully",
                "content": {
                    "application/json": {
                        "example": [
                            {"pid": 1, "name": "init", "status": "running"},
                            {"pid": 2, "name": "bash", "status": "sleeping"}
                        ]
                    }
                }
            },
            401: {
                "description": "Unauthorized. Invalid or missing API key",
                "content": {
                    "application/json": {
                        "example": {"detail": "Invalid or missing API key"}
                    }
                }
            }
        }
)
@limiter.limit("20/minute")
def get_processes(request: Request, user_data = get_user_role("user")):
    processes = list_processes()
    return processes

@router.get(
        "/system/system-infos",
        tags=["System"],
        description="This endpoint returns the system information of the server.",
        responses={
            200: {
                "description": "System information returned",
                "content": {
                    "application/json": {
                        "example": {
                            "system": "Linux",
                            "node_name": "hostname",
                            "release": "system release",
                            "version": "system version",
                            "machine": "x86_64",
                            "processor": "x86_64",
                            "cpu_count": 1,
                            "memory_total": 2062983168,
                            "disk_total": 499963174912
                        }
                    }
                }
            },
            401: {
                "description": "Unauthorized. Invalid or missing API key",
                "content": {
                    "application/json": {
                        "example": {"detail": "Invalid or missing API key"}
                    }
                }
            }
        }
)
@limiter.limit("10/minute")
def system_infos(request: Request, user_data = get_user_role("user")):
    system_info = get_system_infos()
    return system_info

@router.get(
    "/system/system-user",
    tags=["System"],
    description="Returns informations about a specific user account on the server like UID, GID, shell and home dir.",
    responses={
        200: {
            "description": "User informations returned successfully.",
            "content": {
                "application/json": {
                    "example": {
                        "username": "testuser",
                        "uid": 1001,
                        "gid": 1001,
                        "shell": "/bin/bash",
                        "home": "/home/testuser"
                    }
                }
            }
        },
        401: {
            "description": "Unauthorized. Invalid or missing API key",
            "content": {
                "application/json": {
                    "example": {"detail": "Invalid or missing API key"}
                }
            }
        },
        404: {
            "description": "User not found on the system.",
            "content": {
                "application/json": {
                    "example": {"detail": "User not found on the system"}
                }
            }
        }
    }
)
@limiter.limit("5/minute")
def system_user_infos(request: Request, username: str, user_data = get_user_role("user")):
    return_code, user_info = get_system_user_infos(username)

    if return_code == True:
        return user_info
    
    elif return_code == None:
        raise HTTPException(status_code=404, detail="User not found on the system")

@router.get(
        "/system/avg-load",
        tags=["System"],
        description="Returns the average load of the system over the last minutes.",
        responses={
            200: {
                "description": "Average load returned successfully",
                "content": {
                    "application/json": {
                        "examples": {
                            "default_values": {
                                "summary": "Default values (2 decimal places, last 3 loads)",
                                "value": {
                                    "system": {
                                        "average_load": 0.11,
                                        "last_loads": [0.20, 0.10, 0.05]
                                    },
                                    "cpu": {
                                        "average_load": 0.06,
                                        "last_loads": [0.12, 0.05, 0.02]
                                    }
                                }
                            },
                            "custom_values": {
                                "summary": "Custom values (4 decimal places, last 5 loads)",
                                "value": {
                                    "system": {
                                        "average_load": 0.0875,
                                        "last_loads": [0.2034, 0.1023, 0.0543, 0.0456, 0.0321]
                                    },
                                    "cpu": {
                                        "average_load": 0.0458,
                                        "last_loads": [0.1234, 0.0543, 0.0234, 0.0156, 0.0123]
                                    }
                                }
                            },
                            "last_load_length_exceeds_max": {
                                "summary": "Last load length exceeds the maximum (last loads set to 10 but only 5 available)",
                                "value": {
                                    "system": {
                                        "average_load": 0.3012,
                                        "last_loads": [0.1787, 0.1309, 0.3364, 0.2241, 0.1128]
                                    },
                                    "cpu": {
                                        "average_load": 0.2654,
                                        "last_loads": [0.263, 0.25, 0.253, 0.25, 0.25]
                                    }
                                }
                            }
                        }
                    }
                }
            },
            401: {
                "description": "Unauthorized. Invalid or missing API key",
                "content": {
                    "application/json": {
                        "example": {"detail": "Invalid or missing API key"}
                    }
                }
            }
        }
)
@limiter.limit("5/minute")
def avg_load(request: Request, decimal_places: int = 2, last_load_length: int = 3, user_data = get_user_role("user")):
    monitor.set_decimal_place_value(decimal_places)
    return {
        "system": {
            "average_load": monitor.get_average_system_load(),
            "last_loads": monitor.get_last_system_loads(n=last_load_length)
        },
        "cpu": {
            "average_load": monitor.get_average_cpu_load(),
            "last_loads": monitor.get_last_cpu_loads(n=last_load_length)
        }
    }
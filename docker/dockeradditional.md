# Difference Between `pause`, `unpause`, `stop`, and `kill` Commands in Docker 🐳

| Command      | Description                                                                                                                                   | Effect on Container                                                      | Example Usage                               | Notes                                                                                                                                     |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `pause`      | Suspends all processes in a container by signaling them with `SIGSTOP`.                                                                       | Processes are frozen; container remains running but inactive.             | `docker pause <container_id>`               | Useful when you need to temporarily free up system resources without stopping the container completely.                                    |
| `unpause`    | Resumes all processes in a paused container by signaling them with `SIGCONT`.                                                                 | Processes continue execution from where they were paused.                 | `docker unpause <container_id>`             | Use this to resume a container that has been paused.                                                                                      |
| `stop`       | Gracefully stops a running container by sending `SIGTERM`, allowing processes to exit cleanly before sending `SIGKILL` after a timeout period. | Processes are allowed to terminate gracefully; container changes to "stopped" state. | `docker stop <container_id>`                | Good for stopping containers when you want processes to shut down cleanly.                                                                |
| `kill`       | Immediately stops a running container by sending `SIGKILL`, forcefully terminating all processes.                                              | Processes are terminated immediately; container changes to "stopped" state. | `docker kill <container_id>`                | Use this when a container is unresponsive or needs to be stopped immediately.                                                             |

## Detailed Explanation with Examples

### `docker pause`

- **Description:** Freezes all running processes in the specified container.
- **Effect:** The container remains running, but all processes are suspended (no CPU cycles are used).
- **Example Usage:**

  ```bash
  docker pause my_container
  ```

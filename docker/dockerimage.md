# Searching for Docker Images Without GUI

Docker provides the `docker search` command, allowing you to search for images directly from the command line without the need for a graphical user interface (GUI). This command searches Docker Hub (the default public registry) and returns a list of available images matching your search query.

## Basic Syntax

```bash
docker search [OPTIONS] TERM
```
**`TERM`**: The search term you want to use (e.g., nginx, mysql).

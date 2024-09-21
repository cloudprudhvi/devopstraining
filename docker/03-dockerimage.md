# Searching for Docker Images Without GUI

Docker provides the `docker search` command, allowing you to search for images directly from the command line without the need for a graphical user interface (GUI). This command searches Docker Hub (the default public registry) and returns a list of available images matching your search query.

## Basic Syntax

```bash
docker search [OPTIONS] TERM
```
**`TERM`**: The search term you want to use (e.g., nginx, mysql).

# Docker `image history` Command

The `docker image history` command is used to view the history of an image, showing the intermediate layers that make up a Docker image. This can be helpful to understand how an image was built, what commands were run during its creation, and how large each layer is.

## Syntax

```bash
docker image history [OPTIONS] IMAGE
Eg: docker image history nginx
```

## you can try the commands listed below
**`--no-trunc`**: Display the full output, avoiding truncation of long command lines.
```
docker image history --no-trunc nginx
```

**`--quiet, -q`**: Show only numeric IDs of image layers, without additional details.
```
docker image history -q nginx
```
# Docker `save` and `load` Commands

The `docker save` and `docker load` commands are used for saving and loading Docker images in and out of tarball archives. These commands are particularly useful for sharing or backing up Docker images across systems that may not have direct access to Docker registries.

## `docker save` Command

The `docker save` command is used to export one or more Docker images into a tarball (compressed archive). This allows you to save an image to a file, which can then be transferred to another system or stored as a backup.

### Syntax

```bash
docker save [OPTIONS] IMAGE [IMAGE...]
Eg: docker save -o my_image.tar nginx:latest
```

# Docker `load` Command

The `docker load` command is used to load images from a tarball archive created by `docker save`. This allows you to import an image onto another system, even if the system doesn’t have access to a Docker registry.

## Syntax

```bash
docker load [OPTIONS]
Eg: docker load -i my_image.tar
```




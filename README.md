To make the container bash executable

```
docker build -t tasklogger --rm .
docker run -it --name task_logger --rm tasklogger
```
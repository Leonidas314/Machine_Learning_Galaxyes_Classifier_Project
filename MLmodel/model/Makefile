.PHONY:

# Project
build:
	docker build -t model .
run:
	docker run -it --network=host --device=/dev/kfd --device=/dev/dri --ipc=host --shm-size 24G --group-add video --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -e AMDGPU_TARGETS="gfx1032" -e HSA_OVERRIDE_GFX_VERSION="10.3.0" -v .:/workspace model:latest

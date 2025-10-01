# test.thing

A simple, modern VM runner.

## Goals.

 - one-file copypastelib
 - easy to hook up to pytest
 - future-oriented, built on systemd features in the guest (credentials, ssh-over-vsock, etc)
   - might limit usefulness for testing older OSes but we can add
     [workarounds](workarounds/) as required
 - works without networking configured in guest
 - supporting the existing features of [cockpit-bots](https://github.com/cockpit-project/bots)

## Host requirements

 - Python 3.12, standard library
 - qemu
 - ssh
 - [systemd-ssh-proxy](https://www.freedesktop.org/software/systemd/man/latest/systemd-ssh-proxy.html)
   (available since systemd v256, [polyfill
   available](workarounds/systemd-ssh-proxy))
 - [vhost-device-vsock](https://crates.io/crates/vhost-device-vsock)

## Guest requirements

The guest should meet the requirements of the [Virtual Machine Image API
Specification](doc/VirtualMachineAPI.md).

There are polyfills for many of the require functionalities in
[workarounds/](./workarounds/).

## Try it

The easiest way to get `test.thing` is from PyPI:
[test.thing](https://pypi.org/project/test.thing/).

If you want to depend on the package, please pin the version number exactly.
It's early days and there is no guarantees about API (or even CLI)
compatibility, even between micro releases.  You can also simply copy
[testthing.py](./testthing.py) into your project.

For cli use, the easiest thing is to `pip install test.thing` which will put an
executable called `tt` in your path.  This is sort of like the existing
cockpit-bots `vm-run`.  If you want to test Cockpit images, you can do
something like:

```sh
  tt \
      -v \
      -L 9091:127.0.0.1:9090 \
      -s cockpit.socket \
      bots/images/arch
```

An ssh control socket is created for sending commands and can also be used
externally, avoiding the need to authenticate.  A suggested ssh config:

```
Host tt.*
        ControlPath ${XDG_RUNTIME_DIR}/test.thing/%h/ssh
```

And then you can say `ssh tt.0` or `scp file tt.0:/tmp`.

You can also take a look at [`test/test_example.py`](test/test_example.py) and
run `TEST_IMAGE=/path/to/image.qcow2 pytest`.  This was originally tested with
the [examples images from
composefs-rs](https://github.com/containers/composefs-rs/tree/main/examples).

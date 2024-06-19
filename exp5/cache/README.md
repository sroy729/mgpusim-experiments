When you want to change some configuration, then need to get the `samples/runner` files from the MGPUsim repo and do the changes

The top file is the `runner.go` here, only the platform gets built and we can either edit the `timingplatfor.go` file or create our own configuration file, then add it to the `runner.go` file and change it accordingly

You do need to have a main package, here `exp.go` does that work and you can specify which bechmark to run in there.

It's better to have a separate folder for each benchmark, or we can automate this task.

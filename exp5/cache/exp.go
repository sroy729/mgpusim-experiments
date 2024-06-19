package main

import (
	"flag"
	"fmt"

	"github.com/sarchlab/mgpusim/v3/benchmarks/heteromark/fir"
	"github.com/sroy729/mgpusim-experiments/exp5/cache/runner"
)

func main() {
	flag.Parse()

	fmt.Println("trying to run fir benchmark")
	runner := runner.Runner{}
	runner.Init()

	benchmark := fir.NewBenchmark(runner.Driver())
	benchmark.Length = 40962348
	runner.AddBenchmark(benchmark)

	runner.Run()
}

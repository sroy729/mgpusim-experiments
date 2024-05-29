package main

import (
	"flag"
	"fmt"

	"github.com/sarchlab/mgpusim/v3/benchmarks/heteromark/fir"
	"github.com/sarchlab/mgpusim/v3/samples/runner"
)

func main() {
	fmt.Println("vim-go")
	flag.Parse()
	runner := runner.Runner{}
	runner.Init()

	benchmark := fir.NewBenchmark(runner.Driver())
	benchmark.Length = 4096
	runner.AddBenchmark(benchmark)

	runner.Run()
}

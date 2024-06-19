How does `MakeBuilder()` works in GO.
It is way of construct a complex objects. the builder pattern is a design pattern used to create complex objects step by step.

It is useful when you need to create an object with many optional parameters.

**Step1: Define the `Computer` type**
``` 
package main 
import "fmt"

type Computer struct{
	CPU		string
	RAM		int
	Storage	int
	GPU		string
	Monitor	string
	NoofGPU	int
	}

```

**Step2: Define a `ComputerBuilder`**

```
type ComputerBuilder struct{
	cpu		string
	ram		int
	storage	int
	gpu		string
	monitor	string
	noofgpu	int
	}

func MakeBuilder() *ComputerBuilder{
	return &ComputerBuilder{}
}

func (b *ComputerBuilder) WithCPU(cpu string) *ComputerBuilder{
	b.cpu = cpu
	return b
}

func (b *ComputerBuilder) WithRAM(ram int) *ComputerBuilder{
	b.ram = ram
	return b
}

func (b *ComputerBuilder) WithStorage(storage int) *ComputerBuilder{
	b.storage = storage
	return b
}

func (b *ComputerBuilder) WithGPU(gpu string) *ComputerBuilder{
	b.gpu = gpu
	return b
}

func (b *ComputerBuilder) WithMonitor(monitor string) *ComputerBuilder{
	b.monitor = monitor
	return b
}

func (b *ComputerBuilder) WithNoofGPU(noofgpu int) *ComputerBuilder{
	b.noofgpu = noofgpu
	return b
}

func (b *ComputerBuilder) Build() *Computer{
	return &Computer{
		CPU:		b.cpu
		RAM:		b.ram
		Storage:	b.storage
		GPU:		b.GPU
		Monitor:	b.monitor
		NoofGPU:	b.noofgpu
		}
}

```

**Step 3: Using the Builder**

```
func main(){
	computer := MakeBuilder().
		WithCPU("Intel Ultra 5").
		WithRAM(32).
		WithStorage(1000).
		WithGPU("Nvidia 3050").
		WithMonitor("2K Monitor").
		WithNoofGPU(4).
		Build()

	fmt.Printf("Computer: %+v\n", computer)

}
```



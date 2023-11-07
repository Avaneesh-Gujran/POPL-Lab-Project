package main

import (
    "fmt"
    "sync"
)

func main() {
    // Initialize a wait group to synchronize goroutines
    var wg sync.WaitGroup

    // Create a channel to pass data between stages of the pipeline
    dataChannel := make(chan string)

    // First stage: Read data and send it to the channel
    go func() {
        defer close(dataChannel)
        data := []string{"Data 1", "Data 2", "Data 3"} // Simulated data source
        for _, item := range data {
            dataChannel <- item
        }
    }()

    // Second stage: Process data concurrently
    for i := 0; i < 3; i {
        wg.Add(1)
        go func() {
            defer wg.Done()
            for item := range dataChannel {
                // Process the data here
                fmt.Println("Processing:", item)
            }
        }()
    }

    // Wait for all goroutines to finish
    wg.Wait()
}

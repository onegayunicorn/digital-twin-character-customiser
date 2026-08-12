CXX      = g++
CXXFLAGS = -std=c++17 -O2 -Wall -Wextra
TARGET   = mutation_kernel

$(TARGET): mutation_kernel.cpp
	$(CXX) $(CXXFLAGS) -o $(TARGET) mutation_kernel.cpp

test: $(TARGET)
	./$(TARGET) scan ATGAAATGACCC 0
	./$(TARGET) premature ATGAAATGACCC 0 4
	./$(TARGET) gc ATGAAATGACCC

clean:
	rm -f $(TARGET)

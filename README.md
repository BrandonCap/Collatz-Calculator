# Collatz Conjecture Visualizer

An interactive tool that demonstrates the Collatz Conjecture (also known as the 3n+1 problem). This project allows users to explore one of mathematics' most famous unsolved problems through dynamic charts and real-time sequence generation.

## What is the Collatz Conjecture?

The Collatz Conjecture is a mathematical hypothesis that states:

Starting with any positive integer `n`:
- If `n` is **even**, divide it by 2: `n = n / 2`
- If `n` is **odd**, multiply by 3 and add 1: `n = 3n + 1`
- Repeat this process with the resulting number

The conjecture claims that no matter which positive integer you start with, you will **always eventually reach 1**. While this has been verified for incredibly large numbers, it has never been mathematically proven for all numbers!

## Algorithm Explanation

The Python implementation follows these steps:

1. **Input Validation**: Ensures the input is a positive integer
2. **Sequence Generation**:
   ```python
   while altitude != 1:
    if altitude % 2 == 0: #Even Numbers
        altitude  = altitude / 2
        count += 1
        print(int(altitude))

    else: #Odd Numbers
        altitude = (altitude * 3) + 1
        if altitude > maxAltitude:
            maxAltitude = altitude
        count += 1
        print(int(altitude))
    
    y_altitudes.append(altitude)
    x_count.append(count)
   ```
3. **Visualization**: Uses matplotlib to create a line graph showing the sequence
4. **Statistics Calculation**: Tracks steps, maximum value, and displays the complete sequence

## Example Sequences

Try these interesting starting numbers:

- **27**: Takes 111 steps, reaches a maximum of 9,232
- **19**: Takes 20 steps, reaches a maximum of 88
- **6171**: Takes 261 steps, reaches a maximum of 975,400
- **9**: Takes 19 steps, reaches a maximum of 52

## Mathematical Resources

Learn more about the Collatz Conjecture:

- [Wikipedia: Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)
- [Numberphile Video](https://www.youtube.com/watch?v=5mFpVDpKX70)
- [Veritasium Video](https://www.youtube.com/watch?v=094y1Z2wpJg)

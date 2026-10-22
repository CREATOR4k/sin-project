# Sine Calculation

This Python script calculates an approximate value for the sine of an angle in the range of 0° to 90° using the historical **Bhaskara I formula** (7th century).

The key feature of this implementation is its **extreme computational optimization**, designed for resource-constrained systems.

## ⚡ Optimization and Advantages of the Method

Unlike the standard method of calculating sine via a Taylor series expansion (commonly used in software libraries), this algorithm offers several critical advantages:

* **No Factorials:** Calculating factorials—especially for higher-order precision—requires intensive loops that place a heavy load on the processor. This method uses no factorials at all.
* **Basic Arithmetic:** The calculation requires only **3 multiplications, 2 subtractions, and 1 division**.
* **No Heavy Libraries:** The script does not require the `math` module or complex C extensions; all calculations are performed using basic data types.
* **High Precision with Minimal Overhead:** The maximum absolute error of this formula within the [0°, 90°] interval is only **~0.0016**. This makes it ideal for rapid engineering calculations, microcontrollers, and performance-critical tasks in game development, where CPU core speed is paramount.

## 🚀 How It Works

For an angle \(x\) (in degrees), a rational approximation is applied:
# Sine Approximation via the Bhaskara I Formula

An implementation and mathematical analysis of the famous rational formula by the Indian mathematician **Bhaskara I** (7th century), used for the rapid calculation of sine without relying on trigonometric series. ## 📋 Formula

# Fast Sine Approximation (Bhaskara I’s Formula)

A Python script for fast, lightweight calculation of the sine of an angle in the range of 0° to 90°. It is based on a historical formula by the Indian mathematician Bhaskara I (7th century), adapted for use in scenarios where computational speed is critical.

## ⚡ Features and Optimization

Unlike the classic Taylor series expansion for sine, this algorithm is designed to minimize CPU resource usage:

* **No Factorials or Exponents:** It avoids the heavy iterative operations and large-number arithmetic inherent in calculating Taylor series terms.
* **Minimal CPU Cycles:** The entire calculation is reduced to basic arithmetic—requiring only **3 multiplications, 2 subtractions, and 1 division**.
* **Computation Reuse:** The formula’s structure allows the common term `x * (180 - x)` to be calculated once and immediately reused in the denominator.
* **Self-Contained:** The script runs on pure Python, requiring no imports from the `math` library or any other external dependencies.

Despite its simplicity, the algorithm maintains a level of accuracy sufficient for most practical applications—the maximum absolute error across the entire interval does not exceed **~0.0016**.

## 💻 Usage

1. Ensure that **Python 3.x** is installed. 2. Run the script:
```bash
python sin-project.py
```

### Usage Examples

**Successful execution (30°):**
```text
Enter an angle in degrees (from 0 to 90): 30
The accurate sine (approximation) for 30.0° is: 0.5000
```

**Handling an out-of-range value (120°):**
```text
Enter an angle in degrees (from 0 to 90): 120
Error: please enter a number strictly between 0 and 90 degrees.
```

---

## ⚡ Features and Accuracy

The formula is based on the ratio of two parabolas and offers remarkable accuracy for an algorithm developed over 1,300 years ago.

* **Perfectly accurate values** are achieved at five key points within the interval:
* sin(0) = 0
* sin(30)= 0.5
* sin(90) = 1
* sin(150) = 0.5
* sin(180) = 0
* **Maximum absolute error:** \(\approx 0.0016\) (less than \(0.2\%\)), making this formula an excellent choice for rapid calculations on microcontrollers or in applications where the extreme precision of Taylor series expansions is not required. ---

## 💻 Implementation Example (Python)

```python
import math

def bhaskara_sin_deg(x_deg):
"""Calculate the sine of an angle in degrees within the interval [0, 180]"""
# Normalize to the [0, 180] interval to demonstrate the basic algorithm
x = x_deg % 360
sign = 1
if x > 180:
x -= 180
sign = -1

numerator = 4 * x * (180 - x)
denominator = 40500 - x * (180 - x)
return sign * (numerator / denominator)

# Test
angle = 45
print(f"Bhaskara sin({angle}°): {bhaskara_sin_deg(angle):.5f}")
print(f"Exact sin({angle}°):    {math.sin(math.radians(angle)):.5f}")
```

The expression \(x(180 - x)\) is calculated once in the numerator, allowing the result to be reused in the denominator, which reduces the number of CPU cycles required for the computation.

## 📋 Requirements

* **Python 3.x** (no external dependencies).

## 💻 Usage

Run the script via the terminal:

```bash
python sin-project.py
```


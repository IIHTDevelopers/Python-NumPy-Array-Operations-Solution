import numpy as np

class SalesAnalysis:
    def __init__(self, product1_sales, product2_sales):
        """Initialize two NumPy arrays for daily sales data."""
        self.product1_sales = np.array(product1_sales, dtype=np.int32)
        self.product2_sales = np.array(product2_sales, dtype=np.int32)

    def add_sales(self):
        """Add the sales data of two products element-wise."""
        if self.product1_sales.size == 0 or self.product2_sales.size == 0:
            raise ValueError("Sales data cannot be empty")
        return self.product1_sales + self.product2_sales

    def subtract_sales(self):
        """Subtract the sales data of the second product from the first element-wise."""
        if self.product1_sales.size == 0 or self.product2_sales.size == 0:
            raise ValueError("Sales data cannot be empty")
        return self.product1_sales - self.product2_sales

    def calculate_mean(self):
        """Calculate the mean of the total sales (sum of both products)."""
        if self.product1_sales.size == 0 or self.product2_sales.size == 0:
            raise ValueError("Sales data cannot be empty")
        total_sales = self.product1_sales + self.product2_sales
        return np.mean(total_sales)

    def calculate_median(self):
        """Calculate the median of the total sales (sum of both products)."""
        if self.product1_sales.size == 0 or self.product2_sales.size == 0:
            raise ValueError("Sales data cannot be empty")
        total_sales = self.product1_sales + self.product2_sales
        return np.median(total_sales)

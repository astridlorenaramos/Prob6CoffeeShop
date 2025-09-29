Tasks
Load data into NumPy using np.genfromtxt (with delimiter=',', names=True, dtype=None, encoding='utf-8').
Compute daily revenue as: revenue = transactions * avg_ticket - refunds using vectorized ops.
Find:
Mean, median, and standard deviation of daily revenue.
The top 5 revenue days (return their dates and revenue).
Broadcasting scenario: A 10-day promo increases foot traffic by +8% transactions but reduces average ticket by −5% on those same days.
Apply the percent changes to the first 10 days via broadcasting (no loops).
Recompute revenue for those days and report the net revenue change over those 10 days.
Filtering: Count how many days had revenue ≥ the overall median revenue.

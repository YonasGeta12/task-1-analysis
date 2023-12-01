# Example code outline (adapt to your dataset and structure)
import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
# Replace 'your_dataset.csv' with the actual path or method to load your dataset
df = pd.read_csv('your_dataset.csv')

# Convert timestamp columns to datetime format
df['message_timestamp'] = pd.to_datetime(df['message_timestamp'])
df['reply_timestamp'] = pd.to_datetime(df['reply_timestamp'])
df['reaction_timestamp'] = pd.to_datetime(df['reaction_timestamp'])

# Calculate time differences
df['time_diff_messages'] = df['message_timestamp'].diff().dt.total_seconds()
df['time_diff_replies'] = df['reply_timestamp'].diff().dt.total_seconds()
df['time_diff_reactions'] = df['reaction_timestamp'].diff().dt.total_seconds()

# Plot histograms
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.hist(df['time_diff_messages'].dropna(), bins=50, color='blue', alpha=0.7)
plt.title('Time Difference Between Consecutive Messages')
plt.xlabel('Time Difference (seconds)')
plt.ylabel('Frequency')

plt.subplot(2, 2, 2)
plt.hist(df['time_diff_replies'].dropna(), bins=50, color='green', alpha=0.7)
plt.title('Time Difference Between Consecutive Replies')
plt.xlabel('Time Difference (seconds)')
plt.ylabel('Frequency')

plt.subplot(2, 2, 3)
plt.hist(df['time_diff_reactions'].dropna(), bins=50, color='orange', alpha=0.7)
plt.title('Time Difference Between Consecutive Reactions')
plt.xlabel('Time Difference (seconds)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
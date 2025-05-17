import pandas as pd
import matplotlib.pyplot as plt

def plt_accel(df, datetime='datetime', x='x', y='y', z='z'):
    """
    Plot all axises of the given acceleration data.
    
    Parameters
    ----------
    df: pd.DataFrame
        DataFrame containing acceleration data with columns 'x', 'y', 'z'
    """
    df = df.copy()
    df[datetime] = pd.to_datetime(df[datetime])
    df.set_index(datetime, inplace=True)


    plt.figure(figsize=(15,5))
    plt.plot(df.index, df['x'], label='x-axis')
    plt.plot(df.index, df['y'], label='y-axis')
    plt.plot(df.index, df['z'], label='z-axis')
    plt.title('Accelerometer data')
    plt.xlabel('Timestamp')
    plt.ylabel('Acceleration')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
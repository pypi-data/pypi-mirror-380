# File: src/samudra_ai/evaluator.py
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import xarray as xr
from scipy.interpolate import interpn
from .utils import compute_metrics, standardize_dims

def evaluate_model(ref_data, raw_gcm_data, corrected_data, var_name, output_dir):
    print("\n🔎 Memulai proses evaluasi dan plotting otomatis...")

    # Standarisasi dimensi time-lat-lon
    ref_data = standardize_dims(ref_data)
    raw_gcm_data = standardize_dims(raw_gcm_data)
    corrected_data = standardize_dims(corrected_data)

    # Potong ke time length minimum
    time_len = min(len(ref_data.time), len(raw_gcm_data.time), len(corrected_data.time))
    ref_sliced = ref_data.isel(time=slice(0, time_len))
    raw_sliced = raw_gcm_data.isel(time=slice(0, time_len))
    corr_sliced = corrected_data.isel(time=slice(0, time_len))

    # Ambil grid target dari referensi
    target_lat = ref_sliced['lat'].values
    target_lon = ref_sliced['lon'].values
    target_grid_lat, target_grid_lon = np.meshgrid(target_lat, target_lon, indexing='ij')
    target_points = np.array([target_grid_lat.ravel(), target_grid_lon.ravel()]).T

    def manual_interp(source_da, target_da):
        # Pastikan dimensi [time, lat, lon]
        if source_da.dims[-2:] != ("lat", "lon"):
            source_da = source_da.transpose("time", "lat", "lon")

        source_lat = source_da['lat'].values
        source_lon = source_da['lon'].values

        # Validasi monoton
        if not (np.all(np.diff(source_lat) > 0) or np.all(np.diff(source_lat) < 0)):
            raise ValueError("Latitude harus monoton. Urutkan ulang dimensi 'lat'.")
        if not (np.all(np.diff(source_lon) > 0) or np.all(np.diff(source_lon) < 0)):
            raise ValueError("Longitude harus monoton. Urutkan ulang dimensi 'lon'.")

        source_points = (source_lat, source_lon)
        interpolated_values = np.array([
            interpn(
                source_points, source_da.isel(time=t).values, target_points,
                method='linear', bounds_error=False, fill_value=np.nan
            ).reshape(target_grid_lat.shape)
            for t in range(source_da.shape[0])
        ])
        # return xr.DataArray(interpolated_values, coords=ref_sliced.coords, dims=ref_sliced.dims)
        return xr.DataArray(
            interpolated_values,
            coords={"time": target_da["time"], "lat": target_da["lat"], "lon": target_da["lon"]},
            dims=["time", "lat", "lon"]
        )

    # Interpolasi raw GCM ke grid ref
    raw_aligned = manual_interp(raw_sliced, ref_sliced)

    # Rata-rata spasial jadi timeseries
    ref_series = ref_sliced.mean(dim=['lat', 'lon'])
    raw_series = raw_aligned.mean(dim=['lat', 'lon'])
    corr_series = corr_sliced.mean(dim=['lat', 'lon'])

    # Hitung metrik evaluasi
    metrics_raw = compute_metrics(ref_series.values, raw_series.values)
    metrics_corr = compute_metrics(ref_series.values, corr_series.values)
    results_df = pd.DataFrame([
        {'Source': 'GCM Asli', **dict(zip(['Correlation', 'RMSE', 'Bias', 'MAE'], metrics_raw))},
        {'Source': 'GCM Terkoreksi', **dict(zip(['Correlation', 'RMSE', 'Bias', 'MAE'], metrics_corr))},
    ])

    # Simpan summary metrics
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        results_df.to_excel(os.path.join(output_dir, "summary_metrics.xlsx"), index=False)

    # Simpan timeseries per timestep
    df_line = pd.DataFrame({
        "Time": ref_series.time.values,
        "GCM Asli": raw_series.values,
        "GCM Terkoreksi": corr_series.values,
        "Reanalysis (Obs)": ref_series.values
    })

    if output_dir:
        df_line.to_excel(os.path.join(output_dir, "timeseries_comparison.xlsx"), index=False)

    # Plot timeseries
    plt.figure(figsize=(15, 6))
    sns.lineplot(data=df_line)
    plt.title(f"Perbandingan Time Series {var_name.upper()}")
    plt.grid(True)
    if output_dir:
        plt.savefig(os.path.join(output_dir, "timeseries_comparison.png"), dpi=300)
    plt.show()

    # Plot bar metrik
    df_melt = results_df.melt(id_vars=['Source'], var_name='Metric', value_name='Value')
    plt.figure(figsize=(10, 7))
    sns.barplot(data=df_melt, x='Metric', y='Value', hue='Source', palette='viridis')
    plt.title("Perbandingan Metrik Evaluasi")
    if output_dir:
        plt.savefig(os.path.join(output_dir, "metrics_barplot.png"), dpi=300)
    plt.show()

    return results_df, corr_sliced
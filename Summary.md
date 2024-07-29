Using the names of the zip file "sp data original.zip" and the t_0 values from the Excel file "new sp sorted.xlsx", calculate the epoch with the code "època.py".

Employ the coordinates ra and dec from the file "sandra (1).csv" to compute ebv for each sp.

Use the code "correction1.py" to apply the first and second corrections to the spectra, based on the z and ebv data provided in "new sp sorted.xlsx".

Use the code "correction3.py" to apply the third correction to those sp listed with the value of ebv_host in "new sp sorted.xlsx".

Apply the "spectres2.py" code to plot four spectra (original, 1st correction, 2nd correction and 3rd correction if applicable) for each sp.

In the zip files "sp data 1.zip", "sp data 2.zip" and "sp data 3.zip" are all the files of the corrected spectra and the corresponding graphics.

Use "smooth.py" to smooth the previous zip files and save the new files. Select the most appropriate smoothing value for each spectrum in code line sx,sy = x1,savgol_filter(y1,51,3).

Use "error.py" to compute the error once the smoothing is done and save the updated files.

Use the code "smootherror.py" to perform the resampling and generate the corresponding graph for each sp. Save again the updated files.

The zip file "resampling.zip" contains all the sp spectra with the resampled third correction.

The zip file "resampling 2nd correction.zip" contains all the sp spectra with the resampled second correction.

Use "resampleig.py" to plot all the spectra for each bin.

Use "mean.py" to average the spectra of each bin and plot the new spectra.

The zip files "means 2nd correction.zip" and "means 3rd correction.zip" contain the mean files for each bin and a graph with all the means for the second and third correction respectively.

The zip file "ztf_sandra.txt" contains ​​the stretch factor values and the corresponding errors for each sp. With the code "velocity.py", compute the velocity of supernovae with third correction between epochs -1 and 1. 

Using the file "supernovae_velocities and st km.txt" and the code "v vs st.py" code, plot the velocity versus stretch factor (v vs st.png).

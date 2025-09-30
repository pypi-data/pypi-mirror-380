""" 
Author: Ian Black (blackia@oregonstate.edu)
Date: 2020-02-10


-----Description-----
This script provides a class and set of functions for bringing CSPP science variables into Python memory.
This is set up for recovered_cspp streams, but should also work for telemetered data. 
Note that CTD, DOSTA, SPKIR, PAR, and VELPT are the only data sets that are telemetered. OPTAA and NUTNR data
packets are too large to transfer in a short surface window.
There are three general functions and one function for each CSPP data stream.
To make multiple data requests, submit each request before checking to see if the data is available.

-----Required Libraries-----
requests: For issuing and checking request status.
re: For parsing returned json for URLs that contain instrument data.
time: For pausing the script while checking a data request status.
pandas: For organizing data.
xarray: For opening remote NetCDFs.

-----Class-----
OOIM2M() <<< This is the overall class. This must prepend a function.
             
             Example 1: url = OOIM2M.create_url(url,start_date,start_time,stop_date,stop_time)  
                        request = OOIM2M.make_request(url,user,token)
                        nc = OOIM2M.get_location(request)
 
             Example 2: THIS_EXAMPLE_IS_TOO_LONG = OOIM2M()
                        url = THIS_EXAMPLE_IS_TOO_LONG.create_url(url)
                        request = THIS_EXAMPLE_IS_TOO_LONG.make_request(url,user,token)
                        nc = THIS_EXAMPLE_IS_TOO_LONG.get_location(request)

-----General Functions-----
url = OOIM2M.create_url(url,start_date,start_time,stop_date,stop_time) <<< Function for generating a request URL for data between two datetimes. Returns a complete request URL. URL is the base request url for the data you want. Dates in YYYY-MM-DD. Times in HH:MM:SS.

request = OOIM2M.make_request(url,user,token) <<< Function for making the request from the URL created from create_url. User and token are found in your account information on OOINet. Returns a requests object.

nc = OOIM2M.get_location(request) <<< Function that gathers the remote locations of the requested data. Returns a list of URLs where the data is stored as netCDFs. This list includes data that is used in the creation of data products. Example: CTD data accompanies DOSTA data.

-----Instrument Functions-----
ctd = cspp_ctd(nc)  <<< Returns a pandas dataframe that contains datetime, pressure, temperature, salinity, and density.

dosta = cspp_dosta(nc) <<< Returns a pandas dataframe that contains datetime, pressure, temperature, concentration, and estimated saturation. CTD data is also made available.

nutnr = cspp_nutnr(nc) <<< Interpolates pressure for nitrate data using time and CTD pressure. Returns a pandas dataframe that contains datetime, pressure, and nitrate.

par = cspp_parad(nc) <<< Returns a pandas dataframe that contains datetime, pressure, bulk photosynthetically active radiation.

velpt = cspp_velpt(nc) <<< Returns a pandas dataframe that contains datetime, pressure, northward velocity, eastward velocity, upward velocity, heading, pitch, roll, soundspeed, and temperature measured by the aquadopp. 

batt1, batt2 = cspp_batts(nc) <<< Returns two pandas dataframes that contain datetime and voltage for each CSPP battery.

compass = cspp_cpass(nc)  <<< Returns a pandas dataframe that contains datetime, pressure, heading, pitch, and roll from the control can.

sbe50 = cspp_sbe50(nc)  <<< Returns a pandas dataframe that contains datetime, pressure, and profiler velocity calculated from the SBE50 in the control can.

winch = cspp_winch(nc)  <<< Returns a pandas dataframe that contains datetime, pressure, internal temperature of the winch, current seen by the winch, voltage seen by the winch, and the rope on the winch drum.

-----Extra Functions-----
find_site(nc) <<< Function that identifies the requested CSPP site and standard depth of that site. Used in removing bad pressure data. Called by data functions. Not generally called by the user.

-----Notes/Issues-----
NUTNR data does not have pressure data associated with it in the raw files produces by the CSPP. 
The function provided in this script interpolates based on time.
Alternatively, the user can call the int_ctd_pressure variable.

The cspp_optaa function is in the works.

OOI ion-function for VELPT-J assumes data from the instrument is output in mm/s, when it is actually output in m/s.         
https://github.com/oceanobservatories/ion-functions/blob/master/ion_functions/data/vel_functions.py
The simple fix now is to multiply returned velocity values by 1000 to get it back into to m/s.

"""
import requests
import re
import time
import pandas as pd
import numpy as np
import xarray as xr

from ooi_data_explorations.common import AUTH

# CE01ISSP URLs
CE01ISSP_BATTS = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE01ISSP/SP001/00-SPPENG000/recovered_cspp/cspp_eng_cspp_dbg_pdbg_batt_eng_recovered'
CE01ISSP_CPASS = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE01ISSP/SP001/00-SPPENG000/recovered_cspp/cspp_eng_cspp_wc_hmr_eng_recovered'
CE01ISSP_SBE50 = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE01ISSP/SP001/00-SPPENG000/recovered_cspp/cspp_eng_cspp_wc_sbe_eng_recovered'
CE01ISSP_WINCH = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE01ISSP/SP001/00-SPPENG000/recovered_cspp/cspp_eng_cspp_wc_wm_eng_recovered'

# CE02SHSP URLs
CE02SHSP_BATTS = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE02SHSP/SP001/00-SPPENG000/recovered_cspp/cspp_eng_cspp_dbg_pdbg_batt_eng_recovered'
CE02SHSP_CPASS = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE02SHSP/SP001/00-SPPENG000/recovered_cspp/cspp_eng_cspp_wc_hmr_eng_recovered'
CE02SHSP_SBE50 = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE02SHSP/SP001/00-SPPENG000/recovered_cspp/cspp_eng_cspp_wc_sbe_eng_recovered'
CE02SHSP_WINCH = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE02SHSP/SP001/00-SPPENG000/recovered_cspp/cspp_eng_cspp_wc_wm_eng_recovered'

# CE06ISSP URLs
CE06ISSP_BATTS = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE06ISSP/SP001/00-SPPENG000/recovered_cspp/cspp_eng_cspp_dbg_pdbg_batt_eng_recovered'
CE06ISSP_CPASS = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE06ISSP/SP001/00-SPPENG000/recovered_cspp/cspp_eng_cspp_wc_hmr_eng_recovered'
CE06ISSP_SBE50 = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE06ISSP/SP001/00-SPPENG000/recovered_cspp/cspp_eng_cspp_wc_sbe_eng_recovered'
CE06ISSP_WINCH = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE06ISSP/SP001/00-SPPENG000/recovered_cspp/cspp_eng_cspp_wc_wm_eng_recovered'

# CE07SHSP URLs
CE07SHSP_BATTS = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE07SHSP/SP001/00-SPPENG000/recovered_cspp/cspp_eng_cspp_dbg_pdbg_batt_eng_recovered'
CE07SHSP_CPASS = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE07SHSP/SP001/00-SPPENG000/recovered_cspp/cspp_eng_cspp_wc_hmr_eng_recovered'
CE07SHSP_SBE50 = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE07SHSP/SP001/00-SPPENG000/recovered_cspp/cspp_eng_cspp_wc_sbe_eng_recovered'
CE07SHSP_WINCH = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE07SHSP/SP001/00-SPPENG000/recovered_cspp/cspp_eng_cspp_wc_wm_eng_recovered'


class OOIM2M():
    def __init__(self):
        return

    def create_url(url,start_date = '2014-04-04',start_time = '00:00:00',stop_date = '2035-12-31',stop_time = '23:59:59'):  #Create a request URL.
        timestring = "?beginDT=" + start_date + 'T' + start_time + ".000Z&endDT=" + stop_date + 'T' + stop_time + '.999Z' #Get the timespan into an OOI M2M format.
        m2m_url = url + timestring  #Combine the partial URL with the timespan to get a full url.
        return m2m_url
    
    def make_request(m2m_url):    #Request data from UFRAME using the generated request URL.
        request = requests.get(m2m_url, auth=(AUTH[0], AUTH[2]))
        if request.status_code == requests.codes.ok:  #If the response is 200, then continue.
            print('Request successful.')
            return request
        elif request.status_code == requests.codes.bad:  #If the response is 400, then issue a warning to force the user to find an issue.
            print(request)
            print('Bad request. Check request URL, user, and token.')
            return
        elif request.status_code == requests.codes.not_found:  #If the response is 404, there might not be data during the prescribed time period.
            print(request)
            print('Not found. There may be no data available during the requested time period.')
            return
        else:  #If an error that is unusual is thrown, show this message.
            print(request)
            print('Unanticipated error code. Look up error code here: https://github.com/psf/requests/blob/master/requests/status_codes.py')
            return
        
    def get_location(request):      #Check the status of the data request and return the remote location when complete.
        data = request.json()  #Return the request information as a json.
        check = data['allURLs'][1] + '/status.txt'  #Make a checker.  
        for i in range(60*30):   #Given roughly half an hour...
            r = requests.get(check)  #check the request.
            if r.status_code == requests.codes.ok:  #If everything is okay.
                print('Request complete.')  #Print this message.
                break
            else:
                print('Checking request...',end = " ")
                print(i)
                time.sleep(1)  #If the request isn't complete, wait 1 second before checking again.
        print("")
        data_url = data['allURLs'][0]  #This webpage provides all URLs for the request.
        data_urls= requests.get(data_url).text  #Convert the page to text.
        data_nc = re.findall(r'(ooi/.*?.nc)',data_urls)  #Find netCDF urls in the text.
        for j in data_nc:  
            if j.endswith('.nc') == False: #If the URL does not end in .nc, toss it.
                data_nc.remove(j)
        for j in data_nc:
            try:
                float(j[-4]) == True  #If the 4th to last value isn't a number, then toss it.
            except:
                data_nc.remove(j)
        thredds_url = 'https://opendap.oceanobservatories.org/thredds/dodsC/' #This is the base url for remote data access.
        fill = '#fillmismatch'  #Applying fill mismatch prevents issues.
        data_nc = np.char.add(thredds_url,data_nc)  #Combine the thredds_url and the netCDF urls.
        nc = np.char.add(data_nc,fill)  #Append the fill.
        return nc
    
    def find_site(nc):  #Function for finding the requested site and setting the standard depth.
        df = pd.DataFrame(data = {'location':nc})  #Put the remote location in a dataframe.
        url = df['location'].iloc[0]  #Take the first URL...
        banana = url.split("-")  #Split it by the dashes.
        site = banana[1]  #The value in the second location is the site.
        if site == 'CE01ISSP':  #If the site is..
            depth = 25  #This is the standard deployment depth.
        elif site == 'CE02SHSP':
            depth = 80
        elif site == 'CE06ISSP':
            depth = 29
        elif site == 'CE07SHSP':
            depth = 87
        else:
            depth = 87
        return site,depth  #Return the site and depth for use later.

    def cspp_batts(nc):  #Returns two dataframes, one for each battery.
        site,depth = OOIM2M.find_site(nc)
        dfnc = pd.DataFrame(data = {'location':nc})
        batt = dfnc.loc[~dfnc['location'].str.contains('ctdpf_j_cspp_instrument')]
        data = pd.DataFrame()
        for remote in batt['location']:
            dataset = xr.open_dataset(remote)
            d = ({'datetime':dataset['profiler_timestamp'], 
                  'voltage':dataset['battery_voltage_flt32'], 
                  'battery_position':dataset['battery_number_uint8']})
            d = pd.DataFrame(data = d)        
            data = pd.concat([data,d])
        data = data.dropna()  #Remove rows with any NaNs.
        data = data.sort_values('datetime')  #Sort the data chronologically.
        batt1 = data.loc[data['battery_position'].astype('str').str.contains('1.0')]
        batt2 = data.loc[data['battery_position'].astype('str').str.contains('2.0')]
        batt1 = batt1.reset_index(drop=True) 
        batt2 = batt2.reset_index(drop=True) 
        print('Battery data for ' + site + ' available.')
        print('Battery datetime in UTC.')
        print('Battery voltage in volts.')
        return batt1,batt2
    
    def cspp_cpass(nc):
        site,depth = OOIM2M.find_site(nc)
        dfnc = pd.DataFrame(data = {'location':nc})
        hmr = dfnc.loc[~dfnc['location'].str.contains('ctdpf_j_cspp_instrument')]
        data = pd.DataFrame()
        for remote in hmr['location']:
            dataset = xr.open_dataset(remote)
            d =({'datetime':dataset['profiler_timestamp'],  
                 'pressure':dataset['pressure_depth'], 
                 'heading':dataset['heading'], 
                 'pitch':dataset['pitch'],
                 'roll':dataset['roll']})
            d = pd.DataFrame(data = d)        
        data = pd.concat([data,d])
        data = data[data.pressure < depth] #Remove obviously bad values.
        data = data[data.pressure > 0]  
        data = data.dropna()
        data = data.sort_values('datetime')
        data = data.reset_index(drop = True) 
        print('Compass data for ' + site + ' available.')
        print('Compass datetime in UTC.')
        print('Compass pressure in dbars.')
        print('Compass heading, pitch, and roll in degrees.')
        return data
    
    def cspp_sbe50(nc):
        site,depth = OOIM2M.find_site(nc)
        dfnc = pd.DataFrame(data = {'location':nc})
        sbe50 = dfnc.loc[~dfnc['location'].str.contains('ctdpf_j_cspp_instrument')]
        data = pd.DataFrame()
        for remote in sbe50['location']:
            dataset = xr.open_dataset(remote)
            d = ({'datetime':dataset['profiler_timestamp'], 
                  'pressure':dataset['pressure_depth'],  
                  'velocity':dataset['velocity_flt32']})
            d = pd.DataFrame(data = d)        
            data = pd.concat([data,d])
        data = data[data.pressure < depth] #Remove obviously bad values.
        data = data[data.pressure > 0]  
        data = data.dropna()
        data = data.sort_values('datetime')
        data = data.reset_index(drop = True) 
        print('SBE50 data for ' + site + ' available.')
        print('SBE50 datetime in UTC.')
        print('SBE50 pressure in dbars.')
        print('SBE50 velocity in m s^-1.')
        return data
    
    def cspp_winch(nc):
        site,depth = OOIM2M.find_site(nc)
        dfnc = pd.DataFrame(data = {'location':nc})
        winch = dfnc.loc[~dfnc['location'].str.contains('ctdpf_j_cspp_instrument')]
        data = pd.DataFrame()
        for remote in winch['location']:
            dataset = xr.open_dataset(remote)
            d = ({'datetime':dataset['profiler_timestamp'], 
                  'pressure':dataset['pressure_depth'],
                  'wm_temp':dataset['temperature'],
                  'wm_current':dataset['current_flt32'],  
                  'wm_voltage':dataset['voltage_flt32'],  
                  'rope_on_drum':dataset['rope_on_drum']})
            d = pd.DataFrame(data = d)        
            data = pd.concat([data,d])
        data = data[data.pressure < depth] #Remove obviously bad values.
        data = data[data.pressure > 0]  
        data = data.dropna()
        data = data.sort_values('datetime')
        data = data.reset_index(drop = True) 
        print('Winch data for ' + site + ' available.')
        print('WM datetime in UTC.')
        print('WM pressure in dbars.')
        print('WM wm_temp in degC.')
        print('WM wm_current in amps.')
        print('WM wm_voltage in volts.')
        print('WM rope_on_drum in meters.')
        return data

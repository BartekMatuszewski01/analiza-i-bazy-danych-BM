import pandas as pd

def tideDataCleanMess():
    turbecolosis = pd.read_csv('../Original Data/tb.csv')

    tb_types = ['new_sp', 'new_sp_m04', 'new_sp_m514', 'new_sp_m014', 'new_sp_m1524',
                'new_sp_m2534', 'new_sp_m3544', 'new_sp_m4554', 'new_sp_m5564',
                'new_sp_m65', 'new_sp_mu', 'new_sp_f04', 'new_sp_f514', 'new_sp_f014',
                'new_sp_f1524', 'new_sp_f2534', 'new_sp_f3544', 'new_sp_f4554',
                'new_sp_f5564', 'new_sp_f65', 'new_sp_fu']

    iso_ver = set(turbecolosis['iso2'])

    for ver in iso_ver:
        tab = turbecolosis[turbecolosis['iso2'] == ver]

        for ty in tb_types:
            tab2 = tab[['iso2', 'year', ty]]
            tab_final = tab2.dropna()

            tab_final.to_csv(path_or_buf=f"../Analysis Data/tab_{ver}_{ty}.csv")


tideDataCleanMess()

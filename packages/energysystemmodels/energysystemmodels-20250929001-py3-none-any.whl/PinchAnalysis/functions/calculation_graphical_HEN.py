import pandas as pd

###############################"GHE########################################"""""
def graphical_hen_design(self):
    # Initialiser une liste pour les échangeurs installés
    heat_exchangers = []
    remaining_recoverable_heat = self.heat_recovery  # Track remaining recoverable heat
    used_streams = set()  # Track streams that have already been used

    # Initialize remaining stream lists
    self.remain_stream_list_above = self.stream_list_above.copy()
    self.remain_stream_list_below = self.stream_list_below.copy()

    # === Fonction pour appliquer un échange de chaleur au-dessus du pinch ===
    def apply_heat_exchange_above(hot_stream_df, cold_stream_df):
        nonlocal remaining_recoverable_heat, used_streams  # Access the remaining recoverable heat and used streams
        hot_stream = hot_stream_df.iloc[0].to_dict()
        cold_stream = cold_stream_df.iloc[0].to_dict()

        # 1. Filter remaining streams to exclude invalid entries
        self.remain_stream_list_above = self.remain_stream_list_above[
            (self.remain_stream_list_above['delta_H'] != 0) &
            (~self.remain_stream_list_above[['To', 'STo']].isna().any(axis=1))
        ]

        # Debug: Print the filtered list of remaining streams
        print("\n1. Filtered remaining streams above the pinch before testing:")
        print(self.remain_stream_list_above)

        # 2. Validate stream existence in the updated list
        if hot_stream['id'] not in self.remain_stream_list_above['id'].values or \
           cold_stream['id'] not in self.remain_stream_list_above['id'].values:
            print(f"One or both streams in the combination do not exist in the updated list. Skipping combination.")
            return hot_stream_df, cold_stream_df

        # 3. Print the combination being tested
        print(f"\n2. Testing combination above the pinch: HS_id={hot_stream['id']}, CS_id={cold_stream['id']}")

        # Validate stream availability
        if hot_stream['id'] in used_streams or cold_stream['id'] in used_streams:
            print(f"Stream {hot_stream['name']} or {cold_stream['name']} has already been used in another exchanger.")
            return hot_stream_df, cold_stream_df

        # 🔥 Additional validation: Ensure streams are valid
        if pd.isna(hot_stream['id']) or pd.isna(cold_stream['id']):
            print(f"Invalid combination: HS_id={hot_stream['id']}, CS_id={cold_stream['id']}. Skipping.")
            return hot_stream_df, cold_stream_df

        if hot_stream["delta_H"] >= 0 or cold_stream["delta_H"] <= 0:
            print(f"Invalid heat capacity for combination: HS_id={hot_stream['id']}, CS_id={cold_stream['id']}. Skipping.")
            return hot_stream_df, cold_stream_df

        # Quantité de chaleur échangée
        heat_exchanged = min(-hot_stream['delta_H'], cold_stream['delta_H'])
        heat_exchanged = min(heat_exchanged, cold_stream["mCp"] * (cold_stream["To"] - cold_stream["Ti"]))
        heat_exchanged = min(heat_exchanged, remaining_recoverable_heat)  # Ensure it does not exceed recoverable heat

        # Correct calculation of outlet temperatures
        hot_stream["To"] = hot_stream["Ti"] - (heat_exchanged / hot_stream["mCp"])
        cold_stream["To"] = cold_stream["Ti"] + (heat_exchanged / cold_stream["mCp"])
        hot_stream["STo"] = hot_stream["STi"] - (heat_exchanged / hot_stream["mCp"])
        cold_stream["STo"] = cold_stream["STi"] + (heat_exchanged / cold_stream["mCp"])

        # 3. Print the heat exchanger found
        exchanger = {
            'HS_id': hot_stream['id'], 'HS_name': hot_stream['name'],
            'HS_mCp': hot_stream['mCp'], 'HS_Ti': hot_stream['Ti'], 'HS_To': hot_stream['To'],
            'CS_id': cold_stream['id'], 'CS_name': cold_stream['name'],
            'CS_mCp': cold_stream['mCp'], 'CS_Ti': cold_stream['Ti'], 'CS_To': cold_stream['To'],
            'HeatExchanged': heat_exchanged
        }
        heat_exchangers.append(exchanger)
        print("\n3. Heat exchanger created above the pinch:")
        print(exchanger)

        # Update remaining recoverable heat
        remaining_recoverable_heat -= heat_exchanged

        # Update DataFrame with corrected temperatures and remaining capacity
        if not hot_stream_df.empty:
            self.remain_stream_list_above.loc[hot_stream_df.index[0], ['delta_H', 'To', 'STo']] = [
                float(hot_stream['delta_H'] + heat_exchanged), float(hot_stream['To']), float(hot_stream['STo'])
            ]
        if not cold_stream_df.empty:
            self.remain_stream_list_above.loc[cold_stream_df.index[0], ['delta_H', 'To', 'STo']] = [
                float(cold_stream['delta_H'] - heat_exchanged), float(cold_stream['To']), float(cold_stream['STo'])
            ]

        # Remove fully utilized streams but retain their rows with delta_H = 0
        if not cold_stream_df.empty and self.remain_stream_list_above.loc[cold_stream_df.index[0], 'delta_H'] <= 0:
            print(f"Stream {cold_stream['name']} is now fully utilized and will be retained with delta_H = 0.")
            self.remain_stream_list_above.loc[cold_stream_df.index[0], ['delta_H', 'To', 'STo']] = [0, None, None]

        if not hot_stream_df.empty and self.remain_stream_list_above.loc[hot_stream_df.index[0], 'delta_H'] >= 0:
            print(f"Stream {hot_stream['name']} is now fully utilized and will be retained with delta_H = 0.")
            self.remain_stream_list_above.loc[hot_stream_df.index[0], ['delta_H', 'To', 'STo']] = [0, None, None]

        # 🔥 Update the remaining streams list
        self.remain_stream_list_above = self.remain_stream_list_above[
            (self.remain_stream_list_above['delta_H'] != 0) | (self.remain_stream_list_above['delta_H'] == 0)
        ]

        # Update inlet temperatures for the next exchanger
        if not hot_stream_df.empty:
            self.remain_stream_list_above.loc[hot_stream_df.index[0], ['Ti', 'STi']] = [
                float(hot_stream['To']), float(hot_stream['STo'])
            ]
        if not cold_stream_df.empty:
            self.remain_stream_list_above.loc[cold_stream_df.index[0], ['Ti', 'STi']] = [
                float(cold_stream['To']), float(cold_stream['STo'])
            ]

        # 4. Print the updated list of remaining streams
        print("\n4. Updated remaining streams above the pinch:")
        print(self.remain_stream_list_above)

        return hot_stream_df, cold_stream_df

    # === Fonction pour appliquer un échange de chaleur en-dessous du pinch ===
    def apply_heat_exchange_below(hot_stream_df, cold_stream_df):
        nonlocal remaining_recoverable_heat, used_streams  # Access the remaining recoverable heat and used streams
        hot_stream = hot_stream_df.iloc[0].to_dict()
        cold_stream = cold_stream_df.iloc[0].to_dict()

        # 1. Filter remaining streams to exclude invalid entries
        self.remain_stream_list_below = self.remain_stream_list_below[
            (self.remain_stream_list_below['delta_H'] != 0) &
            (~self.remain_stream_list_below[['To', 'STo']].isna().any(axis=1))
        ]

        # Debug: Print the filtered list of remaining streams
        print("\n1. Filtered remaining streams below the pinch before testing:")
        print(self.remain_stream_list_below)

        # 2. Validate stream existence in the updated list
        if hot_stream['id'] not in self.remain_stream_list_below['id'].values or \
           cold_stream['id'] not in self.remain_stream_list_below['id'].values:
            print(f"One or both streams in the combination do not exist in the updated list. Skipping combination.")
            return hot_stream_df, cold_stream_df

        # 3. Print the combination being tested
        print(f"\n2. Testing combination below the pinch: HS_id={hot_stream['id']}, CS_id={cold_stream['id']}")

        # Validate stream availability
        if hot_stream['id'] in used_streams or cold_stream['id'] in used_streams:
            print(f"Stream {hot_stream['name']} or {cold_stream['name']} has already been used in another exchanger.")
            return hot_stream_df, cold_stream_df

        # 🔥 Additional validation: Ensure streams are valid
        if pd.isna(hot_stream['id']) or pd.isna(cold_stream['id']):
            print(f"Invalid combination: HS_id={hot_stream['id']}, CS_id={cold_stream['id']}. Skipping.")
            return hot_stream_df, cold_stream_df

        if hot_stream["delta_H"] >= 0 or cold_stream["delta_H"] <= 0:
            print(f"Invalid heat capacity for combination: HS_id={hot_stream['id']}, CS_id={cold_stream['id']}. Skipping.")
            return hot_stream_df, cold_stream_df

        # Quantité de chaleur échangée
        heat_exchanged = min(-hot_stream['delta_H'], cold_stream['delta_H'])
        heat_exchanged = min(heat_exchanged, cold_stream["mCp"] * (cold_stream["To"] - cold_stream["Ti"]))
        heat_exchanged = min(heat_exchanged, remaining_recoverable_heat)  # Ensure it does not exceed recoverable heat

        # Correct calculation of outlet temperatures
        hot_stream["To"] = hot_stream["Ti"] - (heat_exchanged / hot_stream["mCp"])
        cold_stream["To"] = cold_stream["Ti"] + (heat_exchanged / cold_stream["mCp"])
        hot_stream["STo"] = hot_stream["STi"] - (heat_exchanged / hot_stream["mCp"])
        cold_stream["STo"] = cold_stream["STi"] + (heat_exchanged / cold_stream["mCp"])

        # Debug: Print the calculated temperatures
        print(f"Calculated temperatures for HS (id={hot_stream['id']}): Ti={hot_stream['Ti']}, To={hot_stream['To']}")
        print(f"Calculated temperatures for CS (id={cold_stream['id']}): Ti={cold_stream['Ti']}, To={cold_stream['To']}")

        # 3. Print the heat exchanger found
        exchanger = {
            'HS_id': hot_stream['id'], 'HS_name': hot_stream['name'],
            'HS_mCp': hot_stream['mCp'], 'HS_Ti': hot_stream['Ti'], 'HS_To': hot_stream['To'],
            'CS_id': cold_stream['id'], 'CS_name': cold_stream['name'],
            'CS_mCp': cold_stream['mCp'], 'CS_Ti': cold_stream['Ti'], 'CS_To': cold_stream['To'],
            'HeatExchanged': heat_exchanged
        }
        heat_exchangers.append(exchanger)
        print("\n3. Heat exchanger created below the pinch:")
        print(exchanger)

        # Update remaining recoverable heat
        remaining_recoverable_heat -= heat_exchanged

        # Update DataFrame with corrected temperatures and remaining capacity
        if not hot_stream_df.empty:
            self.remain_stream_list_below.loc[hot_stream_df.index[0], ['delta_H', 'To', 'STo']] = [
                float(hot_stream['delta_H'] + heat_exchanged), float(hot_stream['To']), float(hot_stream['STo'])
            ]
        if not cold_stream_df.empty:
            self.remain_stream_list_below.loc[cold_stream_df.index[0], ['delta_H', 'To', 'STo']] = [
                float(cold_stream['delta_H'] - heat_exchanged), float(cold_stream['To']), float(cold_stream['STo'])
            ]

        # Debug: Print the updated delta_H for hot stream
        print(f"Updated delta_H for HS (id={hot_stream['id']}): {self.remain_stream_list_below.loc[hot_stream_df.index[0], 'delta_H']}")

        # Remove fully utilized streams but retain their rows with delta_H = 0
        if not cold_stream_df.empty and self.remain_stream_list_below.loc[cold_stream_df.index[0], 'delta_H'] <= 0:
            print(f"Stream {cold_stream['name']} is now fully utilized and will be retained with delta_H = 0.")
            self.remain_stream_list_below.loc[cold_stream_df.index[0], ['delta_H', 'To', 'STo']] = [0, None, None]

        if not hot_stream_df.empty and self.remain_stream_list_below.loc[hot_stream_df.index[0], 'delta_H'] >= 0:
            print(f"Stream {hot_stream['name']} is now fully utilized and will be retained with delta_H = 0.")
            self.remain_stream_list_below.loc[hot_stream_df.index[0], ['delta_H', 'To', 'STo']] = [0, None, None]

        # 🔥 Update the remaining streams list
        self.remain_stream_list_below = self.remain_stream_list_below[~self.remain_stream_list_below['delta_H'].isna()]

        # Update inlet temperatures for the next exchanger
        if not hot_stream_df.empty:
            self.remain_stream_list_below.loc[hot_stream_df.index[0], ['Ti', 'STi']] = [
                float(hot_stream['To']), float(hot_stream['STo'])
            ]
        if not cold_stream_df.empty:
            self.remain_stream_list_below.loc[cold_stream_df.index[0], ['Ti', 'STi']] = [
                float(cold_stream['Ti']), float(cold_stream['STo'])
            ]

        # 4. Print the updated list of remaining streams
        print("\n4. Updated remaining streams below the pinch:")
        print(self.remain_stream_list_below)

        return hot_stream_df, cold_stream_df

    # === Échanges au-dessus du pinch ===
    if not self.combinations_above.empty:
        for i in range(len(self.combinations_above)):
            comb = self.combinations_above.iloc[i]
            hot_stream_df = self.remain_stream_list_above[self.remain_stream_list_above['id'] == comb['HS_id']]
            cold_stream_df = self.remain_stream_list_above[self.remain_stream_list_above['id'] == comb['CS_id']]

            # Debug: Print the combination being tested
            print(f"\nEvaluating combination above the pinch: HS_id={comb['HS_id']}, CS_id={comb['CS_id']}")

            if not hot_stream_df.empty and not cold_stream_df.empty:
                hot_stream_df, cold_stream_df = apply_heat_exchange_above(hot_stream_df, cold_stream_df)

    # === Échanges en-dessous du pinch ===
    if not self.combinations_below.empty:
        for i in range(len(self.combinations_below)):
            comb = self.combinations_below.iloc[i]
            hot_stream_df = self.remain_stream_list_below[self.remain_stream_list_below['id'] == comb['HS_id']]
            cold_stream_df = self.remain_stream_list_below[self.remain_stream_list_below['id'] == comb['CS_id']]

            # Debug: Print the combination being tested
            print(f"\nEvaluating combination below the pinch: HS_id={comb['HS_id']}, CS_id={comb['CS_id']}")

            if not hot_stream_df.empty and not cold_stream_df.empty:
                hot_stream_df, cold_stream_df = apply_heat_exchange_below(hot_stream_df, cold_stream_df)

    # === Fonction pour tester d’autres échanges possibles ===
    def check_additional_heat_exchanges(remain_streams, dTmin=0, threshold=1):
        # Debug: Indicate the start of calculations
        if remain_streams is self.remain_stream_list_above:
            print("\n=== Starting additional heat exchanger calculations ABOVE the pinch (outside mCp rule) ===")
        elif remain_streams is self.remain_stream_list_below:
            print("\n=== Starting additional heat exchanger calculations BELOW the pinch (outside mCp rule) ===")

        # Debug: Print the actual remaining streams being passed
        print("\n1. Remaining streams before testing:")
        print(remain_streams)

        hot_streams = remain_streams[remain_streams['StreamType'] == 'HS']
        cold_streams = remain_streams[remain_streams['StreamType'] == 'CS']
        possible_exchanges = []

        for _, hot in hot_streams.iterrows():
            for _, cold in cold_streams.iterrows():
                # 2. Print the combination being tested
                print(f"\n2. Testing combination: HS_id={hot['id']}, CS_id={cold['id']}")

                # Validate remaining heat capacity and temperature range
                if hot['delta_H'] >= 0 or cold['delta_H'] <= 0:
                    print(f"Combination skipped: Invalid delta_H (HS_delta_H={hot['delta_H']}, CS_delta_H={cold['delta_H']})")
                    continue
                if hot['Ti'] <= cold['Ti'] + dTmin:
                    print(f"Combination skipped: Invalid temperature range (HS_Ti={hot['Ti']}, CS_Ti={cold['Ti']}, dTmin={dTmin})")
                    continue

                # Calculate maximum possible heat exchange
                Q_hot_limit = hot['mCp'] * (hot['Ti'] - (cold['Ti'] + dTmin))
                Q_cold_limit = cold['mCp'] * (hot['Ti'] - (cold['Ti'] + dTmin))
                Q_max = min(-hot['delta_H'], cold['delta_H'], Q_hot_limit, Q_cold_limit)

                # Skip if heat exchange is below the threshold
                if Q_max < threshold:
                    print(f"Combination skipped: Q_max below threshold (Q_max={Q_max}, threshold={threshold})")
                    continue

                # Calculate new outlet temperatures
                To_hot_new = hot['Ti'] - Q_max / hot['mCp']
                To_cold_new = cold['Ti'] + Q_max / cold['mCp']

                # Validate that the streams do not cross
                if To_hot_new <= To_cold_new + dTmin:
                    print(f"Combination skipped: Streams cross (To_hot_new={To_hot_new}, To_cold_new={To_cold_new}, dTmin={dTmin})")
                    continue

                # 3. Print the heat exchanger found
                exchanger = {
                    'HS_id': hot['id'], 'CS_id': cold['id'],
                    'Q_possible': Q_max, 'To_hot_new': To_hot_new, 'To_cold_new': To_cold_new
                }
                possible_exchanges.append(exchanger)
                print(f"\n3. Heat exchanger found: {exchanger}")

                # Update remaining streams
                remain_streams.loc[remain_streams['id'] == hot['id'], 'delta_H'] += Q_max
                remain_streams.loc[remain_streams['id'] == cold['id'], 'delta_H'] -= Q_max
                remain_streams.loc[remain_streams['id'] == hot['id'], 'To'] = To_hot_new
                remain_streams.loc[remain_streams['id'] == cold['id'], 'To'] = To_cold_new

                # 4. Print the updated list of remaining streams
                print("\n4. Updated remaining streams:")
                print(remain_streams)

        return possible_exchanges

    # === Vérifier et ajouter les échanges supplémentaires en boucle ===
    while True:
        # Debug: Print the remaining streams before starting additional calculations
        print("\n=== Remaining streams ABOVE the pinch before additional calculations ===")
        print(self.remain_stream_list_above)
        print("\n=== Remaining streams BELOW the pinch before additional calculations ===")
        print(self.remain_stream_list_below)

        exchanges_above = check_additional_heat_exchanges(self.remain_stream_list_above, dTmin=0)
        exchanges_below = check_additional_heat_exchanges(self.remain_stream_list_below, dTmin=0)

        added = False

        if exchanges_above:
            for exch in exchanges_above:
                # Debug: Print the heat exchanger being processed
                print(f"\nProcessing heat exchanger ABOVE the pinch: {exch}")
                if abs(exch['Q_possible']) < 1:
                    print("Skipped: Heat exchange below threshold.")
                    continue
                hs_idx = self.remain_stream_list_above[self.remain_stream_list_above['id'] == exch['HS_id']].index[0]
                cs_idx = self.remain_stream_list_above[self.remain_stream_list_above['id'] == exch['CS_id']].index[0]

                # Update remaining heat capacity
                self.remain_stream_list_above.at[hs_idx, 'delta_H'] += exch['Q_possible']
                self.remain_stream_list_above.at[cs_idx, 'delta_H'] -= exch['Q_possible']

                # Update outlet temperatures
                self.remain_stream_list_above.at[hs_idx, 'To'] = exch['To_hot_new']
                self.remain_stream_list_above.at[cs_idx, 'To'] = exch['To_cold_new']

                # Add the heat exchanger to the list
                heat_exchangers.append({
                    'HS_id': exch['HS_id'], 'HS_name': self.remain_stream_list_above.at[hs_idx, 'name'],
                    'HS_mCp': self.remain_stream_list_above.at[hs_idx, 'mCp'],
                    'HS_Ti': self.remain_stream_list_above.at[hs_idx, 'Ti'], 'HS_To': exch['To_hot_new'],
                    'CS_id': exch['CS_id'], 'CS_name': self.remain_stream_list_above.at[cs_idx, 'name'],
                    'CS_mCp': self.remain_stream_list_above.at[cs_idx, 'mCp'],
                    'CS_Ti': self.remain_stream_list_above.at[cs_idx, 'Ti'], 'CS_To': exch['To_cold_new'],
                    'HeatExchanged': exch['Q_possible']
                })
                print("Added heat exchanger ABOVE the pinch to the list.")
                added = True

            self.remain_stream_list_above = self.remain_stream_list_above[
                abs(self.remain_stream_list_above['delta_H']) > 1
            ]

        if exchanges_below:
            for exch in exchanges_below:
                # Debug: Print the heat exchanger being processed
                print(f"\nProcessing heat exchanger BELOW the pinch: {exch}")
                if abs(exch['Q_possible']) < 1:
                    print("Skipped: Heat exchange below threshold.")
                    continue
                hs_idx = self.remain_stream_list_below[self.remain_stream_list_below['id'] == exch['HS_id']].index[0]
                cs_idx = self.remain_stream_list_below[self.remain_stream_list_below['id'] == exch['CS_id']].index[0]

                # Update remaining heat capacity
                self.remain_stream_list_below.at[hs_idx, 'delta_H'] += exch['Q_possible']
                self.remain_stream_list_below.at[cs_idx, 'delta_H'] -= exch['Q_possible']

                # Update outlet temperatures
                self.remain_stream_list_below.at[hs_idx, 'To'] = exch['To_hot_new']
                self.remain_stream_list_below.at[cs_idx, 'To'] = exch['To_cold_new']

                # Add the heat exchanger to the list
                heat_exchangers.append({
                    'HS_id': exch['HS_id'], 'HS_name': self.remain_stream_list_below.at[hs_idx, 'name'],
                    'HS_mCp': self.remain_stream_list_below.at[hs_idx, 'mCp'],
                    'HS_Ti': self.remain_stream_list_below.at[hs_idx, 'Ti'], 'HS_To': exch['To_hot_new'],
                    'CS_id': exch['CS_id'], 'CS_name': self.remain_stream_list_below.at[cs_idx, 'name'],
                    'CS_mCp': self.remain_stream_list_below.at[cs_idx, 'mCp'],
                    'CS_Ti': self.remain_stream_list_below.at[cs_idx, 'Ti'], 'CS_To': exch['To_cold_new'],
                    'HeatExchanged': exch['Q_possible']
                })
                print("Added heat exchanger BELOW the pinch to the list.")
                added = True

            self.remain_stream_list_below = self.remain_stream_list_below[
                abs(self.remain_stream_list_below['delta_H']) > 1
            ]

        if not added:
            break

    # === Construction finale du DF des échangeurs ===
    self.df_exchangers = pd.DataFrame(heat_exchangers)

    if not self.df_exchangers.empty:
        self.df_exchangers = self.df_exchangers[self.df_exchangers['HeatExchanged'].abs() >= 1]
        self.df_exchangers = self.df_exchangers.sort_values(by="HeatExchanged", ascending=False).reset_index(drop=True)

        # chaleur totale récupérée
        self.total_heat_recovered = self.df_exchangers['HeatExchanged'].sum()
        self.percent_recovered = 100 * self.total_heat_recovered / self.heat_recovery
    else:
        # Aucun échange trouvé
        self.total_heat_recovered = 0.0
        self.percent_recovered = 0.0

    return self.df_exchangers
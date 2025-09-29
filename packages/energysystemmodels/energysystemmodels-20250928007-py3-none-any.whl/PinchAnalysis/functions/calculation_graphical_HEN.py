import pandas as pd

###############################"GHE########################################"""""
def graphical_hen_design(self):
    # Initialiser une liste pour les échangeurs installés
    heat_exchangers = []

    # Fonction pour appliquer un échange de chaleur et modifier les flux
    def apply_heat_exchange_above(hot_stream_df, cold_stream_df):
        #print("*************************Réseau d'échangeur au dessus du pinch*******************************-----------------------------------\n")

        # Convertir les DataFrames en dictionnaires pour traitement
        hot_stream = hot_stream_df.iloc[0].to_dict()
        cold_stream = cold_stream_df.iloc[0].to_dict()

        # Trouver la quantité de chaleur échangée (basée sur la plus petite capacité thermique résiduelle)
        heat_exchanged = min(-hot_stream['delta_H'], cold_stream['delta_H'])
        if (-hot_stream['delta_H'])<cold_stream['delta_H']:
            if cold_stream["STo"]>=self.Pinch_Temperature:
                cold_stream["To"]=(heat_exchanged/cold_stream["mCp"])+cold_stream["Ti"]
                cold_stream["STo"]=(heat_exchanged/cold_stream["mCp"])+cold_stream["STi"]
                #print("============cold_stream To======================",cold_stream["To"])
            else:
                cold_stream["Ti"]=cold_stream["To"]-(heat_exchanged/cold_stream["mCp"])
                cold_stream["STi"]=cold_stream["STo"]-(heat_exchanged/cold_stream["mCp"])
                #print("===========cold_stream Ti================",cold_stream["Ti"])

        # Créer un échangeur de chaleur et l'ajouter à la liste
        exchanger = {
            'HS_id': hot_stream['id'],
            'HS_name': hot_stream['name'],
            'HS_mCp': hot_stream['mCp'],
            'HS_Ti': hot_stream['Ti'],
            'HS_To': hot_stream['To'],

            'CS_id': cold_stream['id'],
            'CS_name': cold_stream['name'],
            'CS_mCp': cold_stream['mCp'],
            'CS_Ti': cold_stream['Ti'],
            'CS_To': cold_stream['To'],
            
            
            'HeatExchanged': heat_exchanged
        }
        heat_exchangers.append(exchanger)

     
        #print(f"Échangeur installé: {exchanger}")

        # Print pour voir la quantité de chaleur échangée
        #print(f"Échange de chaleur entre {hot_stream['name']} et {cold_stream['name']}")
        #print(f"Chaleur échangée : {heat_exchanged}")
        #print(f"Avant échange: delta_H Hot: {hot_stream['delta_H']}, delta_H Cold: {cold_stream['delta_H']}")

        # Mettre à jour les capacités thermiques résiduelles des flux
        hot_stream_df.loc[hot_stream_df.index[0], 'delta_H'] += heat_exchanged
        cold_stream_df.loc[cold_stream_df.index[0], 'delta_H'] -= heat_exchanged
        # mettre à jour To de cold stream
        cold_stream_df.loc[cold_stream_df.index[0], 'To'] = cold_stream['Ti'] #l'entrée de l'échangeur installé
        cold_stream_df.loc[cold_stream_df.index[0], 'STo'] = cold_stream['STi'] #l'entrée de l'échangeur installé


        # Print pour voir les flux après mise à jour
        #print(f"Après échange: delta_H Hot: {hot_stream_df['delta_H'].iloc[0]}, delta_H Cold: {cold_stream_df['delta_H'].iloc[0]}")
        self.df_exchangers = pd.DataFrame(heat_exchangers)
        #print("Réseau d'échangeurs de chaleur:")
        #print(self.df_exchangers)

        # Retourner les DataFrames modifiés
        return hot_stream_df, cold_stream_df

    # Fonction pour appliquer un échange de chaleur et modifier les flux
    def apply_heat_exchange_below(hot_stream_df, cold_stream_df):
        #print('\n')
        #print("*************************Réseau d'échangeur en-dessous du pinch*******************************-----------------------------------\n")

        # Convertir les DataFrames en dictionnaires pour traitement
        hot_stream = hot_stream_df.iloc[0].to_dict()
        cold_stream = cold_stream_df.iloc[0].to_dict()

        # Trouver la quantité de chaleur échangée (basée sur la plus petite capacité thermique résiduelle)
        heat_exchanged = min(-hot_stream['delta_H'], cold_stream['delta_H'])
        #print("------------------------heat_exchanged----------------",heat_exchanged)
        if (-hot_stream['delta_H'])>cold_stream['delta_H']:
            if hot_stream["STo"]<=self.Pinch_Temperature:
                hot_stream["To"]=hot_stream["Ti"]-(heat_exchanged/hot_stream["mCp"])
                hot_stream["STo"]=hot_stream["STi"]-(heat_exchanged/hot_stream["mCp"])
                #print("============cold_stream To======================",cold_stream["To"])
            else:
                pass

        # Créer un échangeur de chaleur et l'ajouter à la liste
        exchanger = {
            'HS_id': hot_stream['id'],
            'HS_name': hot_stream['name'],
            'HS_mCp': hot_stream['mCp'],
            'HS_Ti': hot_stream['Ti'],
            'HS_To': hot_stream['To'],

            'CS_id': cold_stream['id'],
            'CS_name': cold_stream['name'],
            'CS_mCp': cold_stream['mCp'],
            'CS_Ti': cold_stream['Ti'],
            'CS_To': cold_stream['To'],
            
            
            'HeatExchanged': heat_exchanged
        }
        heat_exchangers.append(exchanger)

      
        #print(f"Échangeur installé: {exchanger}")

        # Print pour voir la quantité de chaleur échangée
        #print(f"Échange de chaleur entre {hot_stream['name']} et {cold_stream['name']}")
        #print(f"Chaleur échangée : {heat_exchanged}")
        #print(f"Avant échange: delta_H Hot: {hot_stream['delta_H']}, delta_H Cold: {cold_stream['delta_H']}")

        # Mettre à jour les capacités thermiques résiduelles des flux
        hot_stream_df.loc[hot_stream_df.index[0], 'delta_H'] += heat_exchanged
        cold_stream_df.loc[cold_stream_df.index[0], 'delta_H'] -= heat_exchanged
        # mettre à jour To de cold stream
        cold_stream_df.loc[cold_stream_df.index[0], 'To'] = cold_stream['Ti'] #l'entrée de l'échangeur installé
        cold_stream_df.loc[cold_stream_df.index[0], 'STo'] = cold_stream['STi'] #l'entrée de l'échangeur installé


        # Print pour voir les flux après mise à jour
        #print(f"Après échange: delta_H Hot: {hot_stream_df['delta_H'].iloc[0]}, delta_H Cold: {cold_stream_df['delta_H'].iloc[0]}")
        self.df_exchangers = pd.DataFrame(heat_exchangers)
        #print("Réseau d'échangeurs de chaleur:")
        #print(self.df_exchangers)

        # Retourner les DataFrames modifiés
        return hot_stream_df, cold_stream_df


    # Sélectionner les combinaisons au-dessus du pinch (si disponibles)
    if not self.combinations_above.empty:
        #("**********************************Début des échanges au-dessus du pinch********************************")
        #print(f"Combinaisons disponibles au-dessus du pinch:\n{self.combinations_above}\n")
        for i in range(len(self.combinations_above)):
            i_combination_above = self.combinations_above.iloc[i]
            #print(f"Combinaison au-dessus du pinch à tester: {i_combination_above}")

            # Extraire les flux chauds et froids à partir des identifiants
            hot_stream_id = i_combination_above['HS_id']
            cold_stream_id = i_combination_above['CS_id']

            #print(f"Recherche du flux chaud avec ID: {hot_stream_id}")
            #print(f"Recherche du flux froid avec ID: {cold_stream_id}")

            hot_stream_df = self.stream_list_above[self.stream_list_above['id'] == hot_stream_id]
            cold_stream_df = self.stream_list_above[self.stream_list_above['id'] == cold_stream_id]

            # Vérifier si les flux existent
            if not hot_stream_df.empty and not cold_stream_df.empty and (hot_stream_df['delta_H'].iloc[0] != 0.0 or cold_stream_df['delta_H'].iloc[0] != 0.0):
                # Appliquer l'échange de chaleur pour cette combinaison
                hot_stream_df, cold_stream_df = apply_heat_exchange_above(hot_stream_df, cold_stream_df)

                # Mettre à jour `self.stream_list_above` après l'échange de chaleur
                # Remplacer les flux mis à jour dans le DataFrame principal
                self.remain_stream_list_above=self.stream_list_above
                self.remain_stream_list_above.update(hot_stream_df)
                self.remain_stream_list_above.update(cold_stream_df)

                # Supprimer les flux totalement utilisés
                threshold = 1
                self.remain_stream_list_above = self.remain_stream_list_above[abs(self.remain_stream_list_above['delta_H']) > threshold]

                # Afficher l'état mis à jour des flux
            
            else:
                pass
                #print(f"Flux pour l'indice {i} non trouvés dans la liste.")


    ###

    if not self.combinations_below.empty:
        for i in range(len(self.combinations_below)):
            i_combination_below = self.combinations_below.iloc[i]
            #print(f"Combinaison en-dessous du pinch à tester: {i_combination_below}")

            # Extraire les flux chauds et froids à partir des identifiants
            hot_stream_id = i_combination_below['HS_id']
            cold_stream_id = i_combination_below['CS_id']

            #print(f"Recherche du flux chaud avec ID: {hot_stream_id}")
            #print(f"Recherche du flux froid avec ID: {cold_stream_id}")

            hot_stream_df = self.stream_list_below[self.stream_list_below['id'] == hot_stream_id]
            cold_stream_df = self.stream_list_below[self.stream_list_below['id'] == cold_stream_id]

            # Vérifier si les flux existent
            if not hot_stream_df.empty and not cold_stream_df.empty and (hot_stream_df['delta_H'].iloc[0] != 0.0 or cold_stream_df['delta_H'].iloc[0] != 0.0):
                # Appliquer l'échange de chaleur pour cette combinaison
                hot_stream_df, cold_stream_df = apply_heat_exchange_below(hot_stream_df, cold_stream_df)

                # Mettre à jour `self.stream_list_below` après l'échange de chaleur
                # Remplacer les flux mis à jour dans le DataFrame principal
                self.remain_stream_list_below= self.stream_list_below
                self.remain_stream_list_below.update(hot_stream_df)
                self.remain_stream_list_below.update(cold_stream_df)

                # Supprimer les flux totalement utilisés
                self.remain_stream_list_below = self.remain_stream_list_below[self.remain_stream_list_below['delta_H'] != 0.0]

                # Afficher l'état mis à jour des flux

            else:
                pass
                #print(f"Flux pour l'indice {i} non trouvés dans la liste.")


    ###

    else:
        print("Aucune combinaison disponible au-dessus du pinch pour le moment.")
    self.df_exchangers = pd.DataFrame(heat_exchangers)
    self.df_exchangers = self.df_exchangers[self.df_exchangers['HeatExchanged'].abs() >= 1]
    # print("HEN - Méthode graphique - Liste des échangeurs de chaleur installés:\n")
    # print(self.df_exchangers)
    self.df_exchangers = self.df_exchangers.sort_values(by="HeatExchanged", ascending=False).reset_index(drop=True)
    # Print Redults:

    # print("HEN - Méthode graphique - Liste des échangeurs de chaleur installés:\n")
    # print(self.df_exchangers)

    # print(f"liste des flux restants au-dessus du pinch******************\n")
    # print(self.remain_stream_list_above)

    # print(f"liste des flux restants en-dessous du pinch******************\n")
    # print(self.remain_stream_list_below)
    
    
 
############################
    def check_additional_heat_exchanges(remain_streams, dTmin=0, threshold=1):
        hot_streams = remain_streams[remain_streams['StreamType'] == 'HS']
        cold_streams = remain_streams[remain_streams['StreamType'] == 'CS']
        possible_exchanges = []
        for _, hot in hot_streams.iterrows():
            for _, cold in cold_streams.iterrows():
                deltaT = hot['Ti'] - cold['Ti']
                if deltaT <= dTmin:
                    continue  # Pas de potentiel d'échange

                # Calcul du Q_max pour éviter croisement
                Q_hot_limit = hot['mCp'] * (hot['Ti'] - (cold['Ti'] + dTmin))
                Q_cold_limit = cold['mCp'] * (hot['Ti'] - (cold['Ti'] + dTmin))
                Q_max = min(-hot['delta_H'], cold['delta_H'], Q_hot_limit, Q_cold_limit)

                if Q_max < threshold:
                    continue  # Ignore les échanges trop faibles

                # Calcul des températures de sortie après échange
                To_hot_new = hot['Ti'] - Q_max / hot['mCp']
                To_cold_new = cold['Ti'] + Q_max / cold['mCp']

                # Vérifie qu'il n'y a pas de croisement (pincement respecté)
                if To_hot_new >= To_cold_new + dTmin:
                    possible_exchanges.append({
                        'HS_id': hot['id'],
                        'CS_id': cold['id'],
                        'Q_possible': Q_max,
                        'To_hot_new': To_hot_new,
                        'To_cold_new': To_cold_new
                    })
        return possible_exchanges
    




    #print("\n--- Échanges possibles hors règle mCp (pincement 0, au-dessus du pinch) ---")
    exchanges_above = check_additional_heat_exchanges(self.remain_stream_list_above, dTmin=0)
    if exchanges_above:
        for exch in exchanges_above:
            print(f"HS {exch['HS_id']} <-> CS {exch['CS_id']} : Q_possible={exch['Q_possible']:.2f} kW, To_hot_new={exch['To_hot_new']:.2f}°C, To_cold_new={exch['To_cold_new']:.2f}°C")
    else:
        print("Aucun échange supplémentaire possible sans pincement (au-dessus du pinch).")

    #print("\n--- Échanges possibles hors règle mCp (pincement 0, en-dessous du pinch) ---")
    exchanges_below = check_additional_heat_exchanges(self.remain_stream_list_below, dTmin=0)
    if exchanges_below:
        for exch in exchanges_below:
            print(f"HS {exch['HS_id']} <-> CS {exch['CS_id']} : Q_possible={exch['Q_possible']:.2f} kW, To_hot_new={exch['To_hot_new']:.2f}°C, To_cold_new={exch['To_cold_new']:.2f}°C")
    else:
        print("Aucun échange supplémentaire possible sans pincement (en-dessous du pinch).")


    # === Ajout séquentiel des nouveaux échangeurs trouvés ===
    # Pour au-dessus du pinch
    if exchanges_above:
        for exch in exchanges_above:
            if abs(exch['Q_possible']) < 1:
                continue  # Ignore les échanges trop faibles
            # Mettre à jour les flux restants
            hs_idx = self.remain_stream_list_above[self.remain_stream_list_above['id'] == exch['HS_id']].index[0]
            cs_idx = self.remain_stream_list_above[self.remain_stream_list_above['id'] == exch['CS_id']].index[0]
            # Mettre à jour delta_H
            self.remain_stream_list_above.at[hs_idx, 'delta_H'] += exch['Q_possible']
            self.remain_stream_list_above.at[cs_idx, 'delta_H'] -= exch['Q_possible']
            # Mettre à jour To/Ti
            self.remain_stream_list_above.at[hs_idx, 'To'] = exch['To_hot_new']
            self.remain_stream_list_above.at[cs_idx, 'To'] = exch['To_cold_new']
            # Ajouter l'échangeur détaillé
            heat_exchangers.append({
                'HS_id': exch['HS_id'],
                'HS_name': self.remain_stream_list_above.at[hs_idx, 'name'],
                'HS_mCp': self.remain_stream_list_above.at[hs_idx, 'mCp'],
                'HS_Ti': self.remain_stream_list_above.at[hs_idx, 'Ti'],
                'HS_To': exch['To_hot_new'],
                'CS_id': exch['CS_id'],
                'CS_name': self.remain_stream_list_above.at[cs_idx, 'name'],
                'CS_mCp': self.remain_stream_list_above.at[cs_idx, 'mCp'],
                'CS_Ti': self.remain_stream_list_above.at[cs_idx, 'Ti'],
                'CS_To': exch['To_cold_new'],
                'HeatExchanged': exch['Q_possible']
            })
        # Supprimer les flux totalement utilisés
        self.remain_stream_list_above = self.remain_stream_list_above[abs(self.remain_stream_list_above['delta_H']) > 1]

    # Pour en-dessous du pinch
    if exchanges_below:
        for exch in exchanges_below:
            if abs(exch['Q_possible']) < 1:
                continue  # Ignore les échanges trop faibles
            hs_idx = self.remain_stream_list_below[self.remain_stream_list_below['id'] == exch['HS_id']].index[0]
            cs_idx = self.remain_stream_list_below[self.remain_stream_list_below['id'] == exch['CS_id']].index[0]
            self.remain_stream_list_below.at[hs_idx, 'delta_H'] += exch['Q_possible']
            self.remain_stream_list_below.at[cs_idx, 'delta_H'] -= exch['Q_possible']
            self.remain_stream_list_below.at[hs_idx, 'To'] = exch['To_hot_new']
            self.remain_stream_list_below.at[cs_idx, 'To'] = exch['To_cold_new']
            heat_exchangers.append({
                'HS_id': exch['HS_id'],
                'HS_name': self.remain_stream_list_below.at[hs_idx, 'name'],
                'HS_mCp': self.remain_stream_list_below.at[hs_idx, 'mCp'],
                'HS_Ti': self.remain_stream_list_below.at[hs_idx, 'Ti'],
                'HS_To': exch['To_hot_new'],
                'CS_id': exch['CS_id'],
                'CS_name': self.remain_stream_list_below.at[cs_idx, 'name'],
                'CS_mCp': self.remain_stream_list_below.at[cs_idx, 'mCp'],
                'CS_Ti': self.remain_stream_list_below.at[cs_idx, 'Ti'],
                'CS_To': exch['To_cold_new'],
                'HeatExchanged': exch['Q_possible']
            })
        self.remain_stream_list_below = self.remain_stream_list_below[abs(self.remain_stream_list_below['delta_H']) > 1]

    # Mettre à jour le DataFrame des échangeurs
    self.df_exchangers = pd.DataFrame(heat_exchangers)
    # Supprimer tous les échangeurs avec HeatExchanged nul ou trop faible
    self.df_exchangers = self.df_exchangers[self.df_exchangers['HeatExchanged'].abs() >= 1]
    # Trier par la valeur de chaleur échangée (HeatExchanged) décroissante
    self.df_exchangers = self.df_exchangers.sort_values(by="HeatExchanged", ascending=False).reset_index(drop=True)

    # chaleur totale récupérée du réseau d'échangeurs
    self.total_heat_recovered = self.df_exchangers['HeatExchanged'].sum()
    self.percent_recovered = 100 * self.total_heat_recovered/self.heat_recovery
  
################################################################

 

    return self.df_exchangers

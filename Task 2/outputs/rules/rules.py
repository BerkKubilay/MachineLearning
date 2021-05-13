def findDecision(obj): #obj[0]: Cinsiyet, obj[1]: soru1, obj[2]: soru2, obj[3]: soru3, obj[4]: soru4, obj[5]: soru5, obj[6]: soru6, obj[7]: soru7, obj[8]: soru8, obj[9]: soru9, obj[10]: soru10
   # {"feature": "soru7", "instances": 300, "metric_value": 2.2105, "depth": 1}
   if obj[7] == 'Evet':
      # {"feature": "soru5", "instances": 256, "metric_value": 2.0855, "depth": 2}
      if obj[5] == 'Hayır':
         # {"feature": "soru9", "instances": 245, "metric_value": 2.0469, "depth": 3}
         if obj[9] == 'Evet':
            # {"feature": "soru10", "instances": 196, "metric_value": 1.9113, "depth": 4}
            if obj[10] == 'Evet':
               # {"feature": "Cinsiyet", "instances": 173, "metric_value": 1.7914, "depth": 5}
               if obj[0] == 'Erkek':
                  # {"feature": "soru4", "instances": 160, "metric_value": 1.7544, "depth": 6}
                  if obj[4] == 'Hayır':
                     # {"feature": "soru8", "instances": 94, "metric_value": 1.7699, "depth": 7}
                     if obj[8] == 'Hayır':
                        # {"feature": "soru6", "instances": 80, "metric_value": 1.7788, "depth": 8}
                        if obj[6] == 'Hayır':
                           # {"feature": "soru1", "instances": 73, "metric_value": 1.8031, "depth": 9}
                           if obj[1] == 'Hayır':
                              # {"feature": "soru2", "instances": 43, "metric_value": 1.7966, "depth": 10}
                              if obj[2] == 'Evet':
                                 # {"feature": "soru3", "instances": 42, "metric_value": 1.8069, "depth": 11}
                                 if obj[3] == 'Evet':
                                    return 'CHP'
                                 elif obj[3] == 'Hayır':
                                    return 'CHP'
                                 else:
                                    return 'CHP'
                              elif obj[2] == 'Hayır':
                                 return 'CHP'
                              else:
                                 return 'CHP'
                           elif obj[1] == 'Evet':
                              # {"feature": "soru3", "instances": 30, "metric_value": 1.7032, "depth": 10}
                              if obj[3] == 'Evet':
                                 # {"feature": "soru2", "instances": 15, "metric_value": 1.5329, "depth": 11}
                                 if obj[2] == 'Evet':
                                    return 'CHP'
                                 elif obj[2] == 'Hayır':
                                    return 'CHP'
                                 else:
                                    return 'CHP'
                              elif obj[3] == 'Hayır':
                                 # {"feature": "soru2", "instances": 15, "metric_value": 1.5546, "depth": 11}
                                 if obj[2] == 'Evet':
                                    return 'IYI PARTI'
                                 elif obj[2] == 'Hayır':
                                    return 'IYI PARTI'
                                 else:
                                    return 'IYI PARTI'
                              else:
                                 return 'IYI PARTI'
                           else:
                              return 'IYI PARTI'
                        elif obj[6] == 'Evet':
                           # {"feature": "soru1", "instances": 7, "metric_value": 1.1488, "depth": 9}
                           if obj[1] == 'Hayır':
                              # {"feature": "soru3", "instances": 4, "metric_value": 0.8113, "depth": 10}
                              if obj[3] == 'Evet':
                                 # {"feature": "soru2", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[2] == 'Evet':
                                    return 'CHP'
                                 else:
                                    return 'CHP'
                              elif obj[3] == 'Hayır':
                                 return 'CHP'
                              else:
                                 return 'CHP'
                           elif obj[1] == 'Evet':
                              # {"feature": "soru3", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[3] == 'Evet':
                                 # {"feature": "soru2", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[2] == 'Evet':
                                    return 'IYI PARTI'
                                 else:
                                    return 'IYI PARTI'
                              elif obj[3] == 'Hayır':
                                 return 'CHP'
                              else:
                                 return 'CHP'
                           else:
                              return 'CHP'
                        else:
                           return 'CHP'
                     elif obj[8] == 'Evet':
                        # {"feature": "soru6", "instances": 14, "metric_value": 1.5567, "depth": 8}
                        if obj[6] == 'Hayır':
                           # {"feature": "soru1", "instances": 11, "metric_value": 1.5726, "depth": 9}
                           if obj[1] == 'Hayır':
                              # {"feature": "soru2", "instances": 8, "metric_value": 1.5, "depth": 10}
                              if obj[2] == 'Evet':
                                 # {"feature": "soru3", "instances": 8, "metric_value": 1.5, "depth": 11}
                                 if obj[3] == 'Evet':
                                    return 'IYI PARTI'
                                 elif obj[3] == 'Hayır':
                                    return 'IYI PARTI'
                                 else:
                                    return 'IYI PARTI'
                              else:
                                 return 'IYI PARTI'
                           elif obj[1] == 'Evet':
                              # {"feature": "soru3", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[3] == 'Hayır':
                                 # {"feature": "soru2", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[2] == 'Evet':
                                    return 'CHP'
                                 else:
                                    return 'CHP'
                              elif obj[3] == 'Evet':
                                 return 'CHP'
                              else:
                                 return 'CHP'
                           else:
                              return 'CHP'
                        elif obj[6] == 'Evet':
                           # {"feature": "soru1", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[1] == 'Hayır':
                              # {"feature": "soru2", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[2] == 'Evet':
                                 # {"feature": "soru3", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[3] == 'Evet':
                                    return 'IYI PARTI'
                                 else:
                                    return 'IYI PARTI'
                              else:
                                 return 'IYI PARTI'
                           elif obj[1] == 'Evet':
                              return 'IYI PARTI'
                           else:
                              return 'IYI PARTI'
                        else:
                           return 'IYI PARTI'
                     else:
                        return 'IYI PARTI'
                  elif obj[4] == 'Evet':
                     # {"feature": "soru2", "instances": 66, "metric_value": 1.646, "depth": 7}
                     if obj[2] == 'Evet':
                        # {"feature": "soru3", "instances": 64, "metric_value": 1.6641, "depth": 8}
                        if obj[3] == 'Evet':
                           # {"feature": "soru1", "instances": 42, "metric_value": 1.4555, "depth": 9}
                           if obj[1] == 'Hayır':
                              # {"feature": "soru8", "instances": 35, "metric_value": 1.5074, "depth": 10}
                              if obj[8] == 'Hayır':
                                 # {"feature": "soru6", "instances": 30, "metric_value": 1.4812, "depth": 11}
                                 if obj[6] == 'Hayır':
                                    return 'IYI PARTI'
                                 elif obj[6] == 'Evet':
                                    return 'IYI PARTI'
                                 else:
                                    return 'IYI PARTI'
                              elif obj[8] == 'Evet':
                                 # {"feature": "soru6", "instances": 5, "metric_value": 1.5219, "depth": 11}
                                 if obj[6] == 'Evet':
                                    return 'CHP'
                                 elif obj[6] == 'Hayır':
                                    return 'IYI PARTI'
                                 else:
                                    return 'IYI PARTI'
                              else:
                                 return 'IYI PARTI'
                           elif obj[1] == 'Evet':
                              # {"feature": "soru6", "instances": 7, "metric_value": 0.9852, "depth": 10}
                              if obj[6] == 'Hayır':
                                 # {"feature": "soru8", "instances": 5, "metric_value": 0.971, "depth": 11}
                                 if obj[8] == 'Hayır':
                                    return 'CHP'
                                 elif obj[8] == 'Evet':
                                    return 'IYI PARTI'
                                 else:
                                    return 'IYI PARTI'
                              elif obj[6] == 'Evet':
                                 return 'IYI PARTI'
                              else:
                                 return 'IYI PARTI'
                           else:
                              return 'IYI PARTI'
                        elif obj[3] == 'Hayır':
                           # {"feature": "soru8", "instances": 22, "metric_value": 1.7797, "depth": 9}
                           if obj[8] == 'Hayır':
                              # {"feature": "soru6", "instances": 16, "metric_value": 1.7718, "depth": 10}
                              if obj[6] == 'Hayır':
                                 # {"feature": "soru1", "instances": 13, "metric_value": 1.7381, "depth": 11}
                                 if obj[1] == 'Hayır':
                                    return 'IYI PARTI'
                                 elif obj[1] == 'Evet':
                                    return 'IYI PARTI'
                                 else:
                                    return 'IYI PARTI'
                              elif obj[6] == 'Evet':
                                 # {"feature": "soru1", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[1] == 'Evet':
                                    return 'DIĞER'
                                 elif obj[1] == 'Hayır':
                                    return 'IYI PARTI'
                                 else:
                                    return 'IYI PARTI'
                              else:
                                 return 'DIĞER'
                           elif obj[8] == 'Evet':
                              # {"feature": "soru6", "instances": 6, "metric_value": 1.0, "depth": 10}
                              if obj[6] == 'Hayır':
                                 # {"feature": "soru1", "instances": 4, "metric_value": 0.8113, "depth": 11}
                                 if obj[1] == 'Evet':
                                    return 'DIĞER'
                                 elif obj[1] == 'Hayır':
                                    return 'DIĞER'
                                 else:
                                    return 'DIĞER'
                              elif obj[6] == 'Evet':
                                 return 'CHP'
                              else:
                                 return 'CHP'
                           else:
                              return 'CHP'
                        else:
                           return 'CHP'
                     elif obj[2] == 'Hayır':
                        return 'IYI PARTI'
                     else:
                        return 'IYI PARTI'
                  else:
                     return 'IYI PARTI'
               elif obj[0] == 'Kadın':
                  # {"feature": "soru3", "instances": 13, "metric_value": 1.6143, "depth": 6}
                  if obj[3] == 'Evet':
                     # {"feature": "soru1", "instances": 7, "metric_value": 1.1488, "depth": 7}
                     if obj[1] == 'Hayır':
                        # {"feature": "soru4", "instances": 6, "metric_value": 0.65, "depth": 8}
                        if obj[4] == 'Evet':
                           return 'IYI PARTI'
                        elif obj[4] == 'Hayır':
                           # {"feature": "soru2", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[2] == 'Evet':
                              # {"feature": "soru6", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[6] == 'Hayır':
                                 # {"feature": "soru8", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[8] == 'Hayır':
                                    return 'IYI PARTI'
                                 else:
                                    return 'IYI PARTI'
                              else:
                                 return 'IYI PARTI'
                           else:
                              return 'IYI PARTI'
                        else:
                           return 'IYI PARTI'
                     elif obj[1] == 'Evet':
                        return 'DIĞER'
                     else:
                        return 'DIĞER'
                  elif obj[3] == 'Hayır':
                     # {"feature": "soru4", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[4] == 'Hayır':
                        return 'DIĞER'
                     elif obj[4] == 'Evet':
                        return 'CHP'
                     else:
                        return 'CHP'
                  else:
                     return 'DIĞER'
               else:
                  return 'DIĞER'
            elif obj[10] == 'Hayır':
               # {"feature": "soru2", "instances": 23, "metric_value": 2.2335, "depth": 5}
               if obj[2] == 'Evet':
                  # {"feature": "Cinsiyet", "instances": 22, "metric_value": 2.1905, "depth": 6}
                  if obj[0] == 'Erkek':
                     # {"feature": "soru3", "instances": 21, "metric_value": 2.2126, "depth": 7}
                     if obj[3] == 'Evet':
                        # {"feature": "soru4", "instances": 11, "metric_value": 1.8586, "depth": 8}
                        if obj[4] == 'Evet':
                           # {"feature": "soru1", "instances": 7, "metric_value": 1.9502, "depth": 9}
                           if obj[1] == 'Hayır':
                              # {"feature": "soru6", "instances": 5, "metric_value": 1.9219, "depth": 10}
                              if obj[6] == 'Hayır':
                                 # {"feature": "soru8", "instances": 3, "metric_value": 1.585, "depth": 11}
                                 if obj[8] == 'Hayır':
                                    return 'IYI PARTI'
                                 else:
                                    return 'IYI PARTI'
                              elif obj[6] == 'Evet':
                                 # {"feature": "soru8", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[8] == 'Evet':
                                    return 'CHP'
                                 elif obj[8] == 'Hayır':
                                    return 'AKP'
                                 else:
                                    return 'AKP'
                              else:
                                 return 'AKP'
                           elif obj[1] == 'Evet':
                              # {"feature": "soru6", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[6] == 'Evet':
                                 return 'DIĞER'
                              elif obj[6] == 'Hayır':
                                 return 'AKP'
                              else:
                                 return 'AKP'
                           else:
                              return 'AKP'
                        elif obj[4] == 'Hayır':
                           # {"feature": "soru1", "instances": 4, "metric_value": 0.8113, "depth": 9}
                           if obj[1] == 'Evet':
                              return 'CHP'
                           elif obj[1] == 'Hayır':
                              # {"feature": "soru8", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[8] == 'Evet':
                                 return 'IYI PARTI'
                              elif obj[8] == 'Hayır':
                                 return 'CHP'
                              else:
                                 return 'CHP'
                           else:
                              return 'IYI PARTI'
                        else:
                           return 'CHP'
                     elif obj[3] == 'Hayır':
                        # {"feature": "soru8", "instances": 10, "metric_value": 2.1219, "depth": 8}
                        if obj[8] == 'Hayır':
                           # {"feature": "soru6", "instances": 6, "metric_value": 1.9183, "depth": 9}
                           if obj[6] == 'Hayır':
                              # {"feature": "soru1", "instances": 5, "metric_value": 1.5219, "depth": 10}
                              if obj[1] == 'Hayır':
                                 # {"feature": "soru4", "instances": 4, "metric_value": 1.5, "depth": 11}
                                 if obj[4] == 'Evet':
                                    return 'MHP'
                                 elif obj[4] == 'Hayır':
                                    return 'MHP'
                                 else:
                                    return 'MHP'
                              elif obj[1] == 'Evet':
                                 return 'IYI PARTI'
                              else:
                                 return 'IYI PARTI'
                           elif obj[6] == 'Evet':
                              return 'DIĞER'
                           else:
                              return 'DIĞER'
                        elif obj[8] == 'Evet':
                           # {"feature": "soru1", "instances": 4, "metric_value": 0.8113, "depth": 9}
                           if obj[1] == 'Hayır':
                              # {"feature": "soru4", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[4] == 'Evet':
                                 # {"feature": "soru6", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[6] == 'Hayır':
                                    return 'DIĞER'
                                 else:
                                    return 'DIĞER'
                              else:
                                 return 'DIĞER'
                           elif obj[1] == 'Evet':
                              return 'DIĞER'
                           else:
                              return 'DIĞER'
                        else:
                           return 'DIĞER'
                     else:
                        return 'DIĞER'
                  elif obj[0] == 'Kadın':
                     return 'CHP'
                  else:
                     return 'CHP'
               elif obj[2] == 'Hayır':
                  return 'MHP'
               else:
                  return 'MHP'
            else:
               return 'CHP'
         elif obj[9] == 'Hayır':
            # {"feature": "soru2", "instances": 49, "metric_value": 2.1953, "depth": 4}
            if obj[2] == 'Evet':
               # {"feature": "Cinsiyet", "instances": 47, "metric_value": 2.1644, "depth": 5}
               if obj[0] == 'Erkek':
                  # {"feature": "soru8", "instances": 43, "metric_value": 2.0876, "depth": 6}
                  if obj[8] == 'Hayır':
                     # {"feature": "soru10", "instances": 24, "metric_value": 2.0996, "depth": 7}
                     if obj[10] == 'Evet':
                        # {"feature": "soru3", "instances": 20, "metric_value": 1.815, "depth": 8}
                        if obj[3] == 'Evet':
                           # {"feature": "soru4", "instances": 11, "metric_value": 1.3093, "depth": 9}
                           if obj[4] == 'Hayır':
                              # {"feature": "soru1", "instances": 6, "metric_value": 1.585, "depth": 10}
                              if obj[1] == 'Hayır':
                                 # {"feature": "soru6", "instances": 5, "metric_value": 1.5219, "depth": 11}
                                 if obj[6] == 'Hayır':
                                    return 'CHP'
                                 elif obj[6] == 'Evet':
                                    return 'IYI PARTI'
                                 else:
                                    return 'IYI PARTI'
                              elif obj[1] == 'Evet':
                                 return 'DIĞER'
                              else:
                                 return 'DIĞER'
                           elif obj[4] == 'Evet':
                              return 'DIĞER'
                           else:
                              return 'DIĞER'
                        elif obj[3] == 'Hayır':
                           # {"feature": "soru6", "instances": 9, "metric_value": 1.9749, "depth": 9}
                           if obj[6] == 'Hayır':
                              # {"feature": "soru1", "instances": 8, "metric_value": 1.9056, "depth": 10}
                              if obj[1] == 'Hayır':
                                 # {"feature": "soru4", "instances": 6, "metric_value": 1.585, "depth": 11}
                                 if obj[4] == 'Evet':
                                    return 'MHP'
                                 elif obj[4] == 'Hayır':
                                    return 'CHP'
                                 else:
                                    return 'CHP'
                              elif obj[1] == 'Evet':
                                 # {"feature": "soru4", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[4] == 'Evet':
                                    return 'DIĞER'
                                 elif obj[4] == 'Hayır':
                                    return 'CHP'
                                 else:
                                    return 'CHP'
                              else:
                                 return 'CHP'
                           elif obj[6] == 'Evet':
                              return 'DIĞER'
                           else:
                              return 'DIĞER'
                        else:
                           return 'CHP'
                     elif obj[10] == 'Hayır':
                        # {"feature": "soru1", "instances": 4, "metric_value": 1.5, "depth": 8}
                        if obj[1] == 'Evet':
                           return 'AKP'
                        elif obj[1] == 'Hayır':
                           # {"feature": "soru3", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[3] == 'Evet':
                              return 'IYI PARTI'
                           elif obj[3] == 'Hayır':
                              return 'CHP'
                           else:
                              return 'CHP'
                        else:
                           return 'IYI PARTI'
                     else:
                        return 'AKP'
                  elif obj[8] == 'Evet':
                     # {"feature": "soru4", "instances": 19, "metric_value": 1.581, "depth": 7}
                     if obj[4] == 'Evet':
                        # {"feature": "soru10", "instances": 16, "metric_value": 1.5462, "depth": 8}
                        if obj[10] == 'Evet':
                           # {"feature": "soru1", "instances": 10, "metric_value": 1.2955, "depth": 9}
                           if obj[1] == 'Evet':
                              # {"feature": "soru6", "instances": 5, "metric_value": 0.7219, "depth": 10}
                              if obj[6] == 'Hayır':
                                 return 'DIĞER'
                              elif obj[6] == 'Evet':
                                 # {"feature": "soru3", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[3] == 'Evet':
                                    return 'IYI PARTI'
                                 elif obj[3] == 'Hayır':
                                    return 'DIĞER'
                                 else:
                                    return 'DIĞER'
                              else:
                                 return 'IYI PARTI'
                           elif obj[1] == 'Hayır':
                              # {"feature": "soru3", "instances": 5, "metric_value": 0.971, "depth": 10}
                              if obj[3] == 'Hayır':
                                 # {"feature": "soru6", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[6] == 'Hayır':
                                    return 'AKP'
                                 elif obj[6] == 'Evet':
                                    return 'DIĞER'
                                 else:
                                    return 'DIĞER'
                              elif obj[3] == 'Evet':
                                 return 'AKP'
                              else:
                                 return 'AKP'
                           else:
                              return 'AKP'
                        elif obj[10] == 'Hayır':
                           # {"feature": "soru1", "instances": 6, "metric_value": 1.4591, "depth": 9}
                           if obj[1] == 'Evet':
                              # {"feature": "soru3", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[3] == 'Evet':
                                 # {"feature": "soru6", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[6] == 'Evet':
                                    return 'AKP'
                                 elif obj[6] == 'Hayır':
                                    return 'DIĞER'
                                 else:
                                    return 'DIĞER'
                              elif obj[3] == 'Hayır':
                                 return 'AKP'
                              else:
                                 return 'AKP'
                           elif obj[1] == 'Hayır':
                              return 'IYI PARTI'
                           else:
                              return 'IYI PARTI'
                        else:
                           return 'IYI PARTI'
                     elif obj[4] == 'Hayır':
                        # {"feature": "soru6", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[6] == 'Hayır':
                           return 'IYI PARTI'
                        elif obj[6] == 'Evet':
                           return 'AKP'
                        else:
                           return 'AKP'
                     else:
                        return 'IYI PARTI'
                  else:
                     return 'DIĞER'
               elif obj[0] == 'Kadın':
                  # {"feature": "soru4", "instances": 4, "metric_value": 1.5, "depth": 6}
                  if obj[4] == 'Evet':
                     # {"feature": "soru6", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6] == 'Evet':
                        return 'AKP'
                     elif obj[6] == 'Hayır':
                        return 'MHP'
                     else:
                        return 'MHP'
                  elif obj[4] == 'Hayır':
                     return 'CHP'
                  else:
                     return 'CHP'
               else:
                  return 'CHP'
            elif obj[2] == 'Hayır':
               # {"feature": "soru1", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[1] == 'Evet':
                  return 'MHP'
               elif obj[1] == 'Hayır':
                  return 'IYI PARTI'
               else:
                  return 'IYI PARTI'
            else:
               return 'IYI PARTI'
         else:
            return 'DIĞER'
      elif obj[5] == 'Evet':
         # {"feature": "Cinsiyet", "instances": 11, "metric_value": 2.2999, "depth": 3}
         if obj[0] == 'Erkek':
            # {"feature": "soru3", "instances": 9, "metric_value": 1.7527, "depth": 4}
            if obj[3] == 'Hayır':
               # {"feature": "soru2", "instances": 6, "metric_value": 1.7925, "depth": 5}
               if obj[2] == 'Evet':
                  # {"feature": "soru1", "instances": 5, "metric_value": 1.371, "depth": 6}
                  if obj[1] == 'Evet':
                     # {"feature": "soru4", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[4] == 'Evet':
                        return 'AKP'
                     elif obj[4] == 'Hayır':
                        return 'MHP'
                     else:
                        return 'MHP'
                  elif obj[1] == 'Hayır':
                     # {"feature": "soru4", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[4] == 'Evet':
                        return 'DIĞER'
                     elif obj[4] == 'Hayır':
                        return 'AKP'
                     else:
                        return 'AKP'
                  else:
                     return 'AKP'
               elif obj[2] == 'Hayır':
                  return 'IYI PARTI'
               else:
                  return 'IYI PARTI'
            elif obj[3] == 'Evet':
               return 'IYI PARTI'
            else:
               return 'IYI PARTI'
         elif obj[0] == 'Kadın':
            # {"feature": "soru1", "instances": 2, "metric_value": 1.0, "depth": 4}
            if obj[1] == 'Evet':
               return 'HDP'
            elif obj[1] == 'Hayır':
               return 'CHP'
            else:
               return 'CHP'
         else:
            return 'CHP'
      else:
         return 'IYI PARTI'
   elif obj[7] == 'Hayır':
      # {"feature": "soru5", "instances": 44, "metric_value": 1.8179, "depth": 2}
      if obj[5] == 'Hayır':
         # {"feature": "soru4", "instances": 34, "metric_value": 1.7605, "depth": 3}
         if obj[4] == 'Evet':
            # {"feature": "soru9", "instances": 29, "metric_value": 1.4591, "depth": 4}
            if obj[9] == 'Hayır':
               # {"feature": "soru6", "instances": 23, "metric_value": 0.9976, "depth": 5}
               if obj[6] == 'Evet':
                  # {"feature": "soru3", "instances": 18, "metric_value": 0.8031, "depth": 6}
                  if obj[3] == 'Hayır':
                     # {"feature": "soru10", "instances": 11, "metric_value": 0.4395, "depth": 7}
                     if obj[10] == 'Hayır':
                        return 'AKP'
                     elif obj[10] == 'Evet':
                        # {"feature": "soru8", "instances": 4, "metric_value": 0.8113, "depth": 8}
                        if obj[8] == 'Evet':
                           # {"feature": "Cinsiyet", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[0] == 'Erkek':
                              # {"feature": "soru1", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[1] == 'Evet':
                                 # {"feature": "soru2", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[2] == 'Evet':
                                    return 'AKP'
                                 else:
                                    return 'AKP'
                              else:
                                 return 'AKP'
                           else:
                              return 'AKP'
                        elif obj[8] == 'Hayır':
                           return 'AKP'
                        else:
                           return 'AKP'
                     else:
                        return 'AKP'
                  elif obj[3] == 'Evet':
                     # {"feature": "soru8", "instances": 7, "metric_value": 0.8631, "depth": 7}
                     if obj[8] == 'Evet':
                        # {"feature": "soru10", "instances": 6, "metric_value": 0.65, "depth": 8}
                        if obj[10] == 'Evet':
                           return 'AKP'
                        elif obj[10] == 'Hayır':
                           # {"feature": "soru1", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[1] == 'Hayır':
                              # {"feature": "Cinsiyet", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[0] == 'Erkek':
                                 # {"feature": "soru2", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[2] == 'Evet':
                                    return 'AKP'
                                 else:
                                    return 'AKP'
                              else:
                                 return 'AKP'
                           elif obj[1] == 'Evet':
                              return 'AKP'
                           else:
                              return 'AKP'
                        else:
                           return 'AKP'
                     elif obj[8] == 'Hayır':
                        return 'DIĞER'
                     else:
                        return 'DIĞER'
                  else:
                     return 'AKP'
               elif obj[6] == 'Hayır':
                  # {"feature": "Cinsiyet", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[0] == 'Erkek':
                     # {"feature": "soru3", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[3] == 'Evet':
                        # {"feature": "soru8", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[8] == 'Hayır':
                           # {"feature": "soru1", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[1] == 'Hayır':
                              # {"feature": "soru2", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[2] == 'Evet':
                                 # {"feature": "soru10", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[10] == 'Evet':
                                    return 'AKP'
                                 else:
                                    return 'AKP'
                              else:
                                 return 'AKP'
                           else:
                              return 'AKP'
                        elif obj[8] == 'Evet':
                           return 'DIĞER'
                        else:
                           return 'DIĞER'
                     elif obj[3] == 'Hayır':
                        return 'DIĞER'
                     else:
                        return 'DIĞER'
                  elif obj[0] == 'Kadın':
                     return 'AKP'
                  else:
                     return 'AKP'
               else:
                  return 'DIĞER'
            elif obj[9] == 'Evet':
               # {"feature": "soru10", "instances": 6, "metric_value": 1.7925, "depth": 5}
               if obj[10] == 'Evet':
                  # {"feature": "soru1", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[1] == 'Hayır':
                     # {"feature": "soru6", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6] == 'Evet':
                        # {"feature": "soru8", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[8] == 'Evet':
                           return 'DIĞER'
                        elif obj[8] == 'Hayır':
                           return 'IYI PARTI'
                        else:
                           return 'IYI PARTI'
                     elif obj[6] == 'Hayır':
                        return 'IYI PARTI'
                     else:
                        return 'IYI PARTI'
                  elif obj[1] == 'Evet':
                     return 'IYI PARTI'
                  else:
                     return 'IYI PARTI'
               elif obj[10] == 'Hayır':
                  # {"feature": "soru3", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[3] == 'Evet':
                     return 'AKP'
                  elif obj[3] == 'Hayır':
                     return 'CHP'
                  else:
                     return 'CHP'
               else:
                  return 'AKP'
            else:
               return 'IYI PARTI'
         elif obj[4] == 'Hayır':
            # {"feature": "soru1", "instances": 5, "metric_value": 1.9219, "depth": 4}
            if obj[1] == 'Evet':
               # {"feature": "soru3", "instances": 3, "metric_value": 1.585, "depth": 5}
               if obj[3] == 'Hayır':
                  # {"feature": "soru9", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[9] == 'Evet':
                     return 'DIĞER'
                  elif obj[9] == 'Hayır':
                     return 'MHP'
                  else:
                     return 'MHP'
               elif obj[3] == 'Evet':
                  return 'AKP'
               else:
                  return 'AKP'
            elif obj[1] == 'Hayır':
               return 'CHP'
            else:
               return 'CHP'
         else:
            return 'CHP'
      elif obj[5] == 'Evet':
         # {"feature": "soru9", "instances": 10, "metric_value": 1.1568, "depth": 3}
         if obj[9] == 'Hayır':
            # {"feature": "soru3", "instances": 7, "metric_value": 0.8631, "depth": 4}
            if obj[3] == 'Hayır':
               # {"feature": "soru2", "instances": 6, "metric_value": 0.65, "depth": 5}
               if obj[2] == 'Hayır':
                  # {"feature": "Cinsiyet", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[0] == 'Erkek':
                     # {"feature": "soru4", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[4] == 'Evet':
                        # {"feature": "soru8", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[8] == 'Evet':
                           return 'HDP'
                        elif obj[8] == 'Hayır':
                           return 'AKP'
                        else:
                           return 'AKP'
                     elif obj[4] == 'Hayır':
                        return 'AKP'
                     else:
                        return 'AKP'
                  elif obj[0] == 'Kadın':
                     return 'AKP'
                  else:
                     return 'AKP'
               elif obj[2] == 'Evet':
                  return 'AKP'
               else:
                  return 'AKP'
            elif obj[3] == 'Evet':
               return 'HDP'
            else:
               return 'HDP'
         elif obj[9] == 'Evet':
            # {"feature": "Cinsiyet", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[0] == 'Kadın':
               return 'AKP'
            elif obj[0] == 'Erkek':
               return 'IYI PARTI'
            else:
               return 'IYI PARTI'
         else:
            return 'AKP'
      else:
         return 'AKP'
   else:
      return 'AKP'

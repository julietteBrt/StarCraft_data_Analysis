from django.shortcuts import render
from sklearn.preprocessing import StandardScaler
import pandas as pd
from .forms import SkillForm
# our home page view
def home(request):    
    return render(request, 'home.html')

def standardize_data(data):
    scaler = StandardScaler()
    data_stan = scaler.fit_transform(data)
    
    # When the data has been transformed, a np.array is returned,
    # So we have to convert it back to a dataframe, and insert column names
    return pd.DataFrame(data_stan, columns = data.columns)

import pickle
model = pickle.load(open("rf.pkl", "rb"))    
df_mean = pd.read_pickle('df_with_mean.pkl')

# custom method for generating predictions
def getPredictions(df):
    prediction = model.predict(df)
    
    if prediction == 1:
        return "Bronze or Silver"
    elif prediction == 3:
        return "Gold"
    elif prediction == 4:
        return "Diamond"
    elif prediction == 5:
        return "Platinum"
    elif prediction == 6:
        return "Master or GrandMaster or Professional"
    else:
        return "error"
        

# our result page view
def result(request):
    if request.method == 'POST':
        formset = SkillForm(request.POST)
        if formset.is_valid():
            
            is_player = formset.cleaned_data.get("is_valid")
            action_latency = formset.cleaned_data.get("action_latency")
            apm = formset.cleaned_data.get("apm")
            gap_between_pacs = formset.cleaned_data.get("gap_between_pacs")
            number_of_pacs = formset.cleaned_data.get("number_of_pacs")
            select_by_hotkeys = formset.cleaned_data.get("select_by_hotkeys")
            assign_to_hotkeys = formset.cleaned_data.get("assign_to_hotkeys")
            name = formset.cleaned_data.get("name")
            
            df_mean.loc[df_mean.shape[0]-1,'APM'] = apm
            df_mean.loc[df_mean.shape[0]-1,'ActionLatency'] = (action_latency)
            df_mean.loc[df_mean.shape[0]-1,'GapBetweenPACs'] = (gap_between_pacs)
            df_mean.loc[df_mean.shape[0]-1,'NumberOfPACs'] = (number_of_pacs)
            df_mean.loc[df_mean.shape[0]-1,'SelectByHotkeys'] = (select_by_hotkeys)
            df_mean.loc[df_mean.shape[0]-1,'AssignToHotkeys'] = (assign_to_hotkeys)
            
            df_stan = standardize_data(df_mean)

            result = getPredictions(df_stan[-1:])
            print(result)
    
            return render(request, 'result.html', {'result':result, 'name':name, 'gamer':is_player})
        else:
                return render(request, 'home.html', {'formset': formset})
    else:
        formset = SkillForm()
    return render(request, 'home.html', {'formset': formset})


    

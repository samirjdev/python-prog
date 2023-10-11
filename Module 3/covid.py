# Collaborators: none

def main():
        symptom = False
        POSITIVE_RESPONSE = ('y', 'yes', 'YES', 'Y') # Defines POSITIVE_RESPONSE tuple
        print('Enter y or n for each prompt')
        if input ("Do you have a fever or chills? ") in POSITIVE_RESPONSE:
            symptom = True
        elif input ("Do you have a cough? ") in POSITIVE_RESPONSE:
            symptom = True
        elif input ("Do you have shortness of breath or difficulty breathing? ") in \
        POSITIVE_RESPONSE:
            symptom = True
        elif input ("Do you have muscle or body aches? ") in POSITIVE_RESPONSE:
            symptom = True
        elif input ("Do you have a headache? ") in POSITIVE_RESPONSE:
            symptom = True
        elif input ("Do you have a new loss of taste or smell? ") in POSITIVE_RESPONSE:
            symptom = True
        elif input ("Do you have a sore throat? ") in POSITIVE_RESPONSE:
            symptom = True
        elif input ("Do you have congestion or runny nose? ") in POSITIVE_RESPONSE:
            symptom = True
        elif input ("Do you have nausea or vomiting? ") in POSITIVE_RESPONSE:
            symptom = True
        elif input ("Do you have diarrhea? ") in POSITIVE_RESPONSE:
            symptom = True
        elif input ("Can youn confirm that you are not experiencing any symptoms? ") in \
        POSITIVE_RESPONSE:
                pass
        else:
                symptom = True

        if symptom:
            print(f'Please do not come to campus at this time...')
        elif input(f"Are you taking over counter meds for cold or flu? ") in POSITIVE_RESPONSE:
            print(f'Please do not come to campus at this time...')
        elif input(f"Have you been tested positive for COVID and/or been advised to self-isolate? ") in \
        POSITIVE_RESPONSE:
            print(f'Please do not come to campus at this time...')
        else:
            print(f'You are okay to visit campus')
if __name__ =='__main__':
    main()


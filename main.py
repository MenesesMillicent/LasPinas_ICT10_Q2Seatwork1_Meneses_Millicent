from pyscript import document 

def candidate_checker(e):
    club_members = ["ange del rosario", "lexie uaje", "gilliah tabaldo", "river datiles", "milli meneses"]
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name

    member_checker = candidate.lower() in club_members
    messages = (f'Sorry {candidate}, your name is not on the list.',
                f'Congratualtion {candidate}, you are now apart of Marching Band')
    document.getElementById('result').innerHTML = messages[member_checker]
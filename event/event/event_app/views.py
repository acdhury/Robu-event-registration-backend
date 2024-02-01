from django.shortcuts import render, redirect
from .forms import SoccerbotForm, LineFollowForm, RoboRaceForm, IdeaGenForm, ChatGPTForm
from .models import SoccerbotMember, lineFollowMember, RoboRaceMember, IdeaGenMember

def home(request):
    return render(request, "event_app/home.html", {})


def soccerbot_registration(request):
    if request.method == 'POST':
        form = SoccerbotForm(request.POST)
        if form.is_valid():
            soccerbot_instance = form.save()  
            student_ids = [soccerbot_instance.team_Lead_StudentID]
            for i in range(2, 5):  # Loop through member fields
                member_id_field = f'member_{i}_StudentID'
                member_id = form.cleaned_data.get(member_id_field)
                if member_id:  # If member ID is not empty
                    student_ids.append(member_id)
            # Create SoccerbotMember instances for each student ID
            for student_id in student_ids:
                SoccerbotMember.objects.create(student_ID=student_id)
            return redirect('home')
    else:
        form = SoccerbotForm()
    return render(request, 'event_app/soccer.html', {'form': form})

def linefollow_registration(request):
    if request.method == "POST":
        form = LineFollowForm(request.POST)
        if form.is_valid():
            lineFollow_instance = form.save()  
            student_ids = [lineFollow_instance.team_Lead_StudentID]
            for i in range(2, 5):  # Loop through member fields
                member_id_field = f'member_{i}_StudentID'
                member_id = form.cleaned_data.get(member_id_field)
                if member_id:  # If member ID is not empty
                    student_ids.append(member_id)
            # Create SoccerbotMember instances for each student ID
            for student_id in student_ids:
                lineFollowMember.objects.create(student_ID=student_id)
            return redirect('home')
    else:
        form = LineFollowForm()
    return render(request, 'event_app/lfr.html', {'form': form})

def chatbot_registration(request):
    if request.method =="POST":
        form = ChatGPTForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ChatGPTForm()
    return render(request, "event_app/chatbot.html", {"form":form})

def robo_race_registration(request):
    if request.method == "POST":
        form = RoboRaceForm(request.POST)
        if form.is_valid():
            RoboRace_instance = form.save()  
            student_ids = [RoboRace_instance.team_Lead_StudentID]
            for i in range(2, 5):  # Loop through member fields
                member_id_field = f'member_{i}_StudentID'
                member_id = form.cleaned_data.get(member_id_field)
                if member_id:  # If member ID is not empty
                    student_ids.append(member_id)
            # Create SoccerbotMember instances for each student ID
            for student_id in student_ids:
                RoboRaceMember.objects.create(student_ID=student_id)
            return redirect('home')
    else:
        form = RoboRaceForm()
    return render(request, 'event_app/robo_race.html', {'form': form})

def idea_gen_registration(request):
    if request.method == "POST":
        form = IdeaGenForm(request.POST)
        if form.is_valid():
            idea_gen_instance = form.save()  
            student_ids = [idea_gen_instance.team_Lead_StudentID]
            for i in range(2, 5):  # Loop through member fields
                member_id_field = f'member_{i}_StudentID'
                member_id = form.cleaned_data.get(member_id_field)
                if member_id:  # If member ID is not empty
                    student_ids.append(member_id)
            # Create SoccerbotMember instances for each student ID
            for student_id in student_ids:
                IdeaGenMember.objects.create(student_ID=student_id)
            return redirect('home')
    else:
        form = IdeaGenForm()
    return render(request, 'event_app/ideagen.html', {'form': form})

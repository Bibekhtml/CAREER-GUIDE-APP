from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Career, Video, Test, Playlist

# This view is for the Guidance main page
def index(request):
    careers = Career.objects.all()
    videos = Video.objects.all()
    playlists = Playlist.objects.all()
    context = {
        'careers': careers,
        'videos': videos,
        'playlists': playlists,
    }
    return render(request, 'guidance/index.html', context)

# This view is to load videos for a particular career
def get_video_guidance(request, career_id):
    videos = Video.objects.filter(career_id=career_id)
    video_list = [{'id': video.id, 'title': video.title, 'url': video.url} for video in videos]
    return JsonResponse(video_list, safe=False)

# THIS is the new view to show the available tests page
def tests_index(request):
    tests = Test.objects.all().order_by('id')  # or any other field
    bonus_tests = Test.objects.filter(is_bonus=True).order_by('id')  # Assuming 'is_bonus' field exists

    # Example unlock logic: (you can replace it with real user progress checking)
    unlocked_tests = []
    unlocked_bonus_tests = []

    for idx, test in enumerate(tests):
        unlocked = idx == 0  # First test always unlocked
        unlocked_tests.append({
            'id': test.id,
            'name': test.name,
            'url_name': f'tests:take_test',  # Define this in urls.py
            'unlocked': unlocked,
        })

    for idx, bonus in enumerate(bonus_tests):
        unlocked = False  # Replace with real unlock logic
        unlocked_bonus_tests.append({
            'id': bonus.id,
            'name': bonus.name,
            'url_name': f'tests:take_test',  # Define this in urls.py
            'unlocked': unlocked,
        })

    context = {
        'tests': unlocked_tests,
        'bonus_tests': unlocked_bonus_tests,
    }
    return render(request, 'tests/index.html', context)

# This view is to take a specific test
def take_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    context = {
        'test': test,
    }
    return render(request, 'tests/take_test.html', context)

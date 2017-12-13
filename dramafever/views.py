from django.shortcuts import get_object_or_404, render
from .models import Topics, Comments
from .forms import TopicsForm, CommentsForm

# Create your views here.
def topics(request):
    if request.method == 'POST':
        form = TopicsForm(request.POST)
        if form.is_valid():
            query = Topics(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'])
            query.save()
            
            return render(request, 'dramafever/done.html', {'message': 'Topic \'%s\' successfully added'%(query.title)})

    return render(request, 'dramafever/topics.html', {'topics_list': Topics.objects.all(),})

def topics_detail(request, topic_id):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            query = Comments(comment=form.cleaned_data['comment'], topic_id=topic_id)
            query.save()

            return render(
                request, 'dramafever/done.html', {'message': 'New comment successfully added'})

    topic = get_object_or_404(Topics, pk=topic_id)
    comments_list = Comments.objects.filter(topic_id=topic_id)
    context = {
        'topic': topic,
        'comments_list': comments_list,
    }
    return render(request, 'dramafever/topics_details.html', context)

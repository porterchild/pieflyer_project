from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from .models import Score

from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    #template = loader.get_template("pieflyer/gamedoc.html")
    
    highest_score_list = Score.objects.order_by('-score')[:5]
    new_scorer = Score.objects.get_or_create(playerName = "")
    print "hellooooooooooooooooooooo1"
    context = {'highest_score_list': highest_score_list, 'new_scorer': new_scorer}
    
    
    return render(request, 'pieflyer/gamedoc.html', context)

def record_score(request, new_scorer_id):
    print "hellooooooooooooooooooooo2"
    score = get_object_or_404(Score, pk=new_scorer_id)
    score.playerName = score.get(pk=request.POST['new_scorer'])
    score.save()
    return HttpResponseRedirect(reverse('pieflyer:index'))
    
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))